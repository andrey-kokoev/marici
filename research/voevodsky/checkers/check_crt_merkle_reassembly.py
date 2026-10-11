"""Content-address the fixed CRT derivation and independently verify its certificates.
Standard library only. SHA-256 authenticates bytes relative to a supplied root;
finite evaluation, not hashing, checks mathematical correctness.
"""
from copy import deepcopy
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / 'results' / 'crt_edge_reassembly.json'
PRODUCER = BASE / 'checkers' / 'check_crt_edge_reassembly.py'
source = json.loads(SOURCE.read_text(encoding='utf-8'))
if not source['passed'] or source['checker_sha256'] != sha256(PRODUCER.read_bytes()).hexdigest():
    raise ValueError('Run the current CRT edge reassembly checker first')

DOMAIN = b'marici.typed-crt-merkle.v1\0'
PORTS = {'a': 'Z3', 'b': 'Z5', 'x': 'Z15'}
ROOT_TYPES = {'assembled': 'Z15', 'decomposed': 'Z3xZ5', 'pair_round_trip': 'Z3xZ5', 'residue_round_trip': 'Z15'}
WITNESSES = {
    'residue3': ('assembled', 'output mod 3 = input a'),
    'residue5': ('assembled', 'output mod 5 = input b'),
    'pair_round_trip': ('pair_round_trip', 'output = (input a,input b)'),
    'residue_round_trip': ('residue_round_trip', 'output = input x'),
}
ENVIRONMENTS = [dict(a=a, b=b, x=x) for a, b, x in product(range(3), range(5), range(15))]
STORE = {}

