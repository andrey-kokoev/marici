"""Fix one port; classify every maximal second without skipping. Three independently encoded free ports, symmetry unrestricted. Measure transfer of the first raw Glucose assumption core per failure."""
from ramsey_sat_prefix_pilot import *
from ramsey_fork_audit_uniform import grow,verify
from collections import Counter
from statistics import median

def run():
    keys=json.loads((D/'ramsey_small_obligation_holdout.json').read_text());starts=sorted({(r['record'],a) for r in keys for a in r['pair']});lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];prev=None
    for idx,a in starts:
        if idx!=prev:
            H=decode(lines[idx-1]);I=inds(H);n=len(H);M=sorted(s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)));A=[[-i-1 for i in range(n) if not m>>i&1] for m in M];edges=[[-(i+d+1),-(j+d+1)] for i,j in combinations(range(n),2) if H[i]>>j&1 for d in (0,n,2*n)];prev=idx
        C=edges.copy()
        for t in I:
            z=7-t.bit_count()-int(not t&a);assert z>=0
            if z>=3:continue
            for ports in combinations(range(3),z+1):C.append([1+i+p*n for p in ports for i in bits(t)])
        good=[];bad=[]
        with Solver(name='g4',bootstrap_with=C) as sat:
            for m,u in zip(M,A):
                if sat.solve(assumptions=u):
                    sol=set(sat.get_model());p=[sum(1<<i for i in range(n) if 1+i+k*n in sol) for k in range(1,3)];verify(grow(H,[a,m,*p]),8);good.append(m)
                else:
                    core=sat.get_core();assert core and set(core)<=set(u);g=sum(1<<(-l-1) for l in core);bad.append((m,g))
        assert good;hist=Counter();witness=None
        for m,g in bad:
            assert all(t&g for t in good);others=sum(not t&g for t in M)-1;hist[others]+=1
            if others and witness is None:witness=dict(origin=m,also=next(t for t in M if t!=m and not t&g),guard=list(bits(g)))
        out.append(dict(record=idx,first=a,good=good,failures=bad,hist=hist,example=witness))
    return out
if __name__=='__main__':
    z=run();h=sum((r['hist'] for r in z),Counter());print(len(z),sum(len(r['good']) for r in z),sum(h.values()),h[0],median(h.elements()),sum(sum(r['hist'].values())>2*r['hist'][0] for r in z));print(z[0]['example']);(D/'ramsey_second_port_core_transfer.json').write_text(json.dumps(z)+'\n')
