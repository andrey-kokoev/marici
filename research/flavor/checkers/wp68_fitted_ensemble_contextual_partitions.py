#!/usr/bin/env python3
"""WP68: exact accounting of contextual partitions on fitted flavor data."""

from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp68_fitted_ensemble_contextual_partitions.json"
def load(path): return json.loads((ROOT/path).read_text())

def main():
    w20=load("research/flavor/results/wp20_valley_audit.json")
    stat=load("research/nima/results/flavor-stationarity-sheet-ensemble.json")
    deck=load("research/flavor/results/wp24c_generation_exchange.json")
    nerve=load("research/nima/results/flavor-probe-nerve-doublets.json")
    n=w20["n_minima_audited"]; kinds=w20["valley_kind_counts"]
    diag=deck["diagonal_class"]; paired=diag["n_stored_two_minima"]+diag["n_partner_recovered"]
    gates={
      "complete_1210_sheet_ensemble_accounted":n==1210 and stat["sheet_count"]==1210 and stat["checks"]["all_1210_viable_sheets_recovered"],
      "valley_partition_is_exact":kinds["exact"]+kinds["extra"]==n and kinds=={"exact":370,"extra":840},
      "stationarity_acceptance_class_is_empty":stat["fraction_within_one_sigma"]==0.0 and stat["checks"]["no_sheet_within_one_sigma"],
      "stationarity_ranges_are_disjoint":stat["checks"]["predicted_and_observed_ranges_are_disjoint"],
      "deck_partition_accounting_is_72_plus_1":paired==72 and diag["n_textures"]-paired==1,
      "physical_and_deck_probe_partitions_differ":nerve["probe_matrices"]["physical_rank"]==1 and nerve["probe_matrices"]["full_probe_rank"]==2,
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.fitted-ensemble-contextual-partitions.v1",
      "domain":{"complete_stored_viable_sheet_ensemble":n,"diagonal_texture_reference_domain":diag["n_textures"]},
      "partitions":{
        "fit_valley_provenance":{"exact_target":kinds["exact"],"extra_viable":kinds["extra"]},
        "stationarity_selector":{"accepted_within_one_sigma":0,"rejected":n},
        "generation_exchange_domain":{"paired_textures":paired,"undefined_oddball":1},
        "physical_readout_on_each_deck_doublet":[["s","T(s)"]],
        "physical_plus_deck_odd_on_each_doublet":[["s"],["T(s)"]],
      },
      "stationarity":{"observed_ratio_range":stat["observed_ratio_range"],"predicted_ratio_range":stat["predicted_ratio_range"],"rmse_ratio":stat["rmse_ratio"]},
      "classification":"stationarity selects an empty class on the complete ensemble; deck oddness refines lens presentations only; fitted viability and physical equivalence are distinct partitions",
      "smallest_ensemble_falsifier":"zero of 1210 viable sheets lies within one sigma of its sheet-wise stationary prediction",
      "conclusion":"No tested selector survives the complete fitted ensemble; contextual partitions confirm that readout, viability, stationarity, and presentation equivalence cannot be merged.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"sheets":n,"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()
