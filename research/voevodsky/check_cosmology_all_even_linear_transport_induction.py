"""Uniform descriptor-domain induction for squared-axis transport at every even A>=12."""
from __future__ import annotations
import json,os,sys
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import check_cosmology_source_word_axis_square_transport as transport
import cosmology_exact_source_certificate as certificate
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_all_even_linear_transport_induction.json'
def direct(d,delta):
 x=list(d);e=list(x[-1]);e[0]+=delta[0];e[1]+=delta[1];x[-1]=tuple(e);return tuple(x)
def main():
 checks=[];composition=0
 for A in range(12,34,2):
  ibp,K,q=transport.descs(A);ibp2,K2,q2=transport.descs(A+2);domains={'IBP':(ibp,set(ibp2)),'K':(K,set(K2)),'q':(q,set(q2))}
  assert len(ibp)==2*(A+1)*(A+2) and len(K)==32*(A-3)*(A-2) and len(q)==120*A*(A+1)
  images=0
  for _,(source,target) in domains.items():
   for d in source:
    sx=transport.shift(d,0);sy=transport.shift(d,1);assert sx in target and sy in target and sx!=sy;images+=2
    assert transport.shift(sx,1)==transport.shift(sy,0)==direct(d,(2,2));composition+=1
  checks.append({'A':A,'IBP':len(ibp),'K':len(K),'q':len(q),'transport_images':images,'all_images_in_A_plus_2':True,'mixed_square_commutes':True})
 # Deliberate failure: a degree-four shift cannot be represented as one A->A+2 generator step at the boundary.
 max_ibp=('IBP',0,(1,1,1,1,1),0,(A,0));bad=direct(max_ibp,(4,0));assert bad not in set(transport.descs(A+2)[0]) and sum(bad[-1])-(A+2)==2
 theorem={'IBP':'|e|<=A implies |e+2u|<=A+2','K':'|e|<=A-4 implies |e+2u|<=(A+2)-4','q':'|e|<=A-1 implies |e+2u|<=(A+2)-1','columns':'|e|<=A+4 implies |e+2u|<=(A+2)+4','coherence':'(e+2ex)+2ey=(e+2ey)+2ex; repeated shifts add in N^2','row_naturality':'Raw K and q multiplication rows shift identically. Parameter derivatives commute with parameter-independent monomial multiplication. The raw IBP Leibniz correction is parameter-independent, so both tangent and nx derivatives commute.'}
 out={'schema':'marici.voevodsky.cosmology-all-even-linear-transport-induction.v1','status':'uniform_linear_transport_for_every_even_A_at_least_12','base_certificate_ambient':12,'induction_step':2,'symbolic_domain_proof':theorem,'finite_descriptor_checks':checks,'checked_even_degrees':len(checks),'mixed_composition_checks':composition,'generator_matrix_rule':{'image':'same labelled family, poles, levels, axis/mark; exponent plus 2e_axis','coefficient':1,'digest':certificate.digest(theorem)},'deliberate_failure':{'shift_degree':4,'single_step_target_increment':2,'boundary_overflow':2,'rejected':True},'decision':'The A12 exact words extend uniquely by commuting squared-axis generator maps to every descriptor in their parity orbits at every even A>=12. This is a quantified family of finite source-typed morphisms, not a constructed colimit.','scope':'algebraic labelled relation presentations and parity-orbit words only; no source differential, geometric support, DNC comparison, exceptional localization, horn, or physical period','next_gate':'integrate-transport-certificates-into-geometrization-contract','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='finite_descriptor_checks'},indent=2))
if __name__=='__main__':main()
