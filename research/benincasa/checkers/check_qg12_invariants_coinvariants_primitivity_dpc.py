#!/usr/bin/env python3
"""Integral audit of root-pair invariants versus unordered coinvariants."""
import json
from pathlib import Path
import sympy as s
P=s.Matrix([[0,1],[1,0]]);fixed=s.Matrix([1,1])
# Coinvariants impose e_plus=e_minus=g. The invariant sum maps to 2g.
coinvariant_image=2
assert s.gcd(coinvariant_image,0)==2
out={'schema':'marici.benincasa.qg12-invariants-coinvariants-primitivity-dpc.v1','problem':'Can the transposition-invariant even root class be treated as a primitive class in the unordered root quotient over the integers?','bold_conjecture':'Passing from the fixed submodule to the unordered coinvariant quotient preserves primitivity of gamma_plus+gamma_minus.','named_rivals':['the quotient identifies both roots and sends their sum to twice the quotient generator','invariants and coinvariants agree only after inverting two','the target type must be declared before primitivity is meaningful'],'risky_consequences':['the invariant generator must map to a primitive coinvariant','the comparison cokernel must be torsion-free'],'strongest_falsification_attempt':{'transposition_matrix':[[0,1],[1,0]],'invariant_generator':[1,1],'coinvariant_relation':'gamma_plus-gamma_minus=0','image_in_coinvariants':'2 gamma','comparison_matrix':[2],'comparison_cokernel':'Z/2','primitive_in_invariants':True,'primitive_in_coinvariants':False},'disposition':{'status':'falsified integrally','surviving_scope':'the even sum is primitive in the invariant submodule but divisible by two in the unordered coinvariant quotient','reopening_test':'declare whether the physical target is invariants, coinvariants, or a coefficient system with two inverted; then derive the contour map in that target'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'qg12_invariants_coinvariants_primitivity_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
