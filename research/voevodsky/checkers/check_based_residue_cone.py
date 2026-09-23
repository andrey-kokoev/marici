"""A certified retained base normalizes a refinement prism to a based cone.
Explicit nine-vertex diagram B*(Delta1 x Delta3), not arbitrary cone filling.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_polyhedral_residue_coherence import mat,eye,step,check,compose,fold,all_brackets,refine,extend,forget,encode_obj,mv
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 A=mat([[-1,0],[0,-1],[1,1]]);base=(A,(Q(0),Q(0),Q(1,4)),(Q(0),Q(0)))
 # B: h,k>=0, h+k<=1/4. T_i present h,k>=0,h+k<=1.
 first,base_arrow=step(base,eye(3),(Q(0),Q(0)),(Q(0),Q(0),Q(3,4)))
 objects=[first];arrows=[]
 Ms=[mat([[1,0,0],[0,1,0],[0,0,1],[0,1,1],[1,0,1]]),
 mat([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0]]),mat([[0,1,0],[0,0,1],[1,0,0]])]
 ds=[(Q(1,4),Q(1,4)),(Q(1,4),Q(-1,4)),(Q(-1,2),Q(1,4))]
 for M,d in zip(Ms,ds):
  obj,a=step(objects[-1],M,d);objects.append(obj);arrows.append(a)
 a=(Q(1),Q(0));b=Q(1,2);refined=[refine(o,a,b) for o in objects]
 # The added bound holds on ALL of B, certified by -k+(h+k)<=1/4<=1/2.
 w=(Q(0),Q(1),Q(1));assert tuple(sum(w[i]*A[i][j] for i in range(3)) for j in range(2))==a
 surplus=b-sum(x*y for x,y in zip(w,base[1]));assert surplus==Q(1,4)>=0
 # Store this redundancy proof; then construct the normalized finite diagram
 # with F(B)=B. We do not assert arbitrary row redundancy is a strict inverse.
 M,d,c=base_arrow;refined_base_arrow=(M+(w,),d,c+(surplus,))
 check(base,refined[0],refined_base_arrow)
 old_cones=[base_arrow];new_cones=[refined_base_arrow]
 for i,arrow in enumerate(arrows):
  old_cones.append(compose(old_cones[-1],arrow))
  new_cones.append(compose(new_cones[-1],extend(arrow)))
 for obj,ref,old,new in zip(objects,refined,old_cones,new_cones):
  check(base,obj,old);check(base,ref,new)
  # Vertical base arrow is literally identity in the normalized diagram.
  assert compose(new,forget(obj))==old
 # Four top-dimensional staircase simplices in the cone on the prism.
 final=old_cones[-1];parenthesizations=0
 for k in range(4):
  chain=[refined_base_arrow]+[extend(x) for x in arrows[:k]]+[forget(objects[k])]+arrows[k:]
  assert len(chain)==5
  results=all_brackets(chain);assert len(results)==14 and all(x==final for x in results)
  check(base,objects[-1],fold(chain));parenthesizations+=len(results)
 # Fifth simplex of Delta1 x Delta4 has its two base endpoints identified.
 identity=(eye(3),(Q(0),Q(0)),(Q(0),Q(0),Q(0)))
 assert fold([identity,base_arrow]+arrows)==final
 # Hostile refinement h>=1/2 excludes every point of B: h<=1/4 follows
 # from the same w, so any putative fixed-base gate is impossible.
 badnormal=(Q(-1),Q(0));badbound=Q(-1,2)
 assert badbound+sum(x*y for x,y in zip(w,base[1]))==Q(-1,4)<0
 origin=(Q(0),Q(0));assert all(sum(x*y for x,y in zip(n,origin))<=bound for n,bound in zip(A,base[1]))
 assert sum(x*y for x,y in zip(badnormal,origin))>badbound
 report={'passed':True,'base':encode_obj(base),'presentations':[encode_obj(o) for o in objects],
 'refinement':{'normal':list(map(str,a)),'upper':str(b)},
 'base_preservation_certificate':{'weights':list(map(str,w)),'surplus':str(surplus)},
 'normalized_shape':{'vertices':9,'expression':'B * (Delta^1 x Delta^3)','dimension':5,
 'nondegenerate_top_simplices':4,'five_arrow_parenthesizations':parenthesizations,'base_edge':'identity after certified normalization'},
 'hostile_base_refinement':{'normal':['-1','0'],'upper':'-1/2','contradiction_upper':'-1/4','fixed_base_allowed':False},
 'scope':'Concrete constraint-category model of the earlier based-cone shape. No identification of analytic roles, residue jets or historical authority with these vertices.'}
 (OUT/'based-residue-cone.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ('passed','normalized_shape','hostile_base_refinement')},indent=2))
if __name__=='__main__':main()
