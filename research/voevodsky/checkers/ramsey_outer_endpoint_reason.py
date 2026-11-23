"""Direct local explanation test. When a discarded candidate has all five links absent, propagate only the smaller source rules and mismatch pins. Look for an already absent retained candidate, or a direct contradiction. Also test one-link vertex substitutions before propagation."""
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];r=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=r['address_masks'];E={tuple(e):i for i,e in enumerate(r['edge_order'])};idx=[i for i,a in enumerate(S) if a!=66];Q=S.index(60);bad=set();cs=[];groups=[];slots=lambda J:{E[e] for e in combinations(sorted(J),2) if e in E};mask=lambda J:sum(1<<i for i in J)
for k in range(3,7):
 for J in combinations(idx,k):
  u=0
  for j in J:u|=S[j]
  ls=slots(J);m=mask(J)
  if k==3 and len(ls)==3:cs.append((J,ls,0))
  if u.bit_count()<k:
   if not any(m^(1<<j) in bad for j in J):cs.append((J,ls,1))
   bad.add(m)
for J in combinations([i for i in idx if S[i] not in (60,65)],6):
 K=(*J,Q)
 if any(mask(z) in bad for k in (5,6) for z in combinations(K,k)):continue
 ls=slots(J)
 if len(ls)<=5:groups.append((J,ls))
import sys
small_mode='--small' in sys.argv;out=[];exact=[]
if '--replacement' in sys.argv:
 import z3
 assert small_mode;v=[z3.Bool('x%d'%i) for i in E.values()];solver=z3.SolverFor('QF_FD');solver.add([z3.Or(*[v[i] if x else ~v[i] for i in links]) for _,links,x in cs])
