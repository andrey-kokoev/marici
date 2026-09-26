"""Finite package-indexed extension; signature declaration is explicit input data."""
from reference import Admission,Seed
from port_certificates import Exporter
from port_refinement import reify,contract,diagram

class IndexedExporter(Exporter):
 def __init__(self):self.packages=[];self.rules=[];self.seeds=[]
 def package(self,p):
  if p not in self.packages:self.packages.append(p)
  return 'p'+str(self.packages.index(p))
 def rule(self,r):
  for p in (*r.inputs,r.output):self.package(p)
  if r not in self.rules:self.rules.append(r)
  return 'rule'+str(self.rules.index(r))
 def history(self,h):
  self.package(h.package)
  if isinstance(h,Seed):
   if isinstance(h.evidence,Admission):
    if h.evidence not in self.seeds:self.seeds.append(h.evidence)
    return '(seed evidence'+str(self.seeds.index(h.evidence))+')'
   return '(seed '+self.history(h.evidence)+')'
  name='unary' if len(h.premises)==1 else 'binary'
  return '('+' '.join([name,self.rule(h.rule)]+[self.history(p) for p in h.premises])+')'
 def certificate(self,index,before,pair,after):
  check=diagram(before,pair,after);t,_=reify(before);w,_=reify(after);middle,_=contract(t,check['context_path'])
  source_package=before.validate()[0];target_package=after.validate()[0]
  if source_package!=target_package:raise ValueError('rewrite changed output interface')
  output=self.package(source_package)
  return '\n'.join([f'before{index} after{index} : Term {output}',f'before{index} = {self.term(t)}',f'after{index} = {self.term(w)}',f'proof{index} : RepresentedStep before{index} after{index}',f'proof{index} = represented {self.step(t,check["context_path"])} {self.compression(middle)}',f'sound{index} : interpret before{index} ≡ interpret after{index}',f'sound{index} = represented-sound proof{index}', ''])
 def header(self,module):
  lines=['{-# OPTIONS --safe --cubical --guardedness #-}',f'module {module} where',
   'open import Cubical.Foundations.Prelude','open import CoherenceResolutionClosure',
   'open import ResolutionNetLocalSimulation','open import ResolutionNetCompression',
   'data Pkg : Type where','  '+' '.join('p'+str(i) for i in range(len(self.packages)))+' : Pkg',
   'data U : Pkg → Pkg → Type where']
  for i,r in enumerate(self.rules):
   if len(r.inputs)==1:lines.append(f'  rule{i} : U {self.package(r.inputs[0])} {self.package(r.output)}')
  lines.append('data V : Pkg → Pkg → Pkg → Type where')
  for i,r in enumerate(self.rules):
   if len(r.inputs)==2:lines.append(f'  rule{i} : V {self.package(r.inputs[0])} {self.package(r.inputs[1])} {self.package(r.output)}')
  lines.append('data Evidence : Pkg → Type where')
  for i,e in enumerate(self.seeds):lines.append(f'  evidence{i} : Evidence {self.package(e.package)}')
  lines+=['open Closure Pkg U V public','open Local Pkg U V Evidence public','open Compression Pkg U V Evidence public','']
  return '\n'.join(lines)
