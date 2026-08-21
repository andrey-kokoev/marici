"""Exact character-ring repair for Carrier polarity -> time orientation."""
import itertools,json
from pathlib import Path

# Characters are ordered on generators (r,t):
# r = road/spatial reflection, t = core exchange/time reversal.
polarity=(-1,-1)
time=(1,-1)
chars=list(itertools.product((1,-1),repeat=2))
tensor=lambda x,y:(x[0]*y[0],x[1]*y[1])
repairs=[chi for chi in chars if tensor(polarity,chi)==time]
assert repairs==[(-1,1)]
spatial_orientation=repairs[0]
assert tensor(polarity,spatial_orientation)==time
assert tensor(polarity,time)==spatial_orientation
assert tensor(time,spatial_orientation)==polarity

result={
 "schema":"marici.polarity-orientation-twist.v1",
 "generator_order":["road_or_spatial_reflection","core_exchange_or_time_reversal"],
 "characters":{
  "carrier_polarity":list(polarity),
  "physical_time_orientation":list(time),
  "required_spatial_orientation_twist":list(spatial_orientation),
 },
 "identity":"L_time = L_polarity tensor L_spatial_orientation",
 "uniqueness":{"all_real_Z2xZ2_characters":[list(x) for x in chars],"repair_count":len(repairs)},
 "checks":{
  "unique_character_repair":True,
  "time_equals_polarity_tensor_spatial":True,
  "three_lines_pairwise_recover_each_other":True,
 },
 "typing_boundary":(
  "The character identity is exact after declaring the generator comparison. "
  "It does not derive the spacetime spatial-orientation line or identify "
  "Carrier road reflection with physical parity."
 ),
 "verdict":(
  "The polarity/time mismatch is a one-line twist, not an arbitrary defect. "
  "The unique missing character is spatial parity: odd under spatial "
  "reflection and even under time reversal."
 )
}
out=Path(__file__).parents[1]/"results"/"polarity_orientation_twist.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
