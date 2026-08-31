"""Map exact degree-14 source words by descriptors and verify canonical seed identities at A12/A16 over Q."""
from __future__ import annotations
import json,os,sys
from fractions import Fraction
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_physical_half_twist_seed_exact_rational_minor as exact
VRES=ROOT/'research'/'voevodsky'/'results';BRES=ROOT/'research'/'benincasa'/'results';A=rees.AMBIENT;OUT=BRES/f'cosmology_physical_half_twist_seed_exact_ambient_a{A}.json';PS=exact.PS
def add(row,c,v):
 x=row.get(c,Fraction(0))+v
 if x:row[c]=x
 else:row.pop(c,None)
def qdescs(A):return [d for d in compat.descriptors(A)[0] if d[0]=='q']
def main():
 assert A in (12,16)
 solution=json.loads((BRES/'cosmology_physical_half_twist_seed_exact_rational_minor.json').read_text());d14,sk14=compat.descriptors(14);q14=qdescs(14);dA,skA=compat.descriptors(A);qA=qdescs(A);maps={'T':{d:i for i,d in enumerate(dA)},'S_K':{d:i for i,d in enumerate(skA)},'Q':{d:i for i,d in enumerate(qA)}};old={'T':d14,'S_K':sk14,'Q':q14};point=tuple(json.loads((VRES/'cosmology_rank26_p_normal_protocol_gate.json').read_text())['test_point_xyz']);protocol=json.loads((VRES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());nx=tuple(protocol['integral_unit_normals']['nx']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};original=base.PRIME
 for p in PS:
  base.PRIME=p;rees.charts.GAMMA=-pow(2,-1,p)%p;special=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);dx,_=adapter.derivative_rows(columns,point,nx);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));packets[p]={'T':T,'S_K':special[nI:nI+nK],'Q':special[nI+nK:],'dx':dx}
 base.PRIME=original;levels=(1,1,2,1,1);Kdesc=[]
 for kp in range(charts.K_DEPTH):
  for lev in product(range(1,charts.Q_DEPTH+1),repeat=len(rees.NAMES)):
   for exp in base.monomials_at_most(A-4):Kdesc.append((kp,lev,exp))
 nI=4*len(base.monomials_at_most(A));results={}
 for kp in (0,1):
  recon={};mapped=0
  for item in solution['results'][f'k{kp}']['source_coefficients']:
   kind=item['kind'];desc=old[kind][item['row_index']];idx=maps[kind][desc];row=exact.exact_row([packets[p][kind][idx] for p in PS]);a=Fraction(item['numerator'],item['denominator'])
   for c,v in row.items():add(recon,c,a*v)
   mapped+=1
  ti=nI+Kdesc.index((kp,levels,(0,0)));target=exact.exact_row([packets[p]['dx'][ti] for p in PS]);assert recon==target;results[f'k{kp}']={'mapped_source_rows':mapped,'full_target_reconstruction':True,'target_row_index':ti}
 out={'schema':'marici.benincasa.cosmology-physical-half-twist-seed-exact-ambient-transport.v1','status':'physical_half_twist_exact_rational_seed_words_transport','physical_gamma':'-1/2','ambient_relation_degree':A,'results':results,'decision':'The exact degree-14 source words map descriptorwise and reconstruct the canonical targets over Q at this ambient degree.','limitations':['ambient degrees 12 and16 tested separately','four-prime CRT rational reconstruction under the standard unique-height bound','canonical monomial only'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