for b,pin in enumerate([74,4]):
 ends=sorted(next(k for k,v in E.items() if v==pin),key=lambda i:bool(S[i]&~60));lost=[];keep=[]
 for J,ls in groups:
  if pin in ls:continue
  if len(ls)<5:
   omit=small_mode and ((len(ls)==3 and ends[1] in J) or (len(ls)==4 and ends[0] in J));(lost if omit else keep).append((J,ls));continue
  iso,=[i for i in J if all(i==k or S[i]&S[k] for k in J)];t=tuple((S[iso]&S[j]).bit_count() for j in ends)
  if t==(0,2) and not small_mode:lost.append((J,ls))
  if t in [(1,0),(2,0),(0,1)]:keep.append((J,ls))
 assert (len(lost),len(keep))==((17,106) if small_mode else (4,123))
 for J,ls in lost:
  val={i:0 for i in ls};val.update({4:b,74:1-b});trace=[];reason=None
  while not reason:
   known={i for i,x in val.items() if not x};other=next(((K,links) for K,links in keep if links<=known),None)
   if other:reason={'retained_six':other[0]};break
   for K,links,x in cs:
    if any(val.get(i)==x for i in links):continue
    left=links-val.keys()
    if not left:reason={'conflict':K};break
    if len(left)==1:i,=left;val[i]=x;trace.append((K,i,x));break
   else:break
  split=None
  if not reason:
   def terminal(state):
    steps=[]
    while True:
     z={i for i,x in state.items() if not x};replacement=next((K for K,links in keep if links<=z),None)
     if replacement:return dict(replacement=replacement,steps=steps)
     for K,links,x in cs:
      if any(state.get(i)==x for i in links):continue
      left=links-state.keys()
      if not left:return dict(conflict=K,steps=steps)
      if len(left)==1:i,=left;state[i]=x;steps.append((K,i,x));break
     else:return None
   for i in sorted(set(E.values())-val.keys()):
    branches=[terminal({**val,i:x}) for x in (0,1)]
    if all(branches):split=dict(slot=i,branches=branches);break
  if '--replacement' in sys.argv and reason is None and split is None:
   solver.push();solver.add(v[4]==bool(b),v[74]!=bool(b),*[~v[i] for i in ls]);pool=list(range(len(keep)));models=[]
   while True:
    st=solver.check();assert st in (z3.sat,z3.unsat)
    if st==z3.unsat:break
    mod=solver.model();w=sum(1<<i for i,z in enumerate(v) if z3.is_true(mod.eval(z,model_completion=True)));models.append(w);pool=[k for k in pool if not any((w>>j)&1 for j in keep[k][1])];
    if not pool:break
    solver.add(z3.Or(*[v[j] for j in {j for k in pool for j in keep[k][1]}]))
   solver.pop();status='impossible' if not models else 'fixed' if pool else 'adaptive';exact.append(dict(slot4=b,discarded=J,status=status,fixed=[keep[k][0] for k in pool] if models else [],models=models))
   if '--binary' in sys.argv:
    assert status=='adaptive';solver.push();solver.add(v[4]==bool(b),v[74]!=bool(b),*[~v[i] for i in ls]);masks=[sum(1<<j for j in links) for _,links in keep];readable=sorted(set().union(*(slots(pair) for pair in combinations(idx,2)))-ls-{4,74});rule=None
    for i in readable:
     leaves=[]
     for x in (0,1):
      solver.push();solver.add(v[i]==bool(x));witness=None
      while True:
       candidates=[k for k,m in enumerate(masks) if all(not(w&m) for w in models if (w>>i)&1==x)]
       if not candidates:break
       k=candidates[0];st=solver.check(z3.Or(*[v[j] for j in keep[k][1]]));assert st in (z3.sat,z3.unsat)
       if st==z3.unsat:witness=keep[k][0];break
       mod=solver.model();models.append(sum(1<<j for j,z in enumerate(v) if z3.is_true(mod.eval(z,model_completion=True))))
      solver.pop()
      if witness is None:break
      leaves.append(witness)
     if len(leaves)==2:rule=dict(slot=i,if_zero=leaves[0],if_one=leaves[1]);break
    exact[-1]['binary_rule']=rule
    if '--two' in sys.argv:
     assert rule is None
     def tree(path,depth):
      rows=[w for w in models if all((w>>j)&1==x for j,x in path)]
      for k,m in enumerate(masks):
       if any(w&m for w in rows):continue
       assumptions=[v[j] if x else ~v[j] for j,x in path];st=solver.check(*assumptions,z3.Or(*[v[j] for j in keep[k][1]]));assert st in (z3.sat,z3.unsat)
       if st==z3.unsat:return dict(six=keep[k][0])
       mod=solver.model();w=sum(1<<j for j,z in enumerate(v) if z3.is_true(mod.eval(z,model_completion=True)));rows.append(w);models.append(w)
      if depth:
       for j in readable:
        if any(i==j for i,_ in path):continue
        left=tree(path+[(j,0)],depth-1)
        if left is not None:
         right=tree(path+[(j,1)],depth-1)
         if right is not None:return dict(slot=j,zero=left,one=right)
      return None
     # Bitsets of sampled models prune impossible trees before exact leaf checks.
     def possible(path,d):
      rows=[w for w in models if all((w>>j)&1==x for j,x in path)];a=(1<<len(rows))-1
      hits=[sum(1<<t for t,w in enumerate(rows) if w&m) for m in masks];cols=[sum(1<<t for t,w in enumerate(rows) if (w>>j)&1) for j in readable]
      def ok(ids,n):return any(not ids&h for h in hits) or (n and any(ok(ids&c,n-1) and ok(ids&~c,n-1) for c in cols if ids&c and ids&~c))
      return ok(a,d)
     root=None
     for j in readable:
      paths=[[(j,x)] for x in (0,1)]
      if not all(possible(p,1) for p in paths):continue
      left=tree(paths[0],1)
      if left is not None:
       right=tree(paths[1],1)
       if right is not None:root=dict(slot=j,zero=left,one=right);break
     exact[-1]['two_rule']=root;print('two',b,sorted(ls),bool(root),flush=True)
    solver.pop();print('binary',b,sorted(ls),rule,flush=True)
  out.append(dict(b=b,discarded=J,slots=sorted(ls),trace=trace,reason=reason,split=split));print(b,sorted(ls),len(trace),reason,split and split['slot'])
if exact:
 from collections import Counter
 print(Counter((e['slot4'],e['status']) for e in exact));(D/'results'/('ramsey_two_replacement.json' if '--two' in sys.argv else 'ramsey_binary_replacement.json' if '--binary' in sys.argv else 'ramsey_small_fixed_replacement.json')).write_text(json.dumps(exact,indent=2)+'\n')
(D/'results'/('ramsey_small_endpoint_reason.json' if small_mode else 'ramsey_outer_endpoint_reason.json')).write_text(json.dumps(out,indent=2)+'\n')
