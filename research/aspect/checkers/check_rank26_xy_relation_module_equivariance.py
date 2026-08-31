#!/usr/bin/env python3
"""Verify full labelled raw-relation module equivariance under x/y and u/v swap."""
import argparse,collections,importlib,os,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,choices=(32003,32009),required=True);a=ap.parse_args();ROOT=Path(__file__).resolve().parents[3];os.environ['MARICI_FIELD_PRIME']=str(a.prime);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(ROOT/'research'/'benincasa'));r=importlib.import_module('check_rank26_total_energy_triple_relation_module');_,cols=r.column_packet();inv={i:l for l,i in cols.items()};names=list(r.NAMES);perm={'g1':'g2','g2':'g1','g3':'g3','g23':'g31','g31':'g23'};target_position={name:i for i,name in enumerate(names)}
def map_label(label):
 k,*rest=label;levels=rest[:-1];i,j=rest[-1];mapped=[0]*len(levels)
 for pos,name in enumerate(names):mapped[target_position[perm[name]]]=levels[pos]
 return (k,*mapped,(j,i))
def transform(row):return tuple(sorted((cols[map_label(inv[c])],v) for c,v in row.items()))
src=collections.Counter(transform(x) for x in r.raw_relations((3,6,-3),cols));dst=collections.Counter(tuple(sorted(x.items())) for x in r.raw_relations((6,3,-3),cols));assert src==dst
import json
out={'schema':'marici.aspect.rank26-xy-relation-module-equivariance.v1','prime':a.prime,'ambient':8,'rows_checked':sum(src.values()),'label_action':'u/v monomial exponents swapped; g1<->g2; g23<->g31; g3 fixed','raw_relation_multisets_equal':True,'same_point_transport_constructed':False,'passed':True};(ROOT/f'research/aspect/results/rank26_xy_relation_module_equivariance_p{a.prime}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','prime':a.prime,'rows':sum(src.values())}))
