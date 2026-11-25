"""Combine discovered shadow columns, solve the full-support LP on those columns, then reconstruct a rational primal basis and verify every inequality over integers."""
from ramsey312_fractional_shadow import *
import numpy as np
from scipy.linalg import qr
from flint import fmpz_mat

def restricted(d,s,cols):
 n=len(cols);N=len(s);X=np.asarray(s,dtype=np.uint64)[:,None];g,b,t=map(lambda v:np.array(v,dtype=np.uint64),zip(*cols));M=((X&b!=0)&(X&t==0)).astype(np.int8);cost=np.array([int(x).bit_count() for x in g]);res=linprog(cost,A_ub=-M,b_ub=[-1]*N,method='highs');
 if not res.success or res.fun>d.bit_count()+1e-8:return None
 use=np.flatnonzero(res.x>1e-8);B=M[:,use];tight=B[abs(B@res.x[use]-1)<1e-8];tight=np.unique(tight,axis=0);_,_,piv=qr(tight.T.astype(float),pivoting=True,mode='economic');E=tight[piv[:len(use)]];m=len(use);A=fmpz_mat(E.tolist());v=A.solve(fmpz_mat([[1]]*m));w=[Fraction(str(v[j,0])) for j in range(m)];cert=[(*cols[i],a) for i,a in zip(use,w) if a];assert all(a>0 for g,b,t,a in cert) and sum(g.bit_count()*a for g,b,t,a in cert)==d.bit_count();return cert

def main():
 import sys,math
 el=list(sets(F,11));out=[]
 for suffix,f in zip(['','19'],sys.argv[1:]):
    r=json.loads((D/f'ramsey312_no_budget{suffix}.json').read_text());d,*s=map(int,open(f).read().split());ss=r['challenge'];cols=set();
    for it in range(100):
        val,y,c=solve(d,ss,el);cols.update((g,b,t) for g,b,t,a in c);assert val==6
        if it%4==3:
            cert=restricted(d,s,sorted(cols));print(d,it,len(cols),'exact',bool(cert),flush=True)
            if cert:break
        miss=[x for x in s if sum(a for g,b,t,a in c if x&b and not x&t)<1-1e-7];ss=ss+miss[::max(1,len(miss)//40)][:41]
    else:raise RuntimeError('not converged')
    den=math.lcm(*(a.denominator for g,b,t,a in cert));rows=[(g,b,t,int(a*den)) for g,b,t,a in cert];assert all(sum(w for g,b,t,w in rows if b&x and not t&x)>=den for x in s);out.append(dict(d=d,supports=len(s),den=den,rows=rows));(D/'ramsey312_exact_fractional_six.json').write_text(json.dumps(out));print('weights',len(rows),'denominator',den,flush=True)
if __name__=='__main__':main()
