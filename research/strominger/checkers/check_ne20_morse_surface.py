"""Independent exact ribbon verification of the TypeScript constructor receipt.
Run after pnpm --dir apps/isotope-wiring check:morse-surface. No dependencies.
"""
from copy import deepcopy
from fractions import Fraction
from functools import cmp_to_key
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RECEIPT = ROOT / 'research/strominger/results/ne20-morse-surface.json'


def coordinate(value):
    return Fraction(value) if isinstance(value, int) else Fraction(value['numerator'], value['denominator'])


def verify(packet):
    assert packet['schema'] == 'marici.ne20-morse-surface.v2'
    assert packet['sourceHash'] == sha256((ROOT / 'apps/isotope-wiring/src/examples/neon20.ts').read_bytes()).hexdigest()
    assert packet['constructorHash'] == sha256((ROOT / 'apps/isotope-wiring/src/domain/morse-surface.ts').read_bytes()).hexdigest()
    document, reported = packet['document'], packet['surface']
    graph, layout = document['graph'], document['layout']
    assert reported['documentId'] == document['id'] and reported['revision'] == document['revision']
    positions = {v['vertexId']: (coordinate(v['position']['x']), coordinate(v['position']['y'])) for v in layout['vertices']}
    styles = {e['edgeId']: e for e in layout['edges']}
    alpha, rotation, tangent = {}, {v['id']: [] for v in graph['vertices']}, {}
    adjacency = {v: set() for v in rotation}
    for edge in graph['edges']:
        path = [positions[edge['from']]] + [(coordinate(p['x']), coordinate(p['y'])) for p in styles[edge['id']]['via']] + [positions[edge['to']]]
        adjacency[edge['from']].add(edge['to'])
        adjacency[edge['to']].add(edge['from'])
        for end, other, points in [('from', 'to', path), ('to', 'from', list(reversed(path)))]:
            dart = edge['id'] + ':' + end
            alpha[dart] = edge['id'] + ':' + other
            rotation[edge[end]].append(dart)
            tangent[dart] = next((x-points[0][0], y-points[0][1]) for x, y in points[1:] if (x,y) != points[0])
    def compare(a, b):
        ax, ay = tangent[a]; bx, by = tangent[b]
        ha = 0 if ay > 0 or (ay == 0 and ax >= 0) else 1
        hb = 0 if by > 0 or (by == 0 and bx >= 0) else 1
        if ha != hb:
            return ha - hb
        cross = ax*by - ay*bx
        assert cross != 0
        return -1 if cross > 0 else 1
    for darts in rotation.values():
        darts.sort(key=cmp_to_key(compare))
    assert rotation == {r['vertexId']: r['darts'] for r in reported['rotations']}
    assert alpha == {d['id']: d['mate'] for d in reported['darts']}
    sigma = {dart: darts[(i+1) % len(darts)] for darts in rotation.values() for i, dart in enumerate(darts)}
    cycles, unused = [], set(alpha)
    while unused:
        first = min(unused); dart = first; cycle = []
        while True:
            assert dart in unused
            unused.remove(dart); cycle.append(dart); dart = sigma[alpha[dart]]
            if dart == first:
                break
        cycles.append(cycle)
    unseen, components = set(rotation), 0
    while unseen:
        components += 1; pending = [min(unseen)]
        while pending:
            v = pending.pop()
            if v not in unseen:
                continue
            unseen.remove(v); pending.extend(adjacency[v] & unseen)
    def necklace(cycle):
        return min(tuple(cycle[i:] + cycle[:i]) for i in range(len(cycle))) if cycle else ()
    assert {necklace(c) for c in cycles} == {necklace(c) for component in reported['components'] for c in component['boundaries']}
    v, e, b = len(rotation), len(alpha)//2, len(cycles)
    assert (v,e,components,b) == (12,26,1,6)
    assert sorted(map(len, cycles)) == [8,8,8,8,8,12]
    assert reported['eulerCharacteristic'] == v-e == -14
    assert reported['genus'] == (2*components-b-v+e)//2 == 5
    assert reported['firstBettiNumber'] == e-v+components == 15
    assert len(reported['minima']) == v and len(reported['saddles']) == e and reported['maxima'] == 0
    assert reported['convention'] == 'clockwise-authored-tangents-untwisted' and reported['contractedEdges'] == []
    assert all(p['sourceVertices'] == [p['vertexId']] for p in reported['minima'])
    assert {p['vertexId'] for p in reported['minima']} == set(rotation)
    assert {p['edgeId'] for p in reported['saddles']} == {e['id'] for e in graph['edges']}
    minima = [coordinate(p['level']) for p in reported['minima']]
    saddles = [coordinate(p['level']) for p in reported['saddles']]
    assert all(0 < x < 1 for x in minima) and all(1 < x < 2 for x in saddles)
    assert len(set(minima+saddles)) == v+e and reported['boundaryLevel'] == 3
    # Independent contraction check: delete cancelled ports from the ORIGINAL
    # boundary permutation, then recover the required disk rotations via alpha.
    reduced = packet['reduced']
    assert reduced['convention'] == 'clockwise-authored-tangents-untwisted-contracted'
    assert reduced['contractedEdges'] == ['edge.ne20.8', 'edge.ne20.9']
    removed = {edge+':'+end for edge in reduced['contractedEdges'] for end in ['from','to']}
    survivors = set(alpha) - removed
    phi = {d: sigma[alpha[d]] for d in alpha}
    restricted = {}
    for d in survivors:
        next_dart = phi[d]
        while next_dart in removed:
            next_dart = phi[next_dart]
        restricted[d] = next_dart
    rrot = {r['vertexId']: r['darts'] for r in reduced['rotations']}
    rsigma = {d: ds[(i+1) % len(ds)] for ds in rrot.values() for i,d in enumerate(ds)}
    assert rsigma == {d: restricted[alpha[d]] for d in survivors}
    rdarts = {d['id']: d for d in reduced['darts']}
    assert set(rdarts) == survivors and len(rdarts) == 48
    assert all(rdarts[d]['mate'] == alpha[d] for d in survivors)
    merged = {'vertex.upper-left','vertex.upper-tip','vertex.upper-right'}
    expected_groups = {frozenset(merged)} | {frozenset([v]) for v in rotation if v not in merged}
    groups = {m['vertexId']: m['sourceVertices'] for m in reduced['minima']}
    assert len(groups) == 10 and {frozenset(g) for g in groups.values()} == expected_groups
    assert sorted(v for group in groups.values() for v in group) == sorted(rotation)
    assert all(representative in group for representative, group in groups.items())
    owner = {original: representative for representative, group in groups.items() for original in group}
    original_owner = {d: vertex for vertex, ds in rotation.items() for d in ds}
    assert all(rdarts[d]['vertexId'] == owner[original_owner[d]] for d in survivors)
    assert all(rdarts[d]['vertexId'] == vertex for vertex, ds in rrot.items() for d in ds)
    assert set(rrot) == set(groups)
    assert {necklace([d for d in c if d not in removed]) for c in cycles} == {necklace(c) for component in reduced['components'] for c in component['boundaries']}
    assert len(reduced['components']) == 1
    assert set(reduced['components'][0]['vertices']) == set(groups)
    remaining_edges = {e['id'] for e in graph['edges']} - set(reduced['contractedEdges'])
    assert set(reduced['components'][0]['edges']) == remaining_edges
    assert len(reduced['saddles']) == 24 and {s['edgeId'] for s in reduced['saddles']} == remaining_edges
    assert (reduced['genus'],reduced['boundaryCount'],reduced['eulerCharacteristic'],reduced['firstBettiNumber']) == (5,6,-14,15)
    assert len({rdarts['edge.ne20.12:'+end]['vertexId'] for end in ['from','to']}) == 1
    for edge in ['edge.ne20.10','edge.ne20.11','edge.ne20.27']:
        assert {rdarts[edge+':'+end]['vertexId'] for end in ['from','to']} == {owner['vertex.upper-tip'],'vertex.top-junction'}
    rmin = [coordinate(p['level']) for p in reduced['minima']]
    rsad = [coordinate(p['level']) for p in reduced['saddles']]
    assert all(0 < x < 1 for x in rmin) and all(1 < x < 2 for x in rsad)
    assert len(set(rmin+rsad)) == 34 and reduced['maxima'] == 0 and reduced['boundaryLevel'] == 3
    for presentation in [reported, reduced]:
        ordered_min = sorted(presentation['minima'], key=lambda p: p['vertexId'])
        ordered_sad = sorted(presentation['saddles'], key=lambda p: p['edgeId'])
        assert [coordinate(p['level']) for p in ordered_min] == [Fraction(i+1,len(ordered_min)+1) for i in range(len(ordered_min))]
        assert [coordinate(p['level']) for p in ordered_sad] == [1+Fraction(i+1,len(ordered_sad)+1) for i in range(len(ordered_sad))]
        assert len(presentation['components']) == 1
        component = presentation['components'][0]
        assert presentation['boundaryCount'] == 6
        assert set(component['vertices']) == {p['vertexId'] for p in ordered_min}
        assert set(component['edges']) == {p['edgeId'] for p in ordered_sad}
        ports = [d for r in presentation['rotations'] for d in r['darts']]
        assert len(ports) == len(set(ports)) == len(presentation['darts']) == 2*len(ordered_sad)
        assert len(presentation['rotations']) == len(ordered_min)
        port_owner = {d:r['vertexId'] for r in presentation['rotations'] for d in r['darts']}
        assert set(port_owner) == {d['id'] for d in presentation['darts']}
        assert all(d['vertexId'] == port_owner[d['id']] and d['edgeId'] == d['id'].rsplit(':',1)[0] for d in presentation['darts'])
        assert (component['genus'], component['eulerCharacteristic'], component['firstBettiNumber'],len(component['boundaries'])) == (5,-14,15,6)
    # Same incidence, different ribbon rotations: a planar counter-convention.
    planar = deepcopy(rotation)
    for vertex in ['vertex.upper-tip', 'vertex.left-tip', 'vertex.right-tip', 'vertex.bottom-tip']:
        planar[vertex].reverse()
    junction = planar['vertex.top-junction']
    positions_to_reverse = [i for i, dart in enumerate(junction) if dart in {'edge.ne20.1:to', 'edge.ne20.3:from', 'edge.ne20.23:from'}]
    replacement = [junction[i] for i in positions_to_reverse][::-1]
    for i, dart in zip(positions_to_reverse, replacement):
        junction[i] = dart
    psigma = {dart: darts[(i+1) % len(darts)] for darts in planar.values() for i, dart in enumerate(darts)}
    unused = set(alpha); planar_boundaries = 0
    while unused:
        planar_boundaries += 1; first = min(unused); dart = first
        while True:
            assert dart in unused
            unused.remove(dart); dart = psigma[alpha[dart]]
            if dart == first:
                break
    # Rejected shortcut: these tip/block reversals leave genus five, not zero.
    assert planar_boundaries == 6
    planar = deepcopy(rotation)
    planar['vertex.upper-left'].reverse()
    planar['vertex.upper-right'].reverse()
    planar['vertex.middle-left'] = ['edge.ne20.21:from','edge.ne20.16:to','edge.ne20.17:to','edge.ne20.7:from','edge.ne20.1:from']
    planar['vertex.middle-right'] = ['edge.ne20.19:to','edge.ne20.2:to','edge.ne20.3:to','edge.ne20.7:to','edge.ne20.22:to']
    planar['vertex.bottom-right'] = ['edge.ne20.13:from','edge.ne20.4:to','edge.ne20.20:from','edge.ne20.22:from','edge.ne20.6:to']
    planar['vertex.bottom-left'] = ['edge.ne20.14:from','edge.ne20.6:from','edge.ne20.17:from','edge.ne20.15:from','edge.ne20.18:from']
    assert all(sorted(planar[v]) == sorted(rotation[v]) for v in rotation)
    psigma = {dart: darts[(i+1) % len(darts)] for darts in planar.values() for i, dart in enumerate(darts)}
    unused = set(alpha); planar_boundaries = 0
    while unused:
        planar_boundaries += 1; first = min(unused); dart = first
        while True:
            assert dart in unused
            unused.remove(dart); dart = psigma[alpha[dart]]
            if dart == first:
                break
    assert planar_boundaries == 16, f'Constructive outer-chord rotation produced {planar_boundaries} boundaries'
    assert (2*components-planar_boundaries-v+e)//2 == 0


