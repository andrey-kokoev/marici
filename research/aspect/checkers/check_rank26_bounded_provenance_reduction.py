#!/usr/bin/env python3
"""Bounded production-row exercise of the paired provenance reducer."""
import argparse, importlib, json, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];BEN=ROOT/'research'/'benincasa';sys.path.insert(0,str(BEN));sys.path.insert(0,str(Path(__file__).parent))
from check_sparse_provenance_reducer import reduce_rows, replay

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=1024);a=ap.parse_args();assert 1<=a.limit<=9780
 os.environ['MARICI_FIELD_PRIME']='32003';os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5'
 rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');_,columns=rees.column_packet();rows=[]
 for row in rees.raw_relations((3,6,-3),columns):
  rows.append(row)
  if len(rows)==a.limit:break
 pivots,dependencies=reduce_rows(rows);residuals=[replay(rows,w) for w in dependencies]
 assert all(not r for r in residuals)
 max_provenance=max([len(p) for _,p in pivots.values()]+[len(w) for w in dependencies],default=0)
 out={'schema':'marici.aspect.rank26-bounded-provenance-reduction.v1','prime':32003,'ambient':8,'source_rows_consumed':len(rows),'full_source_rows':9780,'pivot_count':len(pivots),'dependency_count':len(dependencies),'all_dependencies_replay_zero':True,'max_provenance_support':max_provenance,'full_rank26_reduction_completed':len(rows)==9780,'scope':'bounded prefix performance and replay test; not Rees generator extraction','passed':True}
 path=ROOT/f'research/aspect/results/rank26_bounded_provenance_reduction_{a.limit}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
