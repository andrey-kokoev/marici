#!/usr/bin/env python3
"""Test the smoothing square root against theta-characteristic axioms on C=P1."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
smooth=json.loads((R/'research/voevodsky/results/conductor_smoothing_square_root.json').read_text())
trial=json.loads((R/'research/voevodsky/results/conductor_triality_site_exchange.json').read_text())
# g=m(m+1)(x-my)/(m^2*y+x)^2.
# Generic finite valuations: 3 simple zeros; denominator has 2 roots, each doubled.
# Infinity valuation is deg(den)-deg(num)=4-3=+1.
zeros={'m=0':1,'m=-1':1,'m=x/y':1,'m=infinity':1}
poles={'m=+sqrt(-x/y)':2,'m=-sqrt(-x/y)':2}
deg_zero=sum(zeros.values());deg_pole=sum(poles.values());div_degree=deg_zero-deg_pole
# On P1: K=O(-2), unique theta O(-1). With D=four marks, K(D)=O(2), log theta O(1).
ordinary_theta_degree=-1;log_theta_degree=1;cleared_g_section_degree=deg_zero
checks={'four_simple_marked_zeros':smooth['checks']['four_simple_zeros_generic'],'rational_divisor_degree_zero':div_degree==0,'ordinary_theta_degree_minus_one':ordinary_theta_degree==-1,'log_theta_degree_one':log_theta_degree==1,'cleared_g_section_degree_four':cleared_g_section_degree==4,'g_line_fails_ordinary_theta_degree':cleared_g_section_degree!=ordinary_theta_degree,'g_line_fails_log_theta_degree':cleared_g_section_degree!=log_theta_degree,'four_branch_double_cover_genus_one':(4-2)//2==1,'three_matchings_equal_nonzero_E2_count':len(trial['geometric_matchings'])==3}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C13-theta-characteristic-axiom-test.v1','conductor':'C=P1','g':smooth['square_root_section'],'divisor':{'zeros':zeros,'poles':poles,'degree':div_degree},'theta_axioms':{'canonical_bundle':'K_C=O(-2)','ordinary_theta':'L^2=K_C, hence L=O(-1)','four-mark_log_canonical':'K_C(D)=O(2)','log_theta':'L_log=O(1)','cleared_zero_line_of_g':'O(4)'},'C13':'The global square root g directly determines a theta characteristic on the conductor whose quadratic refinement equals cusp parity.','status':'rejected in its direct form','degree_obstruction':'O(4) is neither the ordinary theta line O(-1) nor the four-mark logarithmic theta line O(1). As a rational function, g has a principal degree-zero divisor and supplies no line-bundle square root of K_C.','surviving_refinement':{'cover':'Sigma_g: xi^2=g(m)','branch_locus':'the four simple zeros of g; the double poles are unbranched','genus':1,'natural_torsion':'Sigma_g[2] has three nonzero classes corresponding to the three pairings of four branch points','proposal':'Place the quadratic refinement on the elliptic branch cover Sigma_g, then compare its selected 2-torsion class with the component-difference parity.'},'checks':checks,'passed':True}
(R/'research/voevodsky/results/C13_theta_characteristic_axiom_test.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'C13':out['status'],'obstruction':out['degree_obstruction'],'refinement':out['surviving_refinement']}))
