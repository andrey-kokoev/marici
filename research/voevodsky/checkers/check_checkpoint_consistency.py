"""Conditional cross-observation hash-chain consistency, rollback and gaps."""
from hashlib import sha256
from pathlib import Path
import json
encode=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def block(seq,parent,tag):
 body={'sequence':seq,'parent':parent,'tag':tag}
 return {'body':body,'digest':sha256(encode(body)).hexdigest()}
g=block(0,'genesis','root');h1=block(1,g['digest'],'prepared')
a2=block(2,h1['digest'],'rows-A');b2=block(2,h1['digest'],'rows-B')
a3=block(3,a2['digest'],'audit-A');b3=block(3,b2['digest'],'audit-B')
def consistent(old_head,later_head,witness):
 if later_head['body']['sequence']<old_head['body']['sequence']:return 'ROLLBACK'
 if later_head['body']['sequence']==old_head['body']['sequence']:
  return 'SAME_HEAD' if later_head['digest']==old_head['digest'] else 'SAME_SEQUENCE_FORK'
 chain=[old_head]+list(witness)+[later_head]
 if [b['body']['sequence'] for b in chain]!=list(range(old_head['body']['sequence'],later_head['body']['sequence']+1)):return 'MISSING_INTERMEDIATE_WITNESS'
 for left,right in zip(chain,chain[1:]):
  if right['body']['parent']!=left['digest'] or right['digest']!=sha256(encode(right['body'])).hexdigest():return 'INCONSISTENT_EXTENSION'
 return 'CONDITIONAL_CONSISTENT_EXTENSION'
assert consistent(a2,a3,[])=='CONDITIONAL_CONSISTENT_EXTENSION'
assert consistent(a2,b3,[])=='INCONSISTENT_EXTENSION'
assert consistent(a2,h1,[])=='ROLLBACK'
assert consistent(h1,a3,[])=='MISSING_INTERMEDIATE_WITNESS'
assert consistent(h1,a3,[a2])=='CONDITIONAL_CONSISTENT_EXTENSION'
assert consistent(h1,b3,[b2])=='CONDITIONAL_CONSISTENT_EXTENSION'
assert consistent(a2,b2,[])=='SAME_SEQUENCE_FORK'
report={'passed':True,'honest_extension':'CONDITIONAL_CONSISTENT_EXTENSION','rollback_refused':True,'fork_after_pinned_old_head_refused':True,'missing_intermediate_refused':True,'older_head_at_sequence_one_allows_both_later_forks':True,'noncertification':'Observed heads and witnesses are conditional inputs. Hash linkage cannot authenticate checkpoint origin or exclude unseen forked log heads.'}
out=Path(__file__).resolve().parents[1]/'results/checkpoint-consistency.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
