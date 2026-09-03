#!/usr/bin/env python3
"""Bounded census of declared cosmology degree-two generators and chain maps."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/benincasa/results/cosmology_degree_two_generator_provenance_census.json'
roots=[ROOT/'research/nima/results',ROOT/'research/voevodsky/results']
records=[];chain_maps=[]
for root in roots:
 for p in sorted(root.glob('cosmology*.json')):
  try:d=json.loads(p.read_text())
  except Exception:continue
  gens=d.get('degree_two_generators',d.get('degree_2_generators'))
  if gens is not None:
   records.append({'path':p.relative_to(ROOT).as_posix(),'schema':d.get('schema'),'generators':gens,'relative_differential':d.get('relative_differential',d.get('differential_to_pair_residues_rows_q1q2_q1q3_q2q3_cols_Xi_minusSigma')),'total_chain_map_constructed':d.get('total_Cech_de_Rham_chain_map_constructed',False),'resolved_Rees_chain_lift_constructed':d.get('resolved_Rees_chain_lift_constructed',False)})
  if d.get('total_Cech_de_Rham_chain_map_constructed') is True or d.get('resolved_Rees_chain_lift_constructed') is True:
   chain_maps.append(p.relative_to(ROOT).as_posix())
assert records and not chain_maps
names=sorted({x for r in records for x in r['generators']});assert names==['Xi_log','minus_sigma123']
diffs=[r['relative_differential'] for r in records if r['relative_differential'] is not None];assert diffs and all(x==diffs[0] for x in diffs);D=diffs[0];assert D==[[1,-1],[-1,1],[1,-1]]
out={'schema':'marici.benincasa.cosmology-degree-two-generator-provenance-census.v1','scope':{'roots':[p.relative_to(ROOT).as_posix() for p in roots],'glob':'cosmology*.json','typed_gate':'declared degree_two_generators or degree_2_generators plus explicit chain-map flags'},'records':records,'distinct_declared_generators':names,'distinct_pair_differentials':[D],'constructed_total_or_resolved_chain_maps':chain_maps,'exact_residual':'the bounded declared source envelope contains only Xi_log and minus_sigma123, with opposite circuit-line differentials; it declares no constructed total Cech-de-Rham or resolved Rees chain map','disposition':'no transverse degree-two generator found in the bounded declared source envelope','nonverification':'absence outside the scanned result roots is not established','first_missing_typed_object':'a source-derived degree-two generator with a pair differential transverse to (1,-1,1), or a newly declared chain map exposing one','acceptance_test':'declare its source, exact differential, D-squared-zero witness, and tau_p cancellation','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
