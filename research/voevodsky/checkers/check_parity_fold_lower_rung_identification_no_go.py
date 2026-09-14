#!/usr/bin/env python3
"""Exact no-go for identifying a parity fold with the standard lower translate rung."""
import json
from fractions import Fraction
from pathlib import Path

def main():
 k0=Fraction(1);k1=Fraction(1,2);k2=Fraction(1,4)
 # Positive Toeplitz fixture.
 det3=k0**3-2*k0*k1**2+2*k1**2*k2-k0*k2**2
 assert det3>0
 # In orthonormal basis e+=(e1+e3)/sqrt(2), e2, the diagonal is (k0+k2,k0).
 even_diagonal=[k0+k2,k0]
 odd_scalar=k0-k2
 standard_lower_diagonal=[k0,k0]
 assert even_diagonal!=standard_lower_diagonal and odd_scalar!=k0
 result={'schema':'marici.voevodsky.parity-fold-lower-rung-identification-no-go.v1','positive_toeplitz_fixture':{'K0':str(k0),'K1':str(k1),'K2':str(k2),'rank_three_determinant':str(det3)},'orthonormal_even_fold':{'diagonal':[str(x) for x in even_diagonal],'off_diagonal':'sqrt(2) K1'},'odd_fold_rank_one_value':str(odd_scalar),'standard_lower_translate_diagonal':[str(x) for x in standard_lower_diagonal],'natural_identification_holds':False,'generic_obstruction':'Even-fold diagonal entries are K0+K2 and K0; equality with a standard two-translate rung requires K2=0. The odd fold has value K0-K2 rather than K0.','conclusion':'Parity negativity descends to lower dimension but not to the same translate-rung object. Closing under folds introduces symmetric/antisymmetric wavelet packets whose rank-one positivity is not supplied by base translate positivity.'}
 out=Path(__file__).parents[1]/'results'/'parity_fold_lower_rung_identification_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
