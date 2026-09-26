"""Finite provenance-typed effect table for the fifteen active-pair rules.

ORIGINAL is an internal construction tag, not a source-owner credential.
The table records consumed and created B/N/K agents per local template.
"""
from pathlib import Path
import json

rules={
 ('COPY','B0'):(1,2),('COPY','B1'):(1,2),('COPY','N'):(1,2),
 ('Q_B','K'):(0,0),('Q_B','N'):(0,0),
 ('Q_S','B0'):(0,0),('Q_S','B1'):(0,0),('Q_S','N'):(0,0),
 ('Q_R','B0'):(0,0),('Q_R','B1'):(0,0),('Q_R','N'):(0,0),
 ('E','B0'):(0,0),('E','B1'):(0,0),('E','K'):(0,0),('E','N'):(0,0),
}
# Pair = (consumed ORIGINAL count, created COPIED B/N count).
# Every non-COPY rule consumes one COPIED B/N/K and creates no B/N/K.
assert len(rules)==15
checks=0
for pair,(consumed_original,created_copied) in rules.items():
 family,head=pair
 assert head in ('B0','B1','N','K')
 if family=='COPY':
  assert head!='K' and consumed_original==1 and created_copied==2
 else:
  assert consumed_original==0 and created_copied==0
 for originals in range(consumed_original,8):
  for copies in range(1 if family!='COPY' else 0,8):
   # A COPY rewrite may create copied nodes but decreases the first
   # coordinate. Other rules decrease the second without changing first.
   after=(originals-consumed_original,copies+created_copied-(family!='COPY'))
   assert after<(originals,copies)
   checks+=1

def permitted(family,head,tag):
 if (family,head) not in rules:return False
 return tag==('ORIGINAL' if family=='COPY' else 'COPIED')
assert all(permitted(*pair,'ORIGINAL') for pair in rules if pair[0]=='COPY')
assert all(permitted(*pair,'COPIED') for pair in rules if pair[0]!='COPY')
assert not permitted('E','B0','ORIGINAL')
assert not permitted('Q_R','N','ORIGINAL')
assert not permitted('COPY','B1','COPIED')
report={'passed':True,'typed_rules':len(rules),'symbolic_rank_checks':checks,'provenance_effect':'COPY consumes one ORIGINAL head and creates two COPIED heads; Q/E consumes one COPIED head and creates no B/N/K','rejected':'E/Q on ORIGINAL or COPY on COPIED','scope':'Internal effect-table argument conditional on reachable ownership and accurate operational rule mapping; does not prove complete shape grammar or real row issuer authority.'}
out=Path(__file__).resolve().parents[1]/'results/symbolic-original-copy-rule-types.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
