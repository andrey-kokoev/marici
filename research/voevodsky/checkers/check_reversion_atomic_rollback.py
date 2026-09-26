"""Do not commit a staged g3 reversion until all packets and edges validate."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
rows2=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),2))
rows3=rows2[:3]+(((0,1),1),)
state={'generation':2,'rows':rows2,'packet_ids':('P-g2','Q-g2'),'edges':('E-g2',)}
H=lambda x:sha256(repr(x).encode()).hexdigest()
old=deepcopy(state);old_digest=H(state)
def stage(current,q_surplus,edge_generation):
 p_ok=1+1==2
 q_ok=2+q_surplus==2
 e_ok=edge_generation==3 and p_ok and q_ok
 if not (p_ok and q_ok and e_ok):return current,'ROLLBACK_WHOLE_CANDIDATE'
 return {'generation':3,'rows':rows3,'packet_ids':('P-g3','Q-g3'),'edges':('E-g3',)},'LOCAL_CANDIDATE_ONLY'
rejected,status=stage(state,-1,3)
assert status=='ROLLBACK_WHOLE_CANDIDATE' and rejected is state and H(state)==old_digest
rejected,status=stage(state,0,2)
assert status=='ROLLBACK_WHOLE_CANDIDATE' and rejected is state and H(state)==old_digest
accepted,status=stage(state,0,3)
assert status=='LOCAL_CANDIDATE_ONLY' and accepted['generation']==3 and state==old and H(state)==old_digest
report={'passed':True,'invalid_Q_or_stale_edge':'whole candidate rolled back; g2 source and catalogue unchanged','complete_candidate':'fresh g3 in-memory state, old g2 preserved','scope':'Illustrative atomicity only; simplified packet arithmetic, no actual source mutation, observed edge, owner grant or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/reversion-atomic-rollback.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
