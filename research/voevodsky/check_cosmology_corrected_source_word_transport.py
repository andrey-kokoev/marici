"""Test canonical exact re-solving on transported source bases."""
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
import check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves as solver
import cosmology_exact_source_certificate as certificate
import check_cosmology_source_word_axis_square_transport as naive
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_corrected_source_word_transport.json'
def main():
 old=rees.AMBIENT;rees.AMBIENT=14
 try:
  protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};orig=base.PRIME
  i14,k14,q14=naive.descs(14);all14=i14+k14+q14;nI=len(i14);nK=len(k14)
  for p in exact.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);packets[p]={'T':T,'S_K':raw[nI:nI+nK],'Q':raw[nI+nK:],'dx':dx}
  base.PRIME=orig
 finally:rees.AMBIENT=old
 i12,k12,q12=naive.descs(12);all12=i12+k12+q12;decode={'T':all12,'S_K':k12,'Q':q12};index={'T':{d:i for i,d in enumerate(all14)},'S_K':{d:i for i,d in enumerate(k14)},'Q':{d:i for i,d in enumerate(q14)},'dx':{d:i for i,d in enumerate(all14)}};cache={}
 def row(kind,i):
  key=(kind,i)
  if key not in cache:cache[key]=exact.exact_row([packets[p][kind][i] for p in exact.PS])
  return cache[key]
 families=[('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')];records=[];unsolved=[];changed=0;unsolved_by={'IBP':{'x2':0,'y2':0},'K':{'x2':0,'y2':0},'q':{'x2':0,'y2':0}}
 for family,name in families:
  for record in json.loads((RES/name).read_text())['records']:
   c=record['source_certificate'];oldcoef=[Fraction(0) for _ in c['source_basis']]
   for t in c['sparse_word']:oldcoef[t['basis_index']]=Fraction(t['numerator'],t['denominator'])
   td=naive.target_desc(family,record)
   for axis,label in ((0,'x2'),(1,'y2')):
    transported=[naive.shift(decode[k][i],axis) for k,i in c['source_basis']];rows=[row(k,index[k][d]) for (k,_),d in zip(c['source_basis'],transported)];target=row('dx',index['dx'][naive.shift(td,axis)]);cols=sorted(set(target).union(*(r.keys() for r in rows)))
    try:newcoef,rank=solver.solve_rect(rows,target,cols)
    except AssertionError:
     unsolved_by[family][label]+=1;unsolved.append({'source_target_id':c['canonical_target_id'],'family':family,'axis_square':label,'basis_size':len(rows),'equations':len(cols)});continue
    recon={}
    for a,r in zip(newcoef,rows):
     for col,v in r.items():solver.addq(recon,col,a*v)
    assert recon==target;changed+=newcoef!=oldcoef
    word=[{'basis_index':i,'numerator':a.numerator,'denominator':a.denominator} for i,a in enumerate(newcoef) if a]
    records.append({'source_target_id':c['canonical_target_id'],'family':family,'axis_square':label,'transported_target_id':'target:'+certificate.digest(naive.shift(td,axis)),'transported_source_basis_digest':certificate.digest(transported),'corrected_sparse_word':word,'corrected_word_digest':certificate.digest(word),'rank':rank,'commutation_residual':[]})
 out={'schema':'marici.voevodsky.cosmology-corrected-source-word-transport.v1','status':'transported_same_basis_not_always_spanning' if unsolved else 'all_transports_resolved','transport_squares':2448,'exact_resolved':len(records),'unsolved':len(unsolved),'unsolved_by_family_axis':unsolved_by,'unsolved_records':unsolved,'coefficient_words_changed':changed,'decision':('Every shifted basis spans with the unchanged coefficient word.' if not unsolved and not changed else 'Canonical re-solving is not a total identity transport when unsolved>0 or coefficients change.'),'scope':'A12-to-A14 exact algebraic test only','next_gate':('verify-transport-composition-A12-A14-A16' if not unsolved and not changed else 'transported-source-dag-closure'),'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
