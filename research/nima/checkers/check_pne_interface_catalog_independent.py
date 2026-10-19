"""Independent path enumeration, map and support checks over serialized sources."""
import copy
import hashlib
import json
from pathlib import Path

SOURCE = Path('research/nima/results/pne-interface-catalog/verification.json')
PERMUTATIONS = {'PN': [3,1,2,0,4], 'inverse-PN': [3,1,2,0,4], 'NE': [0,4,2,3,1]}
ADVANCE = {'proton': [2,3,0,1,4], 'neutron': [0,3,4,1,2]}

def validate_case(case):
    reg = case['registry']
    packets, charts, cells, ops = (reg[k] for k in ('packets','charts','cells','operations'))
    allowed = reg['allowedOperations']
    def chart(p): return charts[packets[p]['chart']]
    def cell(p): return chart(p)['cell']
    outgoing = {p: [] for p in reg['universePackets']}
    for i in allowed:
        o = ops[i]
        a, b = packets[o['source']], packets[o['target']]
        ca, cb = chart(o['source']), chart(o['target'])
        delta = int(o['kind'] in ('reader-phase-advance','NN-phase-advance'))
        assert o['phaseDelta'] == delta and b['origin'] == a['origin'] + delta
        perm = ADVANCE[ca['species']] if delta else PERMUTATIONS[o['kind']]
        assert o['permutation'] == perm
        assert b['permutation'] == [a['permutation'][i] for i in perm]
        if not delta:
            for mark in ('C0','M0','C1','M1','C2'):
                assert ca['aliases'][mark] == cb['aliases'][mark]
        if ca['cell'] != cb['cell']:
            shared = set(cells[ca['cell']]['vertices']) & set(cells[cb['cell']]['vertices'])
            assert len(shared) == 3 and shared == set(o['face'])
        else:
            assert o['face'] is None and o['kind'] == 'reader-phase-advance'
        outgoing[o['source']].append(i)
    # Independently enumerate breadth-first by path length, including all starts.
    frontier = [(p, (p,), ()) for p in reg['universePackets']]
    expected = {}
    for length in range(1, 5):
        following = []
        for last, ids, word in frontier:
            for i in outgoing[last]:
                target = ops[i]['target']
                if target in ids:
                    continue
                entry = (target, ids + (target,), word + (i,))
                following.append(entry)
                if length >= 2:
                    expected[entry[2]] = entry[1]
        frontier = following
    actual = {tuple(r['factors']): tuple(r['packets']) for r in case['records']}
    assert len(actual) == len(case['records']) and actual == expected
    def compatible(ids):
        bodies, roles = {}, {}
        for p in ids:
            c = chart(p)
            if c['cell'] in bodies and bodies[c['cell']] != c['species']: return False
            bodies[c['cell']] = c['species']
            for mark, vertex in c['aliases'].items():
                if vertex in roles and roles[vertex] != mark[0]: return False
                roles[vertex] = mark[0]
        items = list(bodies.items())
        for i, (a, sa) in enumerate(items):
            for b, sb in items[i+1:]:
                shared = set(cells[a]['vertices']) & set(cells[b]['vertices'])
                if len(shared) != 3: continue
                if sa == sb and sa != 'neutron' or {sa,sb} == {'proton','electron'}: return False
                expected_m = 2 if {sa,sb} == {'proton','neutron'} else 1
                if sum(roles[v] == 'M' for v in shared) != expected_m: return False
        return True
    for r in case['records']:
        ids, factors = r['packets'], r['factors']
        assert r['source'] == ids[0] and r['target'] == ids[-1]
        composed = list(range(5))
        for i in factors:
            o = ops[i]
            p = ADVANCE[chart(o['source'])['species']] if o['phaseDelta'] else PERMUTATIONS[o['kind']]
            composed = [composed[j] for j in p]
        assert composed == r['permutation']
        assert [packets[ids[0]]['permutation'][i] for i in composed] == packets[ids[-1]]['permutation']
        # Ten basis inputs, real and imaginary, test the entire carried map.
        for axis in range(10):
            v = [[int(axis == 2*j), int(axis == 2*j+1)] for j in range(5)]
            result = v
            for i in factors: result = [result[j] for j in ops[i]['permutation']]
            assert result == [v[j] for j in composed]
        support = sorted({cell(p) for p in ids})
        assert r['referenceSupport'] == support == r['nativePolicy']['requiredOccupied']
        assert r['nativePolicy']['fullSupportCompatible'] == compatible(ids)
        assert r['endpointsCompatible'] == compatible([ids[0],ids[-1]])
        assert r['originDelta'] == packets[ids[-1]]['origin'] - packets[ids[0]]['origin']
        assert len(r['referenceOccurrences']) == len(ids)
        for p, record in zip(ids, r['referenceOccurrences']):
            assert record['packet'] == p and record['origin'] == packets[p]['origin']
            assert record['marks'] == [dict(mark=m, role=m[0], index=int(m[1:])+packets[p]['origin'], vertex=v) for m,v in chart(p)['aliases'].items()]
        internal_n = chart(ids[0])['species'] == 'proton' and chart(ids[-1])['species'] == 'electron' and all(chart(p)['species'] == 'neutron' for p in ids[1:-1])
        assert internal_n == r['internalN']
        eligible = internal_n and r['originDelta'] == 0
        assert bool(r['contractedPolicy']) == eligible
        if eligible:
            assert [ops[i]['kind'] for i in factors] == ['PN','NE']
            policy = r['contractedPolicy']
            assert policy['requiredOccupied'] == [cell(ids[0]),cell(ids[-1])]
            assert policy['requiredVacant'] == [cell(ids[1])]
            assert policy['referenceSupport'] == support
            assert composed == [3,4,2,0,1]
            shared = set(cells[cell(ids[0])]['vertices']) & set(cells[cell(ids[-1])]['vertices'])
            assert shared == {chart(ids[0])['aliases']['C1'],chart(ids[0])['aliases']['M1']}
    return len(actual)

if __name__ == '__main__':
    report = json.loads(SOURCE.read_text())
    counts = [validate_case(c) for c in report['cases']]
    negatives = []
    for name, mutate in [
        ('wrong-map', lambda c: c['records'][0]['permutation'].reverse()),
        ('lost-context-index', lambda c: c['records'][0]['referenceOccurrences'][0]['marks'][0].update(index=999)),
        ('dropped-reference-support', lambda c: c['records'][0]['referenceSupport'].pop()),
        ('incomplete-path-list', lambda c: c['records'].pop()),
    ]:
        c = copy.deepcopy(report['cases'][-1]); mutate(c)
        try: validate_case(c)
        except AssertionError: negatives.append(name)
        else: raise AssertionError('Mutation was accepted: '+name)
    out = {'status':'pass-independent-path-map-support-catalog', 'pathsByDepth':counts, 'basisChecks':10*sum(counts), 'negativeControls':negatives, 'inputSha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(), 'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    SOURCE.with_name('independent-verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
