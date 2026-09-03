"""Classify the four logical escapes from the fixed-horn no-go theorem."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_horn_assumption_relaxation_census.json'
def main():
 census={
  'change_target':{'evades_no_go':True,'solves_original_horn':False,'retains_invariant':False},
  'change_degree_or_equation':{'evades_no_go':True,'solves_original_horn':False,'retains_invariant':True},
  'drop_chain_map':{'evades_no_go':True,'solves_original_horn':False,'retains_invariant':False},
  'drop_regulator_detection':{'evades_no_go':True,'solves_original_horn':False,'retains_invariant':False},
 }
 assert all(v['evades_no_go'] and not v['solves_original_horn'] for v in census.values())
 survivors=[k for k,v in census.items() if v['retains_invariant']];assert survivors==['change_degree_or_equation']
 out={'schema':'marici.voevodsky.cosmology-horn-assumption-relaxation-census.v1','status':'no_relaxation_solves_original_horn_one_preserves_a_new_obstruction_question','census':census,'change_target':'Subtracting, replacing, or killing (Xi_log,-sigma123) removes the required boundary datum and answers a different question.','change_degree_or_equation':'Retaining {u,v} as a closed degree-two obstruction is source-natural and evidence-preserving, but explicitly abandons the demand for a degree-one horn.','drop_chain_map':'Without compatibility with differentials, boundary claims and cohomology transport are undefined; representative-level numbers do not repair this.','drop_regulator_detection':'A quotient that kills Xi_log can admit a filler only by discarding the verified primitive class and cannot support its requested readout.','decision':'None of the four logical escapes constructs the original horn. The only evidence-preserving successor is a new question: normalize and test the sourced K2 obstruction as a mathematical period/readout candidate without calling it a filler.','next_gate':'K2-obstruction-period-normalization: compute the canonical torus period, orientation dependence, and exact boundary between mathematical and physical readout claims','limitations':['logical census relative to the frozen four-premise no-go','does not authorize changing the research objective silently','no physical interpretation established'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
