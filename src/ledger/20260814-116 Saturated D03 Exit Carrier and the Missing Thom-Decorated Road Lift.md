# Saturated D03 Exit Carrier and the Missing Thom-Decorated Road Lift

## Record

Date: 2026-08-14

Status: one proved integral carrier theorem and one sharp falsifier.  The
central positive dual cell is canonically identified with the physical
\(F_{03}\) relative facet, and its oriented boundary is the required
two-road difference.  The existing graph-base-changed absolute scalar
complex does not lift this carrier column to the required Cartier
\(\operatorname{Tor}_1\) column.  The missing Rees conormal must be carried
externally by an extraordinary/Thom correspondence.

## The canonical carrier column

Let the positive central vertex be

\[
v_+=\{x_1,x_3,x_5\}.
\]

In its reversed Boolean coface interval, use the masks

\[
f_+=111,
\qquad
e_3=101,
\qquad
q_0=100,
\qquad
q_2=001.
\]

Thus

\[
e_3=\{x_1,x_5\},
\qquad
q_0=\{x_5\},
\qquad
q_2=\{x_1\}.
\]

The inherited exterior orientation gives

\[
\boxed{
d_{\rm PL}e_3=-q_0+q_2.
}
\]

This is not merely the abstract column of a previously chosen triangle
matrix.  For

\[
A=\{v_+\}\subset B_{\rm short}\subset K_6,
\]

the exact-couple boundary sends the three genuine relative facets
\(F_{14},F_{03},F_{25}\) to their peripheral cycles in
\(H_1(B_{\rm short},A)\).  Any two of those cycles extend the short-facet
boundaries by a unimodular maximal minor.  Hence the connecting map is a
saturated integral isomorphism.

A \(D_3\)-equivariant candidate on the three permutation modules has the
form

\[
M(a,b)=aI+b(J-I),
\qquad a+2b=1.
\]

On the augmentation-zero \(A_2\) lattice it acts by

\[
a-b=1-3b.
\]

Saturation requires \(|1-3b|=1\).  The negative choice has no integral
solution, while the positive choice forces \(b=0\).  Therefore the inverse
peripheral transgression is unique and sends

\[
\boxed{
e_3\longleftrightarrow F_{03}.
}
\]

This is a cone-roof/exact-couple transgression, not a literal inclusion of
the central dual block into the long facet.

Together with entry 112's whole-gallery costalk normalization, the
unloaded associated carrier is therefore intrinsic:

\[
- [n_{03}]
\longmapsto e_3
\longmapsto -q_0+q_2.
\]

## The occurrence boundary is still intrinsic

Before evaluating the labelled principal occurrence lines, the dual-cell
boundary is

\[
\boxed{
d_{\rm occ}e_3=-x_1q_0+x_5q_2.
}
\]

The first term is dual to adding \(x_1\) to
\(q_0=\{x_5\}\); the second is dual to adding \(x_5\) to
\(q_2=\{x_1\}\).  Principal-line duality can evaluate these labelled
coefficients integrally.  It neither inverts an occurrence variable in the
base nor supplies an unrelated normal direction.

## Why the existing multi-Rees lift fails

After the independent graph base change

\[
u_3=t_3x_3,
\]

the \(x_3\)-part of the absolute differential factors as

\[
d_3=x_3B_3,
\qquad
B_3=\delta_3^{\rm rad}+t_3\delta_3^{\rm nor}.
\]

This factorization is canonical, and the full multi-Cartier Bocksteins
remain square-zero and mutually anticommuting.  It nevertheless does not
produce the desired loaded road column.

The exact reason is the facewise normal rule in the absolute scalar
complex:

\[
H\subseteq S.
\]

All three relevant carrier cells omit \(x_3\):

\[
x_3\notin e_3,q_0,q_2.
\]

Consequently none admits an \(h_3\) normal-circle generator.  More
explicitly:

- \(\delta_3^{\rm rad}\) is the incidence
  \(e_3\leftrightarrow f_+\);
- \(t_3\delta_3^{\rm nor}\) acts only on cells whose support already
  contains \(x_3\);
- the normal block is therefore zero on \(e_3,q_0,q_2\); and
- the established carrier sends the lower source cells
  \(q_0,q_1,q_2\) to zero, not to the actual reciprocal/Borel--Moore road
  costalks.

Thus the implication

