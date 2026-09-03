#!/usr/bin/env python3
"""Serialize the all-S principal coefficient cell in the physical half-twist columns."""
import contextlib,io,json,runpy
from pathlib import Path
P=Path(__file__).resolve();ROOT=P.parents[3];mod=ROOT/'research'/'benincasa'/'check_rank26_total_energy_triple_relation_module.py'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(mod))
base=g['base'];protocol=json.loads((ROOT/'research'/'voevodsky'/'results'/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(protocol['test_point_xyz']);k,qs=base.fiber_data(*point);names=g['NAMES'];low,cols=g['column_packet']();prime=base.PRIME
def center(x):
 x%=prime;return x-prime if x>prime//2 else x
def add(a,b,s=1):
 r=dict(a)
 for m,v in b.items():r[m]=(r.get(m,0)+s*v)%prime
 return {m:v for m,v in r.items() if v%prime}
num=add(add({},qs['g1'],-1),qs['g2'],-1);num=add(num,qs['g3'],1);pval=point[0]+point[1]+3*point[2];expected={} if pval%prime==0 else {(0,0):pval%prime};assert num==expected
levels=(1,)*len(names);terms=[]
for m,v in sorted(num.items()):
 label=(0,*levels,m);terms.append({'column_label':[0,*levels,list(m)],'column_index':cols[label],'coefficient':center(v)})
out={'schema':'marici.benincasa.cosmology-all-S-row-serialization.v1','source_names':list(names),'point':list(point),'source_identity':'-q_g1-q_g2+q_g3=p','p_value':pval,'denominator_levels':list(levels),'serialized_terms':terms,'serialization_constructed':True,'normal_derivative_serialization':{'nx':1,'ny':1,'p_tangent':0,'column_label':[0,*levels,[0,0]]},'adapter_domain_check':'raw-relation derivative adapter accepts relation rows, not serialized columns','ordered_laurent_terms':[{'deleted_axis':'q_g1','coefficient':-1},{'deleted_axis':'q_g2','coefficient':-1},{'deleted_axis':'q_g3','coefficient':1}],'next_gate':'differentiate the parameter-dependent serialized section; the raw-relation adapter acts on relation rows, not columns'};(P.parents[1]/'results'/'cosmology_all_S_row_serialization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
