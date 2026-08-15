---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Literal Six-Term Source Periods on Every Lower Collision Component

## Record

Date: 2026-08-15

Status: exact completion packet for the source-weighted local-period clause of
the generic lower-sector physical-activation theorem.

This entry strengthens entry 196. Entry 196 proved the physical
Picard--Lefschetz projection for every cyclic collision but used one explicit
source-weighted period as a representative of the finite quadratic family.
Here the literal six-term residue is computed separately for all five finite
marked pairs and all ten irreducible components of each discriminant.

No source denominator, normalization, support summand, or carrier cell was
changed.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

[
oxed{
	ext{No finite lower-sector discriminant component is silently removed by
the literal six-term source weight before physical PL projection.}
}
]

The finite falsifier was the first pair/component for which the exact
Grothendieck residue at the Cayley--Menger double root was identically zero,
identically polar, or required a different local model.

## Frozen source and residue rule

With

[
L_1=X_1+c+b,quad L_2=X_2+c+a,quad L_3=X_3+a+b,
]

[
L_{12}=X_1+X_2+a+b,quad
L_{23}=X_2+X_3+c+b,quad
L_{31}=X_3+X_1+c+a,
]

and

[
G_{12}=E+c,quad G_{23}=E+a,quad G_{31}=E+b,
]

the frozen source is

[
Omega_{m src}
=
rac{abc}{E L_1L_2L_3}
left[
rac1{G_{12}L_{23}}+rac1{G_{12}L_{31}}
+rac1{G_{23}L_{31}}+rac1{G_{23}L_{12}}
+rac1{G_{31}L_{12}}+rac1{G_{31}L_{23}}
ight].
]

For each finite pair ((q_i,q_j)), the verifier forms the termwise
Grothendieck residue

[
R_{ij}(u)
=
operatorname{Res}_{q_i=q_j=0}Omega_{m src}.
]

Termwise cancellation is essential: a source term contributes only if its
denominator actually contains both marked factors. This avoids the spurious
(0cdotinfty) values produced by substituting a partial pole before taking
the residue.

On the marked line, the frozen Cayley--Menger polynomial is

[
K_{ij}(u)=A_{ij}u^2+B_{ij}u+C_{ij},
]

with double root

[
u_*=-rac{B_{ij}}{2A_{ij}}.
]

The local period at exponent (chi=-1/2) is therefore

[
oxed{
Pi_{ij,f}
=
C_delta
rac{R_{ij}(u_*)}{sqrt{A_{ij}}}
}
]

on every irreducible discriminant component (f=0).

## Exact census

The five finite pairs in the frozen sector are

[
(g_1,g_2),quad
(g_1,g_3),quad
(g_2,g_3),quad
(g_2,g_{23}),quad
(g_3,g_{23}).
]

Each has ten exponent-one discriminant factors. For every one of the fifty
pair/component occurrences, the verifier records:

- the exact restricted quadratic coefficients (A,B,C);
- the exact double-root formula;
- the exact termwise residue (R_{ij}(u));
- an exact rational point on the named irreducible component;
- the exact nonzero values of (A_{ij}) and (R_{ij}(u_*));
- the exact rational value
  [
  R_{ij}(u_*)^2/A_{ij},
  ]
  which is the period square modulo the universal cycle constant.

The result is

[
oxed{
50 	ext{finite nonzero local periods},
qquad
0 	ext{source-weight zeros},
qquad
0 	ext{generic source-pole overlaps},
qquad
0 	ext{degree-drop exceptions}.
}
]

One exact finite nonzero rational witness proves that the restricted rational
coefficient is neither identically zero nor identically polar on that
irreducible component. The calculation supplies such a witness for every
component, not merely one witness per factor class.

Simultaneous cyclic relabeling preserves the Cayley--Menger polynomial and
the six-term source. Hence the exact closure is

[
3 	ext{cyclic sectors},
qquad
15 	ext{finite pairs},
qquad
150 	ext{nonzero local-period occurrences}.
]

## Physical projection

The result concerns the analytically continued coefficient-side vanishing
period. It does not alter entry 188's physical-chain result:

[
leftlangleGamma_{m BD},delta^eeightangle=0
]

for every marked collision. Consequently

[
operatorname{Var}_{f}(Gamma_{m BD})
=
leftlangleGamma_{m BD},delta^eeightangledelta
=
0
]

for all 150 occurrences despite their nonzero local periods.

Thus the separation is now exhaustive:

[
oxed{
	ext{nonzero local coefficient period}
;
otRightarrow;
	ext{physical-sheet activation}.
}
]

The physically active fixed-base Gram Kummer of entry 189 remains an
independent semisimple orientation effect, not a marked-collision
Picard--Lefschetz transvection.

## Endpoint and overlap qualification

The site-face factors appearing in the finite discriminants do not force the
finite quadratic residue itself to vanish or drop degree at a generic point
of that divisor. Literal positive-domain faces, distance-zero vertices,
soft/Gram corners, parallel coincidences, and triple-marked intersections
remain the separately resolved strata classified in entries 188, 193, and
195.

This entry therefore closes the missing source-weight audit without
reclassifying those boundary strata.

## Classification

The complete finite-collision result is:

| Object | Local coefficient period | Physical PL jump | Class |
|---|---:|---:|---|
| 150 cyclic finite components | nonzero | zero | marked-relative coefficient support |
| Physical Heron orientation cover | semisimple sign | active | Kummer coefficient on existing Gram carrier |
| Endpoint/face/soft overlaps | as in entries 193 and 195 | no new transvection | existing CM/soft carrier |
| Graph homology | not generated here | none assigned | separate (H_1) topology |
| New carrier datum | absent | absent | zero occurrences |

The narrow surviving theorem is therefore

[
oxed{
egin{gathered}
	ext{every generic finite lower collision carries a nonzero literal-source
local period,}\
	ext{every such period has zero Bunch--Davies PL intersection,}\
	ext{and no such component requires new carrier incidence.}
end{gathered}
}
]

## Exact evidence

- `research/benincasa/verify_all_lower_source_periods.py`
  - exact termwise residue and component-witness verifier;
- `research/benincasa/all_lower_source_periods_result.json`
  - SHA-256
    `343edba217ec8089726cc16f0c6eb6318f3651cdf716c4fc5c24997e5d375a62`;
- `research/benincasa/verify_global_lower_physical_activation.py`
  - now freezes and requires the complete period census;
- `research/benincasa/global_lower_physical_activation_result.json`
  - SHA-256
    `8e4f6061c11698761e06d1b77aa52d8004b7a9f67982c94f4696dabbe81018fd`.

## Narrow conclusion

The strict completion gap in entry 196 is closed. Its global carrier theorem
survives a component-by-component literal-source audit. The lower sector
contains coefficient-side algebraic variation everywhere in the finite
collision census, but the Bunch--Davies positive chain projects every such
Picard--Lefschetz variation to zero. No first counterexample to the unchanged
energy/Cut/Cayley--Menger carrier appears.
