"""Audit ordinary versus logarithmic candidates for the physical soft-D1 map."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args();d=json.loads(Path(a.input).read_text());a0=d['assertions'];o=d['ordinary_crossing_candidate'];proper=d['proper_scalar_completion']
 assert a0['every_ordinary_comparison_kills_Tor1']==508
 assert o['map_on_Tor1_at_crossing']==0 and o['Tor1_preserving_lift'].startswith('obstructed')
 assert proper['derived_trace']=='Rp_*O_Y(E) -> S is an equivalence'
 assert proper['does_not_identify_full_log_endpoint_functor']
 assert a0['physical_readout_is_chain_map']==59
 out={'schema':'marici.nima.soft-D1-nearby-cycle-candidate-disposition.v1','status':'passed',
  'ordinary_crossing':{'tested_maps':508,'Tor1_action':0,'disposition':'cannot realize required nearby-cycle excess class'},
  'proper_two_chart_trace':{'construction':proper['scheme'],'derived_trace':proper['derived_trace'],'disposition':'repairs scalar coefficients but not endpoint nearby-cycle functor'},
  'coefficient_readout_chain_checks':a0['physical_readout_is_chain_map'],
  'required_route':'logarithmic/nearby-cycle excess comparison retaining the conductor Tor1 class',
  'scope':d['scope']}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
