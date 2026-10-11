"""Proof of concept: realize sector gluing as a retained boundary/filler witness.

Construct a cellular Cech chain complex separately for every original arrow.
This is a linear incidence realization, not an Agda proof of geometric gluing.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
import hashlib

ROOT=Path(__file__).resolve().parents[1]


def main():
    ap=ROOT/'results/twelve-triangle-1836-arrows.json'
    gp=ROOT/'results/twelve-triangle-positive-geometry.json'
    raw=ap.read_bytes();geo=gp.read_bytes()
    arrows=json.loads(raw);geometry=json.loads(geo)
    owner={r['outer_arrow']:r['triangle'][0].removeprefix('F_') for r in geometry['triangles_and_transports']}
    faces=sorted(set(owner.values()))
    stage={('raw','local'):'L',('local','aligned'):'G',('aligned','raw'):'N'}
    supports=[];labels=[]
    for a in arrows:
        supports.append(sorted({owner[a['source'][1]],owner[a['target'][1]]}))
        labels.append(stage[a['source'][0],a['target'][0]])
    assert len(arrows)==1836
    # C0: original arrows as common comparison boundary generators K_e.
    # C1: one occurrence (face,e) for each incident constituent.
    # d1(face,e)=K_e. Cross arrows have two such alternative fillers p_e,q_e.
    # C2: h_e for each cross arrow, with d2 h_e=q_e-p_e.
    c1=[(f,e) for e,s in enumerate(supports) for f in s]
    position={x:i for i,x in enumerate(c1)}
    cross=[e for e,s in enumerate(supports) if len(s)==2]
    internal=[e for e,s in enumerate(supports) if len(s)==1]
    assert len(c1)==3132 and len(cross)==1296 and len(internal)==540

    def boundary1(chain):
        out=Counter()
        for idx,value in chain.items():out[c1[idx][1]]+=value
        return {e:v for e,v in out.items() if v}
    witnesses={}
    for e in cross:
        a,b=supports[e]
        p={position[a,e]:1};q={position[b,e]:1}
        h_boundary={position[b,e]:1,position[a,e]:-1}
        assert boundary1(p)==boundary1(q)=={e:1}
        assert boundary1(h_boundary)=={}
        witnesses[e]=h_boundary
        # Negative control: losing orientation gives 2K rather than a cycle.
        assert boundary1({position[a,e]:1,position[b,e]:1})=={e:2}
    # Distinct witness boundaries have disjoint supports, hence d2 injective.
    used=set()
    for h in witnesses.values():
        assert used.isdisjoint(h)
        used.update(h)
    # For each e, ker d1 has rank (#occurrences-1). Therefore image d2
    # equals ker d1 integrally, with no divisibility/torsion assumptions.
    assert sum(len(s)-1 for s in supports)==len(witnesses)
    # Canonical section chooses the first incident owner, and an explicit
    # contraction recovers the difference from the other occurrence.
    for idx,(f,e) in enumerate(c1):
        selected=position[supports[e][0],e]
        delta=Counter({idx:1});delta[selected]-=1
        delta={i:v for i,v in delta.items() if v}
        if f==supports[e][0]:assert delta=={}
        else:assert delta==witnesses[e]
    pair_rows=[]
    for a,b in combinations(faces,2):
        shared=[e for e,s in enumerate(supports) if s==[a,b]]
        p_count=sum(a in s for s in supports)
        q_count=sum(b in s for s in supports)
        union=sum(a in s or b in s for s in supports)
        assert p_count==q_count==783 and len(shared)==216
        assert union==p_count+q_count-len(shared)==1350
        pair_rows.append(dict(p=a,q=b,shared_K=216,
                              alternative_filler_occurrences=432,
                              comparison_fillers_h=216,
                              K_stages=dict(Counter(labels[e] for e in shared)),union_arrows=union))
    result=dict(schema='marici.nima.witness-sector-counting.v1',status='pass',
                source_sha256=hashlib.sha256(raw).hexdigest(),geometry_sha256=hashlib.sha256(geo).hexdigest(),
                realization='C2 -> C1 -> C0: comparison witnesses -> owner occurrences -> original coefficient arrows',
                dimensions={'C0_boundary_labels':1836,'C1_retained_occurrences':3132,'C2_comparison_fillers':1296},
                relations='d1 p_e=d1 q_e=K_e; d2 h_e=q_e-p_e; d1 d2=0',
                exactness='d1 onto; d2 injective; image d2=kernel d1 over Z; canonical section and occurrence contraction verified',
                stage_counts={'boundary':dict(Counter(labels)),
                              'occurrences':dict(Counter(labels[e] for _,e in c1)),
                              'comparison_fillers':dict(Counter(labels[e] for e in cross))},
                pairs=pair_rows,accounting='3132-1296=1836',
                coefficient_recovery='Both occurrences retain the same original arrow id, hence its exact complex coefficient and typed endpoints are recovered by lookup.',
                residual='h cells are explicitly adjoined incidence comparisons, not extracted geometric face fillers. Counting h as additional primitive paid arrows would change the cost; no cost policy or fractional correction is inferred.')
    out=ROOT/'results/witness-sector-counting.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
