#!/usr/bin/env python3
"""Reduce materialized generators against full dual/triple Rees layers with provenance."""
import argparse,importlib,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];BEN=ROOT/'research'/'benincasa';HERE=Path(__file__).parent;sys.path[:0]=[str(BEN),str(HERE)]
import check_sparse_provenance_reducer as provenance_reducer
from check_sparse_provenance_reducer import add_scaled,reduce_pair,normalize,replay

def build_pivots(rows):
 pivots={};zero=0
 for source_id,row in enumerate(rows):
  row,prov=reduce_pair(row,{source_id:1},pivots)
  if not row:zero+=1;continue
  row,prov=normalize(row,prov);pivots[max(row)]=(row,prov)
 return pivots,zero

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--layer',choices=('dual','triple'),required=True);ap.add_argument('--prime',type=int,choices=(32003,32009),default=32003);ap.add_argument('--gamma',choices=('generic','half'),default='generic');a=ap.parse_args();provenance_reducer.PRIME=a.prime;os.environ['MARICI_FIELD_PRIME']=str(a.prime);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5'
 rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');
 if a.gamma=='half':rees.charts.GAMMA=-(pow(2,-1,a.prime))%a.prime
 _,cols=rees.column_packet();width=len(cols);point=(3,6,-3);direction=(1,0,0);sp=lambda o:tuple(point[i]+o*direction[i] for i in range(3));samples=[rees.raw_relations(sp(o),cols) for o in rees.OFFSETS];w1=rees.interpolation_weights(1);w2=rees.interpolation_weights(2);rows=[]
 for sampled in zip(*samples,strict=True):
  r0=dict(sampled[rees.OFFSETS.index(0)]);r1=rees.combine(sampled,w1)
  if a.layer=='dual':rows.extend((rees.shifted_row(r0,width,1),rees.assemble((r0,r1),width)))
  else:
   r2=rees.combine(sampled,w2);rows.extend((rees.shifted_row(r0,width,2),rees.assemble(({},r0,r1),width),rees.assemble((r0,r1,r2),width)))
 pivots,zero=build_pivots(rows);side_path=(ROOT/f'research/benincasa/results/cosmology_half_twist_syzygy_provenance_p{a.prime}.json') if a.gamma=='half' else (ROOT/f'research/nima/results/cosmology_p_normal_rank26_syzygy_provenance_full_a8_p{a.prime}.json');side=json.loads(side_path.read_text());block=1 if a.layer=='dual' else 2;candidates=[]
 for c in side['candidates']:
  g={int(k)+block*width:int(v) for k,v in c['generator_coordinates'].items()};residual,prov=reduce_pair(g,{},pivots);replay_residual={} if residual else add_scaled(g,replay(rows,prov),1);assert residual or not replay_residual
  candidates.append({'candidate':c['candidate'],'residual_coordinate_count':len(residual),'annihilated':not residual,'annihilation_provenance_count':len(prov) if not residual else 0,'annihilation_replay_zero':not residual and not replay_residual})
 tag='_half' if a.gamma=='half' else '';out={'schema':'marici.aspect.rank26-candidate-layer-selector.v1','layer':a.layer,'prime':a.prime,'gamma_mode':a.gamma,'layer_rows':len(rows),'pivot_count':len(pivots),'zero_relations':zero,'candidate_count':len(candidates),'candidates':candidates,'all_candidates_annihilated':all(c['annihilated'] for c in candidates),'passed':True};path=ROOT/f'research/aspect/results/rank26_candidate_{a.layer}_selector{tag}_p{a.prime}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','layer':a.layer,'gamma':a.gamma,'prime':a.prime,'annihilated':sum(c['annihilated'] for c in candidates)}))
if __name__=='__main__':main()
