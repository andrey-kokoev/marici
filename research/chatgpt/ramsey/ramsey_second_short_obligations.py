"""Query unconditional singleton and binary obligations on an unrestricted second port; use previously verified maximal-second labels only to audit coverage."""
from ramsey_sat_prefix_pilot import *
from statistics import median

def run():
    starts=json.loads((D/'ramsey_second_port_core_transfer.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];last=None
    for r in starts:
        idx=r['record'];a=r['first']
        if idx!=last:
            H=decode(lines[idx-1]);I=inds(H);n=len(H);edges=[[-(i+d+1),-(j+d+1)] for i,j in combinations(range(n),2) if H[i]>>j&1 for d in (0,n,2*n)];last=idx
        C=edges.copy()
        for t in I:
            z=7-t.bit_count()-int(not a&t);assert z>=0
            if z<3:
                for ports in combinations(range(3),z+1):C.append([1+i+p*n for p in ports for i in bits(t)])
        obs=[]
        with Solver(name='g4',bootstrap_with=C) as sat:
            for k in (1,2):
                for vs in combinations(range(n),k):
                    if not sat.solve(assumptions=[-1-i for i in vs]):obs.append(sum(1<<i for i in vs))
        assert all(s&g for s in r['good'] for g in obs);bad=[s for s,_ in r['failures']];single=[g for g in obs if g.bit_count()==1];pair=[g for g in obs if g.bit_count()==2 and not any(g&h for h in single)];coverage=lambda rules:sum(any(not s&g for g in rules) for s in bad);out.append(dict(record=idx,first=a,bad=len(bad),single=coverage(single),combined=coverage(single+pair),singletons=single,pairs=pair))
    return out
if __name__=='__main__':
    z=run();print([sum(r[k] for r in z) for k in ('bad','single','combined')],sum(2*r['combined']>r['bad'] for r in z),median(r['combined']/r['bad'] for r in z),sum(r['combined']==r['bad'] for r in z));print(min(z,key=lambda r:r['combined']/r['bad']));(D/'ramsey_second_short_obligations.json').write_text(json.dumps(z)+'\n')
