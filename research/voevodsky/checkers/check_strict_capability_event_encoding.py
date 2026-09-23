"""Strict JSON source event canonicalization rejects duplicate keys/actions."""
from hashlib import sha256
from pathlib import Path
import json
allowed={'schema','issuer','event_id','generation','manifest','actions'}
actions=['attest-primitive-row-origin','authorize-future-source-rooted-proof-use']
def unique(pairs):
 result={}
 for key,value in pairs:
  if key in result:raise ValueError('DUPLICATE_JSON_KEY')
  result[key]=value
 return result
def parse(raw):
 event=json.loads(raw,object_pairs_hook=unique)
 if set(event)!=allowed or type(event['generation']) is not int or event['generation']<0:raise ValueError('INVALID_EVENT_SCHEMA')
 if not isinstance(event['actions'],list) or any(x not in actions or not isinstance(x,str) for x in event['actions']):raise ValueError('UNKNOWN_ACTION')
 if len(set(event['actions']))!=len(event['actions']):raise ValueError('DUPLICATE_CAPABILITY')
 event['actions']=sorted(event['actions'])
 return event
def H(event):return sha256(json.dumps(event,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
event={'schema':'synthetic-source-event-v1','issuer':'fictional-issuer','event_id':'fictional-evt','generation':1,'manifest':'fictional-hash','actions':actions}
raw=json.dumps(event);reversed_raw=json.dumps(dict(event,actions=list(reversed(actions))),indent=2)
assert H(parse(raw))==H(parse(reversed_raw))
def reject(raw,reason):
 try:parse(raw)
 except ValueError as err:assert str(err)==reason
 else:raise AssertionError('malformed event accepted')
reject(raw.replace('"issuer": "fictional-issuer"','"issuer": "fictional-issuer", "issuer": "other"'),'DUPLICATE_JSON_KEY')
reject(json.dumps(dict(event,actions=[actions[0],actions[0]])),'DUPLICATE_CAPABILITY')
reject(json.dumps(dict(event,actions=['unknown-action'])),'UNKNOWN_ACTION')
reject(json.dumps(dict(event,generation=True)),'INVALID_EVENT_SCHEMA')
reject(json.dumps(dict(event,extra='ignored')),'INVALID_EVENT_SCHEMA')
report={'passed':True,'action_order_and_whitespace':'canonical normalized same digest','duplicate_json_key':'DUPLICATE_JSON_KEY','duplicate_action':'DUPLICATE_CAPABILITY','unknown_action':'UNKNOWN_ACTION','bool_generation_or_unknown_field':'INVALID_EVENT_SCHEMA','status':'TEST_ONLY_CANONICAL_BYTES_NOT_AUTHORIZED','scope':'Local encoding v1, not a standard signature format or authenticated issuer event.'}
out=Path(__file__).resolve().parents[1]/'results/strict-capability-event-encoding.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
