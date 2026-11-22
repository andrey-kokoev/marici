"""Conditional last-arrow port encoding. Use an archived collective column as a common phase reference. Apply the actual proton coefficients over Q(i sqrt(3)); no fit or label-to-coordinate permutation."""
import json
from fractions import Fraction as F
from pathlib import Path
D=Path(__file__).resolve().parent;zero=(F(0),F(0))
def apply(rows,v):
    out={}
    for a,b,(u,w) in rows:
        if a not in v:continue
        x,y=v[a];s,t=out.get(b,zero);out[b]=(s+u*x-3*w*y,t+u*y+w*x)
    return {k:z for k,z in out.items() if z!=zero}

def run():
    src=json.loads((D.parents[1]/'nima/results/twelve-triangle-1836-arrows.json').read_text());ops={}
    for e in src:
        a,b=e['source'],e['target'];ops.setdefault(a[0],[]).append((tuple(a[1:]),tuple(b[1:]),(F(e['weight_real']),F(e['weight_imag_sqrt3']))))
    L,G,N=(ops[s] for s in ('raw','local','aligned'));assert list(map(len,(L,G,N)))==[108,432,1296];v=apply(N,{('AB','x'):(1,0)});modes={a:{k:z for k,z in v.items() if k[0]==a} for a,c in v};aligned={k:(x/12,y/12) for k,(x,y) in v.items()};assert len(modes)==12
    for u in modes.values():assert u and apply(L,u)==u and apply(G,u)==apply(N,u)==aligned
    live=json.loads((D/'ramsey_live_matching_receipt.json').read_text());out=[]
    for t in live:
        for row in t['rows']:
            a,b=row['receipt'][:2];delta={**modes[a],**{k:(-x,-y) for k,(x,y) in modes[b].items()}};assert a!=b and apply(L,delta)==delta and not apply(N,delta);out.append(dict(binding=t['binding'],row=row['row'],handoff=[a,b],bit=row['bit'],nonzero_contrast_slots=len(delta)))
    return dict(reference=['AB','x'],equal_return_for_all_12_ports=True,cases=out)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_proton_handoff_mode_contrast.json').write_text(json.dumps(out)+'\n')