def main():
    receipt = json.loads(RECEIPT.read_text(encoding='utf-8'))
    verify(receipt)
    for defect in ['genus', 'boundary', 'rotation', 'reduced-port', 'reduced-provenance']:
        bad = deepcopy(receipt)
        if defect == 'genus':
            bad['surface']['genus'] = 0
        elif defect == 'boundary':
            bad['surface']['components'][0]['boundaries'][0].pop()
        elif defect == 'rotation':
            bad['surface']['rotations'][0]['darts'].reverse()
        elif defect == 'reduced-port':
            bad['reduced']['rotations'][0]['darts'].pop()
        else:
            next(m for m in bad['reduced']['minima'] if len(m['sourceVertices']) > 1)['sourceVertices'].pop()
        try:
            verify(bad)
        except AssertionError:
            pass
        else:
            raise AssertionError('Undetected defect: '+defect)
    print(json.dumps({'status':'passed','scope':'authored Ne-20 clockwise untwisted ribbon surface', 'genus':5,'boundaries':6,'chi':-14,'betti1':15,'reduced':{'minima':10,'saddles':24,'genus':5,'boundaries':6},'negative_controls':['false genus','lost half-edge','changed rotation','lost reduced port','lost vertex provenance'],'alternative_rotation':{'genus':0,'boundaries':16}, 'not_verified':['numerical smooth atlas','gradient identification','nuclear physics']}))


if __name__ == '__main__':
    main()
