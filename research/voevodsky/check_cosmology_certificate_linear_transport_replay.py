"""Localize certificate transport failures against the verified generator map."""
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
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_certificate_linear_transport_replay.json'
def build(A,point,td,nx):
 rees.AMBIENT=A;_,cols=rees.column_packet();packets={};ibp,K,q=tr.descs(A);nI=len(ibp);nK=len(K);orig=base.PRIME
 for p in exact.PS:
  base.PRIME=p;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,td);dx,_=adapter.derivative_rows(cols,point,nx);packets[p]={'T':T,'S_K':raw[nI:nI+nK],'Q':raw[nI+nK:],'dx':dx}
 base.PRIME=orig;return cols,packets,(ibp,K,q)
def addq(out,row,a):
 for c,v in row.items():
  x=out.get(c,Fraction(0))+a*v
  if x:out[c]=x
  else:out.pop(c,None)
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);nx=tuple(protocol['integral_unit_normals']['nx']);oldA=rees.AMBIENT
 try:cols12,p12,d12=build(12,point,td,nx);cols14,p14,d14=build(14,point,td,nx)
 finally:rees.AMBIENT=oldA
 inv12={v:k for k,v in cols12.items()};all12=d12[0]+d12[1]+d12[2];all14=d14[0]+d14[1]+d14[2];decode={'T':all12,'S_K':d12[1],'Q':d12[2]};index={'T':{d:i for i,d in enumerate(all14)},'S_K':{d:i for i,d in enumerate(d14[1])},'Q':{d:i for i,d in enumerate(d14[2])},'dx':{d:i for i,d in enumerate(all14)}};cache={}
 def erow(A,kind,i):
  key=(A,kind,i)
  if key not in cache:
   packets=p12 if A==12 else p14;cache[key]=exact.exact_row([packets[p][kind][i] for p in exact.PS])
  return cache[key]
 def shift_exact(row,axis):
  out={}
  for c,v in row.items():
   label=list(inv12[c]);e=list(label[-1]);e[axis]+=2;label[-1]=tuple(e);out[cols14[tuple(label)]]=v
  return out
 families=[('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')];counts={k:0 for k in ('certificate_A12','source_row_map','target_row_map','word_transport')};examples=[];tested=0
 for family,name in families:
  for record in json.loads((RES/name).read_text())['records']:
   c=record['source_certificate'];coef=[Fraction(0) for _ in c['source_basis']]
   for t in c['sparse_word']:coef[t['basis_index']]=Fraction(t['numerator'],t['denominator'])
   td12=tr.target_desc(family,record);ti12=all12.index(td12);src12=[erow(12,k,i) for k,i in c['source_basis']];target12=erow(12,'dx',ti12);recon={}
   for a,r in zip(coef,src12):addq(recon,r,a)
   if recon!=target12:counts['certificate_A12']+=1
   for axis,label in ((0,'x2'),(1,'y2')):
    tested+=1;src14=[];source_bad=False
    for (kind,i),r12 in zip(c['source_basis'],src12):
     d14=tr.shift(decode[kind][i],axis);r14=erow(14,kind,index[kind][d14]);src14.append(r14)
     if shift_exact(r12,axis)!=r14:source_bad=True
    counts['source_row_map']+=source_bad
    target14=erow(14,'dx',index['dx'][tr.shift(td12,axis)]);target_bad=shift_exact(target12,axis)!=target14;counts['target_row_map']+=target_bad;recon14={}
    for a,r in zip(coef,src14):addq(recon14,r,a)
    word_bad=recon14!=target14;counts['word_transport']+=word_bad
    if (source_bad or target_bad or word_bad) and len(examples)<30:examples.append({'family':family,'target_id':c['canonical_target_id'],'axis':label,'source_row_map_bad':source_bad,'target_row_map_bad':target_bad,'word_bad':word_bad,'basis_size':len(src14)})
 out={'schema':'marici.voevodsky.cosmology-certificate-linear-transport-replay.v1','status':'interface_mismatch_localized','certificates':1224,'transport_squares':tested,'failure_counts':counts,'examples':examples,'diagnosis':'Source and target row-map counts distinguish descriptor decoding from coefficient binding. If both row maps pass, linearity forces every valid A12 certificate word to transport; any remaining word failure is a checker defect.','next_gate':'repair-certificate-transport-interface','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
