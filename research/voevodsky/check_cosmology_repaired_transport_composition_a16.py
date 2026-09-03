"""Verify direct/iterated A16 composition of repaired certificate transport."""
from __future__ import annotations
import json,os,sys
from fractions import Fraction
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import cosmology_exact_source_certificate as certificate
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_repaired_transport_composition_a16.json'
def addq(out,row,a):
 for c,v in row.items():
  x=out.get(c,Fraction(0))+a*v
  if x:out[c]=x
  else:out.pop(c,None)
def direct(d,delta):
 out=list(d);e=list(out[-1]);e[0]+=delta[0];e[1]+=delta[1];out[-1]=tuple(e);return tuple(out)
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);nx=tuple(protocol['integral_unit_normals']['nx']);oldA=rees.AMBIENT;orig=base.PRIME;rees.AMBIENT=16
 try:
  _,columns=rees.column_packet();i16,k16,q16=tr.descs(16);all16=i16+k16+q16;nI=len(i16);nK=len(k16);packets={}
  for p in exact.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);packets[p]={'T':T,'S_K':raw[nI:nI+nK],'Q':raw[nI+nK:],'dx':dx}
 finally:base.PRIME=orig;rees.AMBIENT=oldA
 i12,k12,q12=tr.descs(12);all12=i12+k12+q12;decode={'T':all12,'S_K':k12,'Q':q12};index={'T':{d:i for i,d in enumerate(all16)},'S_K':{d:i for i,d in enumerate(k16)},'Q':{d:i for i,d in enumerate(q16)},'dx':{d:i for i,d in enumerate(all16)}}
 paths={'x4':(0,0),'x2y2':(0,1),'y2x2':(1,0),'y4':(1,1)};deltas={'x4':(4,0),'x2y2':(2,2),'y2x2':(2,2),'y4':(0,4)};descriptor_checks=0
 for domain in (all12,k12,q12,all12):
  for d in domain:
   for name,(a,b) in paths.items():assert tr.shift(tr.shift(d,a),b)==direct(d,deltas[name]);descriptor_checks+=1
 cache={}
 def erow(kind,i):
  key=(kind,i)
  if key not in cache:cache[key]=exact.exact_row([packets[p][kind][i] for p in exact.PS])
  return cache[key]
 families=[('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')];records=[];failures=0;path_failures=0
 for family,name in families:
  for record in json.loads((RES/name).read_text())['records']:
   c=record['source_certificate'];coef=[Fraction(0) for _ in c['source_basis']]
   for t in c['sparse_word']:coef[t['basis_index']]=Fraction(t['numerator'],t['denominator'])
   td12=tr.target_desc(family,record);endpoint_digests={}
   for path,(a,b) in paths.items():
    transported=[tr.shift(tr.shift(decode[k][i],a),b) for k,i in c['source_basis']];targetd=tr.shift(tr.shift(td12,a),b);recon={}
    for coefficient,(kind,_),desc in zip(coef,c['source_basis'],transported):addq(recon,erow(kind,index[kind][desc]),coefficient)
    target=erow('dx',index['dx'][targetd]);bad=recon!=target;failures+=bad;word_digest=certificate.digest({'basis':transported,'coefficients':c['sparse_word']});endpoint_digests[path]=word_digest
    records.append({'source_target_id':c['canonical_target_id'],'family':family,'path':path,'A16_target_id':'target:'+certificate.digest(targetd),'transported_word_digest':word_digest,'commutation_residual_support':0 if not bad else len(set(recon).union(target)),'commutes':not bad})
   path_failures+=endpoint_digests['x2y2']!=endpoint_digests['y2x2']
 assert len(records)==4896 and failures==path_failures==0
 out={'schema':'marici.voevodsky.cosmology-repaired-transport-composition-a16.v1','status':'direct_and_iterated_A16_transport_commute','descriptor_composition_checks':descriptor_checks,'certificate_path_records':len(records),'certificate_equations':4896,'nonzero_equation_residuals':failures,'mixed_path_word_digest_mismatches':path_failures,'paths':['x4','x2y2','y2x2','y4'],'records':records,'decision':'The repaired labelled transport composes from A12 through A14 to A16; mixed squared-axis order is path-independent, and all unchanged coefficient words solve exactly at A16.','scope':'finite A12/A14/A16 labelled algebraic relation presentations; no source differential, geometric support, DNC comparison, or horn consequence','next_gate':'promote-linear-transport-to-all-even-A','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
