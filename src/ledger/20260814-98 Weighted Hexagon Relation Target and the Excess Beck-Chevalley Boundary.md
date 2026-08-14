# Weighted Hexagon Relation Target and the Excess Beck--Chevalley Boundary

## Record

Date: 2026-08-14

Status: exact finite-nonresonant theorem for the target relation in the
occurrence-weighted hexagon associahedron, together with a sharp source-side
blocker for the full three-pair chain lift.

This entry closes the target half of stage 2 in
`docs/nima-research-objective.md`. It proves that the three-road relation cell
is already present in scalar face geometry. It does **not** construct the
maps from the two conductor top cells to that target.

## Claim

Let \(K_6\) be the three-dimensional associahedron of a labelled hexagon. Its
facets consist of

- the three square long-diagonal road facets
  \(F_{03},F_{14},F_{25}\); and
- the six pentagonal short-diagonal facets.

For a noncrossing dissection \(S\), let \([S]\) denote the corresponding
cell, with \(\dim[S]=3-|S|\). Over the Laurent occurrence ring in the nine
scalar diagonal variables, define

\[
d_X[S]
=
\sum_{a\text{ addable to }S}
\epsilon(S,a)X_a[S\cup\{a\}].
\]

The ordered-normal incidence sign is

\[
\epsilon(S,a)=(-1)^{|\{s\in S:s<a\}|}.
\]

Every codimension-two cell is reached in two orders with equal Laurent
monomial and opposite incidence sign. Hence

\[
\boxed{d_X^2=0.}
\]

Writing

\[
w(S)=\prod_{a\in S}X_a,
\]

the identity

\[
w(S)X_a=w(S\cup\{a\})
\]

conjugates the weighted differential to ordinary cellular incidence. Thus
this is not a fitted complex: it is the scalar associahedral cellular complex
in its canonical occurrence basis.

## The global reciprocal cocycle

On a triangulation \(T\), define

\[
\boxed{
\lambda_{K_6}(T)
=
\left(\prod_{a\in T}X_a\right)^{-1}.
}
\]

This functional kills every weighted edge boundary occurrence by occurrence.
After Laurent diagonal normalization, every flip equation says that the two
endpoint values agree. The fourteen-vertex flip graph is connected, so

\[
H^0\operatorname{Hom}(C_*^{\rm w}(K_6),R_X)\simeq R_X,
\]

and positive value one at one normalized endpoint fixes
\(\lambda_{K_6}\) uniquely.

This global calculation resolves the target-side ambiguity left in entry 97.
On the three road facets, after removing the common physical factor \(X_D^{-1}\)
and pairing the physical normal line \([dX_D]\) positively, its restrictions
are exactly

\[
\begin{array}{c|c}
F_{03}&(x_0,x_1)\boxtimes(x_3,x_4),\\
F_{14}&(x_1,x_2)\boxtimes(x_4,x_5),\\
F_{25}&(x_2,x_3)\boxtimes(x_5,x_0),
\end{array}
\]

with value

\[
\frac1{x_Lx_R}
\]

on each of the twelve road occurrences. These are precisely the three
rotations of entry 97's bivariant trace.

The two no-road triangulations are also fixed rather than freely adjustable.
Their normalized values are one and their raw values are

\[
(x_0x_2x_4)^{-1},
\qquad
(x_1x_3x_5)^{-1}.
\]

This statement concerns the explicit scalar associahedral target. It does
not declare away any additional contact summand in the larger full
\(\operatorname{PC}(\mathsf J_4\boxtimes\mathsf J_6)\) object.

## The relation cell is geometric

Let \(B_{\rm sc}\subset K_6\) be the union of the six short-diagonal
pentagonal facets. A cell survives in the relative complex
\(C_*^{\rm w}(K_6,B_{\rm sc})\) precisely when every diagonal in its
dissection is long.

The three long diagonals cross pairwise. Consequently there are no surviving
edges or vertices, and the relative cellular ranks are

\[
(\operatorname{rk}C_3,
  \operatorname{rk}C_2,
  \operatorname{rk}C_1,
  \operatorname{rk}C_0)
=(1,3,0,0).
\]

