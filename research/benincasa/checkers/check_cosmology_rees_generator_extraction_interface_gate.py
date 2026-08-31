#!/usr/bin/env python3
"""Audit whether the current Rees census interface can extract labelled length-one generators."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research'/'nima';R=ROOT/'research'/'benincasa'/'results'
source=(N/'checkers'/'check_cosmology_p_normal_rank26_rees_census.py').read_text();summary=json.loads((N/'results'/'cosmology_p_normal_rank26_half_twist_gate.json').read_text())
assert summary['elementary_length_census']['length_1']==8
checks={'engine_output_consumed_as_ranks_only':"rank=json.loads(out)" in source and "rank['relation_ranks']" in source,'row_or_column_transformations_serialized':False,'labelled_kernel_or_cokernel_vectors_serialized':False,'length_one_generators_in_receipt':False}
assert checks['engine_output_consumed_as_ranks_only']
out={'schema':'marici.benincasa.cosmology-rees-generator-extraction-interface-gate.v1','physical_length_one_count':8,'interface_checks':checks,'decision':'The current sparse census certifies invariant-factor multiplicities but discards the transformation data needed to extract labelled generators. The eight factors are not eight source objects.','required_capability':'a provenance-preserving exact or modular presentation backend returning labelled basis transformations with replay and cross-prime matching','authority_boundary':'Adding such backend output may enable extraction; the present census alone cannot authorize a quotient line or tau comparison.','passed':True};(R/'cosmology_rees_generator_extraction_interface_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
