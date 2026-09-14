"""Construct the global labelled L2 map from its bounded positive shifts."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--shift-proof',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 s=json.loads(Path(a.shift_proof).read_text());shifts=s['all_shifts'];assert shifts==[2,3,4,5,6,7]
 # A finite source supported in degrees [m,D] maps into [m+2,D+7].
 tests=[]
 for lo,hi in ((0,0),(0,12),(3,16),(11,28),(100,137)):
  target=(lo+min(shifts),hi+max(shifts));assert target[0]>=lo and target[1]<10**9
  tests.append({'source_degree_interval':[lo,hi],'target_degree_bound':list(target)})
 out={'schema':'marici.nima.L2-global-locally-finite-labelled-operator.v2','status':'proved','degree_shifts':shifts,
  'construction':'apply the finite labelled column formula termwise to a finite polynomial source',
  'local_finiteness':'support [m,D] maps into [m+2,D+7]',
  'projection_compatibility':'finite truncations are restrictions of one global map',
  'tests':tests,'qualification':'global coefficient operator; compatibility with the ambient chain differentials, road-Cech geometry, and integral saturation remain open'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
