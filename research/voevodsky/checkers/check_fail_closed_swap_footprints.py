"""Swap decision distinguishes unknown, pure, disjoint and conflicting effects."""
from pathlib import Path
import json
manifest='square-synthetic-event-DAG-v1'
row_deps={'W':('Z',),'V':('Z',),'U':('Z',),'Z':()}
def declaration(event,reads=(),writes=(),binding=manifest):
 return {'event':event,'manifest':binding,'reads':frozenset(reads),'writes':frozenset(writes),'scope':'synthetic-local-effect-model'}
def swap(a,b,footprints):
 if a in row_deps[b] or b in row_deps[a]:raise ValueError('ROW_DEPENDENCY')
 pair=[]
 for event in (a,b):
  data=footprints.get(event)
  if data is None:raise ValueError('UNKNOWN_EFFECT_FOOTPRINT')
  if data['event']!=event or data['manifest']!=manifest or data['scope']!='synthetic-local-effect-model':raise ValueError('STALE_OR_WRONG_EVENT_FOOTPRINT')
  pair.append(data)
 x,y=pair
 if x['writes'] & (y['reads']|y['writes']) or y['writes'] & (x['reads']|x['writes']):raise ValueError('EFFECT_CONFLICT')
 return {'events':(a,b),'footprint_bindings':(x['event'],y['event']),'manifest':manifest,'status':'synthetic-independent'}
unknown={'W':declaration('W')}
try:swap('W','V',unknown)
except ValueError as err:assert str(err)=='UNKNOWN_EFFECT_FOOTPRINT'
else:raise AssertionError('unknown accepted')
pure={'W':declaration('W'),'V':declaration('V')}
assert swap('W','V',pure)['status']=='synthetic-independent'
disjoint={'W':declaration('W',writes=('slot',)),'V':declaration('V',reads=('other',))}
assert swap('W','V',disjoint)['status']=='synthetic-independent'
for footprints,error in (({'W':declaration('W',writes=('slot',)),'V':declaration('V',reads=('slot',))},'EFFECT_CONFLICT'),({'W':declaration('W'),'V':declaration('U')},'STALE_OR_WRONG_EVENT_FOOTPRINT'),({'W':declaration('W'),'V':declaration('V',binding='stale')},'STALE_OR_WRONG_EVENT_FOOTPRINT')):
 try:swap('W','V',footprints)
 except ValueError as err:assert str(err)==error
 else:raise AssertionError('bad footprint accepted')
report={'passed':True,'unknown':'UNKNOWN_EFFECT_FOOTPRINT, fail closed','explicit_pure':'synthetic swap admitted','bound_disjoint':'synthetic swap admitted','read_write_conflict':'EFFECT_CONFLICT','wrong_event_or_stale_manifest':'STALE_OR_WRONG_EVENT_FOOTPRINT','scope':'Local synthetic declarations bound to event IDs and manifest. They do not authenticate real-world effect purity, graph actor authority, row publisher grants or analytic roles.'}
out=Path(__file__).resolve().parents[1]/'results/fail-closed-swap-footprints.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
