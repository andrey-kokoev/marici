#!/usr/bin/env python3
"""Check the noncircular outcome logic and current evidence for constructor flatness."""
import json
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"constructor-flatness-conjecture.v1.json"
LOOP=ASPECT/"results"/"comparison_loop_interferometer.json"
PROBES=ASPECT/"results"/"comparison_loop_optimal_probes.json"
GATE=ASPECT/"results"/"interaction_net_integral_complex_lift_gate.json"
RESULT=ASPECT/"results"/"constructor_flatness_conjecture.json"
def complete(packet,fields): return all(packet.get(k) is True for k in fields)
def flat(target,holonomy,allowed): return holonomy in allowed[target]
def verdict(is_complete,is_flat,outcomes):
 key=("complete_" if is_complete else "incomplete_")+("flat" if is_flat else "nonflat")
 return outcomes[key]
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); loop=json.loads(LOOP.read_text(encoding="utf-8")); probes=json.loads(PROBES.read_text(encoding="utf-8")); gate=json.loads(GATE.read_text(encoding="utf-8"))
 fields=c["source_completeness_fields"]; all_true={k:True for k in fields}; one_missing=dict(all_true,quotient_dual=False); allowed=c["target_flatness"]; outcomes=c["outcomes"]
 scenarios={
  "survival":verdict(complete(all_true,fields),flat("complex","identity",allowed),outcomes),
  "refutation":verdict(complete(all_true,fields),flat("complex","source_dependent",allowed),outcomes),
  "missing":verdict(complete(one_missing,fields),flat("complex","source_dependent",allowed),outcomes),
  "accidental":verdict(complete(one_missing,fields),flat("complex","identity",allowed),outcomes),
  "projective_phase":verdict(complete(all_true,fields),flat("projective","scalar_phase",allowed),outcomes),
  "complex_phase":verdict(complete(all_true,fields),flat("complex","scalar_phase",allowed),outcomes),
  "oriented_conjugation":verdict(complete(all_true,fields),flat("oriented","conjugation",allowed),outcomes)}
 current_complete=gate["status"]=="present_shape_valid" and gate["candidate_present_valid"]
 observed_nonflat=probes["optimal_spread"]>c["current_evidence"]["two_sided_uncertainty"]
 current=verdict(current_complete,not observed_nonflat,outcomes)
 checks={"noncircular_completeness":complete(all_true,fields) and not complete(one_missing,fields),"four_outcomes":scenarios["survival"]=="conjecture_survives" and scenarios["refutation"]=="decisive_refutation" and scenarios["missing"]=="missing_constructor" and scenarios["accidental"]=="accidental_agreement_no_explanation","target_types_separated":scenarios["projective_phase"]=="conjecture_survives" and scenarios["complex_phase"]=="decisive_refutation" and scenarios["oriented_conjugation"]=="decisive_refutation","current_gate_incomplete":not current_complete,"current_holonomy_detected":observed_nonflat,"current_not_false_refutation":current=="missing_constructor","fixtures_present":loop["passed"] and probes["passed"] and gate["passed"],"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.constructor-flatness-conjecture-result.v1","passed":all(checks.values()),"checks":checks,"scenario_verdicts":scenarios,"current_verdict":current,"current_source_complete":current_complete,"current_spread":probes["optimal_spread"],"current_two_sided_uncertainty":c["current_evidence"]["two_sided_uncertainty"],"conjecture_status":"open_awaiting_decisive_source_complete_test"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()

