"""Split the non-K exactness problem into q-natural and IBP-Leibniz branches."""
from __future__ import annotations
import json
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_nonK_family_exactness_split.json'
def monomial_count(d):return (d+1)*(d+2)//2
def main():
 A=14
 ibp_rows=2*1*2*monomial_count(A)
 q_rows=5*3*16*monomial_count(A-1)
 assert ibp_rows==480 and q_rows==25200
 ibp_parity_seeds=2*2*4
 q_parity_seeds=5*3*16*4
 assert ibp_parity_seeds==16 and q_parity_seeds==960
 # Leibniz obstruction for shifting exponent e by x_axis^2:
 # d(x^(e+2))=(e+2)x^(e+1), whereas x^2 d(x^e)=e x^(e+1).
 for e in range(5):assert (e+2)-e==2
 out={'schema':'marici.voevodsky.cosmology-nonK-family-exactness-split.v1','status':'q_family_reduces_to_960_natural_seeds_IBP_requires_Leibniz_transport','degree14_counts':{'IBP':ibp_rows,'marked_q':q_rows},'q_branch':{'descriptor_factors':'5 marked q choices * 3 K poles * 16 compatible level patterns * exponents','axis_square_naturality':'q-multiplication relations commute with monomial multiplication','A12_parity_seeds_required':q_parity_seeds},'IBP_branch':{'descriptor_factors':'2 K poles * 2 fiber axes * all-one level pattern * exponents','formal_parity_seeds':ibp_parity_seeds,'transport_obstruction':'IBP does not commute literally with square multiplication: I_axis(e+2 axis)-x_axis^2 I_axis(e) contains the Leibniz term 2*x_axis^(e+1)','required_correction':'derive the extra Leibniz column through sourced K/q/IBP relations before any seed induction'},'decision':'The non-K problem must split. Exact q seeds can be tested immediately using established Q naturality; IBP needs a separate corrected transport law, so 16 seed solves alone would not prove an unbounded theorem.','next_gate':'exact-solve the 960 q parity seeds over Q, then derive and verify the corrected IBP square-shift identity','limitations':['counts and transport typing only','does not establish exact q seeds or the IBP correction','no complete rank-26 theorem, horn, or Bockstein'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
