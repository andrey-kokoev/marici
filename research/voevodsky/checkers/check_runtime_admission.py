from program_runtime import ProgramRuntime,AdmissionRejected
from program_preflight import preflight
from unittest.mock import patch
import json
from pathlib import Path
ops=[('scan',(0,2)),('ifadd',(0,1,2))];plan=preflight((),ops)
quantities=['constructor_peak_agents','constructor_agent_allocations','rewrite_bound','peak_agent_bound','total_fresh_name_bound']
for name in quantities:
 estimate=getattr(plan,name)
 with patch('program_runtime.ScanningSetProgram',side_effect=AssertionError('graph construction attempted')):
  try:ProgramRuntime((),ops,limits={name:estimate-1})
  except AdmissionRejected as e:assert (e.quantity,e.estimate,e.limit)==(name,estimate,estimate-1)
  else:raise AssertionError('limit ignored')
 runtime=ProgramRuntime((),ops,limits={name:estimate})
 while not runtime.observe()['complete']:runtime.advance(20)
 assert runtime.observe()['word']==(1,1)
for limits in ({'bad':1},{'rewrite_bound':True},{'rewrite_bound':-1},{'rewrite_bound':1.0}):
 with patch('program_runtime.preflight',side_effect=AssertionError('input consumed')):
  try:ProgramRuntime((),(),limits=limits)
  except ValueError:pass
  else:raise AssertionError('invalid limits accepted')
with patch('program_runtime.ScanningSetProgram',side_effect=AssertionError('huge graph allocated')):
 try:ProgramRuntime((),[('scan',(10**12,10**12))],limits={'constructor_peak_agents':100})
 except AdmissionRejected:pass
 else:raise AssertionError('huge program accepted')
net=ProgramRuntime(iter([]),iter([('union',iter([0,1]))]),limits={'constructor_peak_agents':8})
net.advance(100);assert net.observe()['word']==(0,1)
report={'passed':True,'threshold_pairs':5,'invalid_policies':4,'huge_scalar_rejected_before_graph':True,'scope':'Logical admission after finite normalization, not memory/time sandbox.'}
p=Path(__file__).resolve().parents[1]/'results/runtime-admission.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
