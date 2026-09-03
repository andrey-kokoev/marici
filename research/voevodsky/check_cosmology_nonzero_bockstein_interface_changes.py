"""DPC classification of interface changes capable of exposing a nonzero class."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_nonzero_bockstein_interface_changes.json'
def rank(A):
 M=[[Fraction(x) for x in r] for r in A];r=0
 for c in range(len(M[0]) if M else 0):
  p=next((i for i in range(r,len(M)) if M[i][c]),None)
  if p is None:continue
  M[r],M[p]=M[p],M[r];q=M[r][c];M[r]=[x/q for x in M[r]]
  for i in range(len(M)):
   if i!=r and M[i][c]:q=M[i][c];M[i]=[M[i][j]-q*M[r][j] for j in range(len(M[0]))]
  r+=1
 return r
def in_span(cols,x): return rank([list(c) for c in cols])==rank([list(c) for c in cols]+[list(x)])
def main():
 prior=json.loads((RES/'cosmology_algebraic_relative_bockstein.json').read_text());assert prior['rank']==0 and prior['passed']
 x=(1,0);image=[(1,0)]
 assert in_span(image,x)
 basis_changed=[(-1,0)];assert in_span(basis_changed,x)
 enlarged=image+[(0,1)];assert in_span(enlarged,x)
 restricted=[];assert not in_span(restricted,x)
 changed_normal=(0,1);assert not in_span(image,changed_normal)
 classes={'invertible_reparametrization':{'can_make_nonzero':False,'reason':'preserves im(d1)'},'adjoin_source_generators':{'can_make_nonzero':False,'reason':'enlarges im(d1), so every previously exact target remains exact'},'linear_postcomparison':{'can_make_nonzero':False,'reason':'a well-defined linear map sends the zero quotient class to zero'},'restrict_admissible_primitives_by_sourced_support_or_filtration':{'can_make_nonzero':True,'status':'necessary-class candidate, not established'},'change_normal_derivative_or_target':{'can_make_nonzero':True,'status':'necessary-class candidate, not established'},'change_extension_or_quotient_so_current_primitive_does_not_descend':{'can_make_nonzero':True,'status':'necessary-class candidate, not established'}}
 out={'schema':'marici.voevodsky.cosmology-nonzero-bockstein-interface-changes.v1','problem':'Can source enlargement or an interface change turn the certified zero algebraic Bockstein into a nonzero class?','bold_conjecture':'Adjoining more source generators can expose a nonzero Bockstein while retaining the same normal target and quotient rule.','named_rivals':['basis reparametrization changes the class','a linear comparison can send the zero class to a nonzero exceptional class','only a non-monotone admissibility restriction, changed normal target, or changed extension can expose a class'],'risky_consequences':['some previously exact derivative leaves the image after adjoining generators','a well-defined linear comparison maps zero to nonzero'],'strongest_falsification':{'theorem':'If im(d1) is contained in im(d1_prime) and x lies in im(d1), then x lies in im(d1_prime). Also every linear map sends the zero quotient class to zero.','exact_model':{'target':[1,0],'original_image_rank':1,'enlarged_image_rank':2,'target_exact_after_enlargement':True,'target_nonexact_after_restriction':True,'changed_normal_nonexact':True},'residual':'No monotone source enlargement or basis change can expose the class.'},'disposition':{'status':'bold_conjecture_rejected','necessary_disjunction':'A nonzero class requires a sourced restriction of admissible primitives, a changed normal derivative/target, or a changed extension/quotient in which the existing primitive does not descend.','sufficiency_withheld':'None of these changes is constructed or proved sufficient by current artifacts.'},'classification':classes,'next_gate':'test-filtered-bockstein-under-pole-filtration','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
