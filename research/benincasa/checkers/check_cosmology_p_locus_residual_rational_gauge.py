#!/usr/bin/env python3
"""DPC rational-gauge test for the p-locus connection residual."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_p_locus_horizontal_residual.json').read_text());assert prior['passed']
# Ascending coefficients.
D=[4,-12,1,12,-4];S=[0,2,-3,1];P=[8,-36,66,-45,-8,18,-4]
def der(A):return [Fraction(i)*A[i] for i in range(1,len(A))]
def mul(A,B):
 C=[Fraction(0)]*(len(A)+len(B)-1)
 for i,a in enumerate(A):
  for j,b in enumerate(B):C[i+j]+=a*b
 return C
def sub(A,B):
 n=max(len(A),len(B));return [(A[i] if i<len(A) else 0)-(B[i] if i<len(B) else 0) for i in range(n)]
calc=sub(mul(D,der(S)),[x/2 for x in mul(der(D),S)]);assert calc==list(map(Fraction,P))
# D has no rational root and no integral quadratic factor; Gauss gives irreducibility over Q.
cands={Fraction(a,b) for a in (1,-1,2,-2,4,-4) for b in (1,2,4)}
def ev(A,x):return sum(Fraction(c)*x**i for i,c in enumerate(A))
assert all(ev(D,x)!=0 for x in cands)
sol=[]
for a in [i for i in range(-4,5) if i and -4%i==0]:
 for d in [i for i in range(-4,5) if i and a*i==-4]:
  for c in [i for i in range(-4,5) if i and 4%i==0]:
   f=4//c
   for b in range(-30,31):
    for e in range(-30,31):
     if [c*f,b*f+c*e,a*f+b*e+c*d,a*e+b*d,a*d]==D:sol.append((a,b,c,d,e,f))
assert sol==[]
out={'schema':'marici.benincasa.cosmology-p-locus-residual-rational-gauge.v1','conjecture':'the p-locus residual is the logarithmic derivative of a rational gauge over Q(u)','denominator_factors':['u','u-1','u-2','D(u)'],'D':'-4*u^4+12*u^3+u^2-12*u+4','D_irreducible_over_Q':True,'residues_at_u_0_1_2':[1,1,1],'exact_decomposition':'dlog(u*(u-1)*(u-2)) - (1/2)*dlog(D)','required_gauge':'u*(u-1)*(u-2)/sqrt(D)','rational_gauge_exists':False,'falsification_reason':'the irreducible D factor would require valuation -1/2, but rational-function valuations are integral','conjecture_disposition':'falsified','quadratic_algebraic_gauge_exists':True,'quadratic_gauge_source_authorized':False,'next_conjecture':'sqrt(D) is supplied by an existing source-authorized two-cover on the p divisor','next_falsifier':'compare D with every declared quadratic-cover radicand up to rational squares and typed base maps','passed':True};(R/'cosmology_p_locus_residual_rational_gauge.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
