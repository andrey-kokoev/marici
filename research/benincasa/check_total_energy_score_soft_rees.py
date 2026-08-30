"""Forced Rees limits of the three labelled total-energy score ports."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
x, y, s = sp.symbols("x y s")


def load_matrix(path: Path, key_path: tuple[str, ...]) -> sp.Matrix:
    data = json.loads(path.read_text())
    node = data
    for key in key_path:
        node = node[key]
    return sp.Matrix([[sp.sympify(value, locals={"x":x,"y":y}) for value in row] for row in node])


def exceptional(matrix: sp.Matrix, face: str) -> sp.Matrix:
    if face == "x":
        return sp.Matrix(3,3,lambda i,j: sp.factor((x**(i+j)*matrix[i,j]).subs(x,0)))
    if face == "y":
        return sp.Matrix(3,3,lambda i,j: sp.factor((y**(i+j)*matrix[i,j]).subs(y,0)))
    if face == "x+y":
        changed=matrix.subs(y,s-x)
        return sp.Matrix(3,3,lambda i,j: sp.factor((s**(i+j)*changed[i,j]).subs(s,0)))
    raise ValueError(face)


def normalized_family(matrix: sp.Matrix, face: str) -> tuple[sp.Matrix, sp.Symbol]:
    weights=sp.diag(1,1,1)
    if face == "x":
        normal=x; changed=matrix
    elif face == "y":
        normal=y; changed=matrix
    elif face == "x+y":
        normal=s; changed=matrix.subs(y,s-x)
    else:
        raise ValueError(face)
    weights=sp.diag(1,normal,normal**2)
    return weights*changed*weights, normal


def regular_at_zero(value: sp.Expr, normal: sp.Symbol) -> bool:
    _numerator, denominator=sp.fraction(sp.cancel(value))
    return sp.factor(denominator.subs(normal,0)) != 0


def main() -> None:
    g3=load_matrix(HERE/"total-energy-kummer-source-word-scores.json",("hankel_matrix",))
    g1=load_matrix(HERE/"total-energy-tangency-port-recovery.json",("ports","g1","hankel_matrix"))
    g2=load_matrix(HERE/"total-energy-tangency-port-recovery.json",("ports","g2","hankel_matrix"))
    ports={"g1":g1,"g2":g2,"g3":g3}
    faces={}
    for face in ("x","y","x+y"):
        matrices={name:exceptional(matrix,face) for name,matrix in ports.items()}
        families={name:normalized_family(matrix,face) for name,matrix in ports.items()}
        stacked=matrices["g1"].col_join(matrices["g2"]).col_join(matrices["g3"])
        faces[face]={
            "port_matrices":{name:[[str(v) for v in row] for row in matrix.tolist()]
                             for name,matrix in matrices.items()},
            "port_ranks":{name:int(matrix.rank()) for name,matrix in matrices.items()},
            "exceptional_determinants":{name:str(sp.factor(matrix.det()))
                                          for name,matrix in matrices.items()},
            "all_normalized_entries_regular":{
                name:all(regular_at_zero(value,normal) for value in family)
                for name,(family,normal) in families.items()
            },
            "local_DVR_isomorphism":{
                name:(all(regular_at_zero(value,normal) for value in family)
                      and matrices[name].det()!=0)
                for name,(family,normal) in families.items()
            },
            "stacked_rank":int(stacked.rank()),
            "stacked_kernel_dimension":3-int(stacked.rank()),
        }
    result={
        "schema":"marici.benincasa.total-energy-score-soft-rees.v1",
        "forced_weights":{
            "score_row_i":"normal_weight_i",
            "source_word_column_j":"normal_weight_j",
            "entry_ij":"multiply by normal^(i+j) before restriction",
        },
        "faces":faces,
        "all_joint_exceptional_kernels_zero":all(row["stacked_kernel_dimension"]==0 for row in faces.values()),
        "all_ports_are_local_DVR_isomorphisms":all(
            all(row["local_DVR_isomorphism"].values()) for row in faces.values()
        ),
        "observer_cartier_cokernel_length":0,
        "scope":(
            "associated Rees grade of the scalar labelled score cospan; full "
            "nearby-cycle extensions and tensor/polarization ports are not computed"
        ),
    }
    rendered=json.dumps(result,indent=2,sort_keys=True)+"\n"
    (HERE/"total-energy-score-soft-rees.json").write_text(rendered)
    print(rendered,end="")


if __name__=="__main__":
    main()
