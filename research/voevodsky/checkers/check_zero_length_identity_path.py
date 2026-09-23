"""Reflexive identity is a path type, not a witnessed nonempty derivation."""
from pathlib import Path
import json
known={'fictional-P'}
def path(start,end,edges,claim):
 if claim=='identity':
  return 'STRUCTURAL_IDENTITY_NOT_OBSERVED' if start==end and not edges and start in known else 'INVALID_IDENTITY'
 if claim=='nonempty-derivation':
  if not edges:return 'MISSING_DERIVATION_EDGE'
  cursor=start
  for frm,to in edges:
   if frm!=cursor:return 'DISCONNECTED'
   cursor=to
  return 'SYNTHETIC_NONEMPTY_SHAPE' if cursor==end else 'WRONG_END'
 return 'UNKNOWN_PATH_CLAIM'
assert path('fictional-P','fictional-P',[],'identity')=='STRUCTURAL_IDENTITY_NOT_OBSERVED'
assert path('fictional-P','fictional-P',[],'nonempty-derivation')=='MISSING_DERIVATION_EDGE'
assert path('fictional-P','fictional-Q',[],'identity')=='INVALID_IDENTITY'
assert path('fictional-unobserved','fictional-unobserved',[],'identity')=='INVALID_IDENTITY'
report={'passed':True,'known_same_occurrence_empty':'structural identity only','same_occurrence_nonempty_claim':'MISSING_DERIVATION_EDGE','different_or_unknown_occurrence_identity':'rejected','scope':'Fictional known-id registry is not evidence of a real observed occurrence, issuer grant or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/zero-length-identity-path.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
