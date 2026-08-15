"""Exact generic lower-sector Cayley--Menger collision audit.

Frozen variables:
  c=y12, a=y23, b=y31;
  p1,p2,p3 are base momentum-triangle edge lengths;
  x1,x2,x3 are independent site-energy sums.
"""
import json
import sys
sys.stdout = open(r"C:\Users\andrey\src\marici\research\benincasa\generic_lower_collision_run.log", "w", encoding="utf-8")
sys.stderr = sys.stdout
sys.path.insert(0, r"C:\Users\andrey\src\marici\research\benincasa\.tmp_sympy")
import sympy as sp
from pathlib import Path

a,b,c,t = sp.symbols("a b c t")
x1,x2,x3,p1,p2,p3 = sp.symbols("X1 X2 X3 P1 P2 P3")

cm=sp.Matrix([
 [0,1,1,1,1],
 [1,0,c**2,a**2,b**2],
 [1,c**2,0,p2**2,p1**2],
 [1,a**2,p2**2,0,p3**2],
 [1,b**2,p1**2,p3**2,0],
])
K=sp.factor(-cm.det()/2)
lines={
 "g1":c+b+x1,
 "g2":c+a+x2,
 "g3":a+b+x3,
 "g23":c+b+x2+x3,
}
vars3=[a,b,c]

def solve_linear(names):
    eqs=[lines[n] for n in names]
    return sp.solve(eqs, vars3, dict=True)

pairs={}
for i,left in enumerate(lines):
    for right in list(lines)[i+1:]:
        names=(left,right)
        sols=solve_linear(names)
        key=f"{left}__{right}"
        if not sols:
            # Parallel pair: exact coincidence condition from constants.
            pairs[key]={"kind":"parallel","coincidence":sp.sstr(sp.factor(x1-x2-x3)) if {left,right}=={"g1","g23"} else None}
            continue
        sol=sols[0]
        free=[v for v in vars3 if v not in sol]
        assert len(free)==1,(names,sol,free)
        u=free[0]
        restricted=sp.factor(K.subs(sol))
        poly=sp.Poly(restricted,u)
        disc=sp.factor(sp.discriminant(poly.as_expr(),u))
        pairs[key]={
          "kind":"finite_line",
          "free_variable":str(u),
          "degree":poly.degree(),
          "restriction":sp.sstr(restricted),
          "discriminant":sp.sstr(disc),
          "discriminant_factor_list":[[sp.sstr(f),int(e)] for f,e in sp.factor_list(disc)[1]],
        }

triples={}
names=list(lines)
for i in range(len(names)):
 for j in range(i+1,len(names)):
  for k in range(j+1,len(names)):
   ns=(names[i],names[j],names[k])
   sols=solve_linear(ns)
   key="__".join(ns)
   if not sols:
    triples[key]={"kind":"inconsistent_or_positive_dimensional"}
    continue
   sol=sols[0]
   if len(sol)<3:
    triples[key]={"kind":"positive_dimensional","solution":{str(v):sp.sstr(w) for v,w in sol.items()}}
    continue
   value=sp.factor(K.subs(sol))
   triples[key]={
    "kind":"point",
    "K_value":sp.sstr(value),
    "factor_list":[[sp.sstr(f),int(e)] for f,e in sp.factor_list(value)[1]],
   }

# Face roots: each two-distance triangle has signed linear factors.
faces={
 "site1":[x1-p1,x1+p1],
 "site2":[x2-p2,x2+p2],
 "site3":[x3-p3,x3+p3],
}
hom={x1:p1,x2:p2,x3:p3}
for val in pairs.values():
    if val.get("kind")=="finite_line":
        d=sp.sympify(val["discriminant"],locals={str(v):v for v in [x1,x2,x3,p1,p2,p3]})
        hd=sp.factor(d.subs(hom))
        val["homogeneous_discriminant"]=sp.sstr(hd)
        val["homogeneous_discriminant_factor_list"]=[
            [sp.sstr(f),int(e)] for f,e in sp.factor_list(hd)[1]
        ] if hd != 0 else []
for val in triples.values():
    if val.get("kind")=="point":
        q=sp.sympify(val["K_value"],locals={str(v):v for v in [x1,x2,x3,p1,p2,p3]})
        hq=sp.factor(q.subs(hom))
        val["homogeneous_K_value"]=sp.sstr(hq)
        val["homogeneous_factor_list"]=[
            [sp.sstr(f),int(e)] for f,e in sp.factor_list(hq)[1]
        ] if hq != 0 else []
out={
 "schema":"marici.benincasa.generic_lower_collision.v1",
 "K":sp.sstr(K),
 "K_factor_list":[[sp.sstr(f),int(e)] for f,e in sp.factor_list(K)[1]],
 "lines":{k:sp.sstr(v) for k,v in lines.items()},
 "face_factors":{k:[sp.sstr(v) for v in vals] for k,vals in faces.items()},
 "pairs":pairs,
 "triples":triples,
 "homogeneous_specialization":{"X1":"P1","X2":"P2","X3":"P3"},
}
out_path=Path(r"C:\Users\andrey\src\marici\research\benincasa\generic_lower_collision_result.json")
out_path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print("GENERIC LOWER COLLISION AUDIT PASS")
print(f"pairs={len(pairs)} triples={len(triples)}")
for key,val in pairs.items():
 print("PAIR",key,val.get("degree"),val.get("discriminant"))
for key,val in triples.items():
 print("TRIPLE",key,val.get("K_value"))
