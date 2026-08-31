#!/usr/bin/env python3
"""Check the x<->y, u<->v source involution and identify its fixed-point obstruction."""
import argparse,importlib,json,os,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,choices=(32003,32009),required=True);a=ap.parse_args();ROOT=Path(__file__).resolve().parents[3];os.environ['MARICI_FIELD_PRIME']=str(a.prime);sys.path.insert(0,str(ROOT/'research'/'benincasa'));base=importlib.import_module('physical_four_mark_residue_twisted_derham')
name_swap={'g1':'g2','g2':'g1','g3':'g3','g23':'g31','g31':'g23'}
def uv_swap(poly):return {(j,i):c for (i,j),c in poly.items()}
def check(point):
 x,y,z=point;k,q=base.fiber_data(x,y,z);ks,qs=base.fiber_data(y,x,z);assert uv_swap(k)==ks
 for n,m in name_swap.items():assert uv_swap(q[n])==qs[m]
point=(3,6,-3);check(point);check((6,3,-3));out={'schema':'marici.aspect.rank26-xy-source-involution.v1','prime':a.prime,'source_point':list(point),'target_point':[6,3,-3],'parameter_action':'(x,y,z)->(y,x,z)','fiber_coordinate_action':'(u,v)->(v,u)','source_name_action':name_swap,'cayley_menger_equivariant':True,'five_mark_divisor_family_equivariant':True,'normal_action':'nx->ny','fixed_point_condition':'x=y','audit_point_fixed':False,'consequence':'the involution identifies nx data at (3,6,-3) with ny data at (6,3,-3), not with ny data at the original point','missing_cell':'source-derived transport or homotopy along the p-tangent fiber from (6,3,-3) to (3,6,-3)','same_point_normal_image_equality_derived':False,'passed':True};p=ROOT/f'research/aspect/results/rank26_xy_source_involution_p{a.prime}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','prime':a.prime,'fixed':False}))
