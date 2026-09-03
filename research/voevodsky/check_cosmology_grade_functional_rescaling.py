"""Classify the exact grade-7 to grade-8 surviving-line functional rescaling."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_functional_rescaling.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def main():
 d=json.loads((RES/'cosmology_surviving_line_transport.json').read_text());g7,g8=d['groups'];s7=[q(x['scalar']) for x in g7['A12_to_A14_x2_multipliers']];s8=[q(x['scalar']) for x in g8['A12_to_A14_x2_multipliers']];y7=[q(x) for x in g7['y_path_scalar_vector']];y8=[q(x) for x in g8['y_path_scalar_vector']];ds=[b/a for a,b in zip(s7,s8)];dy=[b/a for a,b in zip(y7,y8)];assert ds==dy==[Fraction(1),Fraction(12),Fraction(-108),Fraction(-16)]
 out={'schema':'marici.voevodsky.cosmology-grade-functional-rescaling.v1','status':'exact_common_diagonal_rescaling','diagonal_weights':[enc(x) for x in ds],'holds_for_seed_and_y_path_vectors':True,'decision':'Grade 8 is obtained from grade 7 by the same target-indexed diagonal rescaling on both seed and y2-path scalar vectors.','claim_boundary':'The diagonal is coordinate-indexed finite data; no source-typed grading operator or all-even law is established.','next_gate':'identify-source-descriptor-origin-of-diagonal-weights','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
