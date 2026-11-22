"""Reconstruct the across-entry window from a finite two-flag prefix. Reverse the reflected Hall incidences, not issued native events. Use the old live receipt only as an output oracle."""
from itertools import combinations,permutations
from pathlib import Path
import json
D=Path(__file__).resolve().parent;X=list(combinations(range(1,5),2));P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6]
col=(1,3,2,4);image=[X.index(tuple(sorted(col[v-1] for v in e))) for e in X];rd=lambda d:tuple(sorted(image[k] for k in d));rho=[P.index(rd(d)) for d in P]+[15+T.index(tuple(sorted(map(rd,t)))) for t in T]
def run():
    seed=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());edges={''.join(e) for e in seed['arrows']};faces=[[a+b for a,b in zip(f,f[1:])] for f in seed['retained_face_cycles']];succ={e:f[(i+1)%3] for f in faces for i,e in enumerate(f)};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        rows=[]
        for prefix in [(0,16,13),(0,17,12)]:
            win=[rho[x] for x in prefix[:0:-1]]+list(prefix);assert all(P[min(x,y)] in T[max(x,y)-15] for x,y in zip(win,win[1:]));i,j=P[win[0]];a,=set(X[i])&set(X[j]);v=start=p[a-1];events=[]
            for x,y in zip(win,win[1:]):
                supports=[{p[v-1] for v in X[k]} for k in P[min(x,y)]];options=[e for e in edges if e[0]==v and set(e) in supports];assert len(options)<=1
                if options:
                    e,=options;events.append(e);v=e[1]
                    if v in {'C','D'}-{start}:break
            a,b=events;receipt=events+[succ[b],succ[succ[b]],succ[a],succ[succ[a]]];assert set(receipt)==edges;rows.append(dict(prefix=prefix,window=win,receipt=receipt,bit=int(a[1]==p[0])))
        out.append(dict(binding=''.join(p),rows=rows))
    oracle=json.loads((D/'ramsey_live_matching_receipt.json').read_text());assert [(z['binding'],[(r['receipt'],r['bit']) for r in z['rows']]) for z in out]==[(z['binding'],[(r['receipt'],r['bit']) for r in z['rows']]) for z in oracle];return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_folded_entry_handoff.json').write_text(json.dumps(out)+'\n')
