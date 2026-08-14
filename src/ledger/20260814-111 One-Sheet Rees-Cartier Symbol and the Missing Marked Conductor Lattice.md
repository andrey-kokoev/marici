# One-Sheet Rees--Cartier Symbol and the Missing Marked Conductor Lattice

## Record

Date: 2026-08-14

Status: exact integral theorem for the residual occurrence-line diagram and
the filtered algebraic comparison; conditional as a geometric conductor
map. A strict post-Cartier map to the uniformly filtered free tag complex is
falsified.

## Claim

Let \(R\) be the unlocalized polynomial occurrence ring and let
\(I_3=(x_3)\). After entry 110's endpoint-and-generic-relative reduction, the
expanded \(D03\) gallery has the seven principal coefficient stalks

\[
\begin{array}{c|ccccccc}
\sigma&a&e_c&b_1&h_E&b_D&e_r&c\\ \hline
\mathcal L_\sigma&
(x_1x_5)&(x_1)&(X_{03}x_1)&(X_{03}x_1)&
(X_{03}x_1)&(X_{03})&(X_{03}x_0).
\end{array}
\]

Every unsigned incidence map sends the chosen generator of its source ideal
to the chosen generator of its target ideal. The generator-dual evaluations
therefore form a natural cap on the whole diagram. Because its incidence
graph is connected, compatible integral trivializations are unique up to one
common sign; the positive orientation selects the positive family. This is
one constructible coefficient object, not three independently chosen
divisions.

Suppose, in addition, that a marked geometric correspondence supplies the
cell map

\[
(e_c,h_E,e_r)\longmapsto(t_1,t_3,t_5),
\qquad
(a,b_1,b_D,c)\longmapsto(q_1,q_0,q_2,q_1),
\]

with the orientations of entries 93--94. Then the natural cap gives a strict
lower chain map \(\phi\), and

\[
\phi(\xi)=\Delta,
\qquad
\Delta=t_1+t_3+t_5=d f_+.
\]

Both endpoints map to \(q_1\), so this descends after taking the matching
endpoint-relative source and \(q_1\)-relative target.

The pre-Cartier residual source has the two-level form

\[
C_{\rm res}=[R H\xrightarrow{-x_3\xi}L].
\]

The correct target is not initially the uniformly filtered free complex. It
is the shifted principal-ideal lattice

\[
\boxed{
C_{\rm tag}^{\langle1\rangle}
=[I_3 f_+\xrightarrow{d}P_{\rm tag}],
\qquad d(x_3f_+)=x_3\Delta .
}
\]

There is then a unique strict integral chain map

\[
\boxed{
\widetilde\kappa_{+,03}(H)=-x_3f_+,
\qquad
\widetilde\kappa_{+,03}|_L=\phi .
}
\]

Indeed,

\[
d(-x_3f_+)=-x_3\Delta
=\phi(-x_3\xi).
\]

Equivalently, retain the free target but give it the staggered filtration

\[
F_T^p(Rf_+)=x_3^{p+1}Rf_+,
\qquad
F_T^p(P_{\rm tag})=x_3^pP_{\rm tag},
\]

while the source has the uniform filtration

\[
F_S^pC_{\rm res}=x_3^pC_{\rm res}.
\]

The map has filtered degree zero and both top differentials have filtration
order one. Its first Rees/Cartier symbol is

\[
\bar H\longmapsto-[x_3]\otimes f_+
\quad\text{in}\quad
(I_3/I_3^2)\otimes f_+.
\]

Only after the positive conormal evaluation

\[
x_3^\vee:I_3/I_3^2\longrightarrow R/I_3,
\qquad x_3^\vee([x_3])=1,
\]

does this become

\[
\boxed{\bar H\longmapsto-f_+.}
\]

Thus the desired top map is a first Cartier symbol with its conormal line
retained. It is not the degree-zero differential of the ordinary associated
graded complex.

## The exact no-go

If the target is instead given the uniform \(I_3\)-adic filtration, the
image \(-x_3f_+\) lies in filtration one and its degree-zero symbol is zero.
After the Bockstein, a nonzero strict map from the torsion top source to a
free target is impossible:

\[
\operatorname{Hom}_R(R/(x_3),R)=0.
\]

Consequently, a formula that writes \(\bar H\mapsto-f_+\) while omitting the
conormal factor, the staggered lattice, or an equivalent
\(\operatorname{Ext}^1\)/Gysin variance has silently divided by \(x_3\).

## Provenance boundary

Entries 93--94 do not independently construct either of the two remaining
geometric inputs:

1. the marked gallery-to-triangle correspondence displayed above;
2. the target lattice \(I_3f_+\) as the actual conductor/Rees filtration.

Entry 93 supplies the sheet-resolved first conormal symbol and polarity
line. Entry 94 supplies the augmented triangle, the \(D03\) occurrence
counits, and the associated-grade primitive normalization. Those data are
compatible with the filtered map, but compatibility is not provenance.
Defining the staggered filtration only because it makes the square commute
would be a fitted regrading.

There is also a sharp label-level falsifier for the most tempting derivation
of the cell map. The actual expanded gallery edges are

\[
e_c=\{x_1,x_3\},
\qquad
h_E=\{E,x_3\},
\qquad
e_r=\{D03,x_3\}.
\]

