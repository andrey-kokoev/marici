#!/usr/bin/env python3
"""Resumable sparse mod-101 Q10 tau nonmembership elimination."""
import contextlib,io,json,pickle,runpy,time,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';TMP=ROOT/'.narada/tmp';TMP.mkdir(parents=True,exist_ok=True);CP=TMP/'cosmology-rees-q10-basis.tmpbin';MF=TMP/'cosmology-rees-q10-manifest.tmp.json';P=101;LIMIT=85;t=time.time()
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r=g['construct'](10);complete=g['g'];complete['exact_rows'].__globals__['A']=10;m=complete['configure'](P);_,cols=m.column_packet();width=len(cols);keys=list(r);digest=hashlib.sha256('\n'.join(map(repr,keys)).encode()).hexdigest()
if CP.exists():
 state=pickle.loads(CP.read_bytes());assert state['digest']==digest;basis=state['basis'];start=state['next_row']
else:basis={};start=0
def proj(v):return v.numerator*pow(v.denominator,-1,P)%P
def reduce(row,insert=False):
 while row:
  q=min(row);a=row[q];b=basis.get(q)
  if b is None:
   if insert:
    z=pow(a,-1,P);basis[q]={k:v*z%P for k,v in row.items() if v*z%P}
   return row
  for k,v in b.items():
   x=(row.get(k,0)-a*v)%P
   if x:row[k]=x
   else:row.pop(k,None)
 return {}
i=start
while i<len(keys) and time.time()-t<LIMIT:
 row=r[keys[i]];reduce({grade*width+cols[label]:proj(v) for (grade,label),v in row.items() if proj(v)},True);i+=1
status='checkpointed'
if i==len(keys):
 base=(0,1,1,1,1,1,(0,0));res=reduce({width+cols[base]:3});assert res;out={'schema':'marici.benincasa.cosmology-rees-tau-q10.v1','prime':P,'relation_rows':len(r),'relation_rank':len(basis),'tau_residual_nnz':len(res),'tau_nonzero':True,'passed':True};(R/'cosmology_rees_tau_q10.json').write_text(json.dumps(out,indent=2)+'\n');CP.unlink(missing_ok=True);status='complete'
else:CP.write_bytes(pickle.dumps({'digest':digest,'next_row':i,'basis':basis},protocol=5))
manifest={'schema':'marici.benincasa.q10-checkpoint.v1','status':status,'command':'python research/benincasa/checkers/check_cosmology_rees_tau_q10_checkpointed.py','source':str(Path(__file__).relative_to(ROOT)),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_label_digest':digest,'rows_complete':i,'rows_total':len(keys),'rank_so_far':len(basis),'checkpoint':str(CP.relative_to(ROOT)) if CP.exists() else None,'updated_at_epoch':time.time()};MF.write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest,indent=2))
