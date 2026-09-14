"""Exact-rational denominator audit for labelled soft-axis L2 columns."""
import argparse,json,math
from fractions import Fraction as Q
from pathlib import Path

def add(x,y):
 z=x.copy()
 for m,c in y.items():z[m]=z.get(m,Q(0))+c
 return {m:c for m,c in z.items() if c}
def scale(x,c):return {m:c*x for m,x in x.items() if c*x}
def mul(x,y):
 z={}
 for (u,a,b),c in x.items():
  for (v,d,e),f in y.items():
   if u+v>=2:continue
   m=(u+v,a+d,b+e);z[m]=z.get(m,Q(0))+c*f
 return {m:c for m,c in z.items() if c}
def power(x,n):
 z={(0,0,0):Q(1)}
 for _ in range(n):z=mul(z,x)
 return z
def der(x,var):
 z={}
 for m,c in x.items():
  q=m[var]
  if q:
   n=list(m);n[var]-=1;z[tuple(n)]=c*q
 return z
def exact(sa,sb,f,isq,plus,k,l1,l2m,l2p):
 ea,eb=2-sa,2-sb;l2=l2p if plus else l2m;base=mul(power(l1,ea),power(l2,eb))
 if not isq:
  r=scale(mul(mul(der(f,2),base),k),-1)
  if sa:r=add(r,scale(mul(mul(f,mul(power(l1,ea-1),power(l2,eb))),k),sa))
  return add(r,scale(mul(mul(f,base),der(k,2)),Q(3,2)))
 r=mul(mul(der(f,1),base),k)
 if sb:r=add(r,scale(mul(mul(f,mul(power(l1,ea),power(l2,eb-1))),k),-sb))
 return add(r,scale(mul(mul(f,base),der(k,1)),Q(-3,2)))
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--cutoff',type=int,default=16);a=p.parse_args()
 one={(0,0,0):Q(1)};u={(1,0,0):Q(1)};aa={(0,1,0):Q(1)};b={(0,0,1):Q(1)}
 l1=add(add(b,one),scale(u,-1));l2m=add(aa,scale(u,Q(-1,2)));l2p=add(aa,scale(u,Q(1,2)))
 a2=power(aa,2);k=add(power(aa,4),add(mul(u,a2),scale(mul(mul(u,a2),power(b,2)),-1)))
 dens={};count=0
 for sa,sb in ((1,1),(1,0),(0,1),(0,0)):
  for s in range(a.cutoff+1):
   for i in range(s+1):
    f={(0,i,s-i):Q(1)}
    for plus in (False,True):
     for isq in (False,True):
      col=exact(sa,sb,f,isq,plus,k,l1,l2m,l2p);count+=1
      for (uu,_,_),c in col.items():dens[(uu,c.denominator)]=dens.get((uu,c.denominator),0)+1
 maxden=max(d for _,d in dens);assert set(d for _,d in dens)<= {1,2}
 assert all(d==1 for (uu,d) in dens if uu==0)
 # All-degree denominator certificate. Since u^2=0, powers used here have
 # exponents at most two. Every base/reduced-base multiplier has integral u0
 # part and denominator at most two in u1. The only explicit 3/2 factors
 # multiply derivatives of k whose coefficients are divisible by two.
 def lattice_ok(poly):
  return all(c.denominator==1 if m[0]==0 else c.denominator<=2 for m,c in poly.items())
 symbolic_cases=[]
 for sa,sb in ((1,1),(1,0),(0,1),(0,0)):
  ea,eb=2-sa,2-sb
  for l2name,l2 in (('minus',l2m),('plus',l2p)):
   base=mul(power(l1,ea),power(l2,eb));assert lattice_ok(base)
   if ea:assert lattice_ok(mul(power(l1,ea-1),power(l2,eb)))
   if eb:assert lattice_ok(mul(power(l1,ea),power(l2,eb-1)))
   symbolic_cases.append({'sa':sa,'sb':sb,'side':l2name,'base_lattice_ok':True})
 assert all(c.denominator==1 for c in scale(der(k,2),Q(3,2)).values())
 assert all(c.denominator==1 for c in scale(der(k,1),Q(3,2)).values())
 out={'schema':'marici.nima.L2-integral-denominator-lattice.v1','status':'proved','cutoff':a.cutoff,
  'columns':count,'denominator_counts':{f'u{u}_den{d}':n for (u,d),n in sorted(dens.items())},
  'maximum_denominator':maxden,'u0_sector_integral':True,
  'all_degree_symbolic_cases':symbolic_cases,
  'explicit_three_halves_terms_integral':True,
  'conclusion':'in all degrees, half-integrality is confined to the square-zero u sector; rescaling u/2 as integral generator clears every labelled column',
  'qualification':'all-degree denominator theorem/presentation only; Smith form of the Bockstein relation lattice remains open'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
