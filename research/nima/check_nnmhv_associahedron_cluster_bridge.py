#!/usr/bin/env python3
"""Complete selected histories to the type-A cluster/associahedron diagonal set."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def crosses(d,e):
 a,b=sorted(d);c,d2=sorted(e);return (a<c<b<d2) or (c<a<d2<b)
rows=[]
for m in range(1,11):
 P=m+3;all_diag={(a,b) for a in range(1,P+1) for b in range(a+1,P+1) if b-a>1 and not (a==1 and b==P)};positive={(i,j+2) for i in range(1,m+1) for j in range(i,m+1)};fan={(a,P) for a in range(2,P-1)};crossing_ok=True;simple_ok=True
 for i in range(1,m+1):
  for j in range(i,m+1):
   crossed={a-1 for a in range(2,P-1) if crosses((i,j+2),(a,P))};crossing_ok &= crossed==set(range(i,j+1));simple_ok &= ((i==j)==(len(crossed)==1))
 rows.append({'type':f'A_{m}','polygon_vertices':P,'history_positive_diagonals':len(positive),'vacuum_fan_diagonals':len(fan),'all_cluster_variables':len(all_diag),'partition_complete':positive.isdisjoint(fan) and positive|fan==all_diag,'crossings_encode_root_support':crossing_ok,'boundary_simple_roots_cross_one_fan_diagonal':simple_ok})
checks={'positive_histories_plus_negative_simple_fan_complete_cluster_variables':all(x['partition_complete'] for x in rows),'crossing_vectors_are_root_coefficients':all(x['crossings_encode_root_support'] for x in rows),'boundary_updates_are_single_crossings':all(x['boundary_simple_roots_cross_one_fan_diagonal'] for x in rows),'cluster_variable_count_m_mplus3_over2':all(x['all_cluster_variables']==(int(x['type'][2:])*(int(x['type'][2:])+3))//2 for x in rows)}
out={'schema':'marici.nima.nnmhv-associahedron-cluster-bridge.v1','dictionary':{'history_root_[i,j]':'polygon diagonal (i,j+2)','negative_simple_root_-alpha_k':'reference-fan diagonal (k+1,m+3)','root_coefficient':'crossing number with the corresponding fan diagonal','cluster':'noncrossing diagonal set / polygon triangulation'},'rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'Selected histories are the positive cluster variables of type A_m. Adding the m reference-fan boundary/vacuum variables gives the complete almost-positive-root set and associahedron facet labels.','bridges':['finite-type cluster algebras','associahedra and polygon triangulations','root compatibility via diagonal crossing','mutation as diagonal flip','boundary generators as simple-root crossings']};p=ROOT/'research/nima/results/nnmhv-associahedron-cluster-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'dictionary':out['dictionary'],'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
