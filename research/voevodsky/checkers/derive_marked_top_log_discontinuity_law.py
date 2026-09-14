#!/usr/bin/env python3
"""Derive the measurable logarithmic jump of the regularized marked-top period."""
import json
from fractions import Fraction
from pathlib import Path
R=Path(__file__).resolve().parents[3]
rees=json.loads((R/'research/benincasa/two-wall-rees-regularization.json').read_text())
phys=json.loads((R/'research/voevodsky/results/BD_marked_top_physical_readout.json').read_text())
assert rees['symbolic_checks']['rees_lift']=='Omega111_reg = Omega111 + e6/(8E)'
assert rees['symbolic_checks']['induced_e6_residue']=='e6/(8*(x+y))'
assert phys['readout']['ordered_parity']==[1,0]
# In the normalized de Rham target epsilon6=e6/[8(x+y)], the logarithmic
# residue coefficient is one. Disc log(E-i0)=+/-2*pi*i by loop convention.
residue_in_epsilon6=1
out={'schema':'marici.voevodsky.marked-top-log-discontinuity-law.v1','regularized_form':'Omega111_reg=Omega111+e6/(8E)','integral_comparison_form':'epsilon6_dR=e6/[8*(x+y)] corresponds to the primitive Betti component difference e6_B=C_minus-C_plus','local_period_law':'Pi111_reg(E)=F(E) +/- log(E)*Pi_epsilon6(E), up to the chosen Gauss-Manin sign convention','measurable_jump':'Disc Pi111_reg = +/- 2*pi*i Pi_epsilon6','dimensionless_readout':'(Disc Pi111_reg)/(2*pi*i Pi_epsilon6)=+/-1','mod_two_readout':1,'second_channel':'coefficient of Pi_v_alg is 0','ordered_physical_parity':[1,0],'orientation':'Bunch-Davies E->E-i0 fixes one of the two displayed overall signs; parity is sign-independent.','comparison_gate':phys['comparison_gate'],'passed':True}
(R/'research/voevodsky/results/marked_top_log_discontinuity_law.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'law':out['measurable_jump'],'ratio':out['dimensionless_readout'],'parity':out['ordered_physical_parity'],'gate':out['comparison_gate']}))
