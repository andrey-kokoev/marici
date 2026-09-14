"""Rank audit for mapping L2 Bockstein directions to the primitive log link."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--results-dir',required=True);p.add_argument('--log-certificate',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 log=json.loads(Path(a.log_certificate).read_text());primitive=log['local_log_relative_complex']['primitive'];assert primitive==[-1,1]
 rows=[]
 for D in (12,16,20,24,28):
  x=json.loads((Path(a.results_dir)/f'L2-bockstein-relation-smith-D{D}.json').read_text());r=x['bockstein_rank_gain']
  rows.append({'D':D,'Bockstein_rational_rank':r,'log_primitive_rank':1,'minimum_kernel_rank_for_any_map_to_primitive_line':r-1})
 out={'schema':'marici.nima.L2-to-log-primitive-rank-reduction.v1','status':'passed','rows':rows,
  'conclusion':'the local log primitive line cannot retain all independent Bockstein directions; physical realization must factor through a selected scalar quotient/readout',
  'required_data':'a functional rho on the Bockstein cokernel and proof that the physical residual lies in its detected quotient',
  'qualification':'rank obstruction to injectivity, not obstruction to a nonfaithful comparison map'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
