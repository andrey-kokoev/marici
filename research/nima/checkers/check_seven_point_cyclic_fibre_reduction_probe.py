"""Test whether seven cyclic minor halfspaces alone define positive CZ fibres."""
import json,random
from fractions import Fraction as Q
from itertools import combinations
from check_seven_point_fibre_polygon_stress import N,pairs,line,solve,vertices
from check_seven_point_multichamber_stress import build
cyclic={(i,i+1) for i in range(6)}|{(0,6)}
def poly(lines):
 result=set()
 for p,q in combinations(lines,2):
  z=solve(lines[p],lines[q])
  if z is not None and all(c+a*z[0]+b*z[1]>=0 for c,a,b in lines.values()):result.add(z)
 return result
def bounded(lines):
 # In 2D, a nonzero recession vector exists precisely when a direction
 # perpendicular to one constraint normal or its negative satisfies all.
 normals=[(a,b) for c,a,b in lines.values() if a or b]
 return normals and not any(all(c*a+d*b>=0 for c,d in normals) for a,b in
   [(n[1],-n[0]) for n in normals]+[(-n[1],n[0]) for n in normals])
def main():
 rng=random.Random(20260829);count=0;bad=None;rows=[]
 for neg in range(7):
  for run in range(50):
   if neg==0:
    w=[rng.randint(1,9) for _ in range(7)];t=[0]
    for _ in range(6):t.append(t[-1]+rng.randint(1,12))
    x=[Q(a) for a in w];y=[x[j]*t[j] for j in range(7)]
   else:w,t,x,y=build(rng,neg)
   all_lines={p:line(x,y,*p) for p in pairs};cyclic_lines={p:all_lines[p] for p in cyclic}
   assert all(c>0 for c,a,b in all_lines.values())
   full=vertices(all_lines);partial=poly(cyclic_lines);closed=bounded(cyclic_lines)
   if not closed or full!=partial:
    bad={'negative_initial_columns':neg,'run':run,'weights':w,'slopes':t,
     'cyclic_polygon_bounded':bool(closed),'full_vertices':len(full),'cyclic_vertices':len(partial),
     'nonpositive_cyclic_vertex_count':sum(1 for z in partial if any(c+a*z[0]+b*z[1]<0 for c,a,b in all_lines.values()))};break
   if run==0:rows.append({'negative_initial_columns':neg,'vertex_count':len(full)})
   count+=1
  if bad:break
 # Negative control: cyclic positivity of an arbitrary source does NOT
 # imply its noncyclic positivity. The target here is outside the admitted
 # positive image (full fibre empty), so the positive-Y precondition matters.
 X=list(map(Q,[1,1,0,-1,-1,-1,2]));V=list(map(Q,[0,1,1,1,0,-2,1]))
 exterior={p:line(X,V,*p) for p in pairs};partial_ext={p:exterior[p] for p in cyclic}
 assert all(c>0 for c,a,b in partial_ext.values()) and bounded(partial_ext)
 assert len(poly(partial_ext))==3 and not vertices(exterior)
 negative_control={'source_first_row':list(map(str,X)),'source_second_row':list(map(str,V)),
  'positive_cyclic_minors':7,'cyclic_polygon_vertices':3,'full_positive_fibre_empty':True}
 result={'schema':'marici.nima.seven-point-cyclic-fibre-reduction-probe.v1','passed_samples':count,
  'nonadmitted_target_negative_control':negative_control,
   'first_counterexample':bad,'examples':rows,
   'claim_boundary':'Equal bounded polygons at finitely many strictly positive sources do not prove cyclic sufficiency over the admitted positive image. An explicit target outside that image has all seven cyclic inequalities but an empty full positive fibre.'}
 (N/'results/seven-point-cyclic-fibre-reduction-probe.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
