"""Concrete snapshot codec and finite single-package Agda certificate exporter."""
from dataclasses import fields,is_dataclass
from reference import Package,Admission,Rule,Seed,Step
from local_net import Net,Agent
from port_refinement import reify,contract,compact,diagram
TYPES={c.__name__:c for c in (Package,Admission,Rule,Seed,Step,Agent)}
def encode(x):
 if is_dataclass(x):return {'type':type(x).__name__,'fields':{f.name:encode(getattr(x,f.name)) for f in fields(x)}}
 if isinstance(x,tuple):return {'tuple':[encode(y) for y in x]}
 if x is None or type(x) in (str,int):return x
 raise ValueError('unsupported certificate value')
def decode(x):
 if type(x) is dict:
  if set(x)=={'tuple'}:return tuple(decode(y) for y in x['tuple'])
  if set(x)=={'type','fields'} and x['type'] in TYPES:
   c=TYPES[x['type']]
   if set(x['fields'])!={f.name for f in fields(c)}:raise ValueError('wrong fields')
   return c(**{k:decode(v) for k,v in x['fields'].items()})
  raise ValueError('unknown record')
 if x is None or type(x) in (str,int):return x
 raise ValueError('unknown encoded value')
def snapshot(net):
 return {'agents':[[i,encode(a)] for i,a in sorted(net.agents.items())],
         'wires':[[list(p),list(q)] for p,q in sorted(net.wires.items())],'next_id':net.next_id}
def restore(data):
 if set(data)!={'agents','wires','next_id'}:raise ValueError('bad snapshot schema')
 net=Net.__new__(Net);net.agents={i:decode(a) for i,a in data['agents']};net.wires={tuple(p):tuple(q) for p,q in data['wires']};net.next_id=data['next_id']
 if len(net.agents)!=len(data['agents']) or len(net.wires)!=len(data['wires']):raise ValueError('duplicate snapshot key')
 net.validate();return net

class Exporter:
 def __init__(self,package):self.package=package;self.rules=[];self.seeds=[]
 def rule(self,r):
  if r.output!=self.package or any(p!=self.package for p in r.inputs):raise ValueError('export restricted to one explicit package')
  if r not in self.rules:self.rules.append(r)
  return str(self.rules.index(r))
 def history(self,h):
  if h.package!=self.package:raise ValueError('foreign package')
  if isinstance(h,Seed):
   if isinstance(h.evidence,Admission):
    if h.evidence not in self.seeds:self.seeds.append(h.evidence)
    return '(seed '+str(self.seeds.index(h.evidence))+')'
   return '(seed '+self.history(h.evidence)+')'
  name='unary' if len(h.premises)==1 else 'binary'
  return '('+' '.join([name,self.rule(h.rule)]+[self.history(p) for p in h.premises])+')'
 def term(self,t):
  if t.kind in ('keep','pending'):return '('+t.kind+' '+self.history(t.payload)+')'
  return '('+' '.join([t.kind,self.rule(t.payload)]+[self.term(c) for c in t.children])+')'
 def step(self,t,path):
  if not path:
   d=t.payload
   if isinstance(d,Seed):return '(F-seed '+self.history(d.evidence)+')'
   return '('+' '.join(['F-unary' if len(d.premises)==1 else 'F-binary',self.rule(d.rule)]+[self.history(x) for x in d.premises])+')'
  i=path[0];child=self.step(t.children[i],path[1:]);r=self.rule(t.payload)
  if t.kind=='one':return '(under-one '+r+' '+child+')'
  if i==0:return '(under-left '+r+' '+self.term(t.children[1])+' '+child+')'
  return '(under-right '+r+' '+self.term(t.children[0])+' '+child+')'
 def compression(self,t):
  if t.kind in ('keep','pending'):return 'same'
  cs=[compact(c) for c in t.children];ps=[self.compression(c) for c in t.children];r=self.rule(t.payload)
  lifted='('+' '.join(['in-one' if t.kind=='one' else 'in-two',r]+ps)+')'
  if all(c.kind=='keep' for c in cs):
   packed='('+' '.join(['pack-one' if t.kind=='one' else 'pack-two',r]+[self.history(c.payload) for c in cs])+')'
   return '(chain '+lifted+' '+packed+')'
  return lifted
 def certificate(self,index,before,pair,after):
  check=diagram(before,pair,after);t,_=reify(before);w,_=reify(after);middle,_=contract(t,check['context_path'])
  return '\n'.join([f'before{index} after{index} : Term tt',f'before{index} = {self.term(t)}',f'after{index} = {self.term(w)}',f'proof{index} : RepresentedStep before{index} after{index}',f'proof{index} = represented {self.step(t,check["context_path"])} {self.compression(middle)}',f'sound{index} : interpret before{index} ≡ interpret after{index}',f'sound{index} = represented-sound proof{index}', ''])