def digest(record):
    raw = json.dumps(record, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode('utf-8')
    return sha256(DOMAIN + raw).hexdigest()

def put(record):
    key = digest(record)
    STORE[key] = deepcopy(record)
    return key

def get(key, store=STORE):
    if key not in store or digest(store[key]) != key:
        raise ValueError('missing object or hash mismatch')
    return store[key]

def infer(op, types, parameter):
    unary = {'lift3': ('Z3', 'Z15'), 'lift5': ('Z5', 'Z15'), 'reduce3': ('Z15', 'Z3'), 'reduce5': ('Z15', 'Z5')}
    if op in unary and types == [unary[op][0]] and parameter is None:
        return unary[op][1]
    if op == 'scale' and types == ['Z15'] and type(parameter) is int:
        return 'Z15'
    if op == 'add' and types == ['Z15', 'Z15'] and parameter is None:
        return 'Z15'
    if op == 'pair' and types == ['Z3', 'Z5'] and parameter is None:
        return 'Z3xZ5'
    raise ValueError('invalid typed constructor')

def typed_term(key, cache, store=STORE, visiting=None):
    if key in cache: return cache[key]
    visiting = set() if visiting is None else visiting
    if key in visiting: raise ValueError('cyclic dependency')
    visiting.add(key)
    rec = get(key, store)
    if rec['kind'] == 'input':
        if set(rec) != {'kind', 'name', 'type'} or PORTS.get(rec['name']) != rec['type']:
            raise ValueError('invalid input')
        typ = rec['type']
    elif rec['kind'] == 'operation':
        if set(rec) != {'kind', 'op', 'parameter', 'type', 'inputs'}: raise ValueError('operation shape')
        typ = infer(rec['op'], [typed_term(child, cache, store, visiting) for child in rec['inputs']], rec['parameter'])
        if typ != rec['type']: raise ValueError('output type mismatch')
    else: raise ValueError('not a term')
    visiting.remove(key)
    cache[key] = typ
    return typ

def value(key, env, cache, store=STORE):
    if key in cache: return cache[key]
    rec = get(key, store)
    if rec['kind'] == 'input': result = env[rec['name']]
    else:
        args = [value(child, env, cache, store) for child in rec['inputs']]
        op = rec['op']
        if op in ('lift3', 'lift5'): result = args[0]
        elif op == 'scale': result = rec['parameter'] * args[0] % 15
        elif op == 'add': result = sum(args) % 15
        elif op == 'reduce3': result = args[0] % 3
        elif op == 'reduce5': result = args[0] % 5
        elif op == 'pair': result = args
        else: raise ValueError('unknown operation')
    cache[key] = result
    return result

def rows_for(outputs, store=STORE):
    rows = []
    for env in ENVIRONMENTS:
        cache = {}
        rows.append({'environment': env, 'outputs': {name: value(ref, env, cache, store) for name, ref in outputs.items()}})
    return rows

def correctness(row):
    e, v = row['environment'], row['outputs']
    return (v['assembled'] % 3 == e['a'] and v['assembled'] % 5 == e['b']
            and v['decomposed'] == [e['x'] % 3, e['x'] % 5]
            and v['pair_round_trip'] == [e['a'], e['b']] and v['residue_round_trip'] == e['x'])

def merkleize(graph):
    refs = {name: put({'kind': 'input', 'name': name, 'type': typ}) for name, typ in graph['ports'].items()}
    for edge in graph['edges']:
        refs[edge['output']] = put({'kind': 'operation', 'op': edge['op'], 'parameter': edge['parameter'],
                                    'type': edge['type'], 'inputs': [refs[i] for i in edge['inputs']]})
    outputs = {name: refs[ref] for name, ref in graph['roots'].items()}
    ports = {name: refs[name] for name in PORTS}
    table = put({'kind': 'exhaustive-evaluation', 'domain': 'Z3 x Z5 x Z15', 'rows': rows_for(outputs)})
    witnesses = {}
    for witness in graph['witnesses']:
        witnesses[witness['id']] = put({'kind': 'witness', 'type': 'FixedCRTBoundaryProof',
            'id': witness['id'], 'root_name': witness['root'], 'relation': witness['relation'],
            'subject': outputs[witness['root']], 'ports': ports, 'evaluation': table})
    return put({'kind': 'construction', 'type': 'WitnessedCRT', 'ports': ports, 'outputs': outputs, 'witnesses': witnesses})

def verify(root, store=STORE):
    rec = get(root, store)
    if set(rec) != {'kind', 'type', 'ports', 'outputs', 'witnesses'} or rec['kind'] != 'construction' or rec['type'] != 'WitnessedCRT':
        raise ValueError('construction shape')
    if set(rec['ports']) != set(PORTS) or set(rec['outputs']) != set(ROOT_TYPES) or set(rec['witnesses']) != set(WITNESSES):
        raise ValueError('boundary interface or witness loss')
    types = {}
    for name, key in rec['ports'].items():
        if get(key, store) != {'kind': 'input', 'name': name, 'type': PORTS[name]}: raise ValueError('input identity')
    for name, key in rec['outputs'].items():
        if typed_term(key, types, store) != ROOT_TYPES[name]: raise ValueError('root type')
    rows = rows_for(rec['outputs'], store)
    if not all(correctness(row) for row in rows): raise ValueError('mathematical witness false')
    for name, (root_name, relation) in WITNESSES.items():
        witness = get(rec['witnesses'][name], store)
        expected = {'kind': 'witness', 'type': 'FixedCRTBoundaryProof', 'id': name,
                    'root_name': root_name, 'relation': relation, 'subject': rec['outputs'][root_name],
                    'ports': rec['ports'], 'evaluation': witness.get('evaluation')}
        if witness != expected: raise ValueError('witness attachment mismatch')
        table = get(witness['evaluation'], store)
        if table != {'kind': 'exhaustive-evaluation', 'domain': 'Z3 x Z5 x Z15', 'rows': rows}:
            raise ValueError('evaluation evidence mismatch')
    return rows

def certificate(left, right):
    return put({'kind': 'equivalence', 'type': 'FixedCRTInterfaceEquivalence', 'from': left, 'to': right,
                'method': 'exhaustive evaluation with all boundary witnesses', 'domain': 'Z3 x Z5 x Z15'})

def verify_certificate(key, store=STORE):
    rec = get(key, store)
    if set(rec) != {'kind', 'type', 'from', 'to', 'method', 'domain'} or rec['kind'] != 'equivalence' or rec['type'] != 'FixedCRTInterfaceEquivalence' or rec['method'] != 'exhaustive evaluation with all boundary witnesses' or rec['domain'] != 'Z3 x Z5 x Z15':
        raise ValueError('certificate shape')
    if get(rec['from'], store)['ports'] != get(rec['to'], store)['ports']: raise ValueError('different endpoints')
    if verify(rec['from'], store) != verify(rec['to'], store): raise ValueError('not equivalent')
    return True

def operation_hashes(root):
    reached = set()
    def walk(key):
        if key in reached: return
        rec = get(key)
        if rec['kind'] == 'operation':
            reached.add(key)
            for child in rec['inputs']: walk(child)
    for ref in get(root)['outputs'].values(): walk(ref)
    return reached

def rejected(action):
    try: action()
    except (ValueError, KeyError, TypeError): return True
    return False

roots = {name: merkleize(graph) for name, graph in source['graphs'].items()}
checks = {f'{name}_typed_and_witnessed': len(verify(root)) == 225 for name, root in roots.items()}
checks['expanded_and_shared_same_content_root'] = roots['expanded'] == roots['shared']
checks['normalized_has_different_root'] = roots['expanded'] != roots['normalized']
checks['merkle_sharing_20_to_16_operation_nodes'] = (len(operation_hashes(roots['expanded'])), len(operation_hashes(roots['normalized']))) == (20, 16)
cert = certificate(roots['expanded'], roots['normalized'])
checks['separate_equivalence_certificate_verified'] = verify_certificate(cert)

# Renaming local occurrence IDs does not alter constructor content.
renamed = deepcopy(source['graphs']['expanded'])
rename = {e['output']: f'local_{i}' for i, e in enumerate(renamed['edges'])}
for edge in renamed['edges']:
    edge['output'] = rename[edge['output']]
    edge['inputs'] = [rename.get(i, i) for i in edge['inputs']]
renamed['roots'] = {k: rename.get(v, v) for k, v in renamed['roots'].items()}
checks['local_node_renaming_preserves_root'] = merkleize(renamed) == roots['expanded']

# Honest rehashing changes identity; retaining the old hash exposes tampering.
root = roots['normalized']
bad_store = deepcopy(STORE)
scale_key = next(k for k in operation_hashes(root) if STORE[k]['op'] == 'scale' and STORE[k]['parameter'] == 6)
bad_store[scale_key]['parameter'] = 5
checks['coefficient_tamper_detected_by_hash'] = rejected(lambda: verify(root, bad_store))
bad_root = deepcopy(get(root))
del bad_root['witnesses']['residue5']
erased = put(bad_root)
checks['witness_erasure_changes_root'] = erased != root
checks['rehashed_witness_erasure_rejected'] = rejected(lambda: verify(erased))
wrong_attachment = deepcopy(get(root))
witness = deepcopy(get(wrong_attachment['witnesses']['residue3']))
witness['subject'] = wrong_attachment['outputs']['residue_round_trip']
wrong_attachment['witnesses']['residue3'] = put(witness)
checks['rehashed_attachment_swap_rejected'] = rejected(lambda: verify(put(wrong_attachment)))

bad_graph = deepcopy(source['graphs']['normalized'])
for edge in bad_graph['edges']:
    if edge['op'] == 'scale' and edge['parameter'] == 6: edge['parameter'] = 5
bad = merkleize(bad_graph)
checks['well_hashed_wrong_math_rejected'] = rejected(lambda: verify(bad))
checks['false_equivalence_certificate_rejected'] = rejected(lambda: verify_certificate(certificate(roots['expanded'], bad)))
ordered = deepcopy(source['graphs']['normalized'])
next(e for e in ordered['edges'] if e['op'] == 'pair')['inputs'].reverse()
checks['ordered_ports_affect_hash'] = merkleize(ordered) != root
checks['reordered_typed_pair_rejected'] = rejected(lambda: verify(merkleize(ordered)))

# Keep only the valid reachable artifact; negative-control objects are not published as proofs.
valid = {}
def retain(key):
    if key in valid: return
    rec = get(key)
    valid[key] = rec
    if rec['kind'] == 'operation': refs = rec['inputs']
    elif rec['kind'] == 'construction': refs = list(rec['ports'].values()) + list(rec['outputs'].values()) + list(rec['witnesses'].values())
    elif rec['kind'] == 'witness': refs = [rec['subject'], rec['evaluation']] + list(rec['ports'].values())
    elif rec['kind'] == 'equivalence': refs = [rec['from'], rec['to']]
    else: refs = []
    for ref in refs: retain(ref)
retain(cert)
# Verify from a JSON round trip, not from original in-memory objects alone.
artifact = {'schema': 'marici.typed-crt-merkle-store.v1', 'roots': roots, 'equivalence_certificate': cert, 'objects': valid}
round_trip = json.loads(json.dumps(artifact))
checks['serialized_artifact_reverifies'] = verify_certificate(round_trip['equivalence_certificate'], round_trip['objects'])
result = {
    'schema': 'marici.voevodsky.crt-merkle-reassembly.v1', 'passed': all(checks.values()), 'checks': checks,
    'roots': roots, 'equivalence_certificate': cert,
    'constructor_nodes': {name: len(operation_hashes(root)) for name, root in roots.items()},
    'witness_nodes_per_construction': 4, 'exhaustive_environments': 225, 'stored_objects': len(valid),
    'source_receipt_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope': 'Content identity of pure typed terms modulo occurrence naming and storage sharing; finite extensional equivalence of the fixed CRT interface. Not authenticity, a collision-freedom proof, arbitrary dependent proof equivalence, or tetrahedral reconstruction.',
}
(BASE / 'results' / 'crt_merkle_store.json').write_text(json.dumps(artifact, indent=2) + '\n', encoding='utf-8')
(BASE / 'results' / 'crt_merkle_reassembly.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
if not result['passed']: raise SystemExit(1)
