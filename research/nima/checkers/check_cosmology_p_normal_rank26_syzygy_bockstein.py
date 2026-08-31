"""Extract first normal images of special relation syzygies in the full rank-26 presentation."""
from __future__ import annotations
import argparse,hashlib,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def add_scaled(row,other,scale,P):
 for c,v in other.items():
  z=(row.get(c,0)-scale*v)%P
  if z:row[c]=z
  else:row.pop(c,None)
def reduce_plain(row,piv,P):
 row=dict(row)
 while row:
  p=max(row);q=piv.get(p)
  if q is None:break
  add_scaled(row,q,row[p],P)
 return row
def add_basis(row,piv,P):
 row=reduce_plain(row,piv,P)
 if not row:return False
 p=max(row);iv=pow(row[p],-1,P);row={c:v*iv%P for c,v in row.items()};piv[p]=row;return True
def syzygy_images(special,derivatives,P):
 paired={};raw_images=[];zero_relations=0
 for r0,r1 in zip(special,derivatives,strict=True):
  a=dict(r0);b=dict(r1)
  while a:
   p=max(a);q=paired.get(p)
   if q is None:break
   q0,q1=q;coeff0=a[p];coeff1=b.get(p,0);add_scaled(a,q0,coeff0,P);add_scaled(b,q1,coeff0,P);add_scaled(b,q0,coeff1,P)
  if a:
   p=max(a);iv=pow(a[p],-1,P);a={c:v*iv%P for c,v in a.items()};b={c:v*iv%P for c,v in b.items()};d=b.get(p,0);add_scaled(b,a,d,P);paired[p]=(a,b)
  else:
   zero_relations+=1;raw_images.append(b)
 r0p={p:q[0] for p,q in paired.items()};combined=dict(r0p);base_pivots=set(r0p)
 for b in raw_images:add_basis(b,combined,P)
 images={p:r for p,r in combined.items() if p not in base_pivots}
 return paired,images,zero_relations
def rank_union(bases,P):
 out={}
 for basis in bases:
  for row in basis.values():add_basis(row,out,P)
 return len(out)
def digest_basis(b):
 s=';'.join(','.join(f'{c}:{v}' for c,v in sorted(r.items())) for _,r in sorted(b.items()));return hashlib.sha256(s.encode()).hexdigest()
def run(P,ambient,gamma_mode):
 os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']=str(ambient);os.environ['MARICI_POINT']='2,3,-5'
 sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
 base=importlib.import_module('physical_four_mark_residue_twisted_derham');rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');adapter=importlib.import_module('check_cosmology_rank26_p_normal_raw_relation_adapter')
 if gamma_mode=='half': rees.charts.GAMMA=-(pow(2,-1,P))%P
 point=(3,6,-3);_,cols=rees.column_packet();special=list(rees.raw_relations(point,cols));dirs={'nx':(1,0,0),'ny':(0,1,0),'tangent':(1,-1,0)};results={};bases={}
 for name,d in dirs.items():
  deriv,checked=adapter.derivative_rows(cols,point,d);assert checked==len(special)
  paired,img,zero=syzygy_images(special,deriv,P);bases[name]=img;results[name]={'special_rank':len(paired),'special_syzygy_count':zero,'bockstein_image_rank':len(img),'basis_support_sizes':[len(r) for _,r in sorted(img.items())],'basis_sha256':digest_basis(img)}
 r0p={p:q[0] for p,q in paired.items()}
 def quotient_union(names):
  piv=dict(r0p);start=len(piv)
  for name in names:
   for row in bases[name].values():add_basis(row,piv,P)
  return len(piv)-start
 combined={a+'_'+b:quotient_union((a,b)) for a,b in (('nx','ny'),('nx','tangent'),('ny','tangent'))};combined['all']=quotient_union(tuple(bases))
 packet={'schema':'marici.cosmology-p-normal-rank26-syzygy-bockstein.v1','prime':P,'ambient':ambient,'point':list(point),'gamma_mode':gamma_mode,'twist_gamma_mod_prime':rees.charts.GAMMA,'row_count':len(special),'column_count':len(cols),'directions':results,'combined_image_ranks':combined,'normal_images_equal':combined['nx_ny']==results['nx']['bockstein_image_rank']==results['ny']['bockstein_image_rank'],'tangent_image_contained_in_normal_image':combined['nx_tangent']==results['nx']['bockstein_image_rank'],'tau_p_comparison_computed':False,'physical_period_constructed':False,'passed':True}
 tag='' if gamma_mode=='generic' else '_half';out=ROOT/'research'/'nima'/'results'/f'cosmology_p_normal_rank26_syzygy_bockstein{tag}_a{ambient}_p{P}.json';out.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet,indent=2))
def main():
 a=argparse.ArgumentParser();a.add_argument('--prime',type=int,required=True);a.add_argument('--ambient',type=int,default=8);a.add_argument('--gamma',choices=('generic','half'),default='generic');x=a.parse_args();run(x.prime,x.ambient,x.gamma)
if __name__=='__main__':main()
