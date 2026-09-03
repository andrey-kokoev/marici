"""Exact full F_g-image membership for twelve grade-violating t2 q targets."""
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
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_filtered_violation_full_image.json';CERT=RES/'cosmology_filtered_violation_exact_words.json'
def grade(d):
 if d[0] in ('IBP','K'):return d[1]+sum(d[2])+1
 return d[2]+sum(d[3])+1
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,0)+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def reduce(row,basis,insert=False,source_index=None,defs=None):
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
 audit=json.loads((RES/'cosmology_full_jet_pole_filtered_admissibility.json').read_text());bad={e['target_id']:e['target_grade'] for e in audit['examples']};assert len(bad)==12
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);t1=(1,-1,0);t2=(3,0,-1);_,cols=rees.column_packet();ibp,K,q=tr.descs(12);alls=ibp+K+q;nI=len(ibp);nK=len(K);packets={};old=base.PRIME
 try:
  for p in ex.PS:
   base.PRIME=p;raw=list(rees.raw_relations(point,cols));T,_=adapter.derivative_rows(cols,point,t1);D2,_=adapter.derivative_rows(cols,point,t2);packets[p]={'source':T+raw[nI:nI+nK]+raw[nI+nK:],'target':D2}
 finally:base.PRIME=old
 labels=[('T',i) for i in range(len(alls))]+[('S_K',i) for i in range(len(K))]+[('Q',i) for i in range(len(q))];descs=alls+K+q;grades=[grade(d) for d in descs];allowed=[i for i,g in enumerate(grades) if g<=8];exact_source={i:ex.exact_row([packets[p]['source'][i] for p in ex.PS]) for i in allowed};target_info={}
 for r in json.loads((RES/'cosmology_q_exact_source_certificates_a12.json').read_text())['records']:
  tid=r['source_certificate']['canonical_target_id']
  if tid in bad:target_info[tid]=alls.index(tr.target_desc('q',r))
 assert set(target_info)==set(bad);basis={};defs={};memo={};records=[];nonmembers=[];ranks={};cursor=0;ordered=sorted(allowed,key=lambda i:(grades[i],i))
 def expand(p):
  if p in memo:return memo[p]
  src,deps,inv=defs[p];w={src:inv}
  for q,a in deps:add(w,expand(q),-inv*a)
  memo[p]=w;return w
 for g in (6,7,8):
  while cursor<len(ordered) and grades[ordered[cursor]]<=g:
   i=ordered[cursor];reduce(exact_source[i],basis,True,i,defs);cursor+=1
  ranks[str(g)]=len(basis)
  for tid,tg in bad.items():
   if tg!=g:continue
   target=ex.exact_row([packets[p]['target'][target_info[tid]] for p in ex.PS]);rem,deps=reduce(target,basis,False)
   if rem:
    nonmembers.append({'target_id':tid,'grade':g,'residual_support':len(rem),'residual_sha256':hashlib.sha256(str(sorted(rem.items())).encode()).hexdigest()});continue
   word={}
   for p,a in deps:add(word,expand(p),a)
   recon={}
   for i,a in word.items():add(recon,exact_source[i],a)
   assert recon=={c:Fraction(v) for c,v in target.items()} and all(grades[i]<=g for i in word)
   terms=[{'kind':labels[i][0],'row_index':labels[i][1],'numerator':a.numerator,'denominator':a.denominator,'grade':grades[i]} for i,a in sorted(word.items())];records.append({'target_id':tid,'target_grade':g,'word_terms':terms,'max_source_grade':max((t['grade'] for t in terms),default=g)})
 CERT.write_text(json.dumps({'schema':'marici.voevodsky.filtered-violation-exact-words.v1','records':records},indent=2)+'\n')
 out={'schema':'marici.voevodsky.cosmology-filtered-violation-full-image.v1','status':('all_twelve_have_grade_bounded_exact_primitives' if not nonmembers else 'genuine_pole_filtered_nonmembers_found'),'targets':12,'filtered_image_ranks':ranks,'exact_members':len(records),'exact_nonmembers':len(nonmembers),'nonmembers':nonmembers,'certificate_file':str(CERT.relative_to(ROOT)).replace('\\','/'),'decision':('All twelve earlier violations were poor certificate choices; the full positive jet remains zero in the algebraic pole-filtered quotient.' if not nonmembers else 'Nonzero exact residuals certify algebraic pole-filtered classes for the listed targets.'),'claim_boundary':'Algebraic pole filtration only; no DNC/I-adic, support, exceptional, or physical interpretation.','next_gate':('classify-pole-filtered-full-jet-zero-theorem' if not nonmembers else 'classify-genuine-pole-filtered-jet-classes'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
