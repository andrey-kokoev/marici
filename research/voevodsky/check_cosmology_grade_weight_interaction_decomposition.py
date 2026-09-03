"""Compute the unique square-domain interaction decomposition of grade weights."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_weight_interaction_decomposition.json'
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def main():
 d=json.loads((RES/'cosmology_grade_weight_descriptors.json').read_text());w={tuple(x['descriptor'][4]):Fraction(x['weight']) for x in d['attachments']};C=w[0,0];rx=w[1,0]/C;ry=w[0,1]/C;k=w[1,1]/(C*rx*ry);assert (C,rx,ry,k)==(Fraction(12),Fraction(-9),Fraction(-4,3),Fraction(1,144));assert all(w[a,b]==C*rx**a*ry**b*k**(a*b) for a,b in w)
 out={'schema':'marici.voevodsky.cosmology-grade-weight-interaction-decomposition.v1','status':'unique_square_domain_bilinear_decomposition','C':enc(C),'x_factor':enc(rx),'y_factor':enc(ry),'mixed_factor':enc(k),'decision':'On the four binary exponent descriptors, the unique multiplicative-plus-bilinear decomposition is 12*(-9)^a*(-4/3)^b*(1/144)^(ab).','claim_boundary':'This parametrizes four exact values; it does not derive the mixed factor from tangent or quotient structure.','next_gate':'compare-interaction-factor-before-and-after-quotient-reduction','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
