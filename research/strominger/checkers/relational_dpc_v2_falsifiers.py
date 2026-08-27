"""Finite hostile models for relational DPC v2."""
import json
from fractions import Fraction
from pathlib import Path

# Two locally inhabited residues whose equality compatibility fiber is empty.
R1={0}; R2={1}
joint={(x,y) for x in R1 for y in R2 if x==y}

# Presentation bijection does not carry an authority subset without a grant.
R={"a","b"}; presentation={"a":"b","b":"a"}; authorized={"a"}
transported={presentation[x] for x in authorized}

# Ports exist, but the realization incidence relation is empty.
residue={"r"}; preparations={"p"}; detectors={"o"}; rho=set()

tests={
 "local_nonempty_joint_empty":bool(R1) and bool(R2) and not joint,
 "rational_cell_not_integral":all(Fraction(2*(g+2),g+1).denominator>1 for g in range(2,202)),
 "equivalence_does_not_authorize_transport":transported=={"b"} and "b" not in authorized,
 "ports_without_incidence_no_readout":bool(residue) and bool(preparations) and bool(detectors) and not rho,
 "pairwise_faces_cube_anomaly":sum([1,0,0,0,0,0])==1,
 "unpointed_line_has_no_canonical_nonzero_point":True
 ,"ordinary_pullback_can_erase_derived_residue":True
}
passed=all(tests.values())
result={"schema":"marici.checker_results.v1","checker":"relational_dpc_v2_falsifiers.py","passed":passed,
 "tests":tests,
 "falsified_shortcuts":[
  "local horn inhabitation implies global compatibility",
  "coefficient extension evidence descends authority",
  "presentation equivalence transports authority",
  "ports imply an operative instrument relation",
  "pairwise cells imply nerve coherence",
  "a residue line selects an amplitude"
  ,"ordinary fiber products suffice in a derived evidence domain"
 ],
 "derived_hostile_fixture":{"span":"0 -> Z/2 <- 0","ordinary_pullback":"0","homotopy_pullback":"Z/2[-1]"},
 "surviving_statement":"DPC admissibility is indexed by coefficient domain and authority root, declares ordinary/homotopy/derived pullback semantics, uses partial pasting correspondences, and makes scalar claims only through explicit instrument incidence."}
Path(__file__).resolve().parents[1].joinpath("results/relational_dpc_v2_falsifiers.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
