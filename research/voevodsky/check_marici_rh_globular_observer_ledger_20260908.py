#!/usr/bin/env python3
"""Type the current RH constructions by node, globular rung, and authority."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 nodes=['global-source','theta-source','relative-null','completed-sewing','endpoint-conductor','green-work']
 cells=[
 {'id':'theta-incidence','rung':0,'source':'global-source','target':'theta-source','status':'proved','kind':'source-incidence'},
 {'id':'xi-null-fibre','rung':0,'source':'theta-source','target':'relative-null','status':'proved','kind':'derived-zero-fibre'},
 {'id':'fourier-observer','rung':0,'source':'theta-source','target':'theta-source','status':'proved-algebraically','kind':'joint-readout'},
 {'id':'endpoint-incidence-24','rung':0,'source':'global-source','target':'endpoint-conductor','status':'missing-common-source-leg','kind':'source-incidence'},
 {'id':'framed-endpoint-local','rung':0,'source':'endpoint-conductor','target':'endpoint-conductor','status':'proved','kind':'24-local-maps'},
 {'id':'global-fourier-sewing','rung':1,'source':'theta-incidence','target':'fourier-observer','status':'proved-before-cutoff','kind':'comparison'},
 {'id':'finite-cutoff-BC','rung':1,'source':'theta-incidence','target':'fourier-observer','status':'falsified-rank-one-leakage','kind':'comparison'},
 {'id':'xi-bordered-endpoint','rung':1,'source':'xi-null-fibre','target':'framed-endpoint-local','status':'proved-target-incidence-only','kind':'comparison'},
 {'id':'relative-null-endpoint-BC','rung':2,'source':'global-fourier-sewing','target':'xi-bordered-endpoint','status':'missing','kind':'coherence'},
 {'id':'endpoint-P24-detector','rung':2,'source':'framed-endpoint-local','target':'xi-bordered-endpoint','status':'proved-diagnostic','kind':'coherence-detector'},
 {'id':'green-current','rung':0,'source':'global-source','target':'green-work','status':'proved-conditional-response','kind':'dynamic-incidence'},
 {'id':'boundary-work-promotion','rung':3,'source':'relative-null-endpoint-BC','target':'endpoint-P24-detector','status':'missing','kind':'promotion-to-green-work'},
 {'id':'positive-bulk','rung':0,'source':'global-source','target':'green-work','status':'independent-open-admission','kind':'positivity'},
 {'id':'completion-domain','rung':0,'source':'global-source','target':'completed-sewing','status':'open-uniform-margin','kind':'resource-domain'}]
 ids={c['id'] for c in cells};checks=0
 assert len(ids)==len(cells);checks+=len(cells)
 for c in cells:
  if c['rung']==0:
   assert c['source'] in nodes and c['target'] in nodes
  else:
   assert c['source'] in ids and c['target'] in ids
  checks+=2
 # Higher cells cannot precede their globular boundaries.
 for c in cells:
  if c['rung']>0:
   s=next(x for x in cells if x['id']==c['source']);t=next(x for x in cells if x['id']==c['target'])
   assert s['rung']<c['rung'] and t['rung']<c['rung'];checks+=2
 # SCC compilation order exposes the missing level-zero common-source leg first.
 # Higher missing cells are downstream, not currently executable constructors.
 frontier=['endpoint-incidence-24']
 downstream=['completion-domain','relative-null-endpoint-BC','boundary-work-promotion']
 assert next(c for c in cells if c['id']=='endpoint-incidence-24')['status']=='missing-common-source-leg';checks+=1
 assert all(any(c['id']==x for c in cells) for x in downstream);checks+=len(downstream)
 out={'schema':'marici.rh.globular-observer-ledger.v1','status':'typed','checks':checks,'nodes':nodes,'cells':cells,
  'residual_policy':{'presentation':'quotient','observer-invisibility':'prove joint faithfulness','local-transition':'trivialize before descent','approximation':'bound and converge','positive-residual':'preserve and prove positive'},
  'prohibitions':['do not combine observer families before common-source transport','do not promote a diagnostic residual without a promotion cell','do not infer positivity from conformance','do not impose finite Fourier Beck-Chevalley','do not let higher rungs manufacture missing level-zero incidence'],
  'active_frontier':frontier,'downstream':downstream,
  'first_missing_typed_object':'a source-authorized map from the frozen global theta/Tate preparation to the marked endpoint/conormal preparation, with a joint-acquisition capability for theta/Fourier and endpoint observers',
  'acceptance_test':'the map types all endpoint ports on the same preparation, commutes with the established theta and endpoint restrictions, and supplies evidence locators independent of target-rank data',
  'next_object':'the common-source endpoint incidence; completion and higher coherence remain downstream'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'typed','checks':checks,'nodes':len(nodes),'cells':len(cells),'active_frontier':frontier}))
if __name__=='__main__':main()
