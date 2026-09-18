#!/usr/bin/env python3
"""Top-level integrity manifest for replicated published amplitude benchmarks."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
artifacts=[
 ('ABHY four-point base','abhy-four-point-foundational-benchmark.json'),
 ('ABHY planar amplitudes n=5..14','abhy-biadjoint-replication-suite.json'),
 ('ABHY associahedron canonical forms n=5..10','abhy-associahedron-replication-suite.json'),
 ('ABHY scattering-form projectivity n=5..14','abhy-scattering-form-projectivity-suite.json'),
 ('Double-partial factorization: all cyclic-order pairs n=4..7','exhaustive-double-partial-biadjoint-factorization.json'),
 ('Planar one-loop MHV pre-integration canonical forms','one-loop-mhv-replication-suite.json'),
 ('NMHV momentum-twistor identities n=6..12','momentum-twistor-nmhv-replication-suite.json'),
 ('Momentum-twistor five-bracket covariance','momentum-twistor-covariance-suite.json'),
 ('NMHV identities on generic rational kinematics','nmhv-generic-kinematics-suite.json'),
 ('NMHV dihedral symmetry n=8..12','nmhv-dihedral-replication-suite.json'),
 ('NMHV spurious residue cancellation n=6..9','nmhv-spurious-boundary-replication-suite.json'),
 ('NMHV physical residue survival n=6..9','nmhv-physical-boundary-replication-suite.json'),
 ('NMHV boundary counts n=6..50','nmhv-bcfw-boundary-count-formula.json'),
 ('NMHV oriented boundary cancellation n=6..50','nmhv-bcfw-oriented-boundary-cancellation.json'),
]
rows=[];passed=True
for label,name in artifacts:
 p=R/name;d=json.loads(p.read_text());ok=d.get('passed') is True;passed &= ok;rows.append({'benchmark_family':label,'artifact':str(p.relative_to(ROOT)),'schema':d.get('schema'),'passed':ok})
source_checks=[ROOT/'research/nima'/('check_'+name.removesuffix('.json').replace('-','_')+'.py') for _,name in artifacts]
sources_present=all(p.is_file() for p in source_checks);passed &= sources_present
out={'schema':'marici.nima.irl-amplitudes-replication-manifest.v2','references':[{'arxiv':'1711.09102','title':'Scattering Forms and the Positive Geometry of Kinematics, Color and the Worldsheet'},{'arxiv':'1008.2958','title':'The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM'}],'benchmark_families':rows,'family_count':len(rows),'suite_checkers':[str(p.relative_to(ROOT)) for p in source_checks],'all_suite_checkers_present':sources_present,'all_dependencies_passed':passed,'claim':'Local exact replications of selected published formulas, symmetries, residues, and positive-geometry structures.','nonclaim':'Not a replication of all results in either paper; not experimental validation; finite-range computations are not arbitrary-n proofs.','passed':passed}
p=R/'irl-amplitudes-replication-manifest.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
