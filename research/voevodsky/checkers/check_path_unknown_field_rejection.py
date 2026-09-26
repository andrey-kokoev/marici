"""Exact typed path records refuse ignored extra fields and implicit issuer claims."""
from hashlib import sha256
from pathlib import Path
import json
allowed={'kind','endpoint','edges'}
base={'kind':'original-identity@1','endpoint':'A','edges':[]}
def parse(record):
 if set(record)!=allowed:return 'UNKNOWN_OR_MISSING_FIELDS'
 if record['kind']!='original-identity@1' or record['endpoint']!='A' or record['edges']!=[]:return 'INVALID_TYPED_RECORD'
 return 'STRUCTURAL_ONLY'
def H(obj):return sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
for name,value in (('issuer','fictional-owner'),('origin','fake-origin'),('extensions',{'issuer':'fake'})):
 extra=dict(base,**{name:value})
 assert parse(extra)=='UNKNOWN_OR_MISSING_FIELDS'
 assert H({k:extra[k] for k in allowed})==H(base) and H(extra)!=H(base)
assert parse(base)=='STRUCTURAL_ONLY'
assert parse({'kind':'original-identity@1','endpoint':'A'})=='UNKNOWN_OR_MISSING_FIELDS'
report={'passed':True,'extra_fields':'issuer/origin/extensions refused, not silently stripped','permissive_projection':'would collide with base commitment after ignoring extras','exact_typed_record':'structural only, no issuer authority','scope':'Synthetic strict schema; not observed path, signature verification or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/path-unknown-field-rejection.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
