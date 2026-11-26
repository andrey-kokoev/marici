"""Interval LP certificate with shared edit variables. Supports have size 6 or 7. For a core blue Q the missed-row cap is 8-|Q| unless some proposed red edit is inside Q. Vertex budgets include incident edits, edited endpoints cannot share a support. Solve with violated clique cuts; certify an upper bound by exact integer column pricing, not float infeasibility."""
import json,sys,collections,concurrent.futures as cf
import numpy as np
from scipy.optimize import linprog
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_gain26_minimal.json').read_text());path=P/'ramsey_gain26_budget_joint.json';old=json.loads(path.read_text()) if path.exists() else [];done={z['idx'] for z in old};cleared={z['idx'] for z in json.loads((P/'ramsey_gain26_minimal_portfolio.json').read_text())}|{z['idx'] for z in json.loads((P/'ramsey_gain26_minimal_dual8.json').read_text()) if z['excludes']}
def solve(idx):
 a=R[idx]['adj'];e=R[idx]['edges'];K=80-e
 if K<0:return dict(idx=idx,excluded=True,kind='budget')
 I=[0];
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
 S=np.array([s for s in I if s.bit_count()>=6]);E=np.array([1<<i|1<<j for i,v in enumerate(a) for j in range(i) if not v>>j&1 and not v&a[j]]);n=len(S);m=len(E);Q=np.array([q for q in I if q.bit_count()>=5]);k=np.array([int(q).bit_count() for q in Q]);M=(S&Q[:,None])==0;W=(E&Q[:,None])==E;B=[];caps=[];names=[]
 def add(name,x,y,c):B.append(np.r_[x,y].astype(np.int32));caps.append(c);names.append(name)
 add('budget',np.zeros(n),np.ones(m),K)
 for i,v in enumerate(a):
  x=(S>>i)&1;y=(E>>i)&1;add(['vertex',i],x,y,8-v.bit_count());add(['minvertex',i],-x,-y,v.bit_count()-7)
 for j,s in enumerate(E):add(['edit',int(s)],(S&s)==s,8*(np.arange(m)==j),8)
 active=set();best=None;z=dict(idx=idx,excluded=False,kind='relaxed');
 for it in range(48):
  A=np.array(B);C=np.array(caps);res=linprog(-np.r_[np.ones(n),np.zeros(m)],A_ub=A,b_ub=C,method='highs');
  if not res.success: z['status']=res.message;break
  y=np.maximum(0,np.rint(-1e6*res.ineqlin.marginals)).astype('int64');coef=y@A;den=int(min(coef[:n]));# pay for negative edit column costs by increasing budget multiplier
  extra=max(0,-int(min(coef[n:],default=0)));y[0]+=extra;num=int(y@C);z.update(lp=float(-res.fun),rounds=it+1)
  if den>0 and num<8*den:
   assert min((y@A)[n:],default=0)>=0;z.update(excluded=True,num=num,den=den,weights=[[names[j],int(y[j])] for j in np.flatnonzero(y)]);break
  err=M@res.x[:n]-k*(W@res.x[n:])-(8-k);ix=[int(j) for j in np.argsort(-err)[:24] if err[j]>1e-7 and int(j) not in active]
  if not ix:break
  for j in ix:active.add(j);add(['miss',int(Q[j])],M[j],-k[j]*W[j],8-int(k[j]))
 return z
if __name__=='__main__':
 todo=sorted(set(range(len(R)))-done-cleared,key=lambda i:-R[i]['edges'])[:int(sys.argv[1])];
 with cf.ProcessPoolExecutor(int(sys.argv[2])) as ex:
  for f in cf.as_completed([ex.submit(solve,i) for i in todo]):old.append(f.result());path.write_text(json.dumps(old)+'\n')
 print('solved',len(old),'new exclusions',sum(z['excluded'] for z in old))
