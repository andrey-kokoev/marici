#!/usr/bin/env python3
"""Validate the explicit partial order of the Marici RH constraint programme."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 tasks=[
 ('freeze-source',[], 'established'),
 ('theta-incidence',['freeze-source'],'established'),
 ('endpoint-incidence',['freeze-source'],'open-common-source-leg'),
 ('common-completed-domain',['theta-incidence','endpoint-incidence'],'open'),
 ('global-fourier-sewing',['common-completed-domain'],'established-before-cutoff'),
 ('relative-null-fibre',['global-fourier-sewing'],'established-algebraically'),
 ('completed-endpoint-observation',['global-fourier-sewing','endpoint-incidence'],'open'),
 ('relative-null-endpoint-coherence',['relative-null-fibre','completed-endpoint-observation'],'open'),
 ('identify-coherence-boundary',['relative-null-endpoint-coherence'],'open'),
 ('promote-boundary-to-D-bw',['identify-coherence-boundary'],'open'),
 ('prove-promoted-vanishing',['promote-boundary-to-D-bw','relative-null-fibre'],'open'),
 ('positive-bulk-admission',['common-completed-domain'],'open-independent'),
 ('hermitian-confinement',['prove-promoted-vanishing','positive-bulk-admission'],'machine-checked-conditional'),
 ('finite-six-normal-diagnostics',['hermitian-confinement','completed-endpoint-observation'],'established-object-deferred-use')]
 names=[x[0] for x in tasks];assert len(names)==len(set(names));checks=len(names)
 pos={n:i for i,n in enumerate(names)}
 for n,deps,_ in tasks:
  for d in deps:
   assert d in pos and pos[d]<pos[n];checks+=1
 # Kahn uniqueness is not required: this is a partial order. Record available parallel work.
 edges=[{'from':d,'to':n} for n,deps,_ in tasks for d in deps]
 # Explicit forbidden reversals central to prior falsifiers.
 forbidden=[
  ['finite-six-normal-diagnostics','global-fourier-sewing'],
  ['relative-null-endpoint-coherence','endpoint-incidence'],
  ['promote-boundary-to-D-bw','identify-coherence-boundary'],
  ['hermitian-confinement','positive-bulk-admission']]
 for later,earlier in forbidden:
  assert pos[earlier]<pos[later];checks+=1
 out={'schema':'marici.rh.constraint-dependency-dag.v1','status':'typed','checks':checks,
  'tasks':[{'id':n,'depends_on':deps,'status':s,'topological_index':i} for i,(n,deps,s) in enumerate(tasks)],
  'edges':edges,'forbidden_reversals':forbidden,
  'parallel_branches':[['theta-incidence','endpoint-incidence'],['completed-endpoint-observation','relative-null-fibre'],['positive-bulk-admission','relative-null-endpoint-coherence']],
  'critical_path':['freeze-source','endpoint-incidence','common-completed-domain','global-fourier-sewing','completed-endpoint-observation','relative-null-endpoint-coherence','identify-coherence-boundary','promote-boundary-to-D-bw','prove-promoted-vanishing','hermitian-confinement'],
  'next_ready_task':'endpoint-incidence: construct the common-source leg from the global theta/Tate source before completion',
  'rule':'finite diagnostics are downstream evidence and may not be used to manufacture global sewing or source incidence'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'typed','checks':checks,'tasks':len(tasks),'edges':len(edges),'next_ready_task':out['next_ready_task']}))
if __name__=='__main__':main()
