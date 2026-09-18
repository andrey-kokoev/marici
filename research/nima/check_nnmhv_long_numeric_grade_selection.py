#!/usr/bin/env python3
"""Fast long-section test of the leading finite-cutoff grade."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def add(A,B):return tuple(a+b for a,b in zip(A,B))
def sub(A,B):return tuple(a-b for a,b in zip(A,B))
def mm(A,B):return (A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3])
def rm(r,A):return (r[0]*A[0]+r[1]*A[2],r[0]*A[1]+r[1]*A[3])
def mv(A,v):return (A[0]*v[0]+A[1]*v[1],A[2]*v[0]+A[3]*v[1])
def dot(r,v):return r[0]*v[0]+r[1]*v[1]
def det(A):return A[0]*A[3]-A[1]*A[2]
def adj(A):return (A[3],-A[1],-A[2],A[0])
def outer(a,b):return (a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
def angle(a,b):return a[0]*b[1]-a[1]*b[0]
def section(n,lf,tf):
 lam={i:(1.0,float(lf(i))) for i in range(1,n+1)};til={i:(1.0,float(tf(i))) for i in range(1,n-1)};M=(0.,0.,0.,0.)
 for i in range(1,n-1):M=add(M,outer(lam[i],til[i]))
 L=(lam[n-1][0],lam[n][0],lam[n-1][1],lam[n][1]);Li=tuple(v/det(L) for v in adj(L));Y=mm(Li,tuple(-v for v in M));til[n-1]=(Y[0],Y[1]);til[n]=(Y[2],Y[3]);x={1:(0.,0.,0.,0.)}
 for i in range(1,n+1):x[i+1]=sub(x[i],outer(lam[i],til[i]))
 return lam,x
def interval(x,a,b):return sub(x[a],x[b])
def transport(lam,x,verts):
 r=(-lam[verts[0]][1],lam[verts[0]][0])
 for k,(a,b) in enumerate(zip(verts,verts[1:])):r=rm(r,interval(x,a,b) if k%2==0 else adj(interval(x,a,b)))
 return r
def theta_coeff(lam,a,b,j):
 # coefficient of eta_j in theta_a-theta_b
 return tuple(((-1.0 if j<a else 0.0)-(-1.0 if j<b else 0.0))*v for v in lam[j])
def invariant(lam,x,n,prefix,pair,lower,upper):
 a,b=pair;r=prefix[-1] if prefix else n;xi=transport(lam,x,(n,)+prefix);eps=lambda row:(row[1],-row[0]);kb=eps(upper);kam1=eps(lower);Xra=interval(x,r,a);Xab=interval(x,a,b);Xrb=interval(x,r,b);Xba=interval(x,b,a);L=rm(rm(xi,Xra),adj(Xab));R=rm(rm(xi,Xrb),adj(Xba));q={j:dot(L,theta_coeff(lam,b,r,j))+dot(R,theta_coeff(lam,a,r,j)) for j in (2,3)}
 def sw(X1,X2,k):return dot(rm(rm(xi,X1),adj(X2)),k)
 ds=[det(Xab),sw(Xra,Xab,kb),sw(Xra,Xab,lam[b-1]),sw(Xrb,Xba,lam[a]),sw(Xrb,Xba,kam1)];pref=angle(lam[a],kam1)*angle(kb,lam[b-1])/math.prod(ds);return q,pref
def value(n,lf,tf):
 lam,x=section(n,lf,tf);total=0.;outer_cache={}
 for b1 in range(5,n):
  qo,po=invariant(lam,x,n,(),(2,b1),(-lam[1][1],lam[1][0]),(-lam[b1][1],lam[b1][0]));upper=transport(lam,x,(n,2,b1))
  for b2 in range(5,b1+1):
   qi,pi=invariant(lam,x,n,(b1,2),(3,b2),(-lam[2][1],lam[2][0]),upper if b2==b1 else (-lam[b2][1],lam[b2][0]));w=qo[2]*qi[3]-qo[3]*qi[2];total+=po*pi*w**4
 return total/angle(lam[2],lam[3])**4
def terminal_shell(n,lf,tf):
 lam,x=section(n,lf,tf);b1=n-1;qo,po=invariant(lam,x,n,(),(2,b1),(-lam[1][1],lam[1][0]),(-lam[b1][1],lam[b1][0]));upper=transport(lam,x,(n,2,b1));terms=[]
 for b2 in range(5,b1+1):
  qi,pi=invariant(lam,x,n,(b1,2),(3,b2),(-lam[2][1],lam[2][0]),upper if b2==b1 else (-lam[b2][1],lam[b2][0]));w=qo[2]*qi[3]-qo[3]*qi[2];terms.append(po*pi*w**4/angle(lam[2],lam[3])**4)
 return sum(terms),terms
families={'quadratic_cubic':(lambda j:j*j+j+1,lambda j:j**3+2*j+1),'quadratic_quartic':(lambda j:j*j+2*j+2,lambda j:j**4+j+1),'cubic_quadratic':(lambda j:j**3+j+1,lambda j:j*j+3*j+1)};old=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-cross-family-exponents.json').read_text());qold=json.loads((ROOT/'research/nima/results/nnmhv-full-sum-extended-sections.json').read_text());outf={}
for name,(lf,tf) in families.items():
 exact=(qold['sections'][-1]['normalized_value'] if name=='quadratic_cubic' else old['extended_families'][name]['sections'][-1]['value']);v16=value(16,lf,tf);sections=[]
 for n in (20,24,32,48,64):
  shell,terms=terminal_shell(n,lf,tf);vn=value(n,lf,tf);increment=vn-value(n-1,lf,tf);sections.append({'n':n,'value':vn,'net_increment':increment,'terminal_shell':shell,'prior_shell_reflow':increment-shell,'terminal_history_count':len(terms),'mean_terminal_history':shell/len(terms)})
 vals=[v16]+[r['value'] for r in sections];ns=[16,20,24,32,48,64];eff=[]
 for k in range(1,len(ns)-1):
  # unequal-spacing local exponent from three points, grid minimizing ratio residual with eliminated L,c.
  best=None
  for z in range(50,401):
   a=z/100;x=[q**(-a) for q in ns[k-1:k+2]];y=vals[k-1:k+2];L=(y[1]*x[0]-y[0]*x[1])/(x[0]-x[1]);pred=L+(y[0]-L)*x[2]/x[0];err=abs(pred-y[2]);best=min(best or (err,a), (err,a))
  eff.append({'center_n':ns[k],'alpha':best[1]})
 outf[name]={'relative_validation_error_n16':abs(v16-exact)/abs(exact),'long_sections':sections,'local_exponents':eff}
checks={'numeric_evaluator_matches_exact_n16':all(v['relative_validation_error_n16']<1e-9 for v in outf.values()),'all_long_values_finite':all(math.isfinite(r['value']) for v in outf.values() for r in v['long_sections'])}
out={'schema':'marici.nima.nnmhv-long-numeric-grade-selection.v1','families':outf,'checks':checks,'passed':all(checks.values()),'scope':'Fast double-precision supported-history sums through n=64; local exponent diagnostics.'};p=ROOT/'research/nima/results/nnmhv-long-numeric-grade-selection.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
