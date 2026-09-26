from scanning_set_program import ScanningSetProgram
from conditional_set_program import ConditionalSetProgram
from strict_set_program import StrictSetProgram
from fuel_scanner import FuelScanner
checks=0
for cls in (StrictSetProgram,ConditionalSetProgram,ScanningSetProgram):
 for bits,program in [([2],[]),([True],[]),([0.0],[]),([], [('add',True)]),([], [('member',-1)]),([], [('union',[1,2])]),([], [('bad',0)]),([], [('add',0,1)])]:
  obj=cls.__new__(cls)
  try:cls.__init__(obj,bits,program)
  except (ValueError,TypeError):pass
  else:raise RuntimeError('invalid input accepted')
  if hasattr(obj,'types'):raise RuntimeError('allocated before rejection')
  checks+=1
for cls,op,args in [(ConditionalSetProgram,'ifadd',(0,1)),(ScanningSetProgram,'scan',(0,1,2)),(ScanningSetProgram,'ifadd',(0,-1,2))]:
 obj=cls.__new__(cls)
 try:cls.__init__(obj,(),[(op,args)])
 except ValueError:pass
 else:raise RuntimeError('bad arity/value accepted')
 if hasattr(obj,'types'):raise RuntimeError('allocated before rejection')
 checks+=1
for bits,c,f in [([2],0,1),([],True,1),([],0,-1)]:
 obj=FuelScanner.__new__(FuelScanner)
 try:FuelScanner.__init__(obj,bits,c,f)
 except ValueError:pass
 else:raise RuntimeError('invalid scanner input')
 if hasattr(obj,'types'):raise RuntimeError('allocated before rejection')
 checks+=1
net=ScanningSetProgram(iter([0]),iter([('union',iter([0,1])),('scan',iter([0,1]))]))
while net.enabled():net.step(net.enabled()[0])
if net.observe()['word']!=(1,1):raise RuntimeError('one-shot input changed semantics')
print({'passed':True,'invalid_cases':checks,'one_shot_iterables':True})
