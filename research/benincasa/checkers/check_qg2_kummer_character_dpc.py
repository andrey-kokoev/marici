#!/usr/bin/env python3
"""Exact Kummer-character audit on the q_g2 conductor wall."""
import json
from pathlib import Path
import sympy as s
xi,k,p=s.symbols('xi k p', nonzero=True)
K=16*p**4*(k+xi)**2;root=4*p**2*(k+xi)
assert s.expand(root**2-K)==0
# valuations controlling quadratic-cover monodromy
val_conductor=2
val_endpoint=0 # k != 1 implies K(-1) != 0
characters={'xi=-k':(-1)**val_conductor,'xi=-1':(-1)**val_endpoint}
assert characters=={'xi=-k':1,'xi=-1':1}
out={'schema':'marici.benincasa.qg2-kummer-character-dpc.v1','problem':'Can opposite Kummer character cancel the equal endpoint and conductor residues?','bold_conjecture':'The normalized square root of K|q_g2=16 p^4(kappa+xi)^2 has nontrivial meridian character at xi=-kappa, forcing the connecting residue sum to vanish.','named_rivals':['the order-two zero has trivial quadratic monodromy','the square-root cover splits as y=plus-or-minus 4p^2(kappa+xi)','character may be imported from an unsourced branch convention'],'risky_consequences':['the conductor valuation must be odd','analytic continuation around xi=-kappa must exchange the two square-root sheets'],'strongest_falsification_attempt':{'restricted_K':str(K),'global_square_root':str(root),'valuations':{'xi=-kappa':val_conductor,'xi=-1':val_endpoint},'meridian_characters':characters,'cover_factorization':'(y-4p^2(kappa+xi))(y+4p^2(kappa+xi))'},'disposition':{'status':'falsified for p nonzero and kappa not equal to 1','surviving_scope':'the relative Kummer character is trivial at both finite residues, so they add rather than cancel','remaining_gate':'derive the inverse collision Euler factor and its sign from an oriented excess-Gysin construction'},'passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'qg2_kummer_character_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
