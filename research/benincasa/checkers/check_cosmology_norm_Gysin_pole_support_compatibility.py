#!/usr/bin/env python3
"""DPC exact support preflight for norm correction versus Gysin connection."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
interface=json.loads((R/'cosmology_cm_triangular_connection_interface_gate.json').read_text());prior=json.loads((R/'cosmology_norm_to_Xi_log_specialization_map.json').read_text());assert interface['passed'] and prior['passed']
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim(c)
def scale(a,q):return trim([q*x for x in a])
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def deriv(a):return [F(i)*a[i] for i in range(1,len(a))] or [F(0)]
def rem(a,b):
 a=a[:]
 while len(a)>=len(b) and a!=[0]:
  q=a[-1]/b[-1];d=len(a)-len(b)
  for i,x in enumerate(b):a[i+d]-=q*x
  trim(a)
 return a
def gcd(a,b):
 while b!=[0]:a,b=b,rem(a,b)
 return scale(a,F(1,a[-1]))
u=[F(0),F(1)];one=[F(1)];P=mul(mul(u,add(u,[-1])),add(u,[-2]));D=[F(4),F(-12),F(1),F(12),F(-4)]
# numerator of 2/u+2/(u-1)+2/(u-2)-D'/D over P*D
num=add(add(scale(mul(mul(add(u,[-1]),add(u,[-2])),D),2),scale(mul(mul(u,add(u,[-2])),D),2)),add(scale(mul(mul(u,add(u,[-1])),D),2),scale(mul(deriv(D),P),-1)))
den=mul(P,D);assert gcd(num,den)==one and gcd(D,deriv(D))==one
assert [sum(D[i]*F(a)**i for i in range(len(D))) for a in [0,1,2]]==[4,1,16]
out={'schema':'marici.benincasa.cosmology-norm-Gysin-pole-support-compatibility.v1','conjecture':'every norm-residual pole component lies in typed weighted-Gysin singular support','norm_coordinate_ring':'Q[u]','norm_form':'2*dlog(u*(u-1)*(u-2)/sqrt(D))','D':'-4*u^4+12*u^3+u^2-12*u+4','norm_reduced_denominator':'u*(u-1)*(u-2)*D','rational_pole_components':['u','u-1','u-2','D'],'rational_point_residues':{'0':2,'1':2,'2':2},'D_root_residue':-1,'D_squarefree':True,'Gysin_coordinate_ring':'Q[s1,s2,s3]','Gysin_declared_denominator':interface['available']['denominator'],'required_base_map':'Q[s1,s2,s3] -> Q[u]','typed_base_map_found':False,'support_pullback_defined':False,'conjecture_disposition':'rejected as ill-typed under the active source envelope','reason':'without a source-derived base map, Gysin divisors cannot be pulled back to the u-line and component containment has no meaning','next_conjecture':'the active artifacts contain a source-derived p-locus map assigning s1,s2,s3 as rational functions of u','next_falsifier':'exhaust the p-locus parametrization artifacts and check whether the assignments pull back the declared Gysin denominator','passed':True};(R/'cosmology_norm_Gysin_pole_support_compatibility.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
