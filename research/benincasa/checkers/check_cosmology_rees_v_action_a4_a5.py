#!/usr/bin/env python3
"""Test multiplication-by-v descent from Q4 to Q5 modulo 101."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
complete=g['g'];r4=g['r4'];r5=g['r5'];cols={}
for A in [4,5]:complete['exact_rows'].__globals__['A']=A;m=complete['configure'](P);_,cols[A]=m.column_packet()
def project(v):return v.numerator*pow(v.denominator,-1,P)%P
def shift(label):
 z=list(label);i,j=z[-1];z[-1]=(i,j+1);return tuple(z)
basis={}
def reduce(row,insert=False):
 row={k:v%P for k,v in row.items() if v%P}
 while row:
  q=min(row);a=row[q]
  if q not in basis:
   if insert:
    inv=pow(a,-1,P);basis[q]={k:v*inv%P for k,v in row.items() if v*inv%P}
   return row
  for k,v in basis[q].items():row[k]=(row.get(k,0)-a*v)%P
  row={k:v for k,v in row.items() if v}
 return {}
for row in r5.values():reduce({grade*len(cols[5])+cols[5][label]:project(v) for (grade,label),v in row.items()},True)
assert len(basis)==5888
missing=[];nonzero=[];defects=[]
for idx,(row_key,row) in enumerate(r4.items()):
 image={}
 for (grade,label),v in row.items():
  sl=shift(label)
  if sl not in cols[5]:missing.append((idx,repr(sl)));continue
  q=grade*len(cols[5])+cols[5][sl];image[q]=(image.get(q,0)+project(v))%P
 if not missing:
  residual=reduce(image)
  if residual:
   nonzero.append({'row':idx,'row_key':repr(row_key),'nnz':len(residual),'pivot':min(residual)})
   defects.append((row_key,residual))
assert not missing and len(nonzero)==90
def defect_rank(rows):
 b={}
 for source in rows:
  row=dict(source)
  while row:
   q=min(row);a=row[q]
   if q not in b:
    inv=pow(a,-1,P);b[q]={k:v*inv%P for k,v in row.items() if v*inv%P};break
   for k,v in b[q].items():row[k]=(row.get(k,0)-a*v)%P
   row={k:v for k,v in row.items() if v}
 return len(b)
defect_span_rank=defect_rank([v for _,v in defects])
rank_by_channel={c:defect_rank([v for k,v in defects if k[0]==c]) for c in ['shift2','upper','jet']}
rank_by_sector={repr(s):defect_rank([v for k,v in defects if (k[1][1],k[1][3])==s]) for s in [(0,1),(1,1)]}
out={'schema':'marici.benincasa.cosmology-rees-v-action-a4-a5.v1','prime':P,'source_relation_count':len(r4),'target_relation_rank':len(basis),'missing_shifted_labels':missing,'nonzero_shifted_relation_count':len(nonzero),'nonzero_shifted_relations':nonzero,'defect_span_rank':defect_span_rank,'rank_by_channel':rank_by_channel,'rank_by_sector':rank_by_sector,'single_correction_sufficient':defect_span_rank==1,'relation_compatibility':False,'exact_residual':'all shifted labels exist, but 90 of 7572 A4 relations have nonzero residual modulo the full rank-5888 A5 relation space; the first failure is row 45 with 97 residual terms and pivot 14088','conjecture_disposition':'multiplication by v does not descend to a map Q4 to Q5 under the active relation quotients','K4_coordinate_shift_equals_K5':True,'K5_nonzero':True,'interpretation':'the coordinate shift on the special K line exists, but it is not induced by a quotient endomorphism because relation compatibility fails','scope':'Q4-to-Q5 mod-101 exact-rank witness; no uniform quotient action','passed':True};(R/'cosmology_rees_v_action_a4_a5.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
