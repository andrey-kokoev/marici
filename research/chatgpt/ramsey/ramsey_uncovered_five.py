"""Enumerate inclusion-maximal top-feasible partial three-colourings modulo colour names. Adding a vertex to a support preserves row coverage. At maximality every uncoloured vertex sees all three colours. An unhit five is dominating (else extends to a six with at most one colour)."""
from ramsey_near_row_level_transfer import D,json,graph,inds,bits,combinations,Counter,Solver
from itertools import permutations

def audit(H):
    n=len(H);I=inds(H);T=[t for t in I if t.bit_count()==6];U=[t for t in I if t.bit_count()==5 and not any(t&~s==0 for s in T)];v=lambda i,k:1+3*i+k
    C=[[-v(i,k),-v(j,k)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(3)]+[[-v(i,k),-v(i,h)] for i in range(n) for k,h in combinations(range(3),2)]
    C += [[v(i,k) for i in bits(t) for k in ks] for t in T for ks in combinations(range(3),2)]
    C += [[v(i,h) for h in range(3)]+[v(j,k) for j in bits(H[i])] for i in range(n) for k in range(3)]
    rows=[]
    with Solver(name='g4',bootstrap_with=C) as sat:
        while sat.solve():
            m=set(sat.get_model());S=sorted(sum(1<<i for i in range(n) if v(i,k) in m) for k in range(3));union=sum(S);bad=[t for t in U if not t&union];assert all(t in U or t&union for t in I if t.bit_count()==5);R=((1<<n)-1)^union;edges=[(1<<i)|(1<<j) for i,j in combinations(bits(R),2) if H[i]>>j&1];matching=next((e for e in combinations(edges,3) if (e[0]|e[1]|e[2]).bit_count()==6),None);assert [s.bit_count() for s in S]==[5,5,5] and bool(matching)==(not bad);rows.append(dict(S=S,bad=bad,leftover=R,matching=matching,two_covers=[R^t for t in bad]));
            for p in set(permutations(S)):sat.add_clause([(-1 if s>>i&1 else 1)*v(i,k) for k,s in enumerate(p) for i in range(n)])
    return rows
if __name__=='__main__':
    ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();prev=json.loads((D/'ramsey_near_row_level_transfer.json').read_text())['7'];z={}
    for r in prev:
        if not r['tests']['all']:continue
        i=r['record'];rows=audit(graph(ls[i-1]));assert any(not x['bad'] for x in rows)==r['tests']['full'];z[i]=rows;print(i,len(rows),dict(Counter(len(x['bad']) for x in rows)),len(set.intersection(*(set(x['bad']) for x in rows))),flush=True)
    (D/'ramsey_uncovered_five.json').write_text(json.dumps(z)+'\n')
