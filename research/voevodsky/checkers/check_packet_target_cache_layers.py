"""Cache row-linear evaluation separately from target/surplus validity."""
from hashlib import sha256
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1));m=(0,1,0,0)
def H(x):return sha256(repr(x).encode()).hexdigest()
raw_key=(H(rows),1,H(m));raw_value=((1,0),1)
certs=[{'surplus':0,'normal':(1,0),'bound':1},{'surplus':1,'normal':(1,0),'bound':2},{'surplus':1,'normal':(1,0),'bound':1}]
def valid(c):return c['surplus']>=0 and c['normal']==raw_value[0] and c['bound']==raw_value[1]+c['surplus']
assert [valid(c) for c in certs]==[True,True,False]
keys=[(raw_key,H(c)) for c in certs]
assert len(set(keys))==3
unsafe={raw_key:valid(certs[0])}
assert unsafe[raw_key] is True and valid(certs[2]) is False
report={'passed':True,'raw_evaluation_cache_key':'source digest + generation + multipliers digest','shared_raw_result':'normal(1,0), raw bound1','certificates':'target1 surplus0 valid; target2 surplus1 valid; target1 surplus1 invalid','bare_raw_key_for_certificate':'false cache hit on invalid third certificate','safe_certificate_key':'raw key + exact target normal/bound + surplus digest','scope':'Local rational certificate predicate; no actual proof event, source-owner grant or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/packet-target-cache-layers.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
