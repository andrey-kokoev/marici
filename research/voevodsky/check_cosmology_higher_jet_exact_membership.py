"""Exact Q-membership for all order 3-6 directional-basis seed derivatives."""
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
import check_cosmology_higher_jet_degree_six_audit as audit
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_higher_jet_exact_membership.json';CERT=RES/'cosmology_higher_jet_exact_certificate_words.json';P=32003
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
def derivative_rows(cols,point,d,order):
 samples=adapter.sampled_rows(cols,point,d);w=rees.interpolation_weights(order);return [rees.combine(rows,w) for rows in zip(*samples,strict=True)]
def main():
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);_,cols=rees.column_packet();ibp,K,q=tr.descs(12);all_desc=ibp+K+q;nI=len(ibp);nK=len(K);targets=[];di={d:i for i,d in enumerate(all_desc)}
 for family,name in [('IBP','cosmology_IBP_exact_source_certificates_a12.json'),('K','cosmology_nonmarked_K_exact_seeds_a12.json'),('q','cosmology_q_exact_source_certificates_a12.json')]:
  for rec in json.loads((RES/name).read_text())['records']:targets.append((family,rec['source_certificate']['canonical_target_id'],di[tr.target_desc(family,rec)]))
 directions={k:audit.directional_basis(k)[1] for k in range(3,7)};old=base.PRIME;base.PRIME=P;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,(1,-1,0));sourceP=T+raw[nI:nI+nK]+raw[nI+nK:];mb={};selected=[]
 for i,row in enumerate(sourceP):
  before=len(mb);mod_reduce(row,mb,True)
  if len(mb)>before:selected.append(i)
 assert len(selected)==8793;source_samples={i:[] for i in selected};target_samples={(k,ci):[] for k,ds in directions.items() for ci in range(len(ds))}
 try:
  for prime in ex.PS:
   base.PRIME=prime;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,(1,-1,0));source=T+raw[nI:nI+nK]+raw[nI+nK:]
   for i in selected:source_samples[i].append(source[i])
   for order,ds in directions.items():
    for ci,d in enumerate(ds):
     rows=derivative_rows(cols,point,d,order);target_samples[(order,ci)].append([rows[i] for _,_,i in targets])
 finally:base.PRIME=old
 source_labels=[('T',i) for i in range(len(all_desc))]+[('S_K',i) for i in range(len(K))]+[('Q',i) for i in range(len(q))]
 exact_source={i:ex.exact_row(rows) for i,rows in source_samples.items()};eb={};ed={}
 for i in selected:
  rem,_=exact_reduce(exact_source[i],eb,True,i,ed);assert rem
 memo={}
 def expand(p):
  if p in memo:return memo[p]
  src,deps,inv=ed[p];w={src:inv}
  for q,a in deps:add(w,expand(q),-inv*a)
  memo[p]=w;return w
 certs=[];census={};max_terms=max_num=max_den=0;total=zero=0
 for order,ds in directions.items():
  oc={'components':len(ds),'targets':0,'zero_raw':0,'exact_nonzero':0}
  for ci,d in enumerate(ds):
   prime_lists=target_samples[(order,ci)]
   for ti,(family,tid,index) in enumerate(targets):
    total+=1;oc['targets']+=1;target=ex.exact_row([prime_lists[pj][ti] for pj in range(len(ex.PS))])
    if not target:zero+=1;oc['zero_raw']+=1;continue
    rem,deps=exact_reduce(target,eb,False);assert not rem;word={}
    for p,a in deps:add(word,expand(p),a)
    recon={}
    for j,a in word.items():add(recon,exact_source[j],a)
    assert recon=={c:Fraction(v) for c,v in target.items()};oc['exact_nonzero']+=1;terms=[]
    for j,a in sorted(word.items()):
     kind,row_index=source_labels[j];terms.append({'kind':kind,'row_index':row_index,'numerator':a.numerator,'denominator':a.denominator});max_num=max(max_num,abs(a.numerator));max_den=max(max_den,a.denominator)
    max_terms=max(max_terms,len(terms));digest=hashlib.sha256(json.dumps(terms,separators=(',',':')).encode()).hexdigest();certs.append({'order':order,'basis_index':ci,'direction':d,'family':family,'target_id':tid,'word_terms':terms,'word_sha256':digest})
  census[str(order)]=oc
 assert total==90576
 CERT.write_text(json.dumps({'schema':'marici.voevodsky.higher-jet-exact-certificate-words.v1','records':certs},indent=2)+'\n')
 out={'schema':'marici.voevodsky.cosmology-higher-jet-exact-membership.v1','status':'all_order_3_to_6_seed_derivatives_exact_in_unchanged_Q_image','targets':total,'zero_raw_targets':zero,'nonzero_exact_certificates':len(certs),'source_rank':len(eb),'order_census':census,'max_word_terms':max_terms,'max_abs_numerator':max_num,'max_denominator':max_den,'certificate_file':str(CERT.relative_to(ROOT)).replace('\\','/'),'verification':'Every nonzero target was reconstructed from four-prime CRT integer rows and replayed with exact rational zero residual.','claim_boundary':'Exact raw-derivative membership only; no higher-jet extension, coherent primitive system, or connecting morphism.','next_gate':'transport-higher-jet-exactness-all-even','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
