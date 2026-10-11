"""Audit constituent support of the retained L/G/N coefficient arrows.

Owners are the four parent faces of the existing surface triangulation, each
bounding one tetrahedron in the proposed center-to-face subdivision. This
labels existing ports; it does not create internal geometric-interface data.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]


def main():
    arrow_path=ROOT/'results/twelve-triangle-1836-arrows.json'
    geometry_path=ROOT/'results/twelve-triangle-positive-geometry.json'
    arrow_bytes=arrow_path.read_bytes();geometry_bytes=geometry_path.read_bytes()
    arrows=json.loads(arrow_bytes);geometry=json.loads(geometry_bytes)
    owners={r['outer_arrow']:r['triangle'][0].removeprefix('F_')
            for r in geometry['triangles_and_transports']}
    faces=sorted(set(owners.values()))
    assert len(owners)==12 and len(faces)==4
    assert set(Counter(owners.values()).values())=={3}
    stage_names={('raw','local'):'L',('local','aligned'):'G',('aligned','raw'):'N'}
    edge_owner=[];edge_stage=[];pairs=[]
    within={f:set() for f in faces}
    incident={f:set() for f in faces}
    bridges={p:set() for p in combinations(faces,2)}
    stage_counts=Counter()
    for i,a in enumerate(arrows):
        src,tgt=tuple(a['source']),tuple(a['target'])
        pairs.append((src,tgt))
        stage=stage_names[src[0],tgt[0]];edge_stage.append(stage);stage_counts[stage]+=1
        support=frozenset((owners[src[1]],owners[tgt[1]]));edge_owner.append(support)
        assert 1<=len(support)<=2
        for face in support:incident[face].add(i)
        if len(support)==1:within[next(iter(support))].add(i)
        else:bridges[tuple(sorted(support))].add(i)
    assert len(arrows)==len(set(pairs))==1836
    assert stage_counts=={'L':108,'G':432,'N':1296}
    def counts(indices):return dict(Counter(edge_stage[i] for i in indices))
    for face in faces:
        assert counts(within[face])=={'L':27,'G':27,'N':81}
        assert counts(incident[face])=={'L':27,'G':189,'N':567}
    for pair,ids in bridges.items():
        assert counts(ids)=={'G':54,'N':162}
        assert incident[pair[0]] & incident[pair[1]]==ids
    intersections={}
    for n in range(1,5):
        intersections[n]=[len(set.intersection(*(incident[f] for f in sub)))
                          for sub in combinations(faces,n)]
    assert intersections=={1:[783]*4,2:[216]*6,3:[0]*4,4:[0]}
    ie=sum((-1)**(n+1)*sum(values) for n,values in intersections.items())
    assert ie==1836
    # Disjoint support partition, independent of the overlapping-star cover.
    pieces=list(within.values())+list(bridges.values())
    assert sum(map(len,pieces))==len(set.union(*pieces))==1836
    assert 4*135+6*216==1836
    assert len(set.union(*within.values()))==540
    assert 1836-540==1296  # Not shared internal-face entries: cross-piece arrows.
    # Negative control: duplicate-cover sums count each bridge twice.
    assert sum(map(len,incident.values()))==3132!=1836
    # An induced N block is a fraction of a projector, not a standalone
    # normalized collective identity. Its trace is the face's mode weight.
    trace=Counter()
    for a in arrows:
        src,tgt=tuple(a['source']),tuple(a['target'])
        if stage_names[src[0],tgt[0]]=='N' and src[1:]==tgt[1:]:
            assert F(a['weight_imag_sqrt3'])==0
            trace[owners[src[1]]]+=F(a['weight_real'])
    assert all(trace[f]==F(1,4) for f in faces)
    result=dict(schema='marici.nima.1836-constituent-gluing.v1',status='pass',
                source_sha256=hashlib.sha256(arrow_bytes).hexdigest(),
                geometry_sha256=hashlib.sha256(geometry_bytes).hexdigest(),
                owner_map=owners,global_stage_counts=dict(stage_counts),
                induced_piece_counts={f:counts(within[f]) for f in faces},
                pair_bridge_counts={'/'.join(p):counts(ids) for p,ids in bridges.items()},
                incident_piece_counts={f:counts(incident[f]) for f in faces},
                incident_intersections={str(n):values for n,values in intersections.items()},
                disjoint_support_formula='1836 = 4*135 + 6*216',
                overlapping_incident_formula='1836 = 4*783 - 6*216 + 4*0 - 0',
                collective_face_traces={f:str(trace[f]) for f in faces},
                interpretation='Incident-arrow covers satisfy inclusion-exclusion, but include outgoing cross-piece arrows. Their pair intersections are bridge sets, not independently constructed internal-face kernels.',
                residual='No retained ports for the central vertex or internal faces/edges were introduced. Triple and quadruple primitive-arrow supports vanish. Quark masses or standalone constituent tetrahedron costs are not derived.')
    out=ROOT/'results/1836-constituent-gluing.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
