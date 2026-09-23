"""Exact census of which 21 minor inequalities can support fibre polygon edges."""
import json,random
from pathlib import Path
from fractions import Fraction as Q
from check_seven_point_fibre_polygon_stress import N,pairs,line,vertices,classify
from check_seven_point_multichamber_stress import build

def main():
 rng=random.Random(20260828);edges={};vertex_patterns={};cases=[];count=0
 for neg in range(7):
  for run in range(35):
   if neg==0:
    w=[rng.randint(1,9) for _ in range(7)];t=[0]
    for _ in range(6):t.append(t[-1]+rng.randint(1,12))
    x=[Q(j) for j in w];y=[x[j]*t[j] for j in range(7)]
   else:w,t,x,y=build(rng,neg)
   assert all(line(x,y,*p)[0]>0 for p in pairs)
   _,lines=classify(x,y);poly=vertices(lines)
   active_edges=[]
   for p,(c,a,b) in lines.items():
    hits=[z for z in poly if c+a*z[0]+b*z[1]==0]
    if len(hits)>=2:edges[p]=edges.get(p,0)+1;active_edges.append(p)
   for z in poly:
    pattern=tuple(p for p,(c,a,b) in lines.items() if c+a*z[0]+b*z[1]==0)
    vertex_patterns[pattern]=vertex_patterns.get(pattern,0)+1
   if run==0:cases.append({'negative_initial_columns':neg,'polygon_vertices':len(poly),
                            'active_edge_minors':[[i+1,j+1] for i,j in active_edges]})
   count+=1
 result={'schema':'marici.nima.seven-point-fibre-facet-census.v1','tested':count,
  'facet_support_counts':{f'{i+1},{j+1}':edges.get((i,j),0) for i,j in pairs},
  'never_edge_in_samples':[[i+1,j+1] for i,j in pairs if (i,j) not in edges],
  'distinct_vertex_active_patterns':len(vertex_patterns),
  'example_gauges':cases,
  'scope':'Exact finite halfspace-polygon enumeration across seven source sign gauges. An absent facet in samples is not universally redundant.'}
 (N/'results/seven-point-fibre-facet-census.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'tested':count,'edge_minor_count':len(edges),'never_edges':result['never_edge_in_samples'],
                   'distinct_active_patterns':len(vertex_patterns),'cases':cases},indent=2))
if __name__=='__main__':main()
