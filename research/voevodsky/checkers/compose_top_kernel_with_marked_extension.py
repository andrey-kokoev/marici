#!/usr/bin/env python3
"""Compose the primitive conductor specialization kernel with the marked algebraic extension map."""
import json
from pathlib import Path
from fractions import Fraction
R=Path(__file__).resolve().parents[3]
spec=json.loads((R/'research/benincasa/total-energy-conductor-specialization.json').read_text())
full=json.loads((R/'research/benincasa/full-marked-total-energy-nilpotent.json').read_text())
assert spec['specialization_graph']['primitive_kernel']=='Z*g111_top'
basis=full['blocks']['algebraic_extension']['source_basis']; targets=full['blocks']['algebraic_extension']['target_coordinates'];M=full['blocks']['algebraic_extension']['matrix'];j=basis.index('g111_top');col=[M[i][j] for i in range(len(targets))]
checks={'primitive_kernel_is_top':spec['specialization_graph']['primitive_kernel']=='Z*g111_top','top_is_third_source':j==2,'target_order':targets==['e2','e4','e6','v0'],'top_column_only_e6':col[0]=='0' and col[1]=='0' and col[2]!='0' and col[3]=='0','top_e6_coefficient':col[2]=='1/(8*(x+y))','v0_projection_exactly_zero':col[3]=='0','map_rank_three':full['blocks']['algebraic_extension']['rank']==3}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.top-kernel-marked-extension-composition.v1','specialization_kernel_generator':'g111_top','extension_target_order':targets,'composite_column':col,'support_line':'e6 only','v_alg_quotient_projection':'zero (v0 coordinate)','consequence':'The disappearing conductor quotient generator has no v_alg-direction component in the source-normalized marked extension. Thus the second bit is zero once this source map is used; no conductor point-evaluation argument is needed.','integral_limit':'The nonzero e6 scalar is rational and does not determine whether its primitive integral image is odd or even. The problem is reduced from two bits to one e6 divisibility question.','checks':checks,'passed':True,'next':'compare the primitive Z*g111_top generator with the BD Cech half-boundary to determine the integral index of 1/(8(x+y))*e6'}
(R/'research/voevodsky/results/top_kernel_marked_extension_composition.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'kernel':out['specialization_kernel_generator'],'column':col,'support':out['support_line'],'second_bit':0,'integral_limit':out['integral_limit']}))
