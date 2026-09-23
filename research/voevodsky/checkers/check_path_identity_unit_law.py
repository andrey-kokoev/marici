"""Identity composition preserves synthetic edge sequence without new events."""
from pathlib import Path
import json
known={'P','Q','R'}
def identity(x):
 assert x in known
 return {'start':x,'end':x,'edges':()}
def path(a,b,edges):return {'start':a,'end':b,'edges':tuple(edges)}
def compose(a,b):
 if a['end']!=b['start']:raise ValueError('COMPOSITION_MIDDLE_ID_MISMATCH')
 return path(a['start'],b['end'],a['edges']+b['edges'])
e=('P','Q','bound-weakening@1');p=path('P','Q',(e,))
assert compose(identity('P'),p)==p and compose(p,identity('Q'))==p
assert len(compose(identity('P'),p)['edges'])==1
try:compose(identity('R'),p)
except ValueError as err:assert str(err)=='COMPOSITION_MIDDLE_ID_MISMATCH'
else:raise AssertionError('wrong start identity')
try:compose(p,identity('R'))
except ValueError as err:assert str(err)=='COMPOSITION_MIDDLE_ID_MISMATCH'
else:raise AssertionError('wrong end identity')
report={'passed':True,'left_and_right_units':'retain exact one-edge tuple and P/Q endpoints','wrong_middle_identity':'COMPOSITION_MIDDLE_ID_MISMATCH','scope':'Synthetic path algebra only, no observed occurrence, Farkas proof, issuer or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/path-identity-unit-law.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
