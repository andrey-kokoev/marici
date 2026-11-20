"""Existential 15th-address profiles; old 14-address completion is not preselected.
uv run --with python-sat python research/chatgpt/ramsey/ramsey_38_fifteenth_profile.py
"""
from itertools import combinations,product
from collections import Counter
from pysat.solvers import Solver

def main():
    V=range(15); tests=(4,2,1,6,5,3); edge={e:i+1 for i,e in enumerate(combinations(V,2))}
    clauses=[[-edge[e] for e in combinations(t,2)] for t in combinations(V,3)]+[[edge[e] for e in combinations(t,2)] for t in combinations(V,8)]
    for p,t in product(range(8),range(6)):
        clauses.append([edge[p,8+t] if p&tests[t]==tests[t] else -edge[p,8+t]])
    counts=Counter();accepted=[];rejected=[]
    with Solver(name='cadical195',bootstrap_with=clauses) as s:
        for m in range(256):
            pins=[edge[p,14] if m>>p&1 else -edge[p,14] for p in range(8)]
            ok=s.solve(assumptions=pins);counts[m&1,m>>7,ok]+=1
            (accepted if ok else rejected).append(m)
            if ok:
                model=set(s.get_model());assert all(any(l in model for l in c) for c in clauses);assert all(l in model for l in pins)
    print(sorted(counts.items()));print('exceptional failures', [hex(m) for m in rejected if not(m>>7 and not m&1)]);print('valid',len(accepted))
if __name__=='__main__':main()
