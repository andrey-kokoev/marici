"""Recover the two parallel bundles behind every handoff, identify the actual transport their composition defines, and compare matching-owner order across direct bindings."""
from ramsey_row_quotient_constructor import final,frame_records,move,R,flags
from pathlib import Path
import json
D=Path(__file__).parent

def run():
    m,=final;n=move(m,R);G,H,_=next(z for z in frame_records if m in z[2]);A=m-n;B=n-m;L={i for i,j in A};V={j for i,j in A};assert len(A)==len(B)==5 and set(A|B)=={(i,j) for i,j in flags if i in L and j in V};assert (0,16) in A and (0,17) in B
    a=dict(A);b=dict(B);ai={v:u for u,v in A};bi={v:u for u,v in B};go={i:bi[a[i]] for i in L};back={i:ai[b[i]] for i in L};assert all(back[go[i]]==i and R[go[i]]==back[R[i]] for i in L);orbit=[0];
    while go[orbit[-1]]!=0:orbit.append(go[orbit[-1]])
    assert len(orbit)==5
    from ramsey_partition_turn_replay import run as streams
    bindings=[]
    for bind in streams():
        orders=[]
        for row in bind['rows']:
            path=[0,16,13,19,7] if row['row']=='BRNN' else [0,17,12,27,4];fs=[tuple(sorted(z)) for z in zip(path,path[1:])];picked=[fs[s-1] for _,s,_ in row['events']];assert all(e in A|B for e in picked);orders.append(['entry' if e in A else 'mate' for e in picked])
        assert orders[0]==orders[1] and len(set(orders[0]))==2;bindings.append((bind['binding'],orders[0]))
    return dict(entry_bundle=sorted(A),mate_bundle=sorted(B),entry_then_mate_inverse_cycle=orbit,orders=bindings)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_quotient_handoff_bundle_trace.json').write_text(json.dumps(out)+'\n')
