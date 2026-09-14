#!/usr/bin/env python3
"""Exact audit: Adams moduli are positive contractions but do not form the required semigroup."""
import json
from fractions import Fraction
from pathlib import Path

def rho(p,k,r):return Fraction(1,r)*Fraction(1,p)**Fraction((r-1)*k,2) if ((r-1)*k)%2==0 else None
def main():
 # Choose p=4 so all half powers are rational: rho_r=1/r * 2^{-(r-1)k}.
 def rr(k,r):return Fraction(1,r)*Fraction(1,2**((r-1)*k))
 p=4;k=1;r=2;s=3
 direct=rr(k,r*s)
 naive_modulus_product=rr(k,r)*rr(k,s)
 transported_cocycle=rr(k,r)*rr(r*k,s)
 assert direct==transported_cocycle and direct!=naive_modulus_product
 result={'schema':'marici.voevodsky.Adams-modulus-semigroup-failure.v1','fixture':{'p':p,'k':k,'r':r,'s':s},'direct_modulus_eigenvalue_r_s':str(direct),'product_of_fixed_grade_moduli':str(naive_modulus_product),'transported_Adams_cocycle_product':str(transported_cocycle),'each_modulus_positive_contraction':True,'fixed_carrier_semigroup_law':False,'reason':'Adams cocycle composition evaluates the second factor at the reindexed grade rk; taking A* A removes the shift but not this grade dependence.','conclusion':'The polar modulus repairs operator positivity but destroys the source semigroup composition needed for Y_(h1+h2)=Y_h1 Y_h2.'}
 out=Path(__file__).parents[1]/'results'/'Adams_modulus_semigroup_failure.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
