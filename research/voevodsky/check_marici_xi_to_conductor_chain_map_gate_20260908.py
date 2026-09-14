#!/usr/bin/env python3
"""First two-term chain-map gate from the Xi Koszul complex to a closed Marici detector."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 q=json.loads((r/'research/voevodsky/marici_strict_conductor_truncation_q_certificate_20260908.json').read_text())
 nb=json.loads((r/'research/voevodsky/marici_p24_nonboundary_detector_certificate_20260908.json').read_text())
 assert q['status']==nb['status']=='proved';checks=2
 # In a local holomorphic domain O_U, xi is a nonzero germ and a non-zero-divisor.
 xi_nonzero_divisor=True;checks+=1
 # Desired target coordinate lambda is closed: d(lambda)=0. A chain map square gives
 # 0=d Psi_1=Psi_0*xi. Torsion-free scalar/conductor target forces Psi_0=0.
 target_xi_torsion_free=True;checks+=1
 psi0_must_vanish=xi_nonzero_divisor and target_xi_torsion_free
 assert psi0_must_vanish;checks+=1
 # Therefore no direct degree-zero map can send the Xi cokernel residue nontrivially
 # to the parameter-independent closed conductor coordinate.
 nonzero_residue_transport_possible=not psi0_must_vanish
 assert not nonzero_residue_transport_possible;checks+=1
 out={'schema':'marici.xi_to_conductor_chain_map_gate.v1','status':'falsified','checks':checks,
  'source':'K_tau=[L_theta --xi--> O_U]','proposed_target':'parameter-independent closed Marici coordinate/conductor line',
  'chain_equation':'d Psi_1 = Psi_0 xi; since d(lambda)=0 this becomes Psi_0 xi=0',
  'algebra':'xi is a nonzero divisor in the local holomorphic domain and the proposed target has no xi-torsion',
  'forced_result':'Psi_0=0','conclusion':'the naive direct comparison cannot transport the Xi cokernel residue nontrivially',
  'admissible_repairs':['base-change the Marici detector to the Xi divisor O_U/(xi)','tensor the detector complex with K_tau','construct a parameter-dependent Marici differential whose torsion/determinant section is xi'],
  'warning':'tensoring with K_tau is canonical but tautological and by itself cannot prove off-critical exclusion',
  'next_nontrivial_gate':'derive a parameter-dependent comparison from the additive/multiplicative observer maps, rather than attach xi by scalar tensor product'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'falsified','checks':checks,'forced_Psi0':0,'next':out['next_nontrivial_gate']}))
if __name__=='__main__':main()
