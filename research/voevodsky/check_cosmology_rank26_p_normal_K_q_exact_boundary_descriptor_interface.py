"""Verify typed descriptor interfaces and ambient shift maps for exact boundary source words."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_exact_boundary_descriptor_interface.json'
def key(d):
 f,k,l,ax,m,e=d;return (f,k,tuple(l),ax,m,tuple(e))
def shift(d,n):
 f,k,l,ax,m,e=d;return (f,k,tuple(l),ax,m,(e[0],e[1]+n))
def main():
 summaries={};interfaces={}
 for A in (12,14,16):
  full,sk=compat.descriptors(A);q=[d for d in full if d[0]=='q'];assert len(full)==len(set(map(key,full)));assert len(sk)==len(set(map(key,sk)));assert len(q)==len(set(map(key,q)))
  exact=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json').read_text());assert exact['passed']
  expected=2*sum(d+1 for d in range(A-6,A-3));assert exact['targets_verified']==expected
  summaries[str(A)]={'T_descriptors':len(full),'S_K_descriptors':len(sk),'Q_descriptors':len(q),'boundary_targets':expected};interfaces[A]={'T':full,'S_K':sk,'Q':q}
 transport={}
 for lo,hi in ((12,14),(14,16),(12,16)):
  n=hi-lo;entry={}
  for kind in ('T','S_K','Q'):
   target=set(map(key,interfaces[hi][kind]));images=[shift(d,n) for d in interfaces[lo][kind]];entry[kind]={'source':len(images),'injective':len(set(images))==len(images),'all_images_admitted':all(x in target for x in images)};assert entry[kind]['injective'] and entry[kind]['all_images_admitted']
  transport[f'A{lo}_to_A{hi}']=entry
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-exact-boundary-descriptor-interface.v1','status':'typed_exact_word_interfaces_and_shift_maps_verified','summaries':summaries,'transport':transport,'decision':'Every T, S_K, and Q source row has a unique typed descriptor, and vertical exponent shift defines an admitted injective map for both adjacent and direct ambient inclusions.','limitations':['interface verification only','exact word coefficients are not yet retained','admitted descriptor transport does not prove transported words reconstruct or compose'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
