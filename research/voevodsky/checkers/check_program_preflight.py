from program_preflight import preflight
from scanning_set_program import ScanningSetProgram
from itertools import product
from pathlib import Path
import json
runs=0
alphabet=[('member',2),('add',3),('union',(0,1)),('ifadd',(1,0,3)),('scan',(1,3)),('scan',(0,0))]
for length in range(4):
 for instructions in product(alphabet,repeat=length):
  for bits in ((),(0,),(1,0)):
   plan=preflight(bits,instructions);net=ScanningSetProgram(plan.bits,plan.instructions)
   assert len(net.types)==plan.initial_agents
   start=net.serial;peak=len(net.types)
   while net.enabled():net.step(net.enabled()[0]);peak=max(peak,len(net.types))
   assert net.steps<=plan.rewrite_bound and peak<=plan.peak_agent_bound
   assert net.serial-start<=plan.runtime_fresh_name_bound
   assert len(net.retained())<=plan.final_word_length_bound;runs+=1
plan=preflight(iter([0]),iter([('union',iter([0,1])),('scan',iter([0,2]))]))
assert plan.instructions==( ('union',(0,1)),('scan',(0,2)) )
# Huge scalar operands must stay scalar: no unary graph is constructed here.
huge=preflight((),[('scan',(10**12,10**12))])
assert huge.initial_agents==2*10**12+8
report={'passed':True,'bounded_runs':runs,'huge_scalar_preflight':True,'scope':'Estimate dominance on bounded runs, exact postcompile initial-node count, reusable one-shot normalization; not resource enforcement.'}
p=Path(__file__).resolve().parents[1]/'results/program-preflight.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
