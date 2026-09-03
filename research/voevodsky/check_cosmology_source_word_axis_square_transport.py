"""Replay all A12 source words after x^2/y^2 transport into A14."""
from __future__ import annotations
import json,os,sys
from fractions import Fraction
from itertools import product
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import cosmology_exact_source_certificate as certificate
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_source_word_axis_square_transport.json'
def descs(A):
 ibp=[('IBP',kp,(1,1,1,1,1),axis,e) for kp in range(charts.K_DEPTH) for axis in range(2) for e in base.monomials_at_most(A)]
 K=[('K',kp,lev,e) for kp in range(charts.K_DEPTH) for lev in product(range(1,charts.Q_DEPTH+1),repeat=5) for e in base.monomials_at_most(A-4)]
 q=[('q',qi,kp,lev,e) for qi in range(5) for kp in range(charts.K_DEPTH+1) for lev in product(range(1,charts.Q_DEPTH+1),repeat=5) if lev[qi]!=charts.Q_DEPTH for e in base.monomials_at_most(A-1)]
 return ibp,K,q
def shift(d,axis):
 out=list(d);e=list(out[-1]);e[axis]+=2;out[-1]=tuple(e);return tuple(out)
def target_desc(family,record):
 c=dict(record['source_certificate']['descriptor'])
 if family=='IBP':return ('IBP',c['k_pole'],(1,1,1,1,1),c['axis'],tuple(c['exponent']))
 if family=='K':return ('K',c['k_pole'],tuple(c['levels']),tuple(c['exponent']))
 return ('q',c['q_index'],c['k_pole'],tuple(c['levels']),tuple(c['exponent']))
def main():
 old=rees.AMBIENT;rees.AMBIENT=14
 try:
  protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};origprime=base.PRIME
  i14,k14,q14=descs(14);all14=i14+k14+q14;nI14=len(i14);nK14=len(k14)
  for p in exact.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);packets[p]={'T':T,'S_K':raw[nI14:nI14+nK14],'Q':raw[nI14+nK14:],'dx':dx}
  base.PRIME=origprime
 finally:rees.AMBIENT=old
 i12,k12,q12=descs(12);all12=i12+k12+q12
 families=[('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]
 index14={'T':{d:i for i,d in enumerate(all14)},'S_K':{d:i for i,d in enumerate(k14)},'Q':{d:i for i,d in enumerate(q14)},'dx':{d:i for i,d in enumerate(all14)}};decode12={'T':all12,'S_K':k12,'Q':q12};cache={};records=[];failures={'IBP':{'x2':0,'y2':0},'K':{'x2':0,'y2':0},'q':{'x2':0,'y2':0}}
 def exact_at(kind,index):
  key=(kind,index)
  if key not in cache:cache[key]=exact.exact_row([packets[p][kind][index] for p in exact.PS])
  return cache[key]
 for family,name in families:
  for record in json.loads((RES/name).read_text())['records']:
   c=record['source_certificate'];coef=[Fraction(0) for _ in c['source_basis']]
   for t in c['sparse_word']:coef[t['basis_index']]=Fraction(t['numerator'],t['denominator'])
   td=target_desc(family,record)
   for axis,label in ((0,'x2'),(1,'y2')):
    transported=[];rows=[]
    for kind,idx in c['source_basis']:
     d=shift(decode12[kind][idx],axis);transported.append(d);rows.append(exact_at(kind,index14[kind][d]))
    target=exact_at('dx',index14['dx'][shift(td,axis)]);recon={}
    for a,row in zip(coef,rows):
     for col,v in row.items():recon[col]=recon.get(col,Fraction(0))+a*v
    recon={k:v for k,v in recon.items() if v};residual=dict(recon)
    for col,v in target.items():residual[col]=residual.get(col,Fraction(0))-v
    residual={k:v for k,v in residual.items() if v};failures[family][label]+=bool(residual)
    records.append({'source_target_id':c['canonical_target_id'],'family':family,'axis_square':label,'target_ambient':14,'transported_target_id':'target:'+certificate.digest(shift(td,axis)),'transported_source_basis':transported,'transported_source_basis_digest':certificate.digest(transported),'coefficient_word_action':'identity','coefficient_word_digest':certificate.digest(c['sparse_word']),'commutation_residual_digest':certificate.digest(residual),'commutation_residual_support':len(residual),'commutes':not residual})
 assert len(records)==2448
 zero=sum(r['commutes'] for r in records);failed=len(records)-zero
 out={'schema':'marici.voevodsky.cosmology-source-word-axis-square-transport.v1','status':'naive_descriptor_shift_identity_word_transport_fails' if failed else 'all_words_commute','source_ambient':12,'target_ambient':14,'transport_records':records,'transport_count':len(records),'coefficient_action_tested':'identity on normalized sparse rational coefficients; basis and target descriptors shift exponent by (2,0) or (0,2)','zero_residuals':zero,'nonzero_residuals':failed,'failures_by_family_axis':failures,'decision':('Identity coefficient transport is verified for every generating square.' if not failed else 'Do not serialize naive exponent shift as the source-word transport action when any residual is nonzero.'),'scope':'one generating A12-to-A14 transport square for each axis; no geometric support, source differential, DNC comparison, or horn consequence','next_gate':('verify-transport-composition-A12-A14-A16' if not failed else 'derive-corrected-source-word-transport-action'),'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='transport_records'},indent=2))
if __name__=='__main__':main()
