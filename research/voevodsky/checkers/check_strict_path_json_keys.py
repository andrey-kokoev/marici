"""Refuse duplicate JSON keys before computing a typed path commitment."""
from hashlib import sha256
from pathlib import Path
import json
def unique(pairs):
 obj={}
 for key,value in pairs:
  if key in obj:raise ValueError('DUPLICATE_JSON_KEY')
  obj[key]=value
 return obj
def parse(text):
 value=json.loads(text,object_pairs_hook=unique)
 if not isinstance(value,dict) or set(value)!={'kind','endpoint','edges'} or value['kind']!='original-identity@1' or value['endpoint']!='A' or value['edges']!=[]:raise ValueError('INVALID_TYPED_PATH')
 return value
ambiguous='{"kind":"original-identity@1","kind":"derived-reduction@1","endpoint":"A","edges":[]}'
assert json.loads(ambiguous)['kind']=='derived-reduction@1'
try:parse(ambiguous)
except ValueError as err:assert str(err)=='DUPLICATE_JSON_KEY'
else:raise AssertionError('duplicate key accepted')
a=parse('{"kind":"original-identity@1","endpoint":"A","edges":[]}')
b=parse('{"edges":[],"endpoint":"A","kind":"original-identity@1"}')
H=lambda obj:sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert H(a)==H(b)
report={'passed':True,'duplicate_kind':'rejected before typed commitment','reordered_unique_fields':'identical canonical digest','scope':'Strict parsing illustration only, not signature validation, observed events, owner grant or analytic roles.'}
out=Path(__file__).resolve().parents[1]/'results/strict-path-json-keys.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
