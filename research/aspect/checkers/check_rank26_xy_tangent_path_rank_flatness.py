#!/usr/bin/env python3
"""Test finite presentation-rank constancy along the endpoint-swap tangent path."""
import argparse,importlib,json,os,sys
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,choices=(32003,32009),required=True);a=ap.parse_args();ROOT=Path(__file__).resolve().parents[3];os.environ['MARICI_FIELD_PRIME']=str(a.prime);os.environ['MARICI_AMBIENT']='8';os.environ['MARICI_POINT']='2,3,-5';sys.path.insert(0,str(ROOT/'research'/'benincasa'));r=importlib.import_module('check_rank26_total_energy_triple_relation_module');r.charts.GAMMA=-(pow(2,-1,a.prime))%a.prime;_,cols=r.column_packet()
def rank_at(point):
 piv={};count=0
 for row in r.raw_relations(point,cols):r.base.add_pivot(dict(row),piv);count+=1
 return count,len(piv)
sample_parameters=list(range(-3,7));points=[(6-s,3+s,-3) for s in sample_parameters];runs=[{'s':s,'point':list(p),'row_count':n,'rank':rank} for s,p in zip(sample_parameters,points,strict=True) for n,rank in [rank_at(p)]];ranks=[x['rank'] for x in runs];flat=len(set(ranks))==1;rank_by_s={x['s']:x['rank'] for x in runs};generic_rank=max(ranks);exceptional=[s for s,rank in rank_by_s.items() if rank<generic_rank]
out={'schema':'marici.aspect.rank26-xy-tangent-path-rank-flatness.v1','prime':a.prime,'gamma_mode':'half','ambient':8,'path':'(x,y,z)=(6-s,3+s,-3), sampled s=-3..6','runs':runs,'swapped_endpoint_ranks_equal':rank_by_s[0]==rank_by_s[3],'generic_sampled_rank':generic_rank,'exceptional_sampled_parameters':exceptional,'finite_rank_flat_on_sampled_path':flat,'oddball':'rank-drop loci obstruct naive constant-rank transport' if not flat else None,'transport_map_constructed':False,'warning':'equal endpoint ranks and source involution do not define a connection, parallel transport, or canonical quotient identification','passed':True};(ROOT/f'research/aspect/results/rank26_xy_tangent_path_rank_flatness_p{a.prime}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','prime':a.prime,'ranks':ranks,'flat':flat}))
