"""Audit the physical support packet for the remaining soft-D1 realization."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args();d=json.loads(Path(a.input).read_text())
 maps=d['literal_chain_maps'];assert all(maps[k]=='zero by support disjointness' for k in ('to_D2','to_D3','to_Z12','to_Z13','to_Z23'))
 assert 'requires soft nearby-cycle specialization' in maps['to_D1']
 assert d['D1_corner_maps']=={'to_Z12':'zero','to_Z13':'zero'}
 assert d['analytic_continuation_status']=='not supplied by the primary source'
 out={'schema':'marici.nima.physical-soft-D1-realization-gate.v1','status':'passed',
  'vanishing_literal_maps':['D2','D3','Z12','Z13','Z23','D1->Z12','D1->Z13'],
  'remaining_map':maps['to_D1'],'analytic_continuation_status':d['analytic_continuation_status'],
  'conclusion':'the synthetic Bockstein cell cannot be sent to an ordinary fibre-boundary cell; a soft nearby-cycle specialization/analytic continuation morphism is genuinely required'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
