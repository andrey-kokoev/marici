"""Classify the maximal exact consequence of normal-torsor absorption."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_algebraic_first_jet_zero_theorem.json'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det3(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def main():
 nx=(1,0,0);t1=(1,-1,0);t2=(3,0,-1);p=(1,1,3)
 transport=json.loads((RES/'cosmology_second_direction_all_even_transport.json').read_text());beta=json.loads((RES/'cosmology_algebraic_relative_bockstein.json').read_text());assert transport['passed'] and beta['rank']==0
 determinant=det3(nx,t1,t2);assert abs(determinant)==1 and dot(p,nx)==1 and dot(p,t1)==dot(p,t2)==0
 samples=[(-7,5,2),(0,0,0),(1,1,1),(11,-4,3)]
 decompositions=[]
 for v in samples:
  c=dot(p,v);a=-v[1];b=-v[2];recon=tuple(c*nx[i]+a*t1[i]+b*t2[i] for i in range(3));assert recon==v;decompositions.append({'v':v,'coefficients_nx_t1_t2':[c,a,b]})
 out={'schema':'marici.voevodsky.cosmology-algebraic-first-jet-zero-theorem.v1','status':'entire_xyz_directional_first_jet_zero_in_relation_quotient','basis':{'nx':nx,'tangent_1':t1,'tangent_2':t2,'determinant':determinant,'unimodular':True},'decomposition':'For v=(x,y,z), v=(x+y+3z) nx - y t1 - z t2.','sample_checks':decompositions,'theorem':'For every even A>=12, every labelled IBP/K/q relation R, and every v in Q^3, [D_v R]=0 in C0/im(d1). For integral v the decomposition coefficients are integral.','normal_torsor_corollary':'Every rational or integral n with dp(n)=1 has zero class, independently of normal choice.','stronger_consequence':'No change of derivative direction inside the declared xyz parameter space can produce a nonzero algebraic Bockstein while the quotient is unchanged.','maximal_sourced_scope':'Characteristic-zero labelled algebraic first-jet presentation with squared-axis transport across all even A>=12.','withheld':['geometric normal bundle','DNC or support filtration','specialization to the exceptional triangle','relative-cohomological or physical Bockstein','deformation parameter outside xyz','higher jets'],'next_gate':'audit-external-deformation-interface','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
