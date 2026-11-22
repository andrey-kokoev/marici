"""Fresh induced 21-vertex cores; target still (3,8). Commit rankings before labelling. Exhaust all maximal firsts with joint four-port SAT, verify each positive witness."""
from ramsey_sat_prefix_pilot import *
from ramsey_fork_audit_uniform import grow,verify
from random import Random
from statistics import median
from collections import Counter

def run():
    lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();used={r['record'] for r in json.loads((D/'ramsey_second_port_core_transfer.json').read_text())}|{r['record'] for r in json.loads((D/'ramsey_sat_learning_batch.json').read_text())};rng=Random(92517);out=[]
    for idx in sorted(rng.sample(sorted(set(range(1,len(lines)+1))-used),64)):
        orig=decode(lines[idx-1]);drop=rng.randrange(22);V=[i for i in range(22) if i!=drop];H=[sum(1<<j for j,y in enumerate(V) if orig[x]>>y&1) for x in V];n=len(V);I=inds(H);M=sorted(s for s in I if all(s>>i&1 or s&h for i,h in enumerate(H)));big=[t for t in I if t.bit_count()==6];assert max(map(int.bit_count,I))==6
        score={m:sum(not t&m for t in big) for m in M};rank1=sorted(M,key=lambda m:(score[m],m));rank2=sorted(M,key=lambda m:(-m.bit_count(),m));C=[[-(i+k*n+1),-(j+k*n+1)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(4)]
        for t in I:
            z=7-t.bit_count()
            if z<4:
                for ps in combinations(range(4),z+1):C.append([1+i+n*k for k in ps for i in bits(t)])
        good=[]
        with Solver(name='g4',bootstrap_with=C) as sat:
            for m in M:
                if sat.solve(assumptions=[-i-1 for i in range(n) if not m>>i&1]):
                    model=set(sat.get_model());S=[m]+[sum(1<<i for i in range(n) if n*k+i+1 in model) for k in (1,2,3)];verify(grow(H,S),8);good.append(m)
        pos=lambda order:next((i for i,m in enumerate(order,1) if m in good),None);out.append(dict(parent=idx,deleted=drop,firsts=len(M),good=good,obligation_attempts=pos(rank1),size_attempts=pos(rank2)))
    return out
if __name__=='__main__':
    out=run();(D/'ramsey_bare_core_rank.json').write_text(json.dumps(out)+'\n');z=[r for r in out if r['good']];d=[r['size_attempts']-r['obligation_attempts'] for r in z];print(len(z),median(d),Counter((x>0)-(x<0) for x in d),[median(r[k] for r in z) for k in ('obligation_attempts','size_attempts')]);
