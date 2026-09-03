"""Add the declared representative-change triangles and compute H1 characters."""
import json
import sympy as sp


def main():
    V=["w","-w","a","-a"]
    E=[("w","-w"),("-w","w"),("w","a"),("a","-w"),("-w","-a"),("-a","w"),("-w","a"),("a","w"),("w","-a"),("-a","-w")]
    rv={"w":"-w","-w":"w","a":"-a","-a":"a"}
    d1=sp.zeros(4,10)
    for j,(x,y) in enumerate(E):d1[V.index(x),j]=-1;d1[V.index(y),j]=1
    S1=sp.zeros(10)
    for j,(x,y) in enumerate(E):S1[E.index((rv[x],rv[y])),j]=1
    # Each column is detour minus direct edge, hence a boundary-null triangle.
    specs=[(2,3,0),(4,5,1),(6,7,1),(8,9,0)]
    d2=sp.zeros(10,4)
    for j,(e,f,g) in enumerate(specs):d2[e,j]=1;d2[f,j]=1;d2[g,j]=-1
    S2=sp.zeros(4)
    for j in range(4):
      target=S1*d2[:,j]
      for k in range(4):
       if target==d2[:,k]:S2[k,j]=1;break
    ker_plus=len((S1-sp.eye(10)).col_join(d1).nullspace());ker_minus=len((S1+sp.eye(10)).col_join(d1).nullspace())
    im_plus=sp.Matrix.hstack(*[d2*v for v in (S2-sp.eye(4)).nullspace()]).rank()
    im_minus=sp.Matrix.hstack(*[d2*v for v in (S2+sp.eye(4)).nullspace()]).rank()
    hplus=ker_plus-im_plus;hminus=ker_minus-im_minus
    odd_basis=(S1+sp.eye(10)).col_join(d1).nullspace();odd_boundaries=[d2*v for v in (S2+sp.eye(4)).nullspace()]
    span=sp.Matrix.hstack(*odd_boundaries);rep=next(v for v in odd_basis if sp.Matrix.hstack(span,v).rank()>span.rank())
    representative={f"{E[i][0]}->{E[i][1]}":str(rep[i]) for i in range(10) if rep[i]!=0}
    available=[];available_specs=[]
    for x in V:
     for y in V:
      for z in V:
       if len({x,y,z})<3 or (x,y) not in E or (y,z) not in E or (x,z) not in E:continue
       c=sp.zeros(10,1);c[E.index((x,y))]=1;c[E.index((y,z))]=1;c[E.index((x,z))]=-1;available.append(c);available_specs.append((x,y,z))
    all_triangles=sp.Matrix.hstack(*available)
    fill=all_triangles.gauss_jordan_solve(rep)[0];fill=fill.subs({q:0 for q in fill.free_symbols})
    fill_terms={"->".join(available_specs[i]):str(fill[i]) for i in range(len(available)) if fill[i]!=0}
    checks={"chain_complex":d1*d2==sp.zeros(4,4),"triangles_independent":d2.rank()==4,"triangle_action_intertwines":S1*d2==d2*S2,"h1_plus_dimension_two":hplus==2,"h1_minus_dimension_one":hminus==1,"representative_is_odd_cycle":d1*rep==sp.zeros(4,1) and S1*rep==-rep,"representative_not_triangle_boundary":sp.Matrix.hstack(d2,rep).rank()>d2.rank(),"available_triangles_fill_entire_cycle_space":all_triangles.rank()==7 and all_triangles*fill==rep}
    result={"schema":"marici.grothendieck.voevodsky-fixture-homology-characters.v3","passed":all(checks.values()),"checks":checks,"kernel_characters":{"plus":ker_plus,"minus":ker_minus},"boundary2_characters":{"plus":im_plus,"minus":im_minus},"h1_characters":{"plus":hplus,"minus":hminus},"odd_output_h1_intertwiner_dimension":hminus,"odd_h1_representative":representative,"available_oriented_triangles":len(available),"available_triangle_span_rank":all_triangles.rank(),"explicit_additional_triangle_fill":fill_terms,"disposition":"The existing 1-skeleton already supports simplicial triangles that fill the odd class, but they were not among the four declared 2-cells. Source authority must decide whether those additional triangles are admitted coherence cells."}
    print(json.dumps(result,indent=2))
    if not result['passed']:raise SystemExit(1)
if __name__=='__main__':main()