\[
\text{full }P_{\rm abs}\text{ Bockstein}
+\text{ existing cone roof}
\quad\Longrightarrow\quad
-[n_{03}]\mapsto[t_3](-\tau_{q_0}+\tau_{q_2})
\]

is false.

This is not a no-go for the desired half-object.  It locates its missing
geometric type.  The factor \([t_3]\) cannot be an internal normal circle
of the endpoint cells.  It must be the Thom/conormal line of the
correspondence carrying the oriented dual-cell boundary to the road
costalks.

## Corrected next object

The minimal candidate should have a carrier shadow of the form

\[
\operatorname{Th}^{\rm mR}_{x_3}\otimes
\left[
\mathbb Z\langle e_3\rangle
\xrightarrow{(-1,+1)}
\mathbb Z\langle q_0,q_2\rangle
\right],
\]

with the occurrence-line refinement

\[
e_3\longmapsto -x_1q_0+x_5q_2.
\]

It must then provide extraordinary endpoint maps

\[
q_0\longmapsto\tau_{q_0},
\qquad
q_2\longmapsto\tau_{q_2},
\]

while carrying the single external Rees conormal \([t_3]\) across both
terms.  Equivalently, construct a marked correspondence

\[
\Gamma_{+,03}^{!,\rm mR}
\]

whose:

1. generic leg factors through the saturated cone-roof transgression
   \(e_3\leftrightarrow F_{03}\);
2. special boundary is the actual occurrence-loaded dual-cell boundary;
3. Thom line is \([t_3]\), external to the endpoint face supports;
4. endpoint values are the actual reciprocal/Borel--Moore road
   \(\operatorname{Tor}_1\) costalks;
5. excess, physical normal, and twist reversal agree with entry 100; and
6. Beck--Chevalley comparison intertwines the two length-two paths in the
   carrier/Cartier bicomplex.

Only after this construction exists is it meaningful to test
\(H_\Sigma\), the Yoneda cone roof, the residual \(\mathbb Z/2\) parity,
the negative sheet, or physical-Cut naturality.

## Evidence

New exact certificate:

- `research/voevodsky/check_d03_exit_spatial_kernel.rs`, SHA-256
  `52586b7ced2d0ed4bcb80d25fe5922a6e3e6ef5e04d42dddcf465e5ce62b8e26`.

The checker reconstructs the labelled \(K_6\) face complex, the saturated
peripheral connector, the unique inverse transgression, the central
dual-cell and occurrence boundaries, the exact support masks, the
\(H\subseteq S\) normal-circle rule, the two blocks of \(B_3\), and the
established source-to-road carrier map.

Reproduce with `rustfmt --check`,
`rustc --edition 2021 -D warnings -O`, execution of the certificate, JSON
parsing, and `git diff --check`.

## Outcome contract

```json
{
  "claim": "The D03 carrier column is intrinsic: saturated inverse peripheral transgression identifies e3 with F03 and its oriented dual-cell boundary is -q0+q2. The existing graph-base-changed P_abs Bockstein does not lift this to the required [t3]-valued road Tor column because e3, q0, and q2 omit x3 and therefore carry no h3 normal generator; the lower q-cells also have zero established map to actual road costalks.",
  "status": "falsified",
  "assumptions": [
    "The carrier theorem and falsifier use the established D3 labels and orientations.",
    "Occurrence, Rees, monodromy, and physical-normal lines remain distinct.",
    "The falsifier is scoped to the existing P_abs Bockstein and cone roof, not to a new extraordinary correspondence."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_exit_spatial_kernel.rs",
    "ledger entries 100, 105, 112, and 115"
  ],
  "factorization_test": {
    "saturated_carrier_column": "proved",
    "occurrence_loaded_boundary": "proved",
    "x3_normal_on_e3_q0_q2": "absent by exact support census",
    "existing_P_abs_loaded_lift": "falsified",
    "new_extraordinary_Thom_lift": "unconstructed",
    "full_G03_Cousin": "unconstructed"
  },
  "counterevidence": [
    "The lower source q-cells are not actual road costalks.",
    "The normal part of the x3-Cartier Bockstein cannot act on supports omitting x3.",
    "An external tensor product reproduces the desired symbol but does not construct its spatial realization."
  ],
  "next_experiment": "Construct the Thom-decorated extraordinary D03 dual-cell correspondence carrying external [t3] and the x1/x5 occurrence lines to the two actual reciprocal/BM road Tor1 costalks; then test the loaded Beck-Chevalley square."
}
```
