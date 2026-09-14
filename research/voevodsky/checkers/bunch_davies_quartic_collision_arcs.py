#!/usr/bin/env python3
"""Compute the oriented quartic collision arcs selected by E -> -i0."""
import json, cmath, math
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
E,x,y=s.symbols('E x y', positive=True);z=E-x-y
A=s.expand(x**2+y**2-z**2);Delta=s.factor(A**2-4*x**2*y**2)
lead=s.factor(s.diff(Delta,E).subs(E,0))
# Numerical phase audit with positive x,y and small lower-half-plane E.
x0,y0,eps=2.0,3.0,1e-10; Ec=-1j*eps
Ac=x0*x0+y0*y0-(Ec-x0-y0)**2; Dc=Ac*Ac-4*x0*x0*y0*y0
sqrtD=cmath.sqrt(Dc);rho=math.sqrt(y0/x0)
# r=t^2 displacement is +/- sqrtD/(2x^2); t displacement divides by 2*t0.
dplus=sqrtD/(2*x0*x0)/(2j*rho)
dminus=sqrtD/(2*x0*x0)/(-2j*rho)
def phase(z):return math.atan2(z.imag,z.real)
checks={'central_square':s.expand(A.subs(E,0)+2*x*y)==0,'discriminant_simple_E':lead==-8*x*y*(x+y),'BD_discriminant_phase_pi_over_2':abs(phase(Dc)-math.pi/2)<1e-6,'principal_sqrt_phase_pi_over_4':abs(phase(sqrtD)-math.pi/4)<1e-6,'plus_node_arc_phase_minus_pi_over_4':abs(phase(dplus)+math.pi/4)<1e-6,'minus_node_arc_phase_three_pi_over_4':abs(phase(dminus)-3*math.pi/4)<1e-6,'same_unoriented_line':abs(((phase(dminus)-phase(dplus))%(2*math.pi))-math.pi)<1e-6}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.BD-quartic-collision-arcs.v1','quadratic_variable':'r=t^2','A':str(A),'root_discriminant':str(Delta),'leading_discriminant':str(lead)+'*E','prescription':'E approaches 0 through the lower half-plane','collision_nodes':['t=+i*sqrt(y/x)','t=-i*sqrt(y/x)'],'arc_phases':{'+node':'-pi/4','-node':'3pi/4'},'relation':'the two arcs lie on the same unoriented diagonal and are exchanged by t -> -t','Hurwitz_consequence':'a positive loop around E=0 performs the same-sense half-twist at both nodes; their Dehn-twist contributions are equal, with no additional relative sign from the BD approach','checks':checks,'passed':True,'remaining':'transport these oriented elliptic arcs through the integral specialization map to the algebraic Gysin kernel'}
(R/'research/voevodsky/results/BD_quartic_collision_arcs.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'leading_discriminant':out['leading_discriminant'],'arcs':out['arc_phases'],'consequence':out['Hurwitz_consequence'],'remaining':out['remaining']}))
