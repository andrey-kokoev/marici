"""Verify exact boundary transport differences evaluate to zero in the higher ambient source presentation."""
from __future__ import annotations
import json,os,sys
if '--ambient' in sys.argv: os.environ['MARICI_AMBIENT']=sys.argv[sys.argv.index('--ambient')+1]
if '--prime' in sys.argv: os.environ['MARICI_FIELD_PRIME']=sys.argv[sys.argv.index('--prime')+1]
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
import check_cosmology_rank26_p_normal_K_q_seed_exact_rational_minor as exact
import check_cosmology_rank26_p_normal_K_q_correction_word_ambient_compatibility as compat
import check_cosmology_rank26_p_normal_K_q_exact_base_representative_solves as solver
RES=ROOT/'research'/'voevodsky'/'results';A=rees.AMBIENT;OUT=RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_difference_syzygies_a{A}.json'
def dkey(d):
 f,k,l,ax,m,e=d;return (f,k,tuple(l),ax,m,tuple(e))
def word(r,shift=0):
 out={}
 for x in r['exact_word']:
  f,k,l,ax,m,e=x['descriptor'];d=(x['kind'],f,k,tuple(l),ax,m,(e[0],e[1]+shift));a=Fraction(x['numerator'],x['denominator']);out[d]=out.get(d,Fraction())+a
 return {k:v for k,v in out.items() if v}
def addword(a,b,scale=Fraction(1)):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Fraction())+scale*v
 return {k:v for k,v in out.items() if v}
def main():
 assert A in (14,16,18)
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);td=tuple(protocol['integral_unit_normals']['p_tangent_difference']);_,columns=rees.column_packet();packets={};orig=base.PRIME
 for p in exact.PS:
  base.PRIME=p;sp=list(rees.raw_relations(point,columns));T,_=adapter.derivative_rows(columns,point,td);nI=4*len(base.monomials_at_most(A));nK=64*len(base.monomials_at_most(A-4));packets[p]={'T':T,'S_K':sp[nI:nI+nK],'Q':sp[nI+nK:]}
 base.PRIME=orig;full,sk=compat.descriptors(A);qd=[d for d in full if d[0]=='q'];indexes={'T':{dkey(d):i for i,d in enumerate(full)},'S_K':{dkey(d):i for i,d in enumerate(sk)},'Q':{dkey(d):i for i,d in enumerate(qd)}};cache={}
 high=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json').read_text());hi={(r['k_pole'],*r['exponent']):r for r in high['records']};records=[]
 for lo in ({14:[12],16:[14,12],18:[16,14]}[A]):
  shift=A-lo;low=json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{lo}.json').read_text())
  for r in low['records']:
   kp=r['k_pole'];i,j=r['exponent'];target=hi[(kp,i,j+shift)];diff=addword(word(r,shift),word(target),Fraction(-1));evaluation={}
   for key,a in diff.items():
    kind=key[0];desc=key[1:];idx=indexes[kind][desc];ck=(kind,idx)
    if ck not in cache:cache[ck]=exact.exact_row([packets[p][kind][idx] for p in exact.PS])
    for c,v in cache[ck].items():solver.addq(evaluation,c,a*v)
   records.append({'inclusion':f'A{lo}_to_A{A}','k_pole':kp,'source_exponent':[i,j],'difference_terms':len(diff),'evaluation_zero':not evaluation})
 assert all(r['evaluation_zero'] for r in records)
 summary={}
 for label in sorted(set(r['inclusion'] for r in records)):
  rs=[r for r in records if r['inclusion']==label];summary[label]={'cells':len(rs),'zero_evaluations':sum(r['evaluation_zero'] for r in rs),'terms_min':min(r['difference_terms'] for r in rs),'terms_max':max(r['difference_terms'] for r in rs)}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-exact-difference-syzygies.v1','status':'all_exact_transport_differences_are_source_syzygies','ambient_relation_degree':A,'summary':summary,'decision':'Every transported-minus-local exact boundary word evaluates to the zero target over Q in the higher ambient source presentation.','limitations':['finite ambient degrees','four-prime CRT integer reconstruction','composition equality tested separately'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
