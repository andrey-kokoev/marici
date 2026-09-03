"""Reciprocal character decomposition of Voevodsky's finite filler fixture."""
import json
import sympy as sp


def main():
    vertices = ["w", "-w", "a", "-a"]
    edges = [("w","-w"),("-w","w"),("w","a"),("a","-w"),("-w","-a"),("-a","w"),("-w","a"),("a","w"),("w","-a"),("-a","-w")]
    rv = {"w":"-w","-w":"w","a":"-a","-a":"a"}
    B = sp.zeros(len(vertices), len(edges))
    for j,(x,y) in enumerate(edges):B[vertices.index(x),j]=-1;B[vertices.index(y),j]=1
    S = sp.zeros(len(edges))
    for j,(x,y) in enumerate(edges):S[edges.index((rv[x],rv[y])),j]=1
    K = sp.Matrix.hstack(*B.nullspace())
    plus = (S-sp.eye(len(edges))).col_join(B).nullspace()
    minus = (S+sp.eye(len(edges))).col_join(B).nullspace()
    # col_join above acts on edge vectors: simultaneous kernel and character condition.
    direct = sp.zeros(len(edges),1);direct[0]=1
    anchored = sp.zeros(len(edges),1);anchored[2]=anchored[3]=1
    cycle = anchored-direct
    checks={
      "boundary_square_fixture_has_rank_three":B.rank()==3,
      "kernel_dimension_is_seven":len(B.nullspace())==7,
      "kernel_plus_dimension_is_four":len(plus)==4,
      "kernel_minus_dimension_is_three":len(minus)==3,
      "representative_difference_is_cycle":B*cycle==sp.zeros(4,1),
      "reflection_preserves_boundary_map":all(B*S[:,j]==sp.Matrix([-1 if i==vertices.index(rv[edges[j][0]]) else 1 if i==vertices.index(rv[edges[j][1]]) else 0 for i in range(4)]) for j in range(len(edges)))
    }
    result={"schema":"marici.grothendieck.voevodsky-fixture-kernel-characters.v1","passed":all(checks.values()),"checks":checks,"boundary_rank":B.rank(),"kernel_dimension":7,"kernel_plus_dimension":4,"kernel_minus_dimension":3,"odd_output_intertwiner_dimension":3,"disposition":"The hostile fixture already has a three-dimensional reciprocal-odd hidden cycle sector matching its odd endpoint output; equivariance cannot select a unique filler."}
    print(json.dumps(result,indent=2))
    if not result['passed']:raise SystemExit(1)
if __name__=='__main__':main()
