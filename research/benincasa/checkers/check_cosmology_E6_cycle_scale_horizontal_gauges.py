#!/usr/bin/env python3
"""Test whether recorded E6 cycle scales carry connection-gauge authority."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
e6=json.loads((R/'clifford_e6_cyclic_equivariance.json').read_text());cmp=json.loads((R/'cosmology_qtop_A2_to_E6_grade_comparison.json').read_text());assert cmp['passed']
scales=[Fraction(x) for x in e6['cycle_scales']];assert scales==[2,3,Fraction(1,6)] and scales[0]*scales[1]*scales[2]==1
# For constant scalar gauges dlog(g)=0; horizontality would require equality of line connection forms.
dlog=[0,0,0]
# Deliberate model: same weights and constant scale, unequal connection coefficients.
A1,A2=Fraction(0),Fraction(1);hostile_residual=A2-A1-dlog[0];assert hostile_residual==1
out={'schema':'marici.benincasa.cosmology-E6-cycle-scale-horizontal-gauges.v1','cycle_scales':[str(x) for x in scales],'cycle_product':str(scales[0]*scales[1]*scales[2]),'scale_type':'homogeneity rescalings in the Clifford/E6 cyclic checker','connection_transition_type_declared':False,'constant_scale_dlog':[0,0,0],'conditional_horizontal_equation':'A_next - A_current = dlog(g), hence A_next=A_current for constant g','occurrence_line_connections_serialized':False,'deliberate_same_weight_unequal_connection_residual':str(hostile_residual),'deliberate_failure_nonzero':True,'horizontal_gauges_verified':False,'common_homogeneity_implies_horizontality':False,'conclusion':'the scales close weighted cyclic transport but are not typed as connection transition functions; constant values would require separately proved equality of occurrence-line connections','next_test':'locate or obstruct the three occurrence-line connection restrictions and their chart identifiers in the bivariate E6 connection','passed':True};(R/'cosmology_E6_cycle_scale_horizontal_gauges.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
