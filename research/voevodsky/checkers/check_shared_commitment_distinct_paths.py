"""Shared C occurrence commitment does not identify distinct prefix paths."""
from hashlib import sha256
from pathlib import Path
import json
ctx='square-synthetic-manifest-v1'
def H(value):return sha256(repr(value).encode()).hexdigest()
def commitment(role,id_value,salt):return H(('occurrence-v1',ctx,role,id_value,salt))
c=commitment('C','c#01','private-c-nonce')
base=('A',commitment('B','b#alpha','private-b-alpha'),c,'D')
other=('A',commitment('B','b#beta','private-b-beta'),c,'D')
assert base[2]==other[2] and base[1]!=other[1]
def prefix_hash(path):return H(('trace-prefix-v1',ctx,path[:3]))
assert prefix_hash(base)!=prefix_hash(other)
def compare_paths(x,y,require_full=False):
 if x[2]!=y[2]:raise ValueError('COMMON_COMMITMENT_MISSING')
 if prefix_hash(x)!=prefix_hash(y):
  if require_full:raise ValueError('PATH_IDENTITY_REFUSED')
  return 'SHARED_C_JOIN_ONLY'
 return 'SAME_COMMITTED_PREFIX_ONLY'
assert compare_paths(base,other)=='SHARED_C_JOIN_ONLY'
try:compare_paths(base,other,True)
except ValueError as err:assert str(err)=='PATH_IDENTITY_REFUSED'
else:raise AssertionError('shared C promoted to path identity')
assert compare_paths(base,base)=='SAME_COMMITTED_PREFIX_ONLY'
report={'passed':True,'same_C_commitment':True,'distinct_B_commitments_and_trace_prefixes':True,'cross_path_result':'SHARED_C_JOIN_ONLY','full_path_identity':'PATH_IDENTITY_REFUSED','same_committed_prefix':'not authenticated occurrence execution','scope':'Synthetic context-bound hash model, no real attested event IDs or source/effect issuer grants; digest equality not historical path identity.'}
out=Path(__file__).resolve().parents[1]/'results/shared-commitment-distinct-paths.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
