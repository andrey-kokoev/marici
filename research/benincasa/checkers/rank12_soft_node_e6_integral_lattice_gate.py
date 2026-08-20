"""Show that the rational node/e6 scalar does not determine an integral index."""
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/benincasa/results/rank12-soft-node-e6-integral-lattice-gate.json'
c=Fraction(-1,2)
# Rescaling the rational target frame e6'=q e6 preserves the differential
# module and changes the displayed scalar to c/q.
gauges=[Fraction(1),Fraction(1,2),Fraction(2)]
scalars=[c/q for q in gauges]
assert scalars==[Fraction(-1,2),Fraction(-1),Fraction(-1,4)]
packet={
 'schema':'marici.benincasa.rank12_soft_node_e6_integral_lattice_gate.v1',
 'canonical_rational_scalar':'-1/2',
 'admissible_constant_target_gauges':[str(q) for q in gauges],
 'displayed_scalars_after_gauge':[str(q) for q in scalars],
 'node_integral_generator':'primitive H_1(C*) generator tau',
 'e6_integral_generator':'not fixed by frozen rational de Rham packet',
 'index_two_claim_authorized':False,
 'conclusion':'the rational comparison is canonical in the source de Rham frame, but no integral index is determined without a Betti lattice, polarization, normalized period, or physical pairing'
}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet))
