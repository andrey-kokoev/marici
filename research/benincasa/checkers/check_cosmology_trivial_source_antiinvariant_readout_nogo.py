#!/usr/bin/env python3
"""Representation-theoretic no-go for trivial-source equivariance and anti-invariant readout."""
import json
from pathlib import Path
import sympy as s
P=s.Matrix([[0,1],[1,0]]);v=s.Matrix([1,1]);ell=s.Matrix([[-1,1]])
assert P*v==v
assert ell*P==-ell
assert (ell*v)[0]==0
out={'schema':'marici.benincasa.cosmology-trivial-source-antiinvariant-readout-nogo.v1','problem':'Can a contour with trivial source character map equivariantly to the root pair and have nonzero pairing with the recorded sewn-form linking functional?','bold_conjecture':'Trivial source character, equivariant specialization, and nonzero sewn-form readout are simultaneously compatible.','named_rivals':['equivariance sends the trivial source into the invariant root line','the recorded linking functional is anti-invariant','Schur-type character mismatch forces the pairing to vanish'],'risky_consequences':['the anti-invariant functional must be nonzero on an invariant vector','the source or target character must not matter'],'strongest_falsification_attempt':{'root_action':[[0,1],[1,0]],'trivial_source_image_generator':[1,1],'linking_functional_coordinates':[-1,1],'functional_character':'sign','pairing':0},'disposition':{'status':'falsified','residual':'the invariant image and anti-invariant linking functional have different C2 characters, so their pairing vanishes identically','surviving_scope':'a nonzero readout requires the source contour to carry sign character or requires a transposition-invariant target form','source_conflict':'the materialized q_g2 Kummer character is trivial, so the existing cover does not supply the needed sign representation'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_trivial_source_antiinvariant_readout_nogo.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
