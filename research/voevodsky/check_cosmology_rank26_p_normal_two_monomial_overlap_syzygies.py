"""Verify exact overlap syzygies and commuting squares for the two-monomial source cover."""
from __future__ import annotations
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves as solver
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_two_monomial_overlap_syzygies.json'
def word(r,axis,amount=2):
 out={}
 for x in r['exact_word']:
  f,k,l,ax,m,e=x['descriptor'];q=list(e);q[axis]+=amount;d=(x['kind'],f,k,tuple(l),ax,m,tuple(q));a=Fraction(x['numerator'],x['denominator']);out[d]=out.get(d,Fraction())+a
 return {k:v for k,v in out.items() if v}
def add(a,b,scale=-1):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Fraction())+scale*v
 return {k:v for k,v in out.items() if v}
def dkey(d):f,k,l,ax,m,e=d;return(f,k,tuple(l),ax,m,tuple(e))
def packet(A,point,td):
 rees.AMBIENT=A;_,columns=rees.column_packet();packets={};orig=base.PRIME
 for p in exact.PS:
  base.PRIME=p;sp=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));packets[p]={'T':T,'S_K':sp[nI:nI+nK],'Q':sp[nI+nK:]}
 base.PRIME=orig;full,sk=compat.descriptors(A);q=[d for d in full if d[0]=='q'];return packets,{'T':{dkey(d):i for i,d in enumerate(full)},'S_K':{dkey(d):i for i,d in enumerate(sk)},'Q':{dkey(d):i for i,d in enumerate(q)}}
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);summaries={};all_records=[]
 for lo,hi in ((12,14),(14,16),(16,18)):
  low=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{lo}.json').read_text());li={(r['k_pole'],*r['exponent']):r for r in low['records']};high=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{hi}.json').read_text());packets,index=packet(hi,point,td);cache={};records=[]
  for h in high['records']:
   kp=h['k_pole'];i,j=h['exponent']
   if i<2 or j<2:continue
   wx=word(li[(kp,i-2,j)],0);wy=word(li[(kp,i,j-2)],1);diff=add(wx,wy);evaluation={}
   for key,a in diff.items():
    kind=key[0];idx=index[kind][key[1:]];ck=(kind,idx)
    if ck not in cache:cache[ck]=exact.exact_row([packets[p][kind][idx] for p in exact.PS])
    for c,v in cache[ck].items():solver.addq(evaluation,c,a*v)
   records.append({'k_pole':kp,'higher_exponent':[i,j],'difference_terms':len(diff),'evaluation_zero':not evaluation})
  assert all(r['evaluation_zero'] for r in records);summaries[f'A{lo}_to_A{hi}']={'overlap_cells':len(records),'zero_syzygies':len(records),'terms_min':min(r['difference_terms'] for r in records),'terms_max':max(r['difference_terms'] for r in records)};all_records+=records
 squares={}
 for A in (12,14):
  p=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json').read_text());matches=0
  for r in p['records']:
   xy=word({'exact_word':[dict(x,descriptor=[x['descriptor'][0],x['descriptor'][1],x['descriptor'][2],x['descriptor'][3],x['descriptor'][4],[x['descriptor'][5][0]+2,x['descriptor'][5][1]]]) for x in r['exact_word']]},1)
   yx=word({'exact_word':[dict(x,descriptor=[x['descriptor'][0],x['descriptor'][1],x['descriptor'][2],x['descriptor'][3],x['descriptor'][4],[x['descriptor'][5][0],x['descriptor'][5][1]+2]]) for x in r['exact_word']]},0);matches+=xy==yx
  assert matches==len(p['records']);squares[f'A{A}_to_A{A+4}']={'words':len(p['records']),'commuting_descriptor_squares':matches}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-two-monomial-overlap-syzygies.v1','status':'overlap_contractions_are_exact_syzygies_and_squares_commute','summaries':summaries,'squares':squares,'decision':'The two natural contraction transports differ on overlaps by exact rational source syzygies, and the two monomial shifts commute strictly on source words.','limitations':['finite degrees A12 through A18','selected exact lower contractions','does not choose a canonical section of the contraction torsor'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
