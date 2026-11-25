"""Compile a forced pair-hit into a request on one open exclusive port.
No common-support sextuples and no joint search. All arithmetic exact.
"""
import json,itertools
from pathlib import Path
from ramsey310_matching_sides import decode,instances,sets,F
D=Path(__file__).resolve().parents[1]/'results'

def run():
    rec=json.loads((D/'ramsey310_smallset_parent12_23.json').read_text());p,h=rec['edit'];A=next(itertools.islice(instances(decode((D/'ramsey38_26_e73_hog.g6').read_bytes().splitlines()[p-1])),h,None));e=rec['survivors'][0]['E'];U=rec['survivors'][0]['certificate']['vertices'];u=sum(1<<v for v in U);S=list(sets(A,F,7));T=[(t,k) for k in (6,7) for t in sets(A,F,k)];bad=[s for s in S if not s&u];out=[]
    for port in range(6):
        partner=(port+3)%6
        # Build clauses before seeing the sixth mask: if every bad common row is
        # forbidden, the pair needs >=6. A near-tight witness requires x miss t.
        bans=[];unconditional=0
        for s in bad:
            clause=[]
            for t,k in T:
                if s&t:continue
                lim=6-k+sum(bool(t&e[j] and t&e[j+3]) for j in range(3) if j!=port%3)
                if lim+bool(t&e[partner])<=0:break
                if lim==0:clause.append(t)
            else:bans.append((s,clause));continue
            unconditional+=1
        dom=[x for x in S if not x&e[partner] and x not in e[:port]+e[port+1:] and all((x&e[j]).bit_count()<=5 for j in range(port//3*3,port//3*3+3) if j!=port)]
        fixed=sum(9-A[v].bit_count() for v in U)-sum((y&u).bit_count() for j,y in enumerate(e) if j!=port)
        def excluded(x):
            if fixed-(x&u).bit_count()>=6:return False
            pending=[s for s,clause in bans if not any(not x&t for t in clause)]
            if not pending:return True
            E=e.copy();E[port]=x;sing=sum(1<<v for v,a in enumerate(A) if 9-a.bit_count()-sum(y>>v&1 for y in E)==1)
            gaps=[sing&~(i|j|k) for i,j,k in itertools.product(*zip(E[:3],E[3:]))]
            return all(any((g&s).bit_count()>1 for g in gaps) for s in pending)
        cuts=[x for x in dom if excluded(x)]
        # Count a stronger baseline: both one-side root tests and vertex/edge capacity.
        def viable(x):
            E=e.copy();E[port]=x;side=E[3*(port//3):3*(port//3)+3];need=[9-a.bit_count()-sum(s>>v&1 for s in E) for v,a in enumerate(A)];return min(need)>=1 and max(need)<=6 and all(need[v]+need[w]<=6 for v,a in enumerate(A) for w in range(v) if a>>w&1) and all(not any(not t&(i|j) for t in S) for i,j in itertools.combinations(side,2)) and not any(k==6 and not t&(side[0]|side[1]|side[2]) for t,k in T)
        out.append(dict(port=port,domain=len(dom),unconditional=unconditional,conditional=len(bans),excluded=len(cuts),includes_seed=e[port] in cuts,baseline=sum(map(viable,dom)),baseline_excluded=[x for x in cuts if viable(x)]))
    res=dict(pair=U,bad_rows=len(bad),ports=out);print(json.dumps(res,indent=1));(D/'ramsey310_pair_request.json').write_text(json.dumps(res))
if __name__=='__main__':run()
