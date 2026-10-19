"""Actual Bool-carrier syntax codec and bounded endpoint-only obstruction.
The codec is deliberately NOT admitted as semantic execution of Resolve.
"""
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/conjecture_net'))
from pilot_carrier import PathRecord, Operation, LABELS

NOTE = 'research/voevodsky/restricted-profile-process-comparison-v1.md'
OUT = 'research/voevodsky/results/restricted-profile-process-comparison-v1.json'
REGISTER = 'research/nima/contracts/physics-source-register.v1.json'
TAGS = {'literal': (0, 0, 0), 'identity': (0, 0, 1), 'pair': (0, 1, 0),
        'select-false': (0, 1, 1), 'select-true': (1, 0, 0)}
ARITY = {'literal': 0, 'identity': 1, 'pair': 2, 'select-false': 2, 'select-true': 2}
INVERSE = {v: k for k, v in TAGS.items()}

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def encode(t):
    name, *children = t
    require(name in TAGS and len(children) == ARITY[name], 'wrong source constructor')
    return TAGS[name] + tuple(b for child in children for b in encode(child))

def parse(bits, offset=0):
    tag = tuple(bits[offset:offset+3]); require(tag in INVERSE, 'unknown/truncated code')
    name = INVERSE[tag]; offset += 3; children = []
    for _ in range(ARITY[name]):
        child, offset = parse(bits, offset); children.append(child)
    return (name, *children), offset

def decode(bits):
    term, end = parse(bits)
    require(end == len(bits), 'unconsumed code')
    return term

def cost(t):
    return 1 + sum(cost(child) for child in t[1:])

def path(t, start=(False, False)):
    return PathRecord(start, tuple(Operation.LEFT if b == 0 else Operation.RIGHT for b in encode(t)))

def admit_semantic_bridge(c):
    require(c['native_rule_output_square'] and c['proof_payload_transport']
            and c['resource_guard_translation'], 'encoding alone is not semantic execution')

def main():
    register = json.loads((ROOT/REGISTER).read_text())
    source = next(s for s in register['sources'] if s['id'] == 'native-bool-square-pilot')
    require('research/conjecture_net/pilot_carrier.py' in source['evidence'], 'source implementation changed')
    require(not register['common_physical_witness_constructed'], 'physical scope changed; review required')
    literal = ('literal',); terms = {literal}
    for _ in range(2):
        old = tuple(terms)
        terms |= {('identity', t) for t in old}
        terms |= {(op, t, u) for op in ('pair', 'select-false', 'select-true') for t in old for u in old}
    for t in terms:
        bits = encode(t); p = path(t)
        require(decode(bits) == t and len(p.operations) == 3*cost(t), 'codec/cost mismatch')
        # Use actual endpoint-matched path composition, not tuple concatenation alone.
        for cut in range(len(bits)+1):
            first = PathRecord(p.source, p.operations[:cut])
            second = PathRecord(first.target, p.operations[cut:])
            require(first.then(second) == p, 'actual path composition failure')
    chain = [literal]
    for _ in range(4):
        chain.append(('identity', chain[-1]))
    require(len(set(chain)) == 5 and len(LABELS) == 4, 'pigeonhole fixture')
    assignments = list(itertools.product(range(4), repeat=5))
    require(all(len(set(a)) < 5 for a in assignments), 'five-source endpoint injection unexpectedly exists')
    # Actual codec has a concrete collision but retains distinguishable words.
    collision = next((a, b) for i, a in enumerate(chain) for b in chain[i+1:] if path(a).target == path(b).target)
    a, b = collision
    require(path(a).structural_id != path(b).structural_id and cost(a) != cost(b), 'retained distinction lost')
    malformed_rejected = []
    for name, bits in (('unknown-code', (1,1,1)), ('truncated-child', TAGS['identity']),
                       ('extra-trailing-node', TAGS['literal']*2)):
        try:
            decode(bits)
        except ValueError:
            malformed_rejected.append(name)
        else:
            raise AssertionError('malformed encoding accepted')
    codec_claim = dict(native_rule_output_square=False, proof_payload_transport=False, resource_guard_translation=False)
    try:
        admit_semantic_bridge(codec_claim)
    except ValueError:
        semantic_promotion_rejected = True
    else:
        raise AssertionError('codec admitted as semantic realization')
    paths = [NOTE, REGISTER, 'research/conjecture_net/pilot_carrier.py',
             'research/voevodsky/agda/RestrictedSeedArityProfile.agda',
             Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.restricted-profile-process-comparison.v1', passed=True,
                  source='native-bool-square-pilot', terms_checked=len(terms),
                  endpoint_assignments_rejected=len(assignments),
                  actual_collision=dict(first=a, second=b, endpoint=path(a).target,
                                        node_costs=[cost(a),cost(b)], flip_costs=[len(path(a).operations),len(path(b).operations)]),
                  malformed_controls_rejected=malformed_rejected,
                  semantic_promotion_rejected=semantic_promotion_rejected,
                  disposition='syntax_codec_constructed_endpoint_only_candidate_rejected',
                  native_Resolve_semantics_realized=False, physical_realization_admitted=False,
                  formulation_gate_discharged=False,
                  source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__ == '__main__':
    main()
