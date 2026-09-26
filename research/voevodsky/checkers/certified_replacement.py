"""Typed/freshness boundary over the pure evaluator; not rule-template proof."""
from pure_replacement import replace,require

def identity(name):
 if name in ('RET','ACK'):return name,None
 kind,separator,number=name.rpartition('_')
 require(bool(separator) and bool(kind) and number.isascii() and number.isdecimal(),'invalid allocated name')
 serial=int(number);require(serial>0 and str(serial)==number,'noncanonical serial')
 return kind,serial

def checked_replace(types,wires,names,edges,new,*,before,after,signature,allowed,protected=()):
 """The caller must trust before as historical allocator high-water.

 Signature and allowed-pair tables are explicit inputs, not authenticated rules.
 """
 require(type(before) is int and type(after) is int and 0<=before<=after,'invalid high-water witness')
 new=tuple((n,tuple(ps)) for n,ps in new);names=tuple(names)
 serials=[]
 for n,ps in types.items():
  kind,serial=identity(n)
  require(kind in signature and set(ps)==set(signature[kind]) and len(ps)==len(set(ps)),'old signature mismatch')
  if serial is not None:require(serial<=before,'live name exceeds high-water');serials.append(serial)
 require(len(serials)==len(set(serials)),'duplicate global serial')
 allocated=[]
 for n,ps in new:
  kind,serial=identity(n)
  require(serial is not None and kind in signature and set(ps)==set(signature[kind]) and len(ps)==len(set(ps)),'new signature mismatch')
  allocated.append(serial)
 require(len(allocated)==after-before and all(s==before+i+1 for i,s in enumerate(sorted(allocated))),'allocation interval mismatch')
 require(len(names)==2 and all(n in types for n in names),'missing pair')
 a,b=(identity(n)[0] for n in names)
 require(b in allowed.get(a,()),'typed pair not admitted')
 return replace(types,wires,names,edges,new,protected=protected)
