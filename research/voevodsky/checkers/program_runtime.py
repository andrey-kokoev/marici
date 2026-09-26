"""Supported single-threaded facade; internal nets remain research machinery."""
from scanning_set_program import ScanningSetProgram
from program_preflight import preflight

class AdmissionRejected(ValueError):
 """A conservative logical estimate exceeds an explicit caller limit."""
 def __init__(self,quantity,estimate,limit):
  self.quantity=quantity;self.estimate=estimate;self.limit=limit
  super().__init__(f'{quantity} estimate {estimate} exceeds limit {limit}')

class ProgramRuntime:
 __slots__=('__net',)
 def __init__(self,bits,program,*,limits=None):
  if not __debug__:raise RuntimeError('Runtime requires assertions enabled (no -O).')
  allowed={'constructor_peak_agents','constructor_agent_allocations','rewrite_bound','peak_agent_bound','total_fresh_name_bound'}
  limits={} if limits is None else dict(limits)
  for name,value in limits.items():
   if name not in allowed:raise ValueError('unknown logical resource limit')
   if type(value) is not int or value<0:raise ValueError('limits must be nonnegative exact integers')
  plan=preflight(bits,program)
  for name,value in limits.items():
   estimate=getattr(plan,name)
   if estimate>value:raise AdmissionRejected(name,estimate,value)
  self.__net=ScanningSetProgram(plan.bits,plan.instructions)
 def observe(self):
  return self.__net.observe()
 def advance(self,max_steps=1):
  """Execute at most max_steps local rewrites; return actual count.

  Deterministic first-enabled scheduling. Budget exhaustion is not completion.
  """
  if type(max_steps) is not int or max_steps<0:raise ValueError('max_steps must be a nonnegative exact integer')
  count=0
  while count<max_steps:
   enabled=self.__net.enabled()
   if not enabled:
    if not self.__net.observe()['complete']:raise RuntimeError('Incomplete net has no enabled rewrite')
    break
   self.__net.step(enabled[0]);count+=1
  return count
