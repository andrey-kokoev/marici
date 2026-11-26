"""Transfer the root-15 rotation criterion to the saved multi-root release census."""
import json,argparse
from pathlib import Path
from itertools import combinations
from ramsey38_root15_link_rotation import canon,link_domains,sub
from ramsey38_support_ball_completion import N

def classify(root,drop):
    P=N[root];rows={v:frozenset(P&n) for v,n in N.items() if v not in P|{root}};fs=set(rows.values())|{r|{0} for v,r in rows.items() if v!=drop and len(r)<4};dom={}
    for v in sorted(P|{0}):
        cells=frozenset(s-{v} for s in fs if v in s);E=set.union(set(),*(sub(s,2) for s in cells));V=set.union(set(),*E)
        if len(V)>=3 and len(E)>3*len(V)-6:return 'local'
        dom[v]=link_domains(cells)
        if not dom[v]:return 'local'
    def solve(d):
        if not d:return True
        v=min(d,key=lambda w:len(d[w]))
        for R in d[v]:
            nxt={w:[S for S in opts if w not in R or S[v]==canon(R[w][::-1])] for w,opts in d.items() if w!=v}
            if all(nxt.values()) and solve(nxt):return True
        return False
    return 'pass' if solve(dom) else 'incompatible'

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--all',action='store_true');args=ap.parse_args();path=Path(__file__).resolve().parents[1]/'results/ramsey38_release_census.json';data=json.loads(path.read_text());counts=[0,0,0,0];totals={};joint=[]
    for key,entry in data.items():
        root=int(key);P=N[root];ds=sorted(v for v,n in N.items() if v!=root and v not in P and len(P&n)<4) if args.all else sorted(map(int,entry['shell_counts']));wins=set(map(int,entry['solutions']));out={v:classify(root,v) for v in ds};passed={v for v in ds if out[v]=='pass'};assert wins<=passed
        for v,result in out.items():
            totals[result]=totals.get(result,0)+1
            if result=='incompatible':joint.append((root,v))
        for v in ds:counts[2*(v in passed)+(v in wins)]+=1
        print(root,len(ds),'passes',sorted(passed),'no known filling',sorted(passed-wins),flush=True)
    print('stages',totals,'joint-only rejections',joint)
    print('reject/no ball, reject/ball, pass/no ball, pass/ball:',counts)
