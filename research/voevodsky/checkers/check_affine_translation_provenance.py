"""Affine change y=x+t transports BOTH primitive rows and target bound."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def valid(p,L,T,t):
 a,b,c=map(Q,p);L,T,t=map(Q,(L,T,t))
 return L>0 and min(a,b,c)>=0 and b-a==1 and (-t)*a+(L+t)*b+c==T+t
def norm(p,L,T,t):
 assert valid(p,L,T,t)
 a,b,c=map(Q,p);q=(a+c/Q(L),b+c/Q(L),Q(0))
 assert valid(q,L,T,t);return q
def translate(p,L,T,t,rows=('lower:-y<=-t','upper:y<=L+t')):
 if rows!=('lower:-y<=-t','upper:y<=L+t'):raise PermissionError('MISSING_TRANSLATED_LOWER_ROW')
 assert valid(p,L,T,0)
 assert valid(p,L,T,t)
 return p
checks=0;lower_essential=0
for L,T,t in product((Q(1,2),Q(1),Q(2)),(Q(1),Q(2),Q(3)),(Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1),Q(2))):
 if T<L:continue
 for b in (Q(1),Q(3,2),T/L):
  c=T-L*b
  if c<0:continue
  p=(b-1,b,c)
  assert translate(p,L,T,t)==p
  assert norm(translate(p,L,T,t),L,T,t)==translate(norm(p,L,T,0),L,T,t)
  if t and b!=1:
   naive=(L+t)*b+c
   if naive!=T+t:lower_essential+=1
  checks+=1
assert checks>30 and lower_essential>0
p=(Q(1),Q(2),Q(1));assert valid(p,1,3,0)
assert valid(translate(p,1,3,1),1,3,1)
assert not ((Q(1)+Q(1))*p[1]+p[2]==Q(3)+Q(1))
try:translate(p,1,3,1,rows=('upper:y<=L+t',))
except PermissionError:omitted_lower_refused=True
else:raise AssertionError('untranslated lower primitive row admitted')
report={'passed':True,'translation_checks':checks,'naive_upper_only_failures':lower_essential,'naturality':'N_translated translate = translate N_original strictly on full two-row presentation','omitted_lower_row_refused':omitted_lower_refused,'scope':'Variable translation y=x+t with both primitive bounds and target bound shifted, L>0 and proof nonnegative. Not arbitrary source modification, proof-history identity, live authority or analytic role assignment.'}
out=Path(__file__).resolve().parents[1]/'results/affine-translation-provenance.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
