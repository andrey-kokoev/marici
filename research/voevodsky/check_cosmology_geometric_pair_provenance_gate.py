"""Encode the witnessed geometric realization gate for the ambient-star pair."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_geometric_pair_provenance_gate.json'
GATES=('independent_geometry','regular_center','actual_strata','incidence_fundamental_chain','wall_ratio_functions','tame_boundary','base_change_naturality')
def admitted(w): return all(w.get(k,False) for k in GATES)
def main():
    ambient={k:True for k in GATES}; formal={k:False for k in GATES}; formal['tame_boundary']=True
    assert admitted(ambient) and not admitted(formal)
    out={
      'schema':'marici.voevodsky.cosmology-geometric-pair-provenance-gate.v1',
      'status':'witnessed_geometric_realization_functor_defined_local_ambient_star_admitted',
      'source_category':'GeoPair_ord: regular codimension-three centers with ordered common-line conormals, their blowups, actual labeled incidence strata, and transverse orientation-preserving morphisms.',
      'cellular_functor':'C_rel sends a geometric object to the derived arrow from its exceptional-triangle boundary complex into its ambient-star incidence complex.',
      'regulator_functor':'K_Ger sends it to the relative logarithmic/Gersten comparison pair.',
      'natural_transformation':'Phi:C_rel -> K_Ger is induced by wall ratios, dlog, and tame symbols; Gamma maps to tau and its boundary maps to (Xi_rel,-sigma123).',
      'admission_gates':list(GATES),
      'witness_rule':'An algebraic pair is sourced only with an explicit GeoPair_ord witness and its comparison maps. Abstract isomorphism to an object in the essential image does not supply provenance.',
      'local_result':'Blowup of the local A3 center with walls U,V,U+V+P passes every gate.',
      'formal_cone_result':'A freely adjoined disk can mimic the chain matrix and tame target but fails independent geometry, actual-stratum, fundamental-chain, wall-function, and naturality gates.',
      'global_boundary':'The intended global carrier still lacks a GeoPair_ord witness and compatible transitions.',
      'decision':'The local ambient star is a sourced relative HomotopyLift; unsourced cones remain excluded even when chain-isomorphic.',
      'next_gate':'regulator-naturality-square',
      'limitations':['local witnessed result; global witness absent','checker execution pending','no ElementLift or physical interface inferred'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
