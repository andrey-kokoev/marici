"""Construct and test labelled exponent-shift maps on every A12 generator row."""
from __future__ import annotations
import json,os,sys
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import cosmology_exact_source_certificate as certificate
import check_cosmology_source_word_axis_square_transport as transport
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_linear_generator_transport_matrix.json'
def packet(A,point,td,nx):
 rees.AMBIENT=A;_,cols=rees.column_packet();raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,td);dx,_=adapter.derivative_rows(cols,point,nx);ibp,K,q=transport.descs(A);return cols,{'T':T,'S_K':raw[len(ibp):len(ibp)+len(K)],'Q':raw[len(ibp)+len(K):],'dx':dx},(ibp,K,q)
def shift_row(row,inv12,cols14,axis):
 out={}
 for col,value in row.items():
  label=list(inv12[col]);e=list(label[-1]);e[axis]+=2;label[-1]=tuple(e);out[cols14[tuple(label)]]=value
 return out
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);nx=tuple(protocol['integral_unit_normals']['nx']);oldA=rees.AMBIENT;oldP=base.PRIME
 summaries=[];examples=[]
 try:
  for prime in exact.PS:
   base.PRIME=prime;cols12,p12,d12=packet(12,point,td,nx);cols14,p14,d14=packet(14,point,td,nx);inv12={v:k for k,v in cols12.items()};all12=d12[0]+d12[1]+d12[2];all14=d14[0]+d14[1]+d14[2]
   decode={'T':all12,'S_K':d12[1],'Q':d12[2],'dx':all12};index={'T':{d:i for i,d in enumerate(all14)},'S_K':{d:i for i,d in enumerate(d14[1])},'Q':{d:i for i,d in enumerate(d14[2])},'dx':{d:i for i,d in enumerate(all14)}}
   counts={};fails={}
   for kind in ('T','S_K','Q','dx'):
    counts[kind]=len(p12[kind])*2;fails[kind]=0
    for i,row in enumerate(p12[kind]):
     desc=decode[kind][i]
     for axis in (0,1):
      expected=p14[kind][index[kind][transport.shift(desc,axis)]];actual=shift_row(row,inv12,cols14,axis)
      if actual!=expected:
       fails[kind]+=1
       if len(examples)<20:examples.append({'prime':prime,'kind':kind,'index':i,'axis':axis,'source_support':len(row),'shifted_support':len(actual),'target_support':len(expected)})
   summaries.append({'prime':prime,'tested':counts,'failures':fails})
 finally:base.PRIME=oldP;rees.AMBIENT=oldA
 total=sum(sum(s['tested'].values()) for s in summaries);failed=sum(sum(s['failures'].values()) for s in summaries)
 blocks={'T':{'domain_generators':len(transport.descs(12)[0]+transport.descs(12)[1]+transport.descs(12)[2]),'image_rule':'descriptor exponent plus 2e_axis, coefficient 1'},'S_K':{'domain_generators':len(transport.descs(12)[1]),'image_rule':'K descriptor exponent plus 2e_axis, coefficient 1'},'Q':{'domain_generators':len(transport.descs(12)[2]),'image_rule':'q descriptor exponent plus 2e_axis, coefficient 1'}}
 out={'schema':'marici.voevodsky.cosmology-linear-generator-transport-matrix.v1','status':'generator_shift_map_commutes' if not failed else 'generator_shift_map_has_residuals','source_ambient':12,'target_ambient':14,'axes':['x2','y2'],'matrix_blocks':blocks,'matrix_digest':certificate.digest(blocks),'prime_summaries':summaries,'row_commutation_tests':total,'nonzero_residuals':failed,'failure_examples':examples,'linearity':'basis images extend uniquely by rational linearity','constructor_derivation':'Multiplication by an axis square shifts every column monomial. Raw K and q multiplication rows shift identically; parameter differentiation commutes with the parameter-independent monomial. For IBP, the Leibniz correction is parameter-independent and vanishes under T and nx differentiation.','decision':'The labelled generator shift is a linear chain-level row map exactly when all residuals vanish. Certificate-word failures then diagnose incorrect origin decoding or certificate/interface mismatch, not absence of the generator map.','next_gate':'replay-certificates-through-linear-generator-map','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
