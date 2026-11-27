from collections import Counter
from pathlib import Path
import json, sys
from hashlib import sha256

D=Path(__file__).resolve().parents[1]/'results'
sys.path.insert(0,str(D.parents[1]/'chatgpt'/'ramsey'))
from ramsey_row_quotient_constructor import frame_records, move, R


def cycles(m,n):
    def mates(edges):return {v:w for a,b in edges for v,w in [(a,b),(b,a)]}
    p,q=mates(m),mates(n); todo={v for v in p if p[v]!=q[v]}; out=[]
    while todo:
        start=min(todo);c=[];v=start
        while v not in c:
            c.append(v);todo.remove(v);v=(p if len(c)%2 else q)[v]
        assert v==start;out.append(c)
    return out


def run():
    results=[];marks={(0,16),(7,29)};counterexamples=[]
    for G,H,matchings in frame_records:
        for m in sorted(matchings,key=sorted):
            if not marks<=m:continue
            n=move(m,R);cs=cycles(m,n);entry=next(c for c in cs if c[0]==0);z=dict(frame=sorted(G),matching=sorted(m),swapped=sorted(n),entry_cycle=entry,other_cycles=[c for c in cs if c!=entry]);results.append(z)
    for a in results:
        if a['other_cycles']:continue
        for b in results:
            if not b['other_cycles'] or a['frame']!=b['frame'] or a['entry_cycle']!=b['entry_cycle']:continue
            counterexamples.append([results.index(a),results.index(b)])
    print('solutions',len(results),'cycle counts',Counter(1+len(z['other_cycles']) for z in results),'matched pairs',counterexamples);assert counterexamples
    a,b=counterexamples[0];print(results[a]['entry_cycle'],results[b]['other_cycles']);prefix='ramsey_seed_boundary_residue';out=dict(protocol_sha=sha256((D/(prefix+'_protocol.md')).read_bytes()).hexdigest(),cases=results,matched_pairs=counterexamples);(D/(prefix+'.json')).write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
