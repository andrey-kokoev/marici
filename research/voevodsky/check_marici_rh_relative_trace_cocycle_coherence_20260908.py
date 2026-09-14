#!/usr/bin/env python3
"""Exact Hochschild-style cocycle cancellation for a relative trace defect."""
import argparse,json
from collections import defaultdict
from pathlib import Path

def add(total,term,coefficient):
 total[term]+=coefficient
 if total[term]==0:del total[term]
def defect(total,left,right,sign=1):
 # c(left,right)=tau(left right)-tau(right left), retaining cyclic words.
 add(total,'tau('+left+right+')',sign);add(total,'tau('+right+left+')',-sign)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_relative_trace_cocycle_coherence_certificate_20260908.json');a=p.parse_args();raw=defaultdict(int)
 # c(XY,Z)-c(X,YZ)+c(ZX,Y)
 defect(raw,'XY','Z',1);defect(raw,'X','YZ',-1);defect(raw,'ZX','Y',1)
 assert not raw;checks=1
 # Omitting the transported third face leaves a nonzero cyclic residual.
 hostile=defaultdict(int);defect(hostile,'XY','Z',1);defect(hostile,'X','YZ',-1)
 assert hostile;checks+=1
 out={'schema':'marici.rh.relative-trace-cocycle-coherence.v1','status':'cocycle_closed','checks':checks,'identity':'c(XY,Z)-c(X,YZ)+c(ZX,Y)=0 for c(X,Y)=tau(XY)-tau(YX)','reduced_residual':dict(raw),'missing_transported_face_residual':dict(hostile),'claim':'the relative trace defect carries its own three-fold coherence by cyclic cancellation','disposition':'do not add an independent associator; retain every transported face'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'hostile_terms':len(hostile)}))
if __name__=='__main__':main()
