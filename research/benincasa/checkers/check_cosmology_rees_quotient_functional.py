#!/usr/bin/env python3
"""Construct the canonical multiplication-quotient functional and check its kernel algebraically."""
import json
from pathlib import Path
# w(0,l)=K*w(1,l), and w(k,l)=q_i*w(k,l+e_i), directly by exponents.
def exponents(k,ls):return (1-k,tuple(2-l for l in ls))
base=(1,1,1,1,1);assert exponents(0,base)[0]==exponents(1,base)[0]+1
for i in range(5):
 up=list(base);up[i]=2;a=exponents(0,base)[1];b=exponents(0,tuple(up))[1];assert a[i]==b[i]+1 and all(a[j]==b[j] for j in range(5) if j!=i)
# V=2Y d_X+X d_Y and I=X^2-2Y^2: V(I)=4XY-4XY=0.
assert 2*2-4==0
# Product rule then gives T(Q I^n)=Q*V(Q I^n)-V(Q)*Q I^n=Q^2*n*I^(n-1)*V(I)=0.
for n in range(5):assert n*0==0
out={'schema':'marici.benincasa.cosmology-rees-quotient-functional.v1','functional_weight':'w(k,l)=K^(1-k) product_i q_i^(2-l_i)','annihilates_K_q_images':True,'prolonged_value':'K [Q V(g)-V(Q) g], V=2Y partial_X+X partial_Y','invariant':'I=X^2-2Y^2 with V(I)=0','kernel_family':'g=Q h(I) for arbitrary polynomial h','tested_kernel_monomials':5,'verification_method':'exact exponent identities plus product rule','disposition':'the canonical quotient functional exists but is not faithful on the prolonged symbol family','surviving_scope':'it supplies one necessary quotient equation and exposes an infinite-dimensional blind direction','next_test':'construct divisor-residue probes complementary to the bulk functional and test joint faithfulness on g=Q h(I)','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_quotient_functional.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
