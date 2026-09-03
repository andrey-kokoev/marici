"""Transport all exact Hessian words through A14/A16 squared-axis paths."""
from __future__ import annotations
import json,os,sys
from fractions import Fraction
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as ex
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_second_jet_all_even_transport.json'
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,Fraction())+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def shift(d,path):
 for a in path:d=tr.shift(d,a)
 return d
def second_rows(cols,point,d):
 samples=adapter.sampled_rows(cols,point,d);w=rees.interpolation_weights(2);return [rees.combine(rows,w) for rows in zip(*samples,strict=True)]
def comps(cols,point):
 vec={'00':(1,0,0),'11':(1,-1,0),'22':(3,0,-1)};diag={k:second_rows(cols,point,v) for k,v in vec.items()};out=dict(diag);h=pow(2,-1,base.PRIME)
 for a,b,k in [('00','11','01'),('00','22','02'),('11','22','12')]:
  s=second_rows(cols,point,tuple(vec[a][i]+vec[b][i] for i in range(3)));out[k]=[rees.combine((x,y,z),(h,-h,-h)) for x,y,z in zip(s,diag[a],diag[b],strict=True)]
 return out
def main():
 certs=json.loads((RES/'cosmology_second_jet_exact_certificate_words.json').read_text())['records'];assert len(certs)==7344
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);t1=(1,-1,0);ind=json.loads((RES/'cosmology_all_even_linear_transport_induction.json').read_text());assert ind['passed'];ibp12,K12,q12=tr.descs(12);all12=ibp12+K12+q12;decode={'T':all12,'S_K':K12,'Q':q12};target_desc={}
 for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
  for r in json.loads((RES/name).read_text())['records']:target_desc[r['source_certificate']['canonical_target_id']]=tr.target_desc(family,r)
 plans={14:[(0,),(1,)],16:[(0,0),(0,1),(1,0),(1,1)]};requests={};oldA=rees.AMBIENT
 for A,paths in plans.items():
  rees.AMBIENT=A;_,cols=rees.column_packet();ibp,K,q=tr.descs(A);alls=ibp+K+q;idx={'T':{d:i for i,d in enumerate(alls)},'S_K':{d:i for i,d in enumerate(K)},'Q':{d:i for i,d in enumerate(q)}};req={k:set() for k in ('T','S_K','Q','00','01','02','11','12','22')};items=[]
  for c in certs:
   for path in paths:
    src=[]
    for term in c['word_terms']:
     k=term['kind'];i=idx[k][shift(decode[k][term['row_index']],path)];req[k].add(i);src.append((k,i,Fraction(term['numerator'],term['denominator'])))
    ti=idx['T'][shift(target_desc[c['target_id']],path)];req[c['component']].add(ti);items.append((c['target_id'],c['component'],path,src,ti))
  requests[A]=(cols,req,items,len(ibp),len(K))
 rees.AMBIENT=oldA;exact={}
 try:
  for A,(cols,req,items,nI,nK) in requests.items():
   per={k:{i:[] for i in ids} for k,ids in req.items()};rees.AMBIENT=A
   for p in ex.PS:
    base.PRIME=p;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,t1);pack={'T':T,'S_K':raw[nI:nI+nK],'Q':raw[nI+nK:],**comps(cols,point)}
    for k,ids in req.items():
     for i in ids:per[k][i].append(pack[k][i])
   exact[A]={k:{i:ex.exact_row(rows) for i,rows in vals.items()} for k,vals in per.items()}
 finally:base.PRIME=ex.PS[0];rees.AMBIENT=oldA
 checks={};fail=[]
 for A,(cols,req,items,nI,nK) in requests.items():
  seen={}
  for tid,k,path,src,ti in items:
   recon={}
   for sk,i,a in src:add(recon,exact[A][sk][i],a)
   target={c:Fraction(v) for c,v in exact[A][k][ti].items()}
   if recon!=target:fail.append({'A':A,'target_id':tid,'component':k,'path':path})
   seen[(tid,k,path)]=(tuple(src),target)
  checks[str(A)]={'path_replays':len(items),'failures':sum(x['A']==A for x in fail)}
  if A==16:
   for c in certs:assert seen[(c['target_id'],c['component'],(0,1))]==seen[(c['target_id'],c['component'],(1,0))]
   checks[str(A)]['mixed_path_equalities']=len(certs)
 assert not fail
 out={'schema':'marici.voevodsky.cosmology-second-jet-all-even-transport.v1','status':'all_symmetric_hessian_seed_words_exact_for_every_even_A','seed_component_words':len(certs),'A14':checks['14'],'A16':checks['16'],'exact_arithmetic':'four-prime CRT integer-row reconstruction and rational replay','induction':'Hessian interpolation commutes with the squared-axis descriptor embeddings; mixed paths agree at A16; parity-orbit induction covers every even A>=12.','theorem':'For every even A>=12, every labelled relation seed, and every symmetric bilinear direction in Sym^2(Q^3), the raw Hessian row lies in the unchanged algebraic source image.','claim_boundary':'No second-order jet complex, extension, admissibility rule, geometric comparison, or Bockstein is constructed.','next_gate':'classify-algebraic-second-jet-zero-theorem','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
