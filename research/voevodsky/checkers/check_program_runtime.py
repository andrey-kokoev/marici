from program_runtime import ProgramRuntime
from scanning_set_program import ScanningSetProgram
import subprocess
import sys
runtime=ProgramRuntime((),[('scan',(0,2)),('member',0)])
assert {x for x in dir(runtime) if not x.startswith('_')}=={'observe','advance'}
initial=runtime.observe();assert runtime.advance(0)==0 and runtime.observe()==initial
for invalid in (-1,True,1.5,None):
 try:runtime.advance(invalid)
 except ValueError:pass
 else:raise AssertionError('invalid budget accepted')
 assert runtime.observe()==initial
# Detached report mutation cannot change live state.
initial['complete']=True;assert not runtime.observe()['complete']
count=0
while not runtime.observe()['complete']:
 assert runtime.advance(1)==1;count+=1
assert runtime.observe()=={'observations':(('scan','EXHAUSTED'),('boolean',True)),'complete':True,'word':(1,1)}
assert runtime.advance(100)==0
raw=ScanningSetProgram((),[('scan',(0,2)),('member',0)])
while raw.enabled():raw.step(raw.enabled()[0])
assert raw.steps==count and raw.observe()==runtime.observe()
empty=ProgramRuntime((),[]);assert empty.advance()==0 and empty.observe()['complete']
run=subprocess.run([sys.executable,'-E','-O','-c',"from program_runtime import ProgramRuntime; ProgramRuntime((),[])"],capture_output=True,text=True)
assert run.returncode!=0 and 'Runtime requires assertions enabled' in run.stderr
print({'passed':True,'rewrites':count,'optimized_execution_rejected':True,'public_methods':['advance','observe']})
