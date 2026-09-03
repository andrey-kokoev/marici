"""Construct exact rational source words for six Hessian components on 1,224 seeds."""
from __future__ import annotations
import hashlib,json,os,sys
from fractions import Fraction
from pathlib import Path
os.environ['MARICI_AMBIENT']='12'
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as ex
import check_cosmology_source_word_axis_square_transport as tr
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_second_jet_exact_membership.json';CERT=RES/'cosmology_second_jet_exact_certificate_words.json';P=32003
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,0)+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def mod_reduce(row,basis,insert=False):
 r={c:v%P for c,v in row.items() if v%P}
 while r:
  p=min(r);b=basis.get(p)
  if b is None:
   if insert:q=pow(r[p],-1,P);r={c:(v*q)%P for c,v in r.items()};basis[p]=r
   return r
  a=r[p]
  for c,v in b.items():
   z=(r.get(c,0)-a*v)%P
   if z:r[c]=z
   else:r.pop(c,None)
 return r
def exact_reduce(row,basis,insert=False,source_index=None,defs=None):
 r={c:Fraction(v) for c,v in row.items() if v};deps=[]
 while r:
  p=min(r);b=basis.get(p)
  if b is None:
   if insert:
    inv=1/r[p];r={c:v*inv for c,v in r.items()};basis[p]=r;defs[p]=(source_index,deps,inv)
   return r,deps
  a=r[p];deps.append((p,a));add(r,b,-a)
 return r,deps
def second_rows(columns,point,direction):
 samples=adapter.sampled_rows(columns,point,direction);weights=rees.interpolation_weights(2);return [rees.combine(rows,weights) for rows in zip(*samples,strict=True)]
def components(columns,point):
 vectors={'00':(1,0,0),'11':(1,-1,0),'22':(3,0,-1)};diag={k:second_rows(columns,point,v) for k,v in vectors.items()};out=dict(diag);inv2=pow(2,-1,base.PRIME)
 for a,b,name in [('00','11','01'),('00','22','02'),('11','22','12')]:
  s=second_rows(columns,point,tuple(vectors[a][i]+vectors[b][i] for i in range(3)));out[name]=[rees.combine((x,y,z),(inv2,-inv2,-inv2)) for x,y,z in zip(s,diag[a],diag[b],strict=True)]
 return out
def main():
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);t1=(1,-1,0);_,cols=rees.column_packet();ibp,K,q=tr.descs(12);all_desc=ibp+K+q;nI=len(ibp);nK=len(K);packets={};old=base.PRIME
 try:
  for prime in ex.PS:
   base.PRIME=prime;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,t1);packets[prime]={'source':T+raw[nI:nI+nK]+raw[nI+nK:],**components(cols,point)}
 finally:base.PRIME=old
 source_labels=[('T',i) for i in range(len(all_desc))]+[('S_K',i) for i in range(len(K))]+[('Q',i) for i in range(len(q))];mb={};selected=[]
 for i,row in enumerate(packets[P]['source']):
  before=len(mb);mod_reduce(row,mb,True)
  if len(mb)>before:selected.append(i)
 assert len(selected)==8793
 def esource(i):return ex.exact_row([packets[p]['source'][i] for p in ex.PS])
 def etarget(k,i):return ex.exact_row([packets[p][k][i] for p in ex.PS])
 eb={};ed={}
 for i in selected:
  rem,_=exact_reduce(esource(i),eb,True,i,ed);assert rem
 memo={}
 def expand(p):
  if p in memo:return memo[p]
  src,deps,inv=ed[p];w={src:inv}
  for q,a in deps:add(w,expand(q),-inv*a)
  memo[p]=w;return w
 targets=[]
 for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
  for rec in json.loads((RES/name).read_text())['records']:targets.append((family,rec['source_certificate']['canonical_target_id'],all_desc.index(tr.target_desc(family,rec))))
 certs=[];zero_targets=0;max_terms=max_num=max_den=0;component_census={}
 for k in ('00','01','02','11','12','22'):
  component_census[k]={'targets':0,'zero_raw':0,'exact_nonzero':0}
  for family,tid,i in targets:
   target=etarget(k,i);component_census[k]['targets']+=1
   if not target:zero_targets+=1;component_census[k]['zero_raw']+=1;word={};deps=[]
   else:
    rem,deps=exact_reduce(target,eb,False);assert not rem;word={}
    for p,a in deps:add(word,expand(p),a)
    recon={}
    for j,a in word.items():add(recon,esource(j),a)
    assert recon=={c:Fraction(v) for c,v in target.items()};component_census[k]['exact_nonzero']+=1
   terms=[]
   for j,a in sorted(word.items()):
    kind,row_index=source_labels[j];terms.append({'kind':kind,'row_index':row_index,'numerator':a.numerator,'denominator':a.denominator});max_num=max(max_num,abs(a.numerator));max_den=max(max_den,a.denominator)
   max_terms=max(max_terms,len(terms));digest=hashlib.sha256(json.dumps(terms,separators=(',',':')).encode()).hexdigest();certs.append({'component':k,'family':family,'target_id':tid,'word_terms':terms,'word_sha256':digest})
 assert len(certs)==7344
 CERT.write_text(json.dumps({'schema':'marici.voevodsky.second-jet-exact-certificate-words.v1','records':certs},indent=2)+'\n')
 out={'schema':'marici.voevodsky.cosmology-second-jet-exact-membership.v1','status':'all_7344_hessian_seed_targets_exact_in_unchanged_Q_image','targets':len(certs),'zero_raw_targets':zero_targets,'source_rank':len(eb),'component_census':component_census,'max_word_terms':max_terms,'max_abs_numerator':max_num,'max_denominator':max_den,'certificate_file':str(CERT.relative_to(ROOT)).replace('\\','/'),'verification':'Four-prime CRT-reconstructed integer rows; every nonzero Hessian target replayed from its rational source word with zero residual.','claim_boundary':'Exactness holds in the unchanged A12 algebraic relation image; no second-order extension or Bockstein interface is defined.','next_gate':'transport-second-jet-exactness-all-even','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
