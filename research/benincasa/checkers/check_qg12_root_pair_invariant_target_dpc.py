#!/usr/bin/env python3
"""Audit whether ordering the Cayley-Menger roots is needed for the even target class."""
import json
from pathlib import Path
import sympy as s
P=s.Matrix([[0,1],[1,0]]);I=s.eye(2)
inv=(P-I).nullspace();anti=(P+I).nullspace()
assert inv==[s.Matrix([1,1])]
assert anti==[s.Matrix([-1,1])]
out={'schema':'marici.benincasa.qg12-root-pair-invariant-target-dpc.v1','problem':'Must the two Cayley-Menger roots be ordered before the even root-pair target class can be defined?','bold_conjecture':'Without an ordering of the two split roots, no canonical even target class exists.','named_rivals':['the sum of the two root generators is invariant under transposition','only the odd difference requires ordering or a sign local system','the missing datum lies in the domain-to-target map rather than the target generator'],'risky_consequences':['the transposition-fixed submodule must vanish','the even sum must change under root exchange'],'strongest_falsification_attempt':{'root_transposition_matrix':[[0,1],[1,0]],'fixed_submodule_generator':[1,1],'anti_invariant_generator':[-1,1],'fixed_rank':1},'disposition':{'status':'falsified','surviving_scope':'the unordered root pair canonically defines the invariant even class gamma_plus+gamma_minus','scope_correction':'ordering is needed for individual roots or the odd difference, but not for the even target generator','remaining_gate':'a source-derived chain map from the unsplit contour to this invariant submodule is still absent'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'qg12_root_pair_invariant_target_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
