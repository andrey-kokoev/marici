"""Audit declared p-normal interfaces after exact nx absorption."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_declared_normal_interface_audit.json'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rank2(a,b):return any(a[i]*b[j]-a[j]*b[i] for i in range(3) for j in range(i+1,3))
def main():
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());raw=json.loads((RES/'cosmology_rank26_p_normal_raw_relation_adapter.json').read_text());beta=json.loads((RES/'cosmology_algebraic_relative_bockstein.json').read_text())
 p=gate['p_normal_covector'];normals=gate['integral_unit_normals'];nx=normals['nx'];ny=normals['ny'];t=normals['p_tangent_difference']
 assert dot(p,nx)==dot(p,ny)==1 and dot(p,t)==0
 assert [nx[i]-ny[i] for i in range(3)]==t and raw['tangent_identity']['failures']==0 and beta['rank']==0
 # D_ny R = D_nx R - D_t R; both terms lie in the declared exact image.
 ny_rank=0
 second_normal=[-2,0,1];second_tangent=[nx[i]-second_normal[i] for i in range(3)]
 assert dot(p,second_normal)==1 and dot(p,second_tangent)==0 and rank2(t,second_tangent)
 out={'schema':'marici.voevodsky.cosmology-declared-normal-interface-audit.v1','status':'declared_ny_interface_also_zero_full_normal_torsor_not_tested','declared_unit_normals':{'nx':nx,'ny':ny},'identity':'D_ny R = D_nx R - D_(nx-ny) R','evidence':{'nx_quotient_rank':beta['rank'],'tangent_identity_rows':raw['tangent_identity']['rows_checked'],'tangent_identity_failures':raw['tangent_identity']['failures'],'ny_quotient_rank':ny_rank},'decision':'ny is not a distinct surviving interface: its derivative differs from nx by the declared p-tangent row, so its quotient class is also zero. The listed p_tangent direction is not a normal because dp=0.','scope':'All declared alternative directions are exhausted; this does not prove independence over the full rank-two tangent lattice ker(dp).','unresolved_torsor':{'derived_second_unit_normal':second_normal,'second_tangent_generator':second_tangent,'independent_from_declared_tangent':True,'tested_against_relation_module':False},'first_missing_test':'Differentiate along the second tangent generator (3,0,-1), determine whether those rows lie in the exact image, and then test the derived unit normal (-2,0,1).','next_gate':'test-second-tangent-generator-normal-independence','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
