"""Independent snapshot-based port replacement reference, not rule semantics."""
from collections import Counter

def require(ok,message):
 if not ok:raise ValueError(message)

def validate(types,wires):
 ports=set()
 for n,ps in types.items():
  require(isinstance(n,str) and '.' not in n,'invalid agent name')
  require(len(ps)==len(set(ps)),'duplicate port')
  require(all(isinstance(p,str) and '.' not in p for p in ps),'invalid port name')
  ports.update(n+'.'+p for p in ps)
 require(set(wires)==ports,'wire domain mismatch')
 require(all(p!=q and q in ports and wires.get(q)==p for p,q in wires.items()),'not a matching')

def replace(types,wires,names,edges,new,*,protected=()):
 """Return new dictionaries without mutating input, including on rejection.

 Fresh means disjoint from all live names here, not allocator-history recovery.
 Kinds/rule legality are a separate certificate layer.
 """
 validate(types,wires)
 names=tuple(names);new=tuple((n,tuple(ps)) for n,ps in new);edges=tuple(tuple(e) for e in edges)
 require(len(names)==2 and len(set(names))==2 and all(n in types for n in names),'invalid removed pair')
 old=set(names);require(not old&set(protected),'protected root removal')
 require(all('p' in types[n] for n in names) and wires[names[0]+'.p']==names[1]+'.p','not principal paired')
 fresh_names=[n for n,ps in new]
 require(len(fresh_names)==len(set(fresh_names)) and not set(fresh_names)&set(types),'fresh name collision')
 removed={n+'.'+p for n in names for p in types[n]}
 exposed={p:wires[p] for p in removed if wires[p] not in removed}
 fresh={n+'.'+p for n,ps in new for p in ps}
 require(all(len(e)==2 for e in edges),'invalid edge arity')
 require(Counter(p for e in edges for p in e)==Counter(set(exposed)|fresh),'slot multiplicity')
 result_types={n:tuple(ps) for n,ps in types.items() if n not in old}
 result_types.update(new)
 result_wires={p:q for p,q in wires.items() if p not in removed and q not in removed}
 for a,b in edges:
  a=exposed.get(a,a);b=exposed.get(b,b)
  require(a!=b and a not in result_wires and b not in result_wires,'invalid reconnection')
  result_wires[a]=b;result_wires[b]=a
 validate(result_types,result_wires)
 return result_types,result_wires