Thus \(x_3\) is common to all three edges and cannot select \(h_E\). The
exceptional ray has

\[
q_E=q_{03}q_1,
\]

so it belongs to the blowup of \((D03,x_1)\), not to the positive conductor
normal \(dx_3\). Entry 94's \(dx_3\mapsto d_1\) and road--costalk pairing do
not contain a map \(h_E\mapsto d_1\). Using them as such assumes the missing
comparison. Cyclic symmetry rotates the entire gallery to another physical
road; it does not permute \(e_c,h_E,e_r\) inside this blowup.

No negative-sheet map, alternating six-term assembly, physical Gysin
naturality, global Yoneda specialization, or CHY identification follows from
this entry.

## Evidence

Exact certificate:

- `research/voevodsky/check_d03_one_sheet_cartier_conductor.rs`

SHA-256:

```text
cf736e77f61505848dbbf1deb3cf95f308513c239b6df7634d1262b011a48358
```

It verifies the seven-stalk lcm diagram, natural dual cap, uniqueness up to
orientation, conditional lower matrix and endpoint-relative descent, strict
pre-Cartier map, staggered Rees filtration through powers \(0\) to \(5\),
first conormal symbol, orientation sign, and both free-target no-go tests.

Reproduce with:

```text
rustfmt --edition 2021 --check research/voevodsky/check_d03_one_sheet_cartier_conductor.rs
rustc --edition=2021 -D warnings -O research/voevodsky/check_d03_one_sheet_cartier_conductor.rs -o "$env:TEMP\\marici-one-sheet-cartier-conductor.exe"
& "$env:TEMP\\marici-one-sheet-cartier-conductor.exe"
```

## Consequence

The direct gallery-to-full-triangle formula remains a valid discriminating
test, but it is no longer the simplest construction. The existing geometry
canonically labels the **whole** \(D03\) road by the positive conductor
direction \(d_1\); it does not label the three internal subdivision edges by
the three conductor directions.

The economical objective is therefore:

\[
\boxed{
\kappa^{\rm edge}_{+,03}:
\beta_{x_3}^{\rm Cart}(B_{+,03})
\longrightarrow Rt_3,
\qquad
\kappa^{\rm edge}_{+,03}(-[\widetilde\xi])=+t_3,
}
\]

constructed as an exit-poset/cosheaf Gysin map for the whole marked gallery,
not by assigning its three segments to three tags. Rotate this construction
to the whole roads \(F_{14},F_{03},F_{25}\) and obtain

\[
\kappa^{\rm edge}_{+}
=
\kappa^{\rm edge}_{+,14}
\oplus
\kappa^{\rm edge}_{+,03}
\oplus
\kappa^{\rm edge}_{+,25}
\longrightarrow
R\langle t_1,t_3,t_5\rangle.
\]

Only at that stage should one test whether the three source tops glue to a
single conductor two-cell with boundary

\[
df_+=t_1+t_3+t_5
\]

and whether its actual Rees lattice is \(I f_+\). This separates the two
missing claims: local road-to-tag provenance first, global triangle-top
coherence second. If an independent ringed span instead derives the stronger
segmentwise map, the filtered theorem above applies immediately; it should
not be assumed in advance.

## Outcome contract

```json
{
  "claim": "The expanded D03 residual occurrence diagram has a natural integral dual cap. Conditional on a marked gallery-to-triangle correspondence and the geometric target lattice I3*f_+, it induces a unique strict pre-Cartier map H -> -x3*f_+ whose first Rees symbol becomes -f_+ only after oriented conormal evaluation.",
  "status": "conditional",
  "assumptions": [
    "The marked cell correspondence from the expanded gallery to the positive triangle is geometric rather than assigned.",
    "The normalization-conductor specialization independently supplies the staggered target lattice I3*f_+.",
    "Occurrence x3 remains distinct from monodromy u3."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_one_sheet_cartier_conductor.rs",
    "ledger entries 93, 94, and 110"
  ],
  "factorization_test": {
    "natural_lcm_dual_cap": "passed, unique up to one common sign",
    "conditional_lower_triangle_map": "passed under the named marked-cell input",
    "strict_pre_Cartier_map": "passed integrally",
    "staggered_Rees_symbol": "passed",
    "ordinary_uniform_associated_grade": "zero",
    "post_Cartier_strict_free_target_map": "falsified by Hom_R(R/(x3),R)=0",
    "geometric_staggered_lattice": "unconstructed",
    "attempted_segmentwise_geometric_derivation": "falsified: x3 is a common spectator and E is the (D03,x1) blowup ray",
    "full_one_sheet_kappa": "unconstructed"
  },
  "counterevidence": [
    "Entries 93-94 contain no target filtration with top lattice I3*f_+.",
    "A nonzero map from the post-Bockstein torsion source to the free target cannot be R-linear.",
    "The current gallery-to-triangle cell matching remains an explicit input.",
    "Entry94 labels the whole D03 road by d1; it does not label the exceptional middle edge h_E by d1."
  ],
  "next_experiment": "First construct a marked exit-poset/cosheaf Gysin map from the whole D03 Cartier gallery class to the single positive tag t3, rotate it to t1 and t5, and only then test whether the three tops glue to the triangle relation with a geometrically supplied Rees lattice."
}
```
