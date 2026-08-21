"""Exact character obstruction for Carrier polarity -> time orientation."""
import json
from pathlib import Path
import sympy as sp

a=sp.symbols("a")
# One-dimensional characters on candidate involutions.
characters={
 "carrier_road_reflection":-1,
 "carrier_core_exchange":-1,
 "spatial_reflection_on_time_orientation":1,
 "time_reversal_on_time_orientation":-1,
}

def intertwiner_equation(source_char,target_char):
    return sp.expand(target_char*a-a*source_char)

road_to_spatial=intertwiner_equation(
 characters["carrier_road_reflection"],
 characters["spatial_reflection_on_time_orientation"])
core_to_time=intertwiner_equation(
 characters["carrier_core_exchange"],
 characters["time_reversal_on_time_orientation"])

assert road_to_spatial==2*a
assert sp.solve(road_to_spatial,a)==[0]
assert core_to_time==0

result={
 "schema":"marici.carrier-polarity-time-orientation-character-gate.v1",
 "source_facts":{
  "carrier":"m=3 Hodge comparison: road reflection and polarity/core exchange each negate the relation/polarity line",
  "spacetime":"a transverse spatial reflection preserves future time orientation; time reversal negates it",
 },
 "characters":characters,
 "candidate_comparisons":{
  "road_reflection_to_spatial_reflection":{
   "intertwiner_residual":str(road_to_spatial),
   "only_intertwiner":"zero",
   "status":"obstructed",
  },
  "core_exchange_to_time_reversal":{
   "intertwiner_residual":str(core_to_time),
   "intertwiner_space":"one-dimensional",
   "status":"character-compatible but not canonically normalized or physically typed",
  },
 },
 "verdict":(
  "Carrier polarity is not intrinsically the spacetime time-orientation line. "
  "The natural road-reflection comparison is character-obstructed. A "
  "core-exchange/time-reversal comparison is algebraically possible only "
  "after declaring which Carrier involution represents physical time reversal."
 )
}
out=Path(__file__).parents[1]/"results"/"carrier_polarity_time_orientation_character_gate.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
