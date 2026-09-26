"""Exact integer validation excludes JSON booleans at path generation fields."""
from pathlib import Path
import json
payloads=('1','true','1.0','"1"','0','-1')
def gate(text):
 value=json.loads(text)
 if type(value) is not int:return 'NOT_EXACT_INTEGER'
 if value<1:return 'INVALID_GENERATION'
 return 'STRUCTURAL_GENERATION_ONLY'
assert True==1 and isinstance(True,int)
assert [gate(s) for s in payloads]==['STRUCTURAL_GENERATION_ONLY','NOT_EXACT_INTEGER','NOT_EXACT_INTEGER','NOT_EXACT_INTEGER','INVALID_GENERATION','INVALID_GENERATION']
report={'passed':True,'json_true':'refused though Python true == 1 and isinstance(true,int)','json_1_0_and_string_1':'refused','json_integer_1':'structural generation only','zero_or_negative':'refused','scope':'Local JSON type gate, not event signature, row owner or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/path-generation-boolean-confusion.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
