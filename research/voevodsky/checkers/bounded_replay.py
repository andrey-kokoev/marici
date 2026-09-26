"""Opt-in bounded file intake, not a process memory/time sandbox."""
import json
from program_preflight import preflight
from semantic_replay import semantic_replay

def audit_file(path,*,max_bytes,max_certificates,max_unary,max_rewrites):
 for value in (max_bytes,max_certificates,max_unary,max_rewrites):
  if type(value) is not int or value<0:raise ValueError('limits must be nonnegative exact integers')
 with open(path,'rb') as stream:data=stream.read(max_bytes+1)
 if len(data)>max_bytes:raise ValueError('byte limit exceeded')
 def unique(pairs):
  obj={}
  for k,v in pairs:
   if k in obj:raise ValueError('duplicate JSON key')
   obj[k]=v
  return obj
 def nonfinite(value):raise ValueError('nonfinite JSON number')
 trace=json.loads(data,object_pairs_hook=unique,parse_constant=nonfinite)
 if not isinstance(trace,dict) or not isinstance(trace.get('steps'),list):raise ValueError('invalid trace envelope')
 if len(trace['steps'])>max_certificates:raise ValueError('certificate limit exceeded')
 decl=trace.get('declaration')
 if not isinstance(decl,dict) or set(decl)!={'bits','program'}:raise ValueError('invalid declaration')
 # Normalization does not expand unary operands; source bytes already bounded.
 plan=preflight(decl['bits'],decl['program'])
 for op,arg in plan.instructions:
  values=() if op=='union' else arg if op in ('scan','ifadd') else (arg,)
  if any(x>max_unary for x in values):raise ValueError('unary limit exceeded')
 if plan.rewrite_bound>max_rewrites:raise ValueError('estimated rewrite limit exceeded')
 return semantic_replay(trace)
