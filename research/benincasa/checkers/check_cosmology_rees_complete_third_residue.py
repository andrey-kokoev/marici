#!/usr/bin/env python3
"""Solve the complete constrained third-residue equation exactly."""
import json
from fractions import Fraction as F
from pathlib import Path
# Boundary A(X4)=X6-12X5; A(X3)=-6X4.
# Lower tangential B(1)=-45X6+216X5.
t=F(5,2);u=F(171,2);v=F(-648)
coeff={6:u-45*t,5:-12*u+216*t,4:-6*v}
target={6:F(-27),5:F(-486),4:F(3888)}
assert coeff==target
out={'schema':'marici.benincasa.cosmology-rees-complete-third-residue.v1','problem':'decide tau third-residue membership after boundary-only corrections failed','bold_conjecture':'lower K-level constrained inputs do not repair the -810X5 boundary mismatch','named_rivals':['persistent third-residue obstruction','a lower tangential correction supplies the missing independent coefficient direction'],'risky_consequences':['the combined coefficient system must remain inconsistent','no rational lower correction may match X6 and X5 simultaneously'],'strongest_falsification_attempt':{'boundary_operator_values':['A(X4)=X6-12X5','A(X3)=-6X4'],'lower_operator_value':'B(1)=-45X6+216X5','solution':{'lower_c1':'5/2','boundary_a1':'(171/2)X4-648X3'},'combined_residue':'-27X6-486X5+3888X4','target_residue':'-27X4(X-6)(X+24)','exact_residual':0},'disposition':'the complete constrained third-residue image contains tau; the lower K-level correction removes the boundary mismatch exactly','surviving_scope':'membership is proved only through third normal order, not for the full scalar polynomial','next_test':'form the explicit boundary and lower inputs through order three, subtract their full operator output from Phi(tau), and factor the next residual','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_complete_third_residue.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
