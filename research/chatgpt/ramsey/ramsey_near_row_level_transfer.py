"""Level transfer: three disjoint independent color classes. Classify maximum independent rows by q=max neighbourhood overlap. Predictor q=alpha-1 frozen at the 17-core level; compare exact neighbourhoods, complement, all maximum rows, and full three-port feasibility. Exact SAT not restricted to maximal supports."""
from ramsey_square_level_transfer import D,json,inds,bits,graph,gzip,combinations,Counter,grow,verify
from pysat.solvers import Solver

def audit(H):
    n=len(H);I=inds(H);a=max(map(int.bit_count,I));T=[s for s in I if s.bit_count()==a];U=[s for s in I if s.bit_count()==a-1];q=[max((s&h).bit_count() for h in H) for s in T];C=[[-(1+3*i+k),-(1+3*j+k)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(3)]+[[-(1+3*i+k),-(1+3*i+h)] for i in range(n) for k,h in combinations(range(3),2)];g=3*n+1
    for t,z in zip(T,q):
        for ks in combinations(range(3),2):C.append([-(g+z)]+[1+3*i+k for i in bits(t) for k in ks])
    C.extend([[-(g+a+1)]+[1+3*i+k for i in bits(t) for k in range(3)] for t in U]);out={};witness=None
    with Solver(name='g4',bootstrap_with=C) as sat:
        for name,Q in [('exact',[a]),('near',[a-1]),('other',list(range(a-1))+[a]),('all',list(range(a+1))),('full',list(range(a+2)))]:
            ok=sat.solve(assumptions=[g+z for z in Q]);out[name]=ok
            if ok:
                m=set(sat.get_model());S=[sum(1<<i for i in range(n) if 1+3*i+k in m) for k in range(3)];assert all(not s&t for s,t in combinations(S,2)) and all(s in I for s in S);assert all(sum(bool(s&t) for s in S)>=2 for t,z in zip(T,q) if z in Q)
                if name=='full':verify(grow(H,S),a+2);witness=S
    return dict(rows=len(T),near_rows=q.count(a-1),tests=out,witness=witness)
if __name__=='__main__':
    samples=json.loads((D/'ramsey_square_level_transfer.json').read_text());z={}
    for k,n in ((4,8),(5,13),(6,17),(7,22),(8,27)):
        f=D/'pauli-realization-catalogues'/f'r3{k}_{n}.g6';lines=(gzip.decompress(f.with_suffix('.g6.gz').read_bytes()) if k==8 else f.read_bytes()).splitlines();rs=[dict(record=r['record'],**audit(graph(lines[r['record']-1]))) for r in samples[str(k)]];print(n,len(rs),{p:sum(r['tests'][p] for r in rs) for p in rs[0]['tests']},flush=True);z[k]=rs
    (D/'ramsey_near_row_level_transfer.json').write_text(json.dumps(z)+'\n')
