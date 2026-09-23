"""Row DAG and effect purity do not reconstruct redacted event occurrence ID."""
from hashlib import sha256
from pathlib import Path
import json
roles=('Z','W','V','T');deps={'Z':(), 'W':('Z',),'V':('Z',),'T':('W','V')}
packets={'Z':((1,1),2),'W':((2,1),3),'V':((1,2),3),'T':((3,3),6)}
manifest='square-synthetic-v1';effect_footprints={r:('pure',manifest) for r in roles}
def digest(t):return sha256(repr(t).encode()).hexdigest()
def trace(w_id):return (('Z','z#01'),('W',w_id),('V','v#01'),('T','t#01'))
a=trace('w#alpha');b=trace('w#beta')
def redact(t):return tuple((role,identifier if role!='W' else None) for role,identifier in t)
assert a!=b and digest(a)!=digest(b) and redact(a)==redact(b)
assert all(packets[r]==packets[r] and effect_footprints[r]==('pure',manifest) for r in roles)
def certify_occurrence_swap(t,index):
 x,y=t[index:index+2]
 if x[1] is None or y[1] is None:raise ValueError('UNVERIFIABLE_TRACE')
 if x[0] in deps[y[0]] or y[0] in deps[x[0]]:raise ValueError('DEPENDENT_SWAP')
 return {'event_ids':(x[1],y[1]),'source_hash':digest(t),'manifest':manifest}
assert certify_occurrence_swap(a,1)['event_ids']==('w#alpha','v#01')
assert certify_occurrence_swap(b,1)['event_ids']==('w#beta','v#01')
try:certify_occurrence_swap(redact(a),1)
except ValueError as err:assert str(err)=='UNVERIFIABLE_TRACE'
else:raise AssertionError('redacted ID invented')
assert deps['T']==('W','V') and packets['T']==((3,3),6)
report={'passed':True,'same_redacted_record_two_distinct_complete_traces':True,'same_row_packets_DAG_and_pure_effects':True,'role_W_structurally_required':True,'opaque_W_event_id_recoverable':False,'swap_replay':'UNVERIFIABLE_TRACE, not invalid swap','scope':'Synthetic occurrence IDs. Mathematical DAG/packet and local purity evidence do not authenticate missing occurrence or actual historical execution.'}
out=Path(__file__).resolve().parents[1]/'results/redacted-event-swap-replay.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
