"""Measure logical graph resources, not Python heap bytes or wall-time bounds."""
from scanning_set_program import ScanningSetProgram
from pathlib import Path
import json
profiles=[]
for fuel in (0,8,32,64):
 for cursor in (0,16):
  net=ScanningSetProgram((),[('scan',(cursor,fuel)),('member',cursor),('ifadd',(cursor,1,2)),('union',(0,1))])
  initial=len(net.types);serial=net.serial;peak=initial
  while net.enabled():
   before=len(net.types);old_serial=net.serial;net.step(net.enabled()[0])
   assert len(net.types)<=before+2 and net.serial<=old_serial+4
   assert len(net.types)<=initial+2*net.steps and net.serial<=serial+4*net.steps
   peak=max(peak,len(net.types))
  assert net.observe()['complete']
  profiles.append({'cursor':cursor,'fuel':fuel,'initial_agents':initial,'peak_agents':peak,'final_agents':len(net.types),'rewrites':net.steps,'fresh_names_during_execution':net.serial-serial,'agent_bound':initial+2*net.steps,'allocation_bound':4*net.steps})
report={'passed':True,'profiles':profiles,'scope':'Logical agent/fresh-name counts for eight mixed runs; universal per-rule envelope separately checked by signature audit. Not heap-byte or resource-enforcement guarantee.'}
p=Path(__file__).resolve().parents[1]/'results/runtime-resources.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
