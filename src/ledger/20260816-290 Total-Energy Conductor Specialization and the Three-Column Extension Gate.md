---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Total-Energy Conductor Specialization and the Three-Column Extension Gate

## Result

The marked conductor quotient at total energy has trivial internal
monodromy, and its specialization kernel is exactly the primitive top
cycle.

For the two frozen walls write

\[
R_1(t)=xt^2+D_1(E),
\qquad
R_2(t)=yt^2+D_2(E).
\]

Direct substitution of \(z=E-x-y\) into the source square restrictions
gives

\[
\boxed{
D_1(E)=-E^3+(x+2y)E^2-2xyE-xy^2,
}
\]

\[
\boxed{
D_2(E)=-E^3+(2x+y)E^2-2xyE-x^2y.
}
\]

Consequently,

\[
D_1(0)=-xy^2,
\qquad
D_2(0)=-x^2y,
\]

and both wall-node discriminants remain units at generic nonsoft
total-energy kinematics:

\[
\boxed{
\Delta_{W_1}(0)=\Delta_{W_2}(0)=4x^2y^2\neq0.
}
\]

The two roots on \(W_1\) specialize to \(\pm y\), and those on
\(W_2\) specialize to \(\pm x\). Their occurrence labels continue
analytically around \(E=0\) without permutation.

The same-sheet points satisfy

\[
\Lambda=E(E-2x)(E-2y).
\]

Although they collide at \(E=0\), their labels \(w=\pm\Lambda\) are
also analytic and do not exchange. Thus on the generic rank-three
conductor quotient,

\[
\boxed{
T_W=I_3,
\qquad
N_W=0.
}
\]

The degeneration is detected by specialization, not by an internal
Kummer character.

## Exact source audit

The formulas for \(D_1\) and \(D_2\) were checked directly against the
unexpanded source expressions at

\[
x,y\in\{1,\ldots,7\},
\qquad
E\in\{-5,\ldots,5\}.
\]

This gives \(1078\) exact polynomial comparisons and zero mismatches.
The identities themselves follow by coefficient collection and are not
numerical fits.

No wall, root, or occurrence label was introduced after taking the
total-energy limit.

## Central incidence graph

Generically the wall normalization graph has four component vertices and
six incidence edges, hence

\[
b_1(W_E)=6-4+1=3.
\]

At \(E=0\), one node of each wall and both same-sheet intersections meet
at the physical four-branch incidence point. The barycentric central graph
has four component vertices, three incidence vertices, and eight
half-edges. Therefore

\[
b_1(W_0)=8-7+1=2.
\]

In the primitive generic basis

\[
(g_{101},g_{110},g_{111}^{\rm top}),
\]

and the two surviving central wall-cycle basis, the specialization map is

\[
\boxed{
\operatorname{sp}_W
=
\begin{pmatrix}
1&0&0\\
0&1&0
\end{pmatrix}.
}
\]

Hence

\[
\boxed{
\ker\operatorname{sp}_W
=
\mathbb Z g_{111}^{\rm top}.
}
\]

The kernel is primitive. The two mixed wall cycles survive integrally and
generate the central cycle lattice.

## What this does and does not imply for the marked extension

Consider

\[
0\to H^2(S_E)
\to H^2(S_E\setminus W_E)
\to H^1(W_E)(-1)
\to0.
\]

The quotient computation proves two distinct facts:

1. \(g_{101}\) and \(g_{110}\) are persistent conductor classes;
2. \(g_{111}^{\rm top}\) is the unique quotient vanishing class.

It does **not** prove that the persistent mixed classes possess invariant
lifts through the ambient extension. For an abstract unipotent extension,

\[
T=
\begin{pmatrix}
T_{\rm abs}&C\\
0&I_3
\end{pmatrix},
\]

a column of \(C\) can be nonzero even when its quotient basis vector has
trivial monodromy and nonzero central specialization. Excluding such a
column requires either:

- the actual relative Gauss--Manin connection; or
- a geometric invariant lift in \(H^2(S_E\setminus W_E)\).

Therefore the three off-diagonal columns remain logically separate:

\[
\Theta_{101},
\qquad
\Theta_{110},
\qquad
\Theta_{111}.
\]

Only \(\Theta_{111}\) is forced by quotient rank loss. The mixed columns
are admissible extension classes until independently computed.

This correction preserves the governing warning

\[
\text{associated quotient specialization}
\not\Rightarrow
\text{ambient extension splitting}.
\]

## Relation to existing local evidence

Entries 224--226 construct a source-selected exceptional interval at the
physical total-energy corner and a nonzero algebraic Cut--nearby
functional. This is direct evidence for a local top-column mechanism.

It is not yet a proof that the global top column equals that functional:
the top conductor class is a quotient cohomology vector, whereas the
entry-226 object is a period functional. Their identification requires the
source intersection/duality pairing.

Likewise, the absence of wall-root swaps does not establish
\(\Theta_{101}=\Theta_{110}=0\). Those vanishings must be derived, not
inferred.

## Classification

| Structure | Geometric home |
|---|---|
| \(g_{101},g_{110}\) | persistent wall-conductor Tate cycles |
| \(T_W=I_3\) | analytic occurrence-resolved quotient transport |
| \(g_{111}^{\rm top}\) | primitive disappearing two-wall cycle |
| quotient specialization kernel | top occurrence class |
| three ambient extension columns | uncomputed derived coefficient data |
| new carrier datum | none found |

## Deutsch--Popperian update M2.33

The hard-to-vary claim

\[
\text{the quotient monodromy itself supplies a nontrivial total-energy
Kummer or unipotent block}
\]

is falsified:

\[
T_W=I_3,
\qquad
N_W=0.
\]

The smaller surviving conjecture is

\[
\boxed{
\text{the complete marked }E=0\text{ system is the absolute elliptic
nilpotent plus an extension generated by the frozen wall/enhanced-point
geometry.}
}
\]

No claim about the rank or number of nonzero off-diagonal columns is made
before their actual construction.

## Correction discipline

A preliminary draft of this entry incorrectly inferred vanishing mixed
columns from persistence of \(g_{101}\) and \(g_{110}\) in the central
graph. That inference would confuse quotient specialization with a
splitting of the ambient localization extension. It was removed before
commit.

## Next hostile test

Compute \(\Theta_{101}\) first in the one-wall pair

\[
(S_E,W_1).
\]

Use the exact square restriction \(K_E|_{W_1}=R_1^2\), its two analytic
root sections, and a tubular logarithmic representative of the primitive
wall cycle. Determine whether it extends invariantly through \(E=0\).

Then repeat by symmetry for \(W_2\). Only after the mixed columns are
settled should the two-wall top class be paired with the entry-224
exceptional basis.

The finite outcomes are:

1. a canonical invariant tubular lift, proving the corresponding mixed
   column zero;
2. a source-derived nonzero algebraic column supported at the existing
   enhanced point;
3. failure of the frozen one-wall geometry to generate the column.

Only outcome 3 can challenge the shared-carrier hypothesis.
