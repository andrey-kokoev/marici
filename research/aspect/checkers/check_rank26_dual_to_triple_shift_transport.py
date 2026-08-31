#!/usr/bin/env python3
"""Verify that every dual relation has an exact shifted triple relation."""
import argparse,importlib,json,os,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,choices=(32003,32009),default=32003);args=ap.parse_args();ROOT=Path(__file__).resolve().parents[3];BEN=ROOT/'research'/'benincasa';sys.path.insert(0,str(BEN));os.environ['MARICI_FIELD_PRIME']=str(args.prime);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5'
rees=importlib.import_module('check_rank26_total_energy_triple_relation_module');_,cols=rees.column_packet();width=len(cols);point=(3,6,-3);sp=lambda o:(point[0]+o,point[1],point[2]);samples=[rees.raw_relations(sp(o),cols) for o in rees.OFFSETS];w1=rees.interpolation_weights(1);w2=rees.interpolation_weights(2);checked=0
for sampled in zip(*samples,strict=True):
 r0=dict(sampled[rees.OFFSETS.index(0)]);r1=rees.combine(sampled,w1);r2=rees.combine(sampled,w2)
 dual_a=rees.shifted_row(r0,width,1);dual_b=rees.assemble((r0,r1),width)
 triple_c=rees.shifted_row(r0,width,2);triple_d=rees.assemble(({},r0,r1),width)
 shift=lambda row:{column+width:value for column,value in row.items()}
 assert shift(dual_a)==triple_c and shift(dual_b)==triple_d;checked+=1
assert checked==9780
out={'schema':'marici.aspect.rank26-dual-to-triple-shift-transport.v1','prime':args.prime,'source_relations_checked':checked,'dual_a_to_triple_c':True,'dual_b_to_triple_d':True,'witness_index_transport':'dual row 2*i+a maps to triple row 3*i+a for a in {0,1}','consequence':'every dual annihilation witness transports coefficientwise to a triple t^2-annihilation witness','independent_triple_reduction_required':False,'passed':True};p=ROOT/f'research/aspect/results/rank26_dual_to_triple_shift_transport_p{args.prime}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','prime':args.prime,'checked':checked}))
