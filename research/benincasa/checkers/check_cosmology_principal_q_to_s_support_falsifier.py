#!/usr/bin/env python3
"""Type-check the deliberate candidate s_i=q_gi on the principal divisor."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';sys.path.insert(0,str(B))
import physical_four_mark_residue_twisted_derham as source
prior=json.loads((R/'cosmology_naive_X_to_s_support_falsifier.json').read_text());identity=json.loads((R/'cosmology_principal_three_wall_p_identity.json').read_text());assert prior['passed'] and identity['passed']
_,q=source.fiber_data(2,3,4);principal={k:q[k] for k in ('g1','g2','g3')}
nonconstant={k:sorted([list(e) for e in v if e!=(0,0)]) for k,v in principal.items()};assert nonconstant=={'g1':[[0,1]],'g2':[[1,0]],'g3':[[0,1],[1,0]]}
# The sourced identity cancels the fiber variables only in -q1-q2+q3=p.
def combine(terms):
 out={}
 for c,row in terms:
  for e,v in row.items():out[e]=out.get(e,0)+c*v
 return {e:v for e,v in out.items() if v}
relation=combine([(-1,principal['g1']),(-1,principal['g2']),(1,principal['g3'])]);assert set(relation)<= {(0,0)}
out={'schema':'marici.benincasa.cosmology-principal-q-to-s-support-falsifier.v1','conjecture':'the sourced principal wall functions q_g1,q_g2,q_g3 define Gysin variables as rational functions of u on p=0','candidate_assignment':{'s1':'q_g1','s2':'q_g2','s3':'q_g3'},'q_types':'affine functions in two fiber coordinates with base parameters x,y,z','nonconstant_fiber_monomials':nonconstant,'only_sourced_base_relation':'-q_g1-q_g2+q_g3=p','relation_on_p':'q_g3=q_g1+q_g2','each_q_descends_to_Q_of_u':False,'required_fiber_section_found':False,'Gysin_denominator_pullback_to_u_defined':False,'conjecture_disposition':'falsified by source typing','reason':'restriction to p=0 relates the three affine fiber functions but does not turn them into base functions','assignment_source_authorized':False,'next_conjecture':'after imposing q_g3=q_g1+q_g2, the full Gysin denominator becomes independent of the fiber coordinates','next_falsifier':'substitute the relation into s1*s2*s3*Lambda_P and test whether nonconstant fiber factors remain','passed':True};(R/'cosmology_principal_q_to_s_support_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
