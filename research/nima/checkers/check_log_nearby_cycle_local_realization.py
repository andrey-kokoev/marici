"""Audit the constructed logarithmic normal-link realization and its remaining scope."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args();d=json.loads(Path(a.input).read_text());c=d['checks']
 required=('normal_Tor_to_log_link_chain_map','relative_log_generator_primitive','relative_log_reflection_odd','full_endpoint_pairing_chain_map','explicit_endpoint_comparison_homotopy','generic_trace_times_road_chain_map','all_coefficient_cycle_pairing_is_road_readout','full_log_packet_integral_contraction')
 vals={k:c[k] for k in required};assert all(v>0 for v in vals.values());assert not d['full_geometric_claim']
 out={'schema':'marici.nima.log-nearby-cycle-local-realization.v1','status':'local-realization-constructed',
  'checks':vals,'primitive':d['local_log_relative_complex']['primitive'],
  'pairing':d['pairing_L_P_to_R_shift2'],'trace_road_homotopy':d['trace_road_homotopy'],
  'remaining':d['unconstructed'],
  'conclusion':'the soft-D1 logarithmic normal-link cell, endpoint pairing, and road-readout homotopy exist integrally; comparison from the L2 Bockstein relation system into this packet and the full ringed filtered Q target remains'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
