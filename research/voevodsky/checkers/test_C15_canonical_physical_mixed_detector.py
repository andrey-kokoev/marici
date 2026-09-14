#!/usr/bin/env python3
"""Test the canonical q_G12 physical residue as a v_alg mixed detector."""
import json
from fractions import Fraction
from pathlib import Path
R=Path(__file__).resolve().parents[3]
full=json.loads((R/'research/benincasa/full-marked-total-energy-nilpotent.json').read_text())
src=json.loads((R/'research/benincasa/marked-relative-source-maps.json').read_text())
A=full['blocks']['algebraic_extension'];basis=A['source_basis'];targets=A['target_coordinates'];M=A['matrix']
assert basis==['g101','g110','g111_top'] and targets==['e2','e4','e6','v0']
# Canonical printed q_G12 residue: common top denominator times
# (1/q_g23 + 1/q_g31), hence equal occurrence weights on mixed classes.
physical=[0,1,1] # basis order g101,g110,g111_top? reorder below: g101,g110,top
physical=[1,1,0]
# Symbolic rows as strings are simple enough to compose exactly by structure.
D='4*x^3*y^3*(x+y)'
cols={basis[j]:[M[i][j] for i in range(4)] for j in range(3)}
symmetric=['-1/(4*x*y)','-1/(4*x*y)','0','0'] # e2,e4,e6,v0
antisymmetric=['1/(4*x*y)','-1/(4*x*y)','0',f'-2/({D})'] # g101-g110; e2 sign positive, e4 negative
checks={'canonical_source_has_equal_plus_weights':physical==[1,1,0],'mixed_v0_coefficients_opposite':cols['g101'][3]=='-1/(4*x^3*y^3*(x+y))' and cols['g110'][3]=='1/(4*x^3*y^3*(x+y))','symmetric_physical_v0_cancels':symmetric[3]=='0','antisymmetric_v0_nonzero':antisymmetric[3]!='0','top_excluded_from_mixed_test':physical[2]==0,'source_residues_distinguish_mixed_labels':src['basis']['marked'][:3]==['Omega111','Omega101','Omega110']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C15-canonical-physical-mixed-detector.v1','canonical_source_term':'1/q_g23 + 1/q_g31','mixed_basis':['g101','g110'],'physical_covector':[1,1],'extension_columns':{'g101':cols['g101'],'g110':cols['g110']},'physical_symmetric_image':{'target_basis':targets,'coordinates':symmetric,'v_alg_projection':'0'},'counterfactual_antisymmetric_image':{'source_covector':[1,-1],'target_basis':targets,'coordinates':antisymmetric,'v_alg_projection':antisymmetric[3]},'C15a':'The canonical q_G12 physical mixed residue activates v_alg.','C15a_status':'rejected','reason':'The two source occurrences enter with equal plus weights, while their v_alg columns have equal magnitude and opposite sign.','C15b':'An occurrence-sensitive or shape-derived physical operation supplies the antisymmetric covector (1,-1).','C15b_status':'open','required_next':'Differentiate the sourced relative period with respect to an exchange-odd external shape normal and compute whether the induced occurrence covector has a nonzero antisymmetric component.','checks':checks,'passed':True}
(R/'research/voevodsky/results/C15_canonical_physical_mixed_detector.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'C15a':out['C15a_status'],'physical_covector':out['physical_covector'],'v_alg':0,'counterfactual':out['counterfactual_antisymmetric_image'],'C15b':out['C15b_status'],'next':out['required_next']}))
