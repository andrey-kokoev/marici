#!/usr/bin/env python3
"""WP59: exact gate matrix for the tested physical16 selector frontier."""

from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp59_selector_frontier_matrix.json"

def load(name): return json.loads((ROOT/f"research/flavor/results/{name}.json").read_text())

def main():
    source={
      "wp52":load("wp52_source_selector_audit"),
      "wp53":load("wp53_rg_transport_selector_gate"),
      "wp54":load("wp54_spectral_conditional_expectation"),
      "wp55":load("wp55_relational_reference_port"),
      "wp56":load("wp56_spontaneous_cp_selector_gate"),
      "wp57":load("wp57_invariant_word_complement"),
      "wp58":load("wp58_commutator_score_selector_gate"),
    }
    assert all(all(x["gates"].values()) for x in source.values())
    # D=original full-quotient descent, P=proper physical16 reduction,
    # A=independent source authorization of the reducing operation,
    # I=typed physical implementation, E=survives fitted ensemble.
    rows={
      "measured_and_physical16_readouts":{"D":True,"P":False,"A":True,"I":True,"E":True,"first_failure":"P"},
      "generation_exchange_deck_probe":{"D":False,"P":False,"A":True,"I":False,"E":True,"first_failure":"D"},
      "one_loop_rg_transport":{"D":True,"P":False,"A":True,"I":False,"E":True,"first_failure":"P"},
      "spectral_conditional_expectation":{"D":True,"P":True,"A":False,"I":False,"E":False,"first_failure":"A"},
      "relational_reference_port":{"D":False,"P":False,"A":False,"I":False,"E":True,"first_failure":"D"},
      "discrete_cp_chart_vacua":{"D":False,"P":False,"A":False,"I":False,"E":True,"first_failure":"D"},
      "mixed_gram_word_complement":{"D":True,"P":False,"A":True,"I":True,"E":True,"first_failure":"P"},
      "positive_commutator_score":{"D":True,"P":False,"A":True,"I":True,"E":True,"first_failure":"P"},
    }
    progressive=[k for k,v in rows.items() if all(v[g] for g in "DPAIE")]
    gates={
      "all_dependency_checkers_pass":True,
      "every_candidate_has_declared_first_failure":all(not v[v["first_failure"]] for v in rows.values()),
      "no_candidate_passes_all_five_gates":progressive==[],
      "descent_and_instrument_do_not_imply_selection":rows["positive_commutator_score"]["D"] and rows["positive_commutator_score"]["I"] and not rows["positive_commutator_score"]["P"],
      "proper_image_does_not_imply_physical_authority":rows["spectral_conditional_expectation"]["P"] and not rows["spectral_conditional_expectation"]["A"],
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.selector-frontier-matrix.v1",
      "gates_definition":{"D":"descends on original full weak-basis quotient","P":"reduces to proper physical16 family","A":"reducing operation independently source-authorized","I":"typed physical implementation/instrument","E":"prediction survives fitted ensemble"},
      "candidates":rows,
      "progressive_candidates":progressive,
      "first_missing_arrow":"No tested operation simultaneously supplies proper reduction and independent physical authorization; separators stop at P, while the sole proper-image map stops at A.",
      "sharp_next_target":"a source action or threshold boundary law whose induced quotient map has a proper image, with independently frozen normalization and instrument typing",
      "gates":gates,
      "conclusion":"The tested flavor programme contains separators, transport, rigidifiers, a relational extension, and one unauthorized mathematical selector, but no genuine physical selector.",
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"candidates":len(rows),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()
