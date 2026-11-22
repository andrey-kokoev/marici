"""Same G13 and four new vertices, vary ONLY their internal graph. Compare archived supports, completely free supports (no maximal assumption), and 2K2-donor templates."""
from itertools import combinations,permutations
from pysat.solvers import Solver
from ramsey_capacity_transfer_78 import D,json,inds,bits,Counter
E=list(combinations(range(4),2))
def run():
    n=13;H=[sum(1<<((i+d)%13) for d in (1,-1,5,-5)) for i in range(n)];I=inds(H);F=(1<<n)-1;seeds=[[1,7,11],[3,5,9],[2,6,12],[4,8,10]];fixed=[sum(1<<v for v in s) for s in seeds];P=[sum(1<<j for j,x in enumerate(I) if not s&x) for s in fixed];out=[];sym=[sum(1<<v for v in s) for s in combinations(range(4),3)]
    def change(m,p):return sum(1<<E.index(tuple(sorted((p[i],p[j])))) for a,(i,j) in enumerate(E) if m>>a&1)
    def valid(S,edges,ind):return all(s in I for s in S) and all(not S[i]&S[j] for i,j in edges) and all(t.bit_count()+max((q.bit_count() for q in ind if all(not S[i]&t for i in bits(q))),default=0)<=5 for t in I)
    for m in range(64):
        edges=[e for i,e in enumerate(E) if m>>i&1];ind=[q for q in range(16) if all(not (q>>i&1 and q>>j&1) for i,j in edges)];
        if any(all(tuple(sorted(e)) in edges for e in combinations(v,2)) for v in combinations(range(4),3)):continue
        fixedok=valid(fixed,edges,ind);canonical=min(change(m,p) for p in permutations(range(4)));C=[[-(1+k*n+i),-(1+k*n+j)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(4)]+[[-(1+i*n+v),-(1+j*n+v)] for i,j in edges for v in range(n)]
        for t in I:
            for q in ind:
                if t.bit_count()+q.bit_count()==6:C.append([1+i*n+j for i in bits(q) for j in bits(t)])
        with Solver(name='g4',bootstrap_with=C) as sat:
            ok=sat.solve();model=set(sat.get_model()) if ok else set();S=[sum(1<<j for j in range(n) if 1+i*n+j in model) for i in range(4)];assert not ok or valid(S,edges,ind)
        out.append(dict(mask=m,edges=edges,canon=canonical,free=ok,fixed=fixedok,example=S if ok else None))
    # enumerate pair obstructions for archived supports; any co-missed old four-set forces an internal red edge
    forced={str(e):[t for t in I if t.bit_count()==4 and all(not t&fixed[i] for i in e)] for e in E};partners={s:[z for z in I if not s&z and all((s|z)&t for t in I if t.bit_count()==4)] for s in I};assert all(x&y for zs in partners.values() for x,y in combinations(zs,2));assert not partners[0];return dict(rows=out,forced=forced,partners=partners)
if __name__=='__main__':
    z=run();print([(r['edges'],r['free']) for r in z['rows'] if r['canon']==r['mask']]);print([r['edges'] for r in z['rows'] if r['fixed']]);print({k:len(v) for k,v in z['forced'].items()});(D/'ramsey_thirteen_port_motif_control.json').write_text(json.dumps(z)+'\n')
