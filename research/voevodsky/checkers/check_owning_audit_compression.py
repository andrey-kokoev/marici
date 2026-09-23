"""Owning dictionary elimination and certified sequential redundancy removal."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import sys,json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
sys.path.insert(0,str(ROOT/'research/grothendieck/checkers'))
from joint_audit_tail_interface import JointAuditModel
from check_certified_linear_audit_elimination import eliminate
from check_schema_relative_tail_lp import solve

def main():
 packets=[]
 for m in (3,4,8):
  model=JointAuditModel(m,[0]);rows=[tuple(a)+(b,) for _,(a,b) in model.cuts()]
  frames=[(Q(1),Q(0),Q(-1),Q(0)),(Q(-1),Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1),Q(1))]
  rows+=frames;summary=eliminate(rows);projected=[tuple(map(Q,item['row'])) for item in summary]
  active=list(range(len(projected)));removals=[]
  for i in list(active):
   a,b,rhs=projected[i];found=None
   if a==b==0 and rhs>=0:found=[]
   for k in (1,2):
    if found is not None:break
    for inds in combinations([j for j in active if j!=i],k):
     w=solve([projected[j][:2] for j in inds],(a,b))
     if w is not None and min(w)>=0 and sum(v*projected[j][2] for j,v in zip(inds,w))<=rhs:
      found=[[j,str(v)] for j,v in zip(inds,w)];break
   if found is not None:active.remove(i);removals.append({'removed':i,'weights':found})
  retained=[summary[i]['row'] for i in active]
  enc=lambda x:len(json.dumps(x,separators=(',',':')).encode())
  packet={'m':m,'original':[[str(v) for v in r] for r in rows],'summary':summary,'removals':removals,'retained_indices':active}
  packet['cost']={'original_evidence_bytes':enc([[str(v) for v in r] for r in frames]),
   'materialized_source_and_evidence_bytes':enc(packet['original']),
   'retained_summary_bytes':enc(retained),'migration_packet_bytes':enc(packet),
   'projected_rows':len(summary),'retained_rows':len(active)}
  packets.append(packet)
 (OUT/'owning-audit-compression.json').write_text(json.dumps({'packets':packets},indent=2)+'\n')
 print(json.dumps([{'m':p['m'],**p['cost']} for p in packets],indent=2))
if __name__=='__main__':main()
