"""Strict threshold test on the first 20-address prefix of the delay experiment.
For repeated eigenvalues test the whole eigenspace, not an arbitrary basis.
LP feasibility: scale any strict separating gap to margin one on both sides.
"""
import numpy as np
from scipy.optimize import linprog
from ramsey_37_pair_rotation_rule import build
from ramsey_delayed_address_move import moves


def main():
    n=20;rows=[r&((1<<n)-1) for r in build()[:n]]
    _,six,legal=moves(rows); A=np.array([[r>>j&1 for j in range(n)] for r in rows]);w,V=np.linalg.eigh(A);blocks=np.split(np.arange(n),np.where(np.diff(w)>1e-8)[0]+1)
    print('six sets',six,'legal',len(legal),'spectrum',[(round(w[b[0]],5),len(b)) for b in blocks]);found=set()
    for b in blocks:
        E=V[:,b];hit=[]
        for p in legal:
            y=np.array([1 if p>>i&1 else -1 for i in range(n)]); X=np.column_stack((E,-np.ones(n)))
            lp=linprog(np.zeros(X.shape[1]),A_ub=-y[:,None]*X,b_ub=-np.ones(n),bounds=(None,None),method='highs')
            if lp.success:
                assert min(y*(X@lp.x))>.99
                hit.append([i for i in range(n) if p>>i&1]);found.add(p)
            else:assert lp.status==2
        if hit:print('hit eigenvalue',w[b[0]],hit)
    print('legal columns found',len(found));print('legal sets',[[i for i in range(n) if p>>i&1] for p in legal]);print('omitted original address neighbors',[i for i in range(n) if build()[20]>>i&1])

if __name__=='__main__':main()
