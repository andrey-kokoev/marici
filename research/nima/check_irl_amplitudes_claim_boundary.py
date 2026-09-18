#!/usr/bin/env python3
"""Machine-check the replicated/open claim boundary for the amplitude program."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
manifest=json.loads((R/'irl-amplitudes-replication-manifest.json').read_text());closure=json.loads((R/'irl-amplitudes-replication-closure.json').read_text());provenance=json.loads((R/'irl-amplitudes-replication-provenance.json').read_text())
replicated=[
 {'claim':'ABHY planar biadjoint tree amplitudes','range':'arbitrary n>=3 theorem; executable regressions n=4..14','evidence':'arbitrary-n-planar-biadjoint-amplitude-proof.md, abhy-biadjoint-replication-suite.json, and four-point base'},
 {'claim':'ABHY kinematic associahedron canonical forms','range':'arbitrary n>=4 theorem; executable regressions n=4..10','evidence':'arbitrary-n-abhy-associahedron-canonical-form-pullback-proof.md and abhy-associahedron-replication-suite.json'},
 {'claim':'ABHY planar scattering-form projectivity','range':'arbitrary n>=4 theorem; executable regressions n=4..14','evidence':'arbitrary-n-planar-scattering-form-projectivity-proof.md and abhy-scattering-form-projectivity-suite.json'},
 {'claim':'double-partial biadjoint support and factorization','range':'arbitrary multiplicity and arbitrary cyclic-order pair theorem; selected regressions n=4..9','evidence':'arbitrary-order-double-partial-biadjoint-factorization-proof.md and double-partial-biadjoint-factorization.json'},
 {'claim':'planar one-loop MHV pre-integration integrand','range':'arbitrary n>=4 count, covariance, pole cancellation/survival, and dihedral theorems; exact finite regressions','evidence':'arbitrary-n one-loop MHV proof packets and one-loop-mhv-replication-suite.json'},
 {'claim':'NMHV five-bracket covariance','range':'arbitrary n>=6 theorem; selected exact covariance regressions','evidence':'arbitrary-n-nmhv-momentum-supertwistor-covariance-proof.md and momentum-twistor covariance suites'},
 {'claim':'NMHV dihedral invariance and simplicial triangulation independence','range':'arbitrary n>=6 theorem; finite regressions through stated ranges','evidence':'arbitrary-n cyclic/reflection proofs and nmhv-five-bracket-chain-depends-only-on-its-oriented-boundary.md'},
 {'claim':'NMHV codimension-one physical/spurious boundary behavior','range':'arbitrary n>=6 theorem; exact residue regressions n=6..9; chain regressions n=6..50','evidence':'arbitrary-n boundary, physical-pole, and spurious-pole proofs plus finite suites'},
]
open_claims=['nonplanar and indefinite-sign ABHY geometries','normalized NMHV multiparticle factorization','N^kMHV sectors with k>=2 (source acquisition blocked)','loop-integrand construction beyond one-loop MHV and all-loop recursion','Yangian invariance beyond tested momentum-twistor covariance','gravity amplitudes and double-copy benchmarks','cosmological polytope/wavefunction benchmarks','comparison with experimental scattering data','complete replication of either cited paper']
checks={'manifest_passed':manifest['passed'],'closure_passed':closure['passed'],'provenance_passed':provenance['passed'],'replicated_claims_nonempty':len(replicated)>0,'open_claims_explicit':len(open_claims)>=8,'no_complete_paper_claim':any('complete replication' in q for q in open_claims)}
out={'schema':'marici.nima.irl-amplitudes-claim-boundary.v1','replicated':replicated,'open':open_claims,'checks':checks,'passed':all(checks.values())}
p=R/'irl-amplitudes-claim-boundary.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'replicated_claim_groups':len(replicated),'open_claim_groups':len(open_claims),'checks':checks},indent=2));raise SystemExit(0 if out['passed'] else 1)
