"""Exact finite tests of algebraic Ramsey extension obstruction.
An independent-set polynomial semiring has basis [S] for independent S;
[S]*[T]=[S union T] if the union is independent, else zero.
Independent (k-1)-sets I contribute p_I=sum([v] for v in I).
The product of p_I over a family F is zero iff no independent
S intersects every I in F. Coefficients are nonnegative; we track support.
"""
from pathlib import Path
from collections import Counter
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix
from ramsey_extension_blockers import parse_g6, independent_sets, greedy_certificate
import numpy as np

def supports(H,sets):
    support={0}
    for i,I in enumerate(sets,1):
        new=set()
        for S in support:
            for v in range(len(H)):
                if I>>v&1 and not (H[v]&S):new.add(S | (1<<v))
        support=new
        if not support:return i,[]
    return len(sets), sorted(support)

def maximal_independents(H,k):
    n=len(H)
    return [S for q in range(1,k) for S in independent_sets(H,q)
            if all((S>>v&1) or (H[v]&S) for v in range(n))]

def minimal_family(H,k,time_limit=12):
    all_I=independent_sets(H,k-1)
    max_S=maximal_independents(H,k)
    # A family F annihilates iff each maximal independent S
    # is disjoint from at least one member I of F.
    rows,cols=[],[]
    for r,S in enumerate(max_S):
        for c,I in enumerate(all_I):
            if (S&I)==0:rows.append(r);cols.append(c)
    M=csc_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(max_S),len(all_I)))
    res=milp(c=np.ones(len(all_I)),integrality=np.ones(len(all_I)),
             bounds=Bounds(0,1),constraints=LinearConstraint(M,1,np.inf),
             options={'time_limit':time_limit,'mip_rel_gap':0.0})
    if res.x is None:return {"status":res.status,"message":res.message}
    chosen=[all_I[i] for i,x in enumerate(res.x) if x>.5]
    stopped,left=supports(H,chosen)
    assert not left, (len(chosen),stopped,len(left))
    return {"status":res.status,"minimum_if_optimal":len(chosen),
            "lower_bound":getattr(res,'mip_dual_bound',None),
            "chosen":chosen,"number_of_maximal_independent":len(max_S),
            "maximal_sizes":dict(Counter(S.bit_count() for S in max_S))}

def main():
    for path,k in [('/mnt/data/ramsey37_first5.g6',7),('/mnt/data/ramsey36_all7.g6',6)]:
        print('DATA',path,flush=True)
        for i,line in enumerate(Path(path).read_text().splitlines(),1):
            H=parse_g6(line)
            counts,greedy=greedy_certificate(H,k)
            rounds,remaining=supports(H,greedy)
            assert remaining==[],f'greedy certificate fails on graph {i} at degree {k}'
            opt=minimal_family(H,k)
            print(i,'greedy',len(greedy),'zero round',rounds,
                  'MILP', {x:y for x,y in opt.items() if x!='chosen'},flush=True)
            if opt.get('chosen') and i==1:
                print('CERTIFICATE',[[v for v in range(len(H)) if S>>v&1] for S in opt['chosen']],flush=True)

if __name__=='__main__': main()
