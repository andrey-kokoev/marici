"""Test whether descriptor weights factor into independent x/y normalizations."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_weight_separability.json'
def main():
 d=json.loads((RES/'cosmology_grade_weight_descriptors.json').read_text());w={tuple(x['descriptor'][4]):Fraction(x['weight']) for x in d['attachments']};assert set(w)=={(0,0),(1,0),(0,1),(1,1)};lhs=w[1,1]*w[0,0];rhs=w[1,0]*w[0,1];k=lhs/rhs;assert lhs!=rhs and k==Fraction(1,144)
 out={'schema':'marici.voevodsky.cosmology-grade-weight-separability.v1','status':'independent_axis_factorization_falsified','weights':{str(k):int(v) for k,v in w.items()},'separability_lhs':int(lhs),'separability_rhs':int(rhs),'interaction_ratio':{'numerator':k.numerator,'denominator':k.denominator},'decision':'No factorization w(a,b)=C r^a s^b fits the four descriptor weights; the square interaction ratio is 1/144.','claim_boundary':'This is an exact obstruction to independent-axis normalization for these four weights, not a geometric interaction term.','next_gate':'classify-nonseparable-grade-rescaling-source','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
