from __future__ import annotations
import json
from pathlib import Path

SRC=Path('research/voevodsky/arithmetic-generator-gb.json')
OUT=Path('research/voevodsky/results/arithmetic_generator_gb.json')

def main():
 d=json.loads(SRC.read_text(encoding='utf-8'));p=d['parameter_sort'];o=d['object_sort'];n=d['normalization']
 source_paths=[Path(p['source_formula']),Path(p['source_result']),Path(p['fourier_convention'])]
 checks={
  'source_references_materialized':all(x.exists() for x in source_paths),
  'three_sectors_exact':set(p['sector_inputs'])=={'endpoint','gamma','prime'},
  'assemble_before_scalarization':o['cancellation_policy']=='assemble all sectors before scalarization',
  'no_positive_sector_decomposition':o['positive_sector_decomposition_asserted'] is False,
  'uniform_common_factor':n['source_to_marici_common_positive_factor']==4 and set(n['factor_applies_uniformly_to'])==set(p['sector_inputs']),
  'factor_two_rejected':n['factor_two_convention_rejected'] is True,
  'raw_probe_codomain':d['output_interfaces']['raw_probe_evaluation'].endswith('O_C_raw'),
  'no_rh_or_positivity_asserted':d['rh_or_positivity_asserted'] is False}
 result={'schema':'marici.voevodsky.arithmetic-generator-gb-check.v1',**checks,
  'G_B_materialized':all(checks.values()),'passed':all(checks.values())}
 text=json.dumps(result,indent=2,sort_keys=True);OUT.write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
