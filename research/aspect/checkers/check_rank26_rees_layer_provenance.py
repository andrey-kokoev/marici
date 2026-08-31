#!/usr/bin/env python3
"""Paired provenance reduction for dual or triple rank-26 Rees presentations."""
import argparse, importlib, json, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];BEN=ROOT/'research'/'benincasa';sys.path[:0]=[str(BEN),str(Path(__file__).parent)]
from check_sparse_provenance_reducer import reduce_rows, replay

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--layer',choices=('dual','triple'),required=True);ap.add_argument('--source-limit',type=int,default=9780);a=ap.parse_args();assert 1<=a.source_limit<=9780
 os.environ['MARICI_FIELD_PRIME']='32003';os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5'
 rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');_,columns=rees.column_packet();width=len(columns);point=(3,6,-3);direction=(1,0,0)
 shifted_point=lambda o:tuple(point[i]+o*direction[i] for i in range(3));samples=[rees.raw_relations(shifted_point(o),columns) for o in rees.OFFSETS];w1=rees.interpolation_weights(1);w2=rees.interpolation_weights(2);rows=[];source_count=0
 for sampled in zip(*samples,strict=True):
  r0=dict(sampled[rees.OFFSETS.index(0)]);r1=rees.combine(sampled,w1)
  if a.layer=='dual': rows.extend((rees.shifted_row(r0,width,1),rees.assemble((r0,r1),width)))
  else:
   r2=rees.combine(sampled,w2);rows.extend((rees.shifted_row(r0,width,2),rees.assemble(({},r0,r1),width),rees.assemble((r0,r1,r2),width)))
  source_count+=1
  if source_count==a.source_limit:break
 pivots,dependencies=reduce_rows(rows);residuals=[replay(rows,w) for w in dependencies];assert all(not r for r in residuals)
 max_support=max([len(p) for _,p in pivots.values()]+[len(w) for w in dependencies],default=0)
 out={'schema':'marici.aspect.rank26-rees-layer-provenance.v1','layer':a.layer,'prime':32003,'ambient':8,'source_relations_consumed':source_count,'full_source_relations':9780,'layer_rows':len(rows),'pivot_count':len(pivots),'dependency_count':len(dependencies),'all_dependencies_replay_zero':True,'max_provenance_support':max_support,'full_layer_completed':source_count==9780,'length_one_generators_extracted':False,'passed':True}
 path=ROOT/f'research/aspect/results/rank26_rees_{a.layer}_provenance_{source_count}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
