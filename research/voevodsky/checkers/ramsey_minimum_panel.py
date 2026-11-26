"""Counterexample-guided exact hitting set for one fixed panel. A countermodel flips exactly one marked color, leaving the others as read. Each such model gives a necessary hitting clause. Lower bound from optimal hitting set, upper from UNSAT against every such model."""
import json,time
from pysat.solvers import Solver
from pysat.formula import WCNF
from pysat.examples.rc2 import RC2

def run(idx,E,V,cs,spec,inputs,erasures=1):
 from itertools import combinations
 g=list(spec);ix={v:i+1 for i,v in enumerate(g)};bad=[V[e] for e in E];cs=cs+[bad]+[[-i for i in t] for t in combinations(bad,erasures+1)];cuts=[];wit=[];start=time.monotonic();lb=3
 with Solver(name='g4',bootstrap_with=cs) as sl:
  assert not sl.solve(assumptions=g);ub=sl.get_core()
  for v in ub.copy():
   if not sl.solve(assumptions=[t for t in ub if t!=v]):ub.remove(v)
  while lb<len(ub) and time.monotonic()-start<52:
   w=WCNF();w.extend(cuts)
   for t in g:w.append([-ix[t]],weight=1)
   with RC2(w) as opt:m=opt.compute();lb=max(lb,opt.cost)
   if lb>=len(ub):break
   sel=[t for t in g if ix[t] in m];
   if not sl.solve(assumptions=sel):ub=sel;lb=len(ub);break
   def agree():
    pos=set(sl.get_model());return {t for t in g if sum(i in pos for i in inputs[t])==spec[t][-1]},pos
   good,pos=agree()
   for t in g:
    if t not in good and sl.solve(assumptions=[*good,t]):good,pos=agree()
   cuts.append([ix[t] for t in g if t not in good]);wit.append([e for e,v in V.items() if v in pos]);
  assert not sl.solve(assumptions=ub)
 out=dict(core=idx,lower=lb,upper=len(ub),panel=[spec[t] for t in ub],countermodels=wit);print(idx,lb,len(ub),len(cuts),out['panel'],flush=True);return out
