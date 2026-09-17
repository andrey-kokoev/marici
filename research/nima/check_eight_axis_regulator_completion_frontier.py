#!/usr/bin/env python3
"""Materialize the eight-axis local cube and regulator/completion face frontier."""
import json,math,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
axes=('H_input_arity','V_output_arity','D_polarity','q_chart_successor','L_convolution_degree','C_realization_comparison','O_observation','R_regulator_completion')
n=len(axes)
counts={'vertices':2**n,'edges':n*2**(n-1),'squares':math.comb(n,2)*2**(n-2),'three_faces':math.comb(n,3)*2**(n-3),'four_faces':math.comb(n,4)*2**(n-4),'five_faces':math.comb(n,5)*2**(n-5),'six_faces':math.comb(n,6)*2**(n-6),'seven_faces':math.comb(n,7)*2,'eight_cells':1,'maximal_Freudenthal_8_simplices':math.factorial(n)}
regulator_faces={
 'R x H':'finite restriction acts cellwise on the nerve; completion compatibility requires the declared product-cell bounds',
 'R x V':'finite cut coaction exists; completed strictness depends on leakage convergence',
 'R x D':'constructed on aperture/projective graph completion',
 'R x q':'lax at finite cutoff via A_X=P_X F (I-P_X); strict completion requires compatible leakage nullhomotopy or convergence',
 'R x L':'character truncations and degree successors act on the common spectral tower; unbounded symbols require graph-domain invariance',
 'R x C':'completion-level comparison functor remains missing',
 'R x O':'weighted trace-class and joint-graph endpoint completion constructed in declared carriers; raw positive-leg strong convergence fails',
}
def gray(i):return i^(i>>1)
cycle=[tuple((gray(i)>>j)&1 for j in reversed(range(n))) for i in range(2**n)]
def ham(a,b):return sum(x!=y for x,y in zip(a,b))
checks={'eight_axes':n==8,'counts_exact':counts=={'vertices':256,'edges':1024,'squares':1792,'three_faces':1792,'four_faces':1120,'five_faces':448,'six_faces':112,'seven_faces':16,'eight_cells':1,'maximal_Freudenthal_8_simplices':40320},'cyclic_eight_bit_gray_code':all(ham(cycle[i],cycle[(i+1)%len(cycle)])==1 for i in range(len(cycle))),'all_seven_new_pair_types_classified':len(regulator_faces)==7,'full_eight_cell_constructed':False}
out={'schema':'marici.nima.eight-axis-regulator-completion-frontier.v1','axes':axes,'counts':counts,'regulator_pair_faces':regulator_faces,'checks':checks,'passed':all(v for k,v in checks.items() if k!='full_eight_cell_constructed'),'observation':'The 40320 maximal ordered simplices equal 8!, matching the repository schedule count. This is a structural numerical match; identifying those historical schedules with these eight named operations requires an explicit schedule dictionary.'}
p=ROOT/'research/nima/results/eight-axis-regulator-completion-frontier.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
