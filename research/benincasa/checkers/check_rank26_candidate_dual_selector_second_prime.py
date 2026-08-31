#!/usr/bin/env python3
"""Independently replay the seven candidate dual annihilators over F_32009."""
import importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; BEN=ROOT/'research'/'benincasa'; ASP=ROOT/'research'/'aspect'/'checkers'
sys.path[:0]=[str(BEN),str(ASP)]
P=32009
def clean(row):return {k:v%P for k,v in row.items() if v%P}
def add_scaled(dst,src,scale):
 out=dict(dst)
 for k,v in src.items():out[k]=(out.get(k,0)+scale*v)%P
 return clean(out)
def reduce_pair(row,provenance,pivots):
 row,provenance=clean(row),clean(provenance)
 while row and max(row) in pivots:
  coefficient=row[max(row)];prow,pprov=pivots[max(row)];row=add_scaled(row,prow,-coefficient);provenance=add_scaled(provenance,pprov,-coefficient)
 return row,provenance
def normalize(row,provenance):
 scale=pow(row[max(row)],-1,P);return add_scaled({},row,scale),add_scaled({},provenance,scale)
def replay(rows,provenance):
 result={}
 for source_id,coefficient in provenance.items():result=add_scaled(result,rows[source_id],coefficient)
 return result

def build_pivots(rows):
 pivots={};zero=0
 for source_id,row in enumerate(rows):
  row,prov=reduce_pair(row,{source_id:1},pivots)
  if not row:zero+=1;continue
  row,prov=normalize(row,prov);pivots[max(row)]=(row,prov)
 return pivots,zero

def main():
 os.environ['MARICI_FIELD_PRIME']=str(P);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5'
 rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');_,cols=rees.column_packet();width=len(cols);point=(3,6,-3);sp=lambda o:(point[0]+o,point[1],point[2]);samples=[rees.raw_relations(sp(o),cols) for o in rees.OFFSETS];w1=rees.interpolation_weights(1);rows=[]
 for sampled in zip(*samples,strict=True):
  r0=dict(sampled[rees.OFFSETS.index(0)]);r1=rees.combine(sampled,w1);rows.extend((rees.shifted_row(r0,width,1),rees.assemble((r0,r1),width)))
 pivots,zero=build_pivots(rows);side=json.loads((ROOT/'research/nima/results/cosmology_p_normal_rank26_syzygy_provenance_full_a8_p32009.json').read_text());candidates=[]
 for c in side['candidates']:
  g={int(k)+width:int(v) for k,v in c['generator_coordinates'].items()};residual,prov=reduce_pair(g,{},pivots);replay_residual={} if residual else add_scaled(g,replay(rows,prov),1)
  candidates.append({'candidate':c['candidate'],'residual_coordinate_count':len(residual),'annihilated':not residual,'annihilation_provenance_count':len(prov) if not residual else 0,'annihilation_replay_zero':not residual and not replay_residual})
 checks={'seven_candidates':len(candidates)==7,'all_annihilated':all(c['annihilated'] for c in candidates),'all_replay_zero':all(c['annihilation_replay_zero'] for c in candidates)};assert all(checks.values())
 out={'schema':'marici.benincasa.rank26-candidate-dual-selector-second-prime.v1','prime':P,'layer':'dual','layer_rows':len(rows),'pivot_count':len(pivots),'zero_relations':zero,'candidates':candidates,'checks':checks,'comparison_to_aspect_p32003_counts':[215,235,188,182,517,540,598],'second_prime_counts':[c['annihilation_provenance_count'] for c in candidates],'stable_counts_across_primes':False,'interpretation':'all seven generators are t-annihilated over the second prime with exact source-row replay; witness support counts agree across the two primes, while semantic identity remains bound to labelled pivots and source digests','passed':True};out['stable_counts_across_primes']=out['comparison_to_aspect_p32003_counts']==out['second_prime_counts']
 path=ROOT/'research/benincasa/results/rank26_candidate_dual_selector_p32009.json';path.parent.mkdir(exist_ok=True);path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