After the canonical Laurent normalization and compatible facet orientations,
the remaining differential is

\[
\boxed{
d\mathcal K_{\rm rel}^{\rm PC}
=
\mathcal T_0^{\rm PC}
+\mathcal T_1^{\rm PC}
+\mathcal T_2^{\rm PC}.
}
\]

Here the three target facets correspond to

\[
(u_2,u_5)\to d_0,
\qquad
(u_0,u_3)\to d_1,
\qquad
(u_1,u_4)\to d_2.
\]

Entry 38's target-first face-tube construction applies to this actual
relative face pair. Therefore \(\mathcal K_{\rm rel}^{\rm PC}\) is a scalar
relative-associahedral object, not a formal cone adjoined to force the desired
boundary.

Equivalently, the closed inclusion of the three road facets into \(K_6\)
gives a dual restriction map whose normalized global class restricts to the
three entry-97 classes. The relative and dual-restriction descriptions are
the same target-only construction.

## Rotated local compatibility

The second certificate rotates the entry-97 calculation through all three
opposite normal pairs while keeping its layers separate:

- the scalar occurrence variables \(x_j\);
- the six independent monodromies \(q_j\) and \(u_j=q_j-1\);
- reciprocal-twist regular support versus original-twist locally finite
  support;
- the ordered normal wedges;
- the polarity/core character \(\chi_N\); and
- the independent positive physical normal \([dX_D]\).

For all three pairs it verifies

\[
u_j^\vee=-q_j^{-1}u_j,
\qquad
\beta_j(p_j,h_j^\vee)=1,
\qquad
\beta_j(h_j,p_j^\vee)=-q_j,
\]

as well as unit primitive occurrences, sheet value two, vanishing endpoint
difference, and polarized road value four. No numeric denominator and no
identification of distinct normal characters is used.

Thus the target relation and every pair-local trace are now established. The
remaining problem is their source-side comparison.

## Sharp blocker: six excess-one source attachments

The two normalization branches have normal ideals

\[
I_+=(u_1,u_3,u_5),
\qquad
I_-=(u_0,u_2,u_4),
\]

while the three local traces have pair ideals

\[
I_0=(u_2,u_5),
\qquad
I_1=(u_0,u_3),
\qquad
I_2=(u_1,u_4).
\]

Every branch/pair combination shares exactly one normal generator. It is
therefore nonnested and excess one. If

\[
S_{\pm i}=R/(I_\pm+I_i),
\]

the exact Koszul calculation is

\[
\operatorname{Tor}_k^R(R/I_\pm,R/I_i)
\simeq
\begin{cases}
S_{\pm i},&k=0,1,\\
0,&\text{otherwise},
\end{cases}
\]

and

