"""Compose the explicit L2 detector with the primitive logarithmic line."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--detector',required=True);p.add_argument('--log',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 d=json.loads(Path(a.detector).read_text());l=json.loads(Path(a.log).read_text())
 assert d['rho0_on_A_image']==0 and d['rho0_on_distinguished_transition']==3
 assert l['primitive']==[-1,1]
 out={'schema':'marici.nima.L2-selected-log-line-comparison.v1','status':'proved',
  'integral_map':'[f] maps to rho0(f)*gamma','A_image_maps_to':0,
  'distinguished_transition_maps_to':'3*gamma','integral_image_index_in_log_line':3,
  'localized_map':'over Z[1/3], (rho0/3) maps transition to primitive gamma',
  'alternatives':['invert 3','adjoin an integral cube-root/divided transition cell','accept the index-3 log sublattice if physical normalization permits'],
  'scope':'selected rank-one coefficient-to-local-log comparison; full filtered Q correspondence remains open'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
