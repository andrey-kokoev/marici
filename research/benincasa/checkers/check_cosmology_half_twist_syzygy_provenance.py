#!/usr/bin/env python3
"""Materialize replayable degree-eight half-twist p-normal syzygy provenance."""
import argparse,hashlib,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,required=True,choices=(32003,32009));ap.add_argument('--ambient',type=int,choices=(8,10,12,14),default=8);ap.add_argument('--k-depth',type=int,choices=(2,3,4),default=2);a=ap.parse_args();P=a.prime;A=a.ambient;KD=a.k_depth;os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']=str(A);os.environ['MARICI_POINT']='2,3,-5';sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
 rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');adapter=importlib.import_module('check_cosmology_rank26_p_normal_raw_relation_adapter');rees.charts.GAMMA=-pow(2,-1,P)%P;rees.charts.K_DEPTH=KD
 def sub(dst,src,k):
  for c,v in src.items():
   z=(dst.get(c,0)-k*v)%P
   if z:dst[c]=z
   else:dst.pop(c,None)
 def scale(row,k):return {c:v*k%P for c,v in row.items() if v*k%P}
 def replay(rows,prov):
  out={}
  for i,k in prov.items():
   for c,v in rows[i].items():
    z=(out.get(c,0)+k*v)%P
    if z:out[c]=z
    else:out.pop(c,None)
  return out
 def reduce(row,piv):
  row=dict(row)
  while row:
   p=max(row);q=piv.get(p)
   if q is None:break
   sub(row,q,row[p])
  return row
 def addpivot(row,piv):
  row=reduce(row,piv)
  if not row:return None
  p=max(row);piv[p]=scale(row,pow(row[p],-1,P));return p
 point=(3,6,-3);low,cols=rees.column_packet();ordered=[None]*len(cols)
 for label,c in cols.items():ordered[c]=label
 special=list(rees.raw_relations(point,cols));deriv,checked=adapter.derivative_rows(cols,point,(1,0,0));assert checked==len(special);paired={};deps=[]
 for sid,(r0,r1) in enumerate(zip(special,deriv,strict=True)):
  x=dict(r0);y=dict(r1);prov={sid:1}
  while x:
   p=max(x);q=paired.get(p)
   if q is None:break
   q0,q1,qp=q;c0=x[p];c1=y.get(p,0);sub(x,q0,c0);sub(y,q1,c0);sub(y,q0,c1);sub(prov,qp,c0)
  if x:
   p=max(x);iv=pow(x[p],-1,P);x=scale(x,iv);y=scale(y,iv);prov=scale(prov,iv);sub(y,x,y.get(p,0));paired[p]=(x,y,prov)
  else:deps.append((y,prov))
 r0p={p:q[0] for p,q in paired.items()};combined=dict(r0p);selected=[]
 for y,prov in deps:
  p=addpivot(y,combined)
  if p is not None and p not in r0p:
   assert not replay(special,prov);selected.append((p,combined[p],prov,replay(deriv,prov)))
 expected={8:8,10:7,12:11,14:14}[A] if KD==2 else len(selected)
 if KD==2:assert len(selected)==expected
 span=dict(r0p)
 for _,_,_,row in selected:addpivot(row,span)
 assert len(span)-len(r0p)==expected
 items=[]
 for i,(p,g,prov,dr) in enumerate(selected):items.append({'candidate':i,'pivot_column':p,'pivot_label':ordered[p],'source_coefficients':{str(k):v for k,v in sorted(prov.items())},'generator_coordinates':{str(k):v for k,v in sorted(g.items())},'derivative_replay_coordinates':{str(k):v for k,v in sorted(dr.items())},'source_coefficient_count':len(prov)})
 body={'schema':'marici.benincasa.cosmology-half-twist-syzygy-provenance.v1','prime':P,'gamma_mod_prime':rees.charts.GAMMA,'ambient':A,'K_DEPTH':KD,'special_rank':len(paired),'dependency_count':len(deps),'candidate_count':len(items),'candidates':items,'all_special_replays_zero':True,'physical_period_constructed':False,'passed':True};raw=json.dumps(body,separators=(',',':'))+'\n';path=ROOT/'research'/'benincasa'/'results'/((f'cosmology_half_twist_syzygy_provenance_p{P}.json' if A==8 else f'cosmology_half_twist_syzygy_provenance_a{A}_p{P}.json') if KD==2 else f'cosmology_half_twist_syzygy_provenance_kd{KD}_a{A}_p{P}.json');path.write_text(raw);print(json.dumps({'prime':P,'ambient':A,'K_DEPTH':KD,'candidate_count':len(items),'sha256':hashlib.sha256(raw.encode()).hexdigest(),'passed':True}))
if __name__=='__main__':main()
