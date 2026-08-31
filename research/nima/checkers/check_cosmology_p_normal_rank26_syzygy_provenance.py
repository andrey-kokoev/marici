"""Emit bounded replayable provenance for independent p-normal syzygy images."""
from __future__ import annotations
import hashlib,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];P=int(os.environ.get('MARICI_FIELD_PRIME','32003'));A=int(os.environ.get('MARICI_AMBIENT','8'))
os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']=str(A);os.environ['MARICI_POINT']='2,3,-5';sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');adapter=importlib.import_module('check_cosmology_rank26_p_normal_raw_relation_adapter')
def sub(dst,src,k):
 for c,v in src.items():
  z=(dst.get(c,0)-k*v)%P
  if z:dst[c]=z
  else:dst.pop(c,None)
def scale(row,k):return {c:v*k%P for c,v in row.items() if v*k%P}
def digest(row):return hashlib.sha256(';'.join(f'{c}:{v}' for c,v in sorted(row.items())).encode()).hexdigest()
def replay(rows,prov):
 out={}
 for i,k in prov.items():
  for c,v in rows[i].items():
   z=(out.get(c,0)+k*v)%P
   if z:out[c]=z
   else:out.pop(c,None)
 return out
def reduce_row(row,piv):
 row=dict(row)
 while row:
  p=max(row);q=piv.get(p)
  if q is None:break
  sub(row,q,row[p])
 return row
def add_pivot(row,piv):
 row=reduce_row(row,piv)
 if not row:return False,None
 p=max(row);iv=pow(row[p],-1,P);row=scale(row,iv);piv[p]=row;return True,p
def main():
 point=(3,6,-3);low,cols=rees.column_packet();ordered=[None]*len(cols)
 for label,c in cols.items():ordered[c]=label
 special=list(rees.raw_relations(point,cols));deriv,_=adapter.derivative_rows(cols,point,(1,0,0));paired={};deps=[]
 for sid,(r0,r1) in enumerate(zip(special,deriv,strict=True)):
  a=dict(r0);b=dict(r1);prov={sid:1}
  while a:
   p=max(a);q=paired.get(p)
   if q is None:break
   q0,q1,qp=q;c0=a[p];c1=b.get(p,0);sub(a,q0,c0);sub(b,q1,c0);sub(b,q0,c1);sub(prov,qp,c0)
  if a:
   p=max(a);iv=pow(a[p],-1,P);a=scale(a,iv);b=scale(b,iv);prov=scale(prov,iv);d=b.get(p,0);sub(b,a,d);paired[p]=(a,b,prov)
  else:deps.append((b,prov))
 r0p={p:q[0] for p,q in paired.items()};combined=dict(r0p);base=set(r0p);selected=[]
 for b,prov in deps:
  before=set(combined);added,p=add_pivot(b,combined)
  if added and p not in base:
   special_replay=replay(special,prov);assert not special_replay
   dreplay=replay(deriv,prov);selected.append((p,combined[p],prov,dreplay))
 assert len(selected)==7
 replay_span=dict(r0p);start=len(replay_span)
 for _,_,_,dreplay in selected:add_pivot(dreplay,replay_span)
 assert len(replay_span)-start==7
 full=[];preview=[]
 for idx,(pivot,generator,prov,dreplay) in enumerate(selected):
  assert reduce_row(dict(dreplay),r0p) and reduce_row(dict(generator),r0p)
  # The selected normalized quotient basis and replayed derivative span the same
  # growing image; exact scalar equality is not required candidate-by-candidate.
  item={'candidate':idx,'pivot_column':pivot,'pivot_label':ordered[pivot],'source_coefficients':{str(k):v for k,v in sorted(prov.items())},'generator_coordinates':{str(k):v for k,v in sorted(generator.items())},'derivative_replay_coordinates':{str(k):v for k,v in sorted(dreplay.items())},'special_replay_residual':special_replay}
  full.append(item);preview.append({'candidate':idx,'pivot_column':pivot,'pivot_label':ordered[pivot],'source_coefficient_count':len(prov),'source_sha256':digest(prov),'generator_coordinate_count':len(generator),'generator_sha256':digest(generator),'special_replay_zero':True})
 side=ROOT/'research'/'nima'/'results'/f'cosmology_p_normal_rank26_syzygy_provenance_full_a{A}_p{P}.json';side.write_text(json.dumps({'schema':'marici.cosmology-p-normal-rank26-syzygy-provenance-full.v1','candidates':full},separators=(',',':'))+'\n')
 payload={'schema':'marici.cosmology-p-normal-rank26-syzygy-provenance.v1','prime':P,'ambient':A,'point':list(point),'row_count':len(special),'special_rank':len(paired),'dependency_count':len(deps),'selected_length_one_image_count':len(selected),'candidates':preview,'full_sidecar':str(side.relative_to(ROOT)).replace('\\','/'),'full_sidecar_sha256':hashlib.sha256(side.read_bytes()).hexdigest(),'all_special_dependency_replays_zero':True,'input_identity':'source-version-bound ordinal row ids per Benincasa v1 contract','tau_p_map_constructed':False,'physical_period_constructed':False,'passed':True}
 out=ROOT/'research'/'nima'/'results'/f'cosmology_p_normal_rank26_syzygy_provenance_a{A}_p{P}.json';out.write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps({'passed':True,'selected':len(selected),'sidecar_sha256':payload['full_sidecar_sha256']}))
if __name__=='__main__':main()