\[
\operatorname{Ext}^k_R(R/I_\pm,R/I_i)
\simeq
\begin{cases}
S_{\pm i},&k=2,3,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular, direct \(\operatorname{Hom}\) and \(\operatorname{Ext}^1\)
vanish. The carrier incidence

\[
K_{\rm alt}d_2=\Delta(1,-1)
\]

therefore does not itself define the loaded PC attachment. Each of the six
branch/pair squares requires an excess Beck--Chevalley comparison carrying
the rank-one \(\operatorname{Tor}_1\) orientation, occurrence pullback,
reciprocal/Borel--Moore support pairing, and lower Cousin terms.

The full source top square remains untyped:

\[
\boxed{
\rho\,a_\pm
\overset{?}{=}
\bigoplus_{i=0}^2
\operatorname{Tr}_{i,\partial}^{\rm PC}\,
\partial_{\pm i}.
}
\]

The target restriction \(\rho\), the three local traces, and the associated
carrier identity are known. The maps \(a_\pm\) are not. They may not be
defined by the displayed equality.

## Rejected shortcuts

Three tempting simplifications fail or are unnecessary:

1. A formal cone on
   \(\mathcal T_0+\mathcal T_1+\mathcal T_2\) is unnecessary because the
   relative associahedron already supplies the target relation. It would not
   solve the source attachment.
2. A branch codimension-three Gysin class cannot be restricted directly to
   an opposite cross-sheet pair. Its codimension-two faces are same-sheet;
   the desired comparison has the excess \(\operatorname{Tor}_1\) term.
3. The perfect-matching products
   \((x_2x_5,x_0x_3,x_1x_4)\), or their product-monodromy analogues, have the
   wrong support. They replace a codimension-two intersection by a reducible
   union or a rank-one product-character hypersurface and erase the ordered
   two-normal wedge.

Nonresonant inversion can contract the Koszul complexes, but doing so erases
the support filtration in which the source lift must be constructed.

## Evidence

Exact certificates:

- `research/voevodsky/check_d03_relative_associahedron_pc.rs`
- `research/voevodsky/check_d03_three_pair_pc_extension.rs`

SHA-256:

```text
86675e9e5470ff04b840fad264d64a34d90eca77f9c205bb83dee4316f9c0993
b426e863eaddf3cde8e806dd5be65f6b1215a7793dab38592281a3bd09f4de21
```

The first checker proves the \((1,9,21,14)\) face census, weighted
\(d^2=0\), Laurent normalization, the unique global reciprocal cocycle, both
central values, all twelve road restrictions, the relative rank vector, and
the three-term relation boundary. The second proves the rotated occurrence,
twist, normal-orientation, endpoint, and carrier identities and computes the
six excess Tor/Ext patterns.

Reproduce with:

```powershell
$sources = @(
  "research/voevodsky/check_d03_relative_associahedron_pc.rs",
  "research/voevodsky/check_d03_three_pair_pc_extension.rs"
)
foreach ($src in $sources) {
  $exe = Join-Path $env:TEMP ((Split-Path $src -LeafBase) + ".exe")
  rustfmt --edition 2021 --check $src
  rustc --edition=2021 -D warnings -O $src -o $exe
  & $exe | ConvertFrom-Json | Out-Null
}
```

Inherited Marici inputs are entries 38, 86, and 93--97.

## Consequence and next formula

The next move is singular. Construct one excess comparison, beginning with
the plus branch and the \(D=03\) pair:

\[
I_+=(u_1,u_3,u_5),
\qquad
I_{03}=(u_0,u_3).
\]

It must be derived from the actual normalization--conductor and face-tube
square, not from the desired target equation. Its first test is

\[
\boxed{
\rho_{03}a_+^{\rm ex}
=
\operatorname{Tr}_{03,\partial}^{\rm PC}
\,\partial_{+,03},
}
\]

with the excess orientation, occurrence weights, reciprocal twist, lower
Cousin boundary, and physical normal line all retained. Only after this one
square passes should it be rotated to the remaining five attachments and
assembled into the full \((f_+,f_-)\mapsto(+1,-1)\) top map.

The research state is therefore

\[
\boxed{
\text{geometric target relation: proved},
\qquad
\text{source excess comparison: open}.
}
\]

## Outcome contract

```json
{
  "claim": "The weighted hexagon associahedron, relative to its six short-diagonal facets, canonically supplies the three-road PC relation target and its normalized global reciprocal cocycle.",
  "status": "proved",
  "assumptions": [
    "Entry 38 applies to the actual labelled-hexagon face complex with ordered normal orientations.",
    "Scalar occurrence variables are Laurent-normalized while monodromy variables remain a separate PC coefficient layer.",
    "The relative boundary is the union of the six short-diagonal pentagon facets."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_relative_associahedron_pc.rs",
    "research/voevodsky/check_d03_three_pair_pc_extension.rs",
    "ledger entries 38, 86, and 93-97"
  ],
  "factorization_test": {
    "target_relation": "passed",
    "three_rotated_local_traces": "passed",
    "source_top_square": "untyped because all six branch/pair intersections have rank-one excess"
  },
  "counterevidence": [
    "The target theorem does not construct either conductor-top source map.",
    "The theorem does not remove the contact kernel of a larger full PC object.",
    "A direct branch-to-pair attachment misses the nonzero Tor_1 excess class."
  ],
  "next_experiment": "Construct the plus-sheet/D03 excess Beck-Chevalley comparison and test its boundary against the entry-97 trace before using cyclic symmetry."
}
```
