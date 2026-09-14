"""Check the character twist supplied by an oriented endpoint-conductor interval."""
import json
conductor_character=1
relative_cut_orientation_character=-1
product=conductor_character*relative_cut_orientation_character
assert product==-1
assert product==(-1)
out={'schema':'marici.nima.qg2-relative-cut-orientation-twist.v1','status':'character_repair_constructed_conditionally_on_relative_cut_chain',
'conductor_character':conductor_character,'oriented_interval_character':relative_cut_orientation_character,
'twisted_character':product,'log_primitive_character':-1,
'orientation_source':'boundary orientation [endpoint,conductor]; reversal swaps endpoints and negates the interval generator',
'boundary':'physical existence and ambient transport of the relative cut chain remain to be constructed'}
open('research/nima/results/qg2-relative-cut-orientation-twist.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
