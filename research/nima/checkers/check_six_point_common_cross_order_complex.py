from __future__ import annotations
import itertools,json
from collections import defaultdict
from pathlib import Path
import sympy as sp
from check_six_point_nmhv_ordering_relations import sij

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-common-cross-order-complex.json"
VERTICES=tuple(range(1,7))

def parity(values):
 return -1 if sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))%2 else 1

def add(out,key,value):
 out[key]=sp.cancel(out[key]+value)
 if out[key]==0:del out[key]
def simplex_chain(order):
 terms=[order[:5],(order[0],order[1],order[2],order[4],order[5]),(order[0],order[2],order[3],order[4],order[5])]
 out=defaultdict(lambda:sp.Integer(0))
 for term in terms:add(out,tuple(sorted(term)),sp.Integer(parity(term)))
 return dict(out)
def boundary(chain):
 out=defaultdict(lambda:sp.Integer(0))
 for cell,c in chain.items():
  for i in range(len(cell)):add(out,cell[:i]+cell[i+1:],(-1)**i*c)
 return dict(out)
def scale_chain(chain,c):return {k:sp.cancel(c*v) for k,v in chain.items() if sp.cancel(c*v)!=0}
def sum_chain(target,source):
 for k,v in source.items():add(target,k,v)
def canonical_dihedral_orders():
 out=[]
 for tail in itertools.permutations((2,3,4,5,6)):
  o=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if o<rev:out.append(o)
 return out
def classify(chain,bd5):
 if not chain:return "zero"
 bd=boundary(chain)
 if bd:return "not_cycle"
 pivot=next(iter(bd5));ratio=sp.cancel(chain.get(pivot,0)/bd5[pivot])
 if ratio!=0 and all(sp.cancel(chain.get(k,0)-ratio*v)==0 for k,v in bd5.items()) and set(chain)<=set(bd5):return "boundary"
 return "nonzero_homology_class"
def main():
 orders=canonical_dihedral_orders();embeddings=[]
 for o in orders:
  c=simplex_chain(o);embeddings.append({"ordering":list(o),"top_cells":{"".join(map(str,k)):str(v) for k,v in sorted(c.items())},"residues":{"".join(map(str,k)):str(v) for k,v in sorted(boundary(c).items())}})
 top={VERTICES:sp.Integer(1)};bd5=boundary(top)
 relations=[]
 for p in itertools.permutations((2,3,4,5)):
  raw=defaultdict(lambda:sp.Integer(0));weight=sp.Integer(0)
  for k in range(1,5):
   weight+=sij(1,p[k-1]);o=p[:k]+(1,)+p[k:]+(6,);sum_chain(raw,scale_chain(simplex_chain(o),weight))
  raw=dict(raw);bd=boundary(raw);relations.append({"permutation":list(p),"classification":classify(raw,bd5),"top_chain":{"".join(map(str,k)):str(v) for k,v in sorted(raw.items())},"boundary_residue_count":len(bd),"boundary_residues":{"".join(map(str,k)):str(v) for k,v in sorted(bd.items())}})
 # Verify d^2 on every basis cell in dimensions 2 through 5.
 d2=all(not boundary(boundary({cell:sp.Integer(1)})) for r in range(3,7) for cell in itertools.combinations(VERTICES,r))
 c4=list(itertools.combinations(VERTICES,5));c3=list(itertools.combinations(VERTICES,4))
 d4=sp.Matrix([[boundary({cell:sp.Integer(1)}).get(face,0) for cell in c4] for face in c3])
 counts={name:sum(r["classification"]==name for r in relations) for name in ("zero","boundary","nonzero_homology_class","not_cycle")}
 checks={"60_dihedral_orderings_embedded":len(embeddings)==60,"all_embeddings_use_common_six_vertex_complex":all(set(map(int,key))<=set(VERTICES) for e in embeddings for key in e["top_cells"]),"boundary_squared_zero":d2,"full_simplex_contractible_H4_zero":len(c4)-d4.rank()==1,"all_24_bcj_chains_classified":len(relations)==24}
 out={"schema":"marici.nima.six_point_common_cross_order_complex.result.v1","status":"passed" if all(checks.values()) else "failed","complex":{"name":"oriented simplicial chains of the abstract 5-simplex on labels 1,...,6","chain_ranks":{"C5":1,"C4":6,"C3":15,"C2":20,"C1":15,"C0":6},"top_boundary":{"".join(map(str,k)):str(v) for k,v in sorted(bd5.items())},"residue_map":"The codimension-one residue is the signed simplicial boundary C4 -> C3; individual facet residues are its coordinate projections."},"checks":checks,"classification_counts":counts,"ordered_triangulation_embeddings":embeddings,"bcj_chains":relations,"claim_boundary":"Constructs the minimal common labelled simplicial complex and classifies the 24 raw BCJ-weighted top chains. A chain with nonzero simplicial boundary is not a homology class. This abstract common refinement does not prove that cross-order label identifications are induced by a common positive geometry."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
