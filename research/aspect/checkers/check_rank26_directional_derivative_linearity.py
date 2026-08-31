#!/usr/bin/env python3
"""Verify rowwise D_(1,-1,0)=D_(1,0,0)-D_(0,1,0) for rank-26 relations."""
import argparse,importlib,json,os,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,choices=(32003,32009),required=True);ap.add_argument('--ambient',type=int,choices=(8,16),required=True);a=ap.parse_args();ROOT=Path(__file__).resolve().parents[3];os.environ['MARICI_FIELD_PRIME']=str(a.prime);os.environ['MARICI_AMBIENT']=str(a.ambient);os.environ['MARICI_POINT']='2,3,-5';sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky'),str(ROOT/'research'/'nima'/'checkers')]
rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');rees.charts.GAMMA=-(pow(2,-1,a.prime))%a.prime;adapter=importlib.import_module('check_cosmology_rank26_p_normal_raw_relation_adapter');_,cols=rees.column_packet();point=(3,6,-3);dx,nx=adapter.derivative_rows(cols,point,(1,0,0));dy,ny=adapter.derivative_rows(cols,point,(0,1,0));dt,nt=adapter.derivative_rows(cols,point,(1,-1,0));assert nx==ny==nt
for x,y,t in zip(dx,dy,dt,strict=True):
 expected=dict(x)
 for c,v in y.items():
  z=(expected.get(c,0)-v)%a.prime
  if z:expected[c]=z
  else:expected.pop(c,None)
 assert expected==t
out={'schema':'marici.aspect.rank26-directional-derivative-linearity.v1','prime':a.prime,'ambient':a.ambient,'gamma_mode':'half','rows_checked':nt,'identity':'D_tangent = D_nx - D_ny rowwise','consequence':'the induced first-syzygy maps obey b_tangent=b_nx-b_ny on their common domain','does_not_prove':'surjectivity of b_nx-b_ny onto the shared normal image or unbounded stabilization','passed':True};p=ROOT/f'research/aspect/results/rank26_directional_derivative_linearity_half_a{a.ambient}_p{a.prime}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','rows':nt,'prime':a.prime,'ambient':a.ambient}))
