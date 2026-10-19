"""Structural overlay validation only; does not rerun source mathematics."""
import copy
import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = 'research/conjecture_net/contracts/hodge-coherence-leads.v1.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))


def validate(c):
    require(c['schema'] == 'marici.hodge-coherence-leads.v1', 'schema')
    require(c['Hodge_proved'] is False and c['Hodge_refuted'] is False, 'no Hodge promotion')
    base = load(c['base_contract'])
    require(base['iteration'] == c['base_iteration'] == 52, 'base iteration')
    require(base['source_pins'] == c['base_pins'], 'base pins')
    require(set(c['base_nodes']) <= {n['id'] for n in base['conjectures']}, 'base node binding')
    nodes = {n['id']: n for n in c['leads']}
    require(len(nodes) == len(c['leads']) == 14, 'lead inventory')
    allowed = {'candidate': 'blocked', 'safeguard': 'required',
               'rejected_route': 'rejected_at_scope', 'context': 'context_only'}
    for n in nodes.values():
        require(allowed.get(n['kind']) == n['status'], 'status boundary')
        require(set(n['depends_on']) <= nodes.keys(), 'missing dependency')
        for key in ('hypothesis', 'missing', 'test', 'falsifier'):
            require(bool(n[key].strip()), 'missing field '+key)
        require(bool(n['sources']), 'no sources')
        for p in n['sources']:
            require((ROOT/p).is_file(), 'missing source '+p)
    conjectures = c['conjectures']
    require(len(conjectures) == 4, 'conjecture inventory')
    for n in conjectures:
        require(n['id'] not in nodes, 'duplicate conjecture id')
        require(n['status'] == 'open' and n['outcome'] is None, 'conjecture promotion')
        require(n['execution_status'] == 'blocked_on_source_binding', 'conjecture execution')
        for key in ('statement', 'quantifiers', 'source_result', 'missing', 'acceptance', 'falsifier', 'next_test'):
            require(bool(n[key].strip()), 'missing conjecture field '+key)
        require(bool(n['guards']) and bool(n['sources']), 'conjecture guards and provenance')
        for p in n['sources']:
            require((ROOT/p).is_file(), 'missing source '+p)
        nodes[n['id']] = n
    for n in conjectures:
        require(set(n['depends_on']) <= nodes.keys(), 'missing conjecture dependency')
    for binding in c.get('tested_bindings', []):
        require(set(binding['conjectures']) <= nodes.keys(), 'binding conjecture reference')
        for key in ('note', 'checker', 'receipt'):
            require((ROOT/binding[key]).is_file(), 'binding evidence missing')
        receipt = load(binding['receipt'])
        require(receipt['passed'] and not receipt['Hodge_proved'] and not receipt['Hodge_refuted'], 'binding claim promotion')
    done, visiting = set(), set()
    def visit(node):
        require(node not in visiting, 'dependency cycle')
        if node in done:
            return
        visiting.add(node)
        for dep in nodes[node]['depends_on']:
            visit(dep)
        visiting.remove(node)
        done.add(node)
    for node in nodes:
        visit(node)
    require(c['frontier']['executable_Hodge_detector_tasks'] == [], 'blocked execution')
    require(c['frontier']['first_source_construction_candidate'] in nodes, 'priority binding')
    require((ROOT/c['guide']).is_file(), 'guide')
    from check_hodge_coherence_relations import validate as validate_relations
    validate_relations(load(c['relation_contract']), c)


def main():
    c = load(CONTRACT)
    validate(c)
    mutations = []
    bad = copy.deepcopy(c); bad['Hodge_refuted'] = True; mutations.append(bad)
    bad = copy.deepcopy(c); bad['leads'][0]['depends_on'].append('absent'); mutations.append(bad)
    bad = copy.deepcopy(c); bad['frontier']['executable_Hodge_detector_tasks'] = ['joint-matching-obstruction']; mutations.append(bad)
    bad = copy.deepcopy(c); bad['leads'][1]['depends_on'] = ['joint-matching-obstruction']; mutations.append(bad)
    bad = copy.deepcopy(c); bad['conjectures'][0]['outcome'] = 'proved'; mutations.append(bad)
    bad = copy.deepcopy(c); bad['conjectures'][1]['depends_on'] = ['absent']; mutations.append(bad)
    for bad in mutations:
        try:
            validate(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('hostile incorrectly accepted')
    pins = load(c['base_pins'])['source_sha256']
    for p, digest in pins.items():
        require(sha256((ROOT/p).read_bytes()).hexdigest() == digest, 'base source drift '+p)
    paths = {CONTRACT, c['guide'], c['base_contract'], c['base_pins'],
             Path(__file__).relative_to(ROOT).as_posix()}
    paths.update(p for n in c['leads'] + c['conjectures'] for p in n['sources'])
    relations = load(c['relation_contract'])
    paths.update([c['relation_contract'], relations['guide'], relations['execution']['abstract_tests']])
    paths.update(b[k] for b in c.get('tested_bindings', []) for k in ('note','checker','receipt'))
    result = {'passed': True, 'leads': len(c['leads']), 'conjectures': len(c['conjectures']), 'hostile_controls': len(mutations),
              'base_source_hashes_unchanged': True,
              'classification': 'lead_registration_not_mathematical_verification',
              'residuals': ['Hodge source bridges and universal necessity missing'],
              'Hodge_proved': False, 'Hodge_refuted': False,
              'source_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(paths)}}
    out = ROOT/'research/voevodsky/results/hodge-coherence-leads-v1.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}))


if __name__ == '__main__':
    main()
