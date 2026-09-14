"""Census the finite 2/3-primary cells needed to saturate the L2 relation image."""
import argparse,json,collections
from pathlib import Path

def valuation(n,p):
 k=0
 while n%p==0:n//=p;k+=1
 return k

def main():
 p=argparse.ArgumentParser();p.add_argument('--results-dir',required=True);p.add_argument('--output',required=True);a=p.parse_args();rows=[]
 for D in (12,16,20,24,28):
  x=json.loads((Path(a.results_dir)/f'L2-bockstein-relation-smith-D{D}.json').read_text());fs=x['augmented_smith_nonunits'];c=collections.Counter(fs)
  assert all(n//(2**valuation(n,2)*3**valuation(n,3))==1 for n in fs)
  rows.append({'D':D,'torsion_cells':len(fs),'invariant_factor_counts':dict(sorted(c.items())),
   'two_primary_length':sum(valuation(n,2) for n in fs),
   'three_primary_length':sum(valuation(n,3) for n in fs),
   'distinguished_transition_removes':'one Z/2 cell'})
 out={'schema':'marici.nima.L2-derived-torsion-cell-census.v1','status':'passed','rows':rows,
  'construction_target':'attach one derived cell for each listed invariant factor, with differential multiplication by that factor',
  'scope':'finite-cutoff cell census; compatibility maps between cutoffs and global tower remain open'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
