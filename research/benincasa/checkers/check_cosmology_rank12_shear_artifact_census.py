#!/usr/bin/env python3
"""Census candidate artifacts for the missing q0-to-e6 rank-twelve shear."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa'
paths=['e6-bridge-exceptional-extension-certificate.json','cyclic-leray-naturality-certificate.json','double-soft-cospan-closure.json','triple-soft-exceptional-resolution-certificate.json']
d={p:json.loads((B/p).read_text()) for p in paths}
assert 'not the full rank-twelve connection' in d[paths[0]]['scope']
assert 'not a global equality of rank-twelve connection matrices' in d[paths[1]]['scope']
assert 'full rank-twelve logarithmic extension remains open' in d[paths[2]]['verdict']
assert 'not a full rank-twelve nearby connection' in d[paths[3]]['scope']
out={'schema':'marici.benincasa.cosmology-rank12-shear-artifact-census.v1','candidates':[{'artifact':paths[0],'result':'e6 line and top-column bridge only','exclusion':'explicitly not full rank twelve'},{'artifact':paths[1],'result':'six local Leray germs are C3 equivariant','exclusion':'no overlap transition or global connection equality'},{'artifact':paths[2],'result':'carrier and e6 bridge close on existing resolution','exclusion':'full logarithmic extension explicitly remains open'},{'artifact':paths[3],'result':'exceptional-plane and center census','exclusion':'explicitly not a full nearby connection'}],'source_derived_q0_to_e6_shear_count':0,'cyclically_coherent_full_rank12_transport_count':0,'disposition':'exhausted among audited artifacts','not_promoted':['local cyclic equivariance','bridge persistence','absence of new exceptional carrier'],'next_candidate':'derive the Cayley-Menger cyclic transverse connection in a source-normalized triangular frame and test its q0-to-e6 block','passed':True};(B/'results/cosmology_rank12_shear_artifact_census.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
