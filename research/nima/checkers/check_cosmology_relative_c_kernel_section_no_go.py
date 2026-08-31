"""Test whether c=-E gives a canonical section of the p-normal line."""
import json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'results'/'cosmology_relative_c_kernel_section_no_go.json'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rank2(a,b,p):
 for i in range(3):
  for j in range(i+1,3):
   if (a[i]*b[j]-a[j]*b[i])%p:return 2
 return 1 if any(x%p for x in a+b) else 0
def main():
 pc=(1,1,3);ec=(1,1,1);normals={'nx':(1,0,0),'ny':(0,1,0),'n_alt_unit':(-2,0,1),'n_alt_nonunit':(4,0,-1)}
 rows={k:{'vector':list(n),'dp':dot(pc,n),'dE':dot(ec,n),'dc_on_graph':-dot(ec,n)} for k,n in normals.items()}
 assert all(v['dp']==1 for v in rows.values());assert rows['nx']['dc_on_graph']==-1 and rows['n_alt_unit']['dc_on_graph']==1 and rows['n_alt_nonunit']['dc_on_graph']==-3
 tangent=tuple(normals['n_alt_unit'][i]-normals['nx'][i] for i in range(3));assert dot(pc,tangent)==0 and dot(ec,tangent)==-2
 ff={str(p):{'rank_p_E':rank2(pc,ec,p),'E_vanishes_on_p_tangent':dot(ec,tangent)%p==0} for p in (101,103)}
 assert all(x['rank_p_E']==2 and not x['E_vanishes_on_p_tangent'] for x in ff.values())
 packet={'schema':'marici.cosmology-relative-c-kernel-section-no-go.v1','status':'c_equals_minus_E_does_not_descend_to_canonical_p_normal_section','p_covector':list(pc),'E_covector':list(ec),'graph_relation':'c=-E','unit_p_normals':rows,'p_tangent_witness':{'vector':list(tangent),'dp':0,'dE':dot(ec,tangent),'change_in_dc':-dot(ec,tangent)},'finite_field_witnesses':ff,'factorization_required':'E must vanish on ker(dp), equivalently E=lambda*p, for dc=-dE to depend only on the p-normal quotient','factorization_holds':False,'primitive_unit_ambiguity':'fixed dp=1 permits dc=-1,+1,-3; the exceptional-face orientation is already fixed, so this is not simultaneous orientation reversal','source_derived_kernel_section_constructed':False,'tau_p_map_constructed':False,'physical_period_constructed':False,'conclusion':'the frozen graph relation c=-E supplies relative tangent lifts but not a canonical section of the p-normal quotient; p-tangent changes alter the c coefficient, reproducing the missing Rees/cover-choice ambiguity','passed':True}
 OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet,indent=2))
if __name__=='__main__':main()
