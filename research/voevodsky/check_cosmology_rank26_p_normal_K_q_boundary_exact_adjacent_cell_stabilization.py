"""Test whether adjacent exact boundary syzygy cells stabilize under ambient descriptor shift."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_boundary_exact_adjacent_cell_stabilization.json'
def word(r,shift=0):
 out={}
 for x in r['exact_word']:
  f,k,l,ax,m,e=x['descriptor'];d=(x['kind'],f,k,tuple(l),ax,m,(e[0],e[1]+shift));a=Fraction(x['numerator'],x['denominator']);out[d]=out.get(d,Fraction())+a
 return {k:v for k,v in out.items() if v}
def add(a,b,scale=-1):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Fraction())+scale*v
 return {k:v for k,v in out.items() if v}
def shiftword(a,n):return {(kind,f,k,l,ax,m,(e[0],e[1]+n)):v for (kind,f,k,l,ax,m,e),v in a.items()}
def main():
 packets={A:json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_exact_all_a{A}.json').read_text()) for A in (12,14,16,18)};idx={A:{(r['k_pole'],*r['exponent']):r for r in p['records']} for A,p in packets.items()};summaries={};failures=[]
 for a,b,c in ((12,14,16),(14,16,18)):
  matches=0;diffs=[]
  for ra in packets[a]['records']:
   kp=ra['k_pole'];i,j=ra['exponent'];rb=idx[b][(kp,i,j+2)];rc=idx[c][(kp,i,j+4)];dab=add(word(ra,2),word(rb));dbc=add(word(rb,2),word(rc));res=add(shiftword(dab,2),dbc);same=not res;matches+=same
   if not same:diffs.append(len(res));failures.append({'triple':[a,b,c],'k_pole':kp,'source_exponent':[i,j],'residual_terms':len(res)})
  summaries[f'A{a}_A{b}_A{c}']={'cells':len(packets[a]['records']),'stabilized_matches':matches,'failures':len(diffs),'residual_terms_min':min(diffs) if diffs else 0,'residual_terms_max':max(diffs) if diffs else 0}
 passed=not failures;out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-exact-adjacent-cell-stabilization.v1','status':'adjacent_exact_cells_stabilize' if passed else 'adjacent_exact_cells_do_not_stabilize','summaries':summaries,'failure_sample':failures[:12],'decision':'A single ambient-independent adjacent syzygy cell transports across the tested degrees.' if passed else 'Adjacent syzygy cells compose but are not coefficient-identical after vertical shift; literal cell stabilization cannot serve as the induction recurrence.','limitations':['finite degrees 12,14,16,18','tests literal equality of selected exact cells','does not exclude higher-order or constructor-level recurrence'],'passed':passed};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
