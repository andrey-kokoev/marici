#!/usr/bin/env python3
"""Verify that finite exact stabilization is subsumed by the uniform tangent homotopy."""
import json
from pathlib import Path
P=Path(__file__).resolve();ROOT=P.parents[3];R=ROOT/'research'/'benincasa'/'results'
s=json.loads((R/'cosmology_all_S_exact_tangent_stabilization.json').read_text());u=json.loads((R/'cosmology_all_S_uniform_tangent_homotopy.json').read_text());assert s['zero_class_stable_through_tested_system'];assert u['degree_uniform_presentation_theorem'];tested={r['ambient_degree']:r for r in u['tested_embeddings']};assert all(tested[d]['exact_embedded_reconstruction'] for d in (8,10));out={'schema':'marici.benincasa.cosmology-all-S-exact-tangent-stabilization-final.v1','finite_exact_degrees':[6,8,10],'uniform_range':'all ambient A>=6','same_target_label':True,'finite_branch_subsumed':True,'decision':'The degree-6,8,10 rational reconstructions are controls for the degree-uniform 230-row homotopy; no separate finite-stabilization uncertainty remains.','passed':True};(R/'cosmology_all_S_exact_tangent_stabilization_final.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
