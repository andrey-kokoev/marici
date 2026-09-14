#!/usr/bin/env python3
"""Distinguish four-chart horizontal descent from parameter fixed-point descent."""
import json
from fractions import Fraction as F
from pathlib import Path
from evidence_policy import write_result
R=Path(__file__).resolve().parents[2]
# A four-cycle of invertible scalar chart transitions with product one.
Fj=(F(2),F(3),F(5),F(1,30))
def horizontal(x0):
 x=[x0]
 for a in Fj[:3]: x.append(a*x[-1])
 return tuple(x)
def defect(x): return tuple(x[(j+1)%4]-Fj[j]*x[j] for j in range(4))
x=horizontal(F(7));z=(F(1,3),F(2,5));tau=(-z[0],z[1])
checks={'four_product_one':Fj[0]*Fj[1]*Fj[2]*Fj[3]==1,'horizontal_nonzero':x!=(0,0,0,0),'equalizer_defect_zero':defect(x)==(0,0,0,0),'evaluation_recovers_x0':x[0]==7,'off_seam_base_not_fixed':z!=tau};assert all(checks.values())
out={'schema':'marici.conjecture-replay.CR1-horizontal-equalizer-not-fixed-descent.v1','passed':True,'claim_status':'proved','evidence':[{'class':'SYMBOLIC','claim':'An exact nonzero four-chart horizontal section exists and is uniquely determined by one chart whenever transition product is one, independently of whether the parameter is fixed by reciprocal-Real transport.','checker':'research/conjecture_replay/check_CR1_horizontal_equalizer_not_fixed_descent.py'},{'class':'SOURCE_DERIVED','claim':'The stratified Fourier horizontal equalizer is closed and evaluation at any chart is a topological isomorphism; off-axis archimedean transition remains nonvanishing on compact pole-free sets.','source':'research/nima/the-stratified-fourier-equalizer-is-closed-before-anomaly-line-trivialization.md'}],'outcome':'horizontal four-presentation descent does not impose critical-line fixedness','horizontal_object':'X_hor={(x_j):x_(j+1)=F_j x_j}; evaluation at chart zero is an isomorphism when F_3F_2F_1F_0=I','parameter_action':'Reciprocal-Real sends z to -conjugate(z). The four charts may lie over the resulting parameter orbit and be connected by transport.','key_distinction':'Horizontal descent identifies presentations along an orbit. Fixed-point descent would additionally require the orbit base z to equal -conjugate(z).','off_seam_model':'The checker exhibits a nonzero exact horizontal section with an independently chosen off-seam rational complex parameter.','archimedean':'A nonvanishing off-axis Tate transition supports orbit transport; unit modulus is needed only on the sewing axis for isometry, not for existence of the horizontal line.','consequence':'The horizontal equalizer removes fourfold presentation duplication but cannot turn reciprocal-Real covariance into Re(z)=0.','forbidden_inference':'evaluation-at-one-chart isomorphism plus one divisor copy does not imply that the chart parameter is a fixed point of the base involution.','remaining_confinement_input':'A new source theorem must force characteristic states to descend to the fixed-point base rather than merely to equivariant sections over reciprocal-Real orbits. No such map is present in the current source packet.','RH':False,'disposition':'The reciprocal-Real plus horizontal-descent confinement route is exhausted at current assumptions.','next':'reopen_only_if_a_source_derived_fixed_state_descent_or_self_adjoint_pencil_is_constructed'}
write_result(R/'research/conjecture_replay/results/CR1_horizontal_equalizer_not_fixed_descent.json',out);print(json.dumps({'passed':True,'horizontal_section':True,'off_seam_allowed':True,'fixed_descent':False,'RH':False}))
