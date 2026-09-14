"""Aggregate exact L2 Smith presentations and audit localization support."""
import argparse,json,math
from pathlib import Path

def primes(n):
 out=set();p=2
 while p*p<=n:
  while n%p==0:out.add(p);n//=p
  p+=1
 if n>1:out.add(n)
 return out
def main():
 p=argparse.ArgumentParser();p.add_argument('--results-dir',required=True);p.add_argument('--output',required=True);a=p.parse_args();rows=[]
 for D in (12,16,20,24,28):
  x=json.loads((Path(a.results_dir)/f'L2-bockstein-relation-smith-D{D}.json').read_text())
  support=set().union(*(primes(n) for n in x['augmented_smith_nonunits'])) if x['augmented_smith_nonunits'] else set()
  assert support<={2,3};assert x['transition_torsion_index_ratio']==2
  rows.append({'D':D,'rank_gain':x['bockstein_rank_gain'],'torsion_support':sorted(support),
               'Z[1/6]_saturated':True,'transition_index_ratio':2})
 assert [r['rank_gain'] for r in rows]==[8,14,18,22,26]
 out={'schema':'marici.nima.L2-relation-lattice-localization.v1','status':'passed','rows':rows,
  'uniform_tested_localization':'Z[1/6]','conclusion':'the full relation-derived Bockstein image is saturated after inverting 6 at all five exact cutoffs',
  'scope':'five exact cutoffs; not an all-degree saturation theorem or integral road-Cech map'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
