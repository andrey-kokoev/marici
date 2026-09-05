"""Exact algebraic core of the Stieltjes pole-locus converse."""
import json
from fractions import Fraction as Q
from pathlib import Path

def square(a,b): return a*a-b*b,2*a*b
def on_negative_real_axis(z): return z[1]==0 and z[0]<0
def prefactor_at(z): return 4*z[0]-1,4*z[1]

off_line=[]
for a,b in ((Q(1,4),Q(3)),(Q(-1,5),Q(7,2)),(Q(1,10),Q(1,3))):
    z=square(a,b)
    assert not on_negative_real_axis(z)
    assert prefactor_at(z)!=(Q(0),Q(0))
    off_line.append({'centered_real_part':str(a),'imaginary_part':str(b),
                     'squared_coordinate':[str(z[0]),str(z[1])]})
critical=[]
for b in (Q(1),Q(7,2),Q(14)):
    z=square(Q(0),b); assert on_negative_real_axis(z)
    critical.append({'imaginary_part':str(b),'squared_coordinate':[str(z[0]),str(z[1])]})
real_centered=[]
for a in (Q(1,10),Q(-1,3)):
    z=square(a,Q(0)); assert z[1]==0 and z[0]>0
    real_centered.append({'centered_real_part':str(a),'squared_coordinate':[str(z[0]),str(z[1])]})
assert prefactor_at((Q(1,4),Q(0)))==(Q(0),Q(0))
result={
    'map':'t=(rho-1/2)^2',
    'negative_real_t_implies_centered_coordinate_pure_imaginary':True,
    'nonreal_off_critical_line_maps_off_negative_axis':True,
    'critical_line_maps_to_negative_axis':True,
    'real_centered_points_map_to_positive_axis':True,
    'prefactor_4t_minus_1_only_cancels_at_t_one_quarter':True,
    'off_line_fixtures':off_line,
    'critical_line_fixtures':critical,
    'real_centered_fixtures':real_centered,
    'positive_axis_analyticity_excludes_real_centered_zero_poles':True,
    'requires_analytic_proof_that_positive_representation_has_no_off_cut_poles':True,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'stieltjes-pole-locus-converse.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
