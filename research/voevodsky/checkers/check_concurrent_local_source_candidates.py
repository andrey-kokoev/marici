"""Pure in-memory CAS admits one old-generation source candidate at a time."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
base=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
a=base[:3]+(((0,1),2),)
b=base[:1]+(((1,0),2),)+base[2:]
ab=b[:3]+(((0,1),2),)
def H(rows):return sha256(repr(rows).encode()).hexdigest()
def proof(rows):
 # x-upper multiplier1, exact target x<=2, with required surplus.
 upper=Q(rows[1][1]);c=Q(2)-upper
 assert c>=0 and rows[1][0]==(1,0)
 return ((Q(0),Q(1),Q(0),Q(0)),c)
for rows in (a,b,ab):assert proof(rows)[1]>=0
store={'version':1,'rows':base,'ids':set()}
def cas(current,expected_version,expected_digest,rows,candidate_id):
 if candidate_id in current['ids']:return current,'IDEMPOTENT_NO_CHANGE'
 if current['version']!=expected_version or H(current['rows'])!=expected_digest:return current,'STALE_CANDIDATE_REVALIDATION_REQUIRED'
 proof(rows)
 return {'version':current['version']+1,'rows':rows,'ids':current['ids']|{candidate_id}},'LOCAL_MATH_CAS_COMMITTED_NO_AUTHORITY'
snapshot=(store['version'],H(store['rows']))
winner,status=cas(store,*snapshot,a,'A')
assert status=='LOCAL_MATH_CAS_COMMITTED_NO_AUTHORITY'
loser,status=cas(winner,*snapshot,b,'B')
assert loser is winner and status=='STALE_CANDIDATE_REVALIDATION_REQUIRED'
rebased,status=cas(winner,winner['version'],H(winner['rows']),ab,'B-rebased')
assert status=='LOCAL_MATH_CAS_COMMITTED_NO_AUTHORITY' and rebased['version']==3
assert store['version']==1 and winner['version']==2 and H(rebased['rows'])!=H(b)
assert cas(rebased,rebased['version'],H(rebased['rows']),ab,'B-rebased')[1]=='IDEMPOTENT_NO_CHANGE'
report={'passed':True,'two_old_version_candidates':'A y-upper2 and B x-upper2 both locally validate alone','first_winner':'A version2','loser':'B stale; no last writer wins','rebased_combined':'A+B version3 after new proof/surplus revalidation','unchanged_old_version':1,'authorization':'NONE; all versions in memory only','scope':'Local compare-and-swap illustration, not persistent source edit, actual concurrency implementation, issuer grant or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/concurrent-local-source-candidates.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
