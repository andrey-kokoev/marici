"""Role-fiber adapter candidate: coherence is separate from PN-law transport."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/voevodsky'
INPUT = BASE / 'results/ramsey-native-PN-overlap-span-input-v1.json'
CONTRACT = BASE / 'contracts/ramsey-context-edge-adapter-attempt.v1.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def key(p):
    return [p['chart'], p['face']]

def bit(p, v):
    return int(p['role'][v] == 'M')

def adapter(a, b, support):
    return {'source': key(a), 'target': key(b),
            'support': sorted(support),
            'flip': {v: bit(a,v) ^ bit(b,v) for v in sorted(support)}}

def act(e, v, r):
    assert v in e['support'] and r in (0,1)
    return r ^ e['flip'][v]

def validate(e, a, b, support):
    assert e == adapter(a,b,support), 'adapter or parent context changed'

def main():
    raw = json.loads(INPUT.read_text())
    ports = raw['ports']
    vertices = list(ports[0]['role'])
    facets = [set(vertices)-{v} for v in vertices]
    groups = [[p for p in ports if set(p['faceVertices']) == f] for f in facets]
    assert list(map(len, groups)) == [12]*4
    assert len({tuple(key(p)) for p in ports}) == 48
    for p in ports:
        assert sum(bit(p,v) for v in p['faceVertices']) == 2
    edge_cells = triple_cells = covers = 0
    for cover in itertools.product(*groups):
        edges = {}
        for i,j in itertools.combinations(range(4),2):
            support = facets[i] & facets[j]
            a,b = cover[i],cover[j]
            e = adapter(a,b,support)
            reverse = adapter(b,a,support)
            validate(e,a,b,support)
            edges[i,j] = e
            for v in support:
                assert act(e,v,bit(a,v)) == bit(b,v)
                restricted = adapter(a,b,{v})
                for r in (0,1):
                    assert act(reverse,v,act(e,v,r)) == r
                    assert act(e,v,r) == act(restricted,v,r)
                    edge_cells += 1
        for i,j,k in itertools.combinations(range(4),3):
            support = facets[i] & facets[j] & facets[k]
            assert len(support) == 1
            v = next(iter(support))
            for r in (0,1):
                assert act(edges[j,k],v,act(edges[i,j],v,r)) == act(edges[i,k],v,r)
                triple_cells += 1
        covers += 1
    # Test the standard law on arbitrary role assignments, not just the one
    # occupied source role. Choose two valid records on the SAME triangle.
    law_counterexample = None
    for a,b in itertools.product(groups[0],repeat=2):
        support = sorted(facets[0])
        e = adapter(a,b,support)
        for roles in itertools.product((0,1),repeat=3):
            out = [act(e,v,r) for v,r in zip(support,roles)]
            if sum(roles) == 2 and sum(out) != 2:
                law_counterexample = {'adapter':e, 'input_roles':list(roles),
                                      'output_roles':out, 'source_M_count':2,
                                      'target_M_count':sum(out),
                                      'occupied_source':[bit(a,v) for v in support],
                                      'occupied_target':[bit(b,v) for v in support]}
                break
        if law_counterexample:
            break
    assert law_counterexample is not None
    # Pullback of the old predicate is always possible but is a DIFFERENT law.
    e = law_counterexample['adapter']
    pulled_back_checks = 0
    for roles in itertools.product((0,1),repeat=3):
        transported = [act(e,v,r) for v,r in zip(e['support'],roles)]
        restored = [act(e,v,r) for v,r in zip(e['support'],transported)]
        assert sum(restored) == sum(roles)
        pulled_back_checks += 1
    a,b = groups[0][0], groups[1][0]
    support = facets[0] & facets[1]
    good = adapter(a,b,support)
    controls = []
    def reject(name, bad):
        try:
            validate(bad,a,b,support)
        except AssertionError:
            controls.append(name)
        else:
            raise AssertionError('hostile accepted: '+name)
    bad = json.loads(json.dumps(good))
    bad['flip'][sorted(support)[0]] ^= 1
    reject('tampered vertex flip',bad)
    bad = json.loads(json.dumps(good))
    del bad['source']
    reject('erased parent context',bad)
    controls.append('standard PN law transport refuted by explicit counterexample')
    assert (covers,edge_cells,triple_cells) == (20736,497664,165888)
    result = {
        'schema':'marici.ramsey-context-edge-adapter.audit.v1',
        'status':'coherent-role-fiber-adapter-with-standard-PN-law-obstruction',
        'scope_id':'vertexwise-role-fiber-edge-adapter-v1',
        'covers':covers, 'edge_fiber_checks':edge_cells,
        'triple_vertex_fiber_checks':triple_cells,
        'pullback_law_checks':pulled_back_checks,
        'controls':controls, 'standard_PN_counterexample':law_counterexample,
        'native_comparison_derivation_proved':False,
        'standard_PN_predicate_preserved':False,
        'physical_role_motion_proved':False,
        'parent_descent_resolved':False,
        'source_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):sha(p)
                         for p in [INPUT,CONTRACT,Path(__file__)]}}
    (BASE/'results/ramsey-context-edge-adapter-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
