#!/usr/bin/env python3
"""DPC pullback of the E6/q_top diagonal residual to the principal p divisor."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
chart=json.loads((B/'rank12-radial-chart.json').read_text());prior=json.loads((R/'cosmology_u0_horizontal_comparison_target_factorization.json').read_text());assert prior['passed']
assert chart['normalized_chart']['inverse']['X2/X1']=='(u+v)/2-1' and chart['normalized_chart']['inverse']['X3/X1']=='(u-v)/2'
# p/X1 = 1 + X2/X1 + 3 X3/X1 = 2u-v, so p=0 is v=2u.
u=Fraction(3);v=2*u
D=4*u**4-4*u**3*v+4*u**3+4*u**2*v-7*u**2+2*u*v-4*u+v**2-4*v+4
E6u=(-8*u**3+6*u**2*v-6*u**2-4*u*v+7*u-v+2)/D;E6v=(2*u**3-2*u**2-u-v+2)/D
Qtu=-2*(u-1)/(u*(u-2));Qtv=-1/(v-2);Ru=E6u-Qtu;Rv=E6v-Qtv;pull=Ru+2*Rv
assert (Ru,Rv,pull)==(Fraction(95,69),Fraction(-93,92),Fraction(-89,138))
out={'schema':'marici.benincasa.cosmology-p-locus-horizontal-residual.v1','conjecture':'the actual principal divisor p=0 supports the E6/q_top horizontal comparison','normalized_identity':'p/X1=2u-v','p_locus':'v=2u','pullback_rule':'dv=2du','pulled_residual_numerator':'-4*u^6+18*u^5-8*u^4-45*u^3+66*u^2-36*u+8','pulled_residual_denominator':'D(u,2u)*u*(u-2)*(u-1)','falsifier_point':{'u':3,'v':6,'E6_minus_qtop_du':str(Ru),'E6_minus_qtop_dv':str(Rv),'pulled_coefficient':str(pull)},'falsifier_regular':D!=0 and u not in (0,1,2),'conjecture_disposition':'falsified','horizontal_comparison_on_p_locus':False,'survivor':'the associated-grade cyclic map remains algebraic, but the sourced diagonal connections are not horizontal on the target divisor','next_conjecture':'the nonzero p-locus residual is removable by a source-authorized scalar gauge','next_falsifier':'factor the one-variable residual and test whether it is a logarithmic derivative of an admissible rational gauge','passed':True};(R/'cosmology_p_locus_horizontal_residual.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
