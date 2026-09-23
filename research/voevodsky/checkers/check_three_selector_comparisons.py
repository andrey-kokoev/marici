"""Additive signed comparisons forget selector-path middle evidence."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
A=((Q(0),Q(1),Q(0),Q(1)),Q(1));B=((Q(1),Q(2),Q(0),Q(1)),Q(0));C=((Q(0),Q(1),Q(1),Q(2)),Q(0))
def delta(x,y):return tuple(y[0][i]-x[0][i] for i in range(4))+(y[1]-x[1],)
def packet_id(p):return sha256(repr(p).encode()).hexdigest()[:16]
def edge(x,y,source,target):return {'source_selector':source,'target_selector':target,'source_packet':packet_id(x),'target_packet':packet_id(y),'delta':delta(x,y)}
ab=edge(A,B,'sA','sB');bc=edge(B,C,'sB','sC');ac=edge(A,C,'sA','sC')
assert tuple(ab['delta'][i]+bc['delta'][i] for i in range(5))==ac['delta']
assert ab['target_packet']==bc['source_packet']
def compose(e,f):
 if (e['target_selector'],e['target_packet'])!=(f['source_selector'],f['source_packet']):raise ValueError('MIDDLE_CERTIFICATE_MISMATCH')
 return tuple(e['delta'][i]+f['delta'][i] for i in range(5))
assert compose(ab,bc)==ac['delta']
# Equal endpoint delta does not make these TWO selector paths the same history.
via_B=(ab,bc);via_C=(ac,edge(C,C,'sC','sC'))
assert via_B!=via_C and compose(*via_B)==compose(*via_C)
try:compose(ab,edge(C,C,'sB','sC'))
except ValueError as err:assert str(err)=='MIDDLE_CERTIFICATE_MISMATCH'
else:raise AssertionError('mismatched intermediate packet allowed')
report={'passed':True,'ab_delta':list(map(str,ab['delta'])),'bc_delta':list(map(str,bc['delta'])),'ac_delta':list(map(str,ac['delta'])),'additive_telescope':True,'two_distinct_paths_same_endpoint_delta':True,'intermediate_packet_mismatch_refused':True,'scope':'Frozen old-square signed packet comparisons with selector IDs, not equality of proof histories, existing 2-cell authority or analytic role assignment.'}
out=Path(__file__).resolve().parents[1]/'results/three-selector-comparisons.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
