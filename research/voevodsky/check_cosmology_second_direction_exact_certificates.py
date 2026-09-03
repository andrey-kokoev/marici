"""Construct exact rational full-image words for the 390 second-tangent targets."""
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
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_second_direction_exact_certificates.json';CERT=RES/'cosmology_second_direction_exact_certificate_words.json';P=32003
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,0)+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def mod_reduce(row,basis,insert=False,source_index=None,defs=None):
 r={c:v%P for c,v in row.items() if v%P};deps=[]
 while r:
  p=min(r);b=basis.get(p)
  if b is None:
   if insert:
    inv=pow(r[p],-1,P);r={c:(v*inv)%P for c,v in r.items()};basis[p]=r;defs[p]=(source_index,deps,inv)
   return r
  a=r[p];deps.append((p,a));
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
def main():
 prior=json.loads((RES/'cosmology_second_tangent_normal_exact_replay.json').read_text());wanted=set(prior['unresolved_target_ids']);gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);t1=tuple(gate['integral_unit_normals']['p_tangent_difference']);t2=(3,0,-1);_,cols=rees.column_packet();ibp,K,q=tr.descs(12);all_desc=ibp+K+q;nI=len(ibp);nK=len(K);packets={};old=base.PRIME
 try:
  for prime in ex.PS:
   base.PRIME=prime;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,t1);D2,_=adapter.derivative_rows(cols,point,t2);packets[prime]=(T+raw[nI:nI+nK]+raw[nI+nK:],D2)
 finally:base.PRIME=old
 source_labels=[('T',i) for i in range(len(all_desc))]+[('S_K',i) for i in range(len(K))]+[('Q',i) for i in range(len(q))]
 mb={};md={};selected=[]
 for i,row in enumerate(packets[P][0]):
  before=len(mb);mod_reduce(row,mb,True,i,md)
  if len(mb)>before:selected.append(i)
 assert len(selected)==8793
 def erow_source(i):return ex.exact_row([packets[p][0][i] for p in ex.PS])
 def erow_target(i):return ex.exact_row([packets[p][1][i] for p in ex.PS])
 eb={};ed={}
 for i in selected:
  rem,_=exact_reduce(erow_source(i),eb,True,i,ed);assert rem
 assert len(eb)==len(selected)
 records={}
 for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
  for rec in json.loads((RES/name).read_text())['records']:
   tid=rec['source_certificate']['canonical_target_id']
   if tid in wanted:records[tid]=(family,tr.target_desc(family,rec))
 index={d:i for i,d in enumerate(all_desc)};memo={}
 def expand(p):
  if p in memo:return memo[p]
  src,deps,inv=ed[p];word={src:inv}
  for q,a in deps:add(word,expand(q),-inv*a)
  memo[p]=word;return word
 certs=[];max_terms=0;max_num=0;max_den=0
 for tid,(family,d) in sorted(records.items()):
  target=erow_target(index[d]);rem,deps=exact_reduce(target,eb,False);assert not rem;word={}
  for p,a in deps:add(word,expand(p),a)
  recon={}
  for i,a in word.items():add(recon,erow_source(i),a)
  assert recon=={c:Fraction(v) for c,v in target.items()};terms=[]
  for i,a in sorted(word.items()):
   k,j=source_labels[i];terms.append({'kind':k,'row_index':j,'numerator':a.numerator,'denominator':a.denominator});max_num=max(max_num,abs(a.numerator));max_den=max(max_den,a.denominator)
  max_terms=max(max_terms,len(terms));dig=hashlib.sha256(json.dumps(terms,separators=(',',':')).encode()).hexdigest();certs.append({'target_id':tid,'family':family,'word_terms':terms,'word_sha256':dig,'term_count':len(terms)})
 CERT.write_text(json.dumps({'schema':'marici.voevodsky.second-direction-exact-certificate-words.v1','records':certs},indent=2)+'\n')
 out={'schema':'marici.voevodsky.cosmology-second-direction-exact-certificates.v1','status':'all_390_second_tangent_targets_exactly_absorbed_over_Q','certificates':len(certs),'full_source_rank':len(eb),'max_word_terms':max_terms,'max_abs_numerator':max_num,'max_denominator':max_den,'certificate_file':str(CERT.relative_to(ROOT)).replace('\\','/'),'verification':'Every sparse rational word was replayed against four-prime CRT-reconstructed integer rows with exact zero residual.','consequence':'The second tangent class and, by D_n2=D_nx-D_t2, the derived unit-normal class vanish over Q for all 390 formerly unresolved A12 targets.','scope':'A12 labelled algebraic presentation; all-even transport and geometric normal-bundle interpretation are separate gates.','next_gate':'transport-second-direction-exact-certificates-all-even','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
