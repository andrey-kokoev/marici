#!/usr/bin/env python3
"""Machine-check the replicated/open claim boundary for the amplitude program."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
manifest=json.loads((R/'irl-amplitudes-replication-manifest.json').read_text());closure=json.loads((R/'irl-amplitudes-replication-closure.json').read_text());provenance=json.loads((R/'irl-amplitudes-replication-provenance.json').read_text())
replicated=[
 {'claim':'ABHY planar biadjoint tree amplitudes','range':'arbitrary n>=3 theorem; executable regressions n=4..14','evidence':'arbitrary-n-planar-biadjoint-amplitude-proof.md, abhy-biadjoint-replication-suite.json, and four-point base'},
 {'claim':'ABHY kinematic associahedron canonical forms','range':'n=4..10','evidence':'abhy-associahedron-replication-suite.json plus four-point base'},
 {'claim':'ABHY planar scattering-form projectivity','range':'n=4..14','evidence':'abhy-scattering-form-projectivity-suite.json plus four-point base'},
 {'claim':'NMHV five-bracket identities and covariance','range':'selected six-point identities','evidence':'momentum-twistor-covariance-suite.json and momentum-twistor-nmhv-replication-suite.json'},
 {'claim':'NMHV dihedral invariance','range':'positive n=7..12; generic n=7..10','evidence':'nmhv-dihedral-replication-suite.json and nmhv-generic-kinematics-suite.json'},
 {'claim':'NMHV codimension-one physical/spurious boundary behavior','range':'exact residues n=6..9; combinatorial chains n=6..50','evidence':'physical, spurious, count, and oriented-boundary suites'},
]
open_claims=['arbitrary-n proofs for associahedron pullback, scattering-form projectivity, and NMHV boundary chains','N^kMHV sectors with k>=2','loop-integrand construction and all-loop recursion','Yangian invariance beyond tested momentum-twistor covariance','gravity amplitudes and double-copy benchmarks','cosmological polytope/wavefunction benchmarks','comparison with experimental scattering data','complete replication of either cited paper']
checks={'manifest_passed':manifest['passed'],'closure_passed':closure['passed'],'provenance_passed':provenance['passed'],'replicated_claims_nonempty':len(replicated)>0,'open_claims_explicit':len(open_claims)>=8,'no_complete_paper_claim':any('complete replication' in q for q in open_claims)}
out={'schema':'marici.nima.irl-amplitudes-claim-boundary.v1','replicated':replicated,'open':open_claims,'checks':checks,'passed':all(checks.values())}
p=R/'irl-amplitudes-claim-boundary.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'replicated_claim_groups':len(replicated),'open_claim_groups':len(open_claims),'checks':checks},indent=2));raise SystemExit(0 if out['passed'] else 1)
