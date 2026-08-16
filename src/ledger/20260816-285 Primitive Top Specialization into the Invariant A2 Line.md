---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Primitive Top Specialization into the Invariant A2 Line

## Result

Entries 282--284 reduce the finite \(\ell_1=0\) marked degeneration to
one undetermined integral scalar

\[
N_{\rm rel}(g_{111})
=
c(\alpha-\beta)
\]

in the invariant line of the \(A_2\) lattice. The local log resolution of
the frozen pair fixes this scalar:

\[
\boxed{
N_{\rm rel}(g_{111})
=
\pm(\alpha-\beta).
}
\]

The sign depends only on the orientation convention for the top graph
cycle. Its absolute coefficient is one.

Thus the finite \((+1)\) extension is nonzero and primitive. It is the
canonical incidence extension between

- the disappearing four-cycle in the marked conductor graph; and
- the invariant algebraic class in the resolved \(A_2\) exceptional
  chain.

On this finite block,

\[
\operatorname{rank}N_{\rm rel}=1,
\qquad
N_{\rm rel}^2=0.
\]

No fitted scalar, extra support summand, or new carrier stratum is needed.
The simultaneous elliptic unipotent contribution remains a distinct
block.

## Central marked model

After analytic splitting, the central surface germ is

\[
X Y=t^3.
\]

The two walls each have two branches. Up to nonzero analytic units, one
wall supplies the coordinate branches

\[
C_X:\ X=t=0,
\qquad
C_Y:\ Y=t=0.
\]

The other supplies branches with valuations

\[
D_X:
\quad
X\sim c t^2,
\quad
Y\sim c^{-1}t,
\]

\[
D_Y:
\quad
X\sim c^{-1}t,
\quad
Y\sim c t^2,
\]

where \(c\) is a nonzero kinematic unit.

These valuations are fixed by the source wall equations
\(u=0\), \(v=0\) and the reduced coordinates used in entries 282--283.
They are not chosen after inspecting the exceptional geometry.

## One blowup resolves the central A2 germ

Blow up the singular point. In the \(t\)-chart write

\[
X=ta,
\qquad
Y=tb.
\]

The strict-transform equation is

\[
ab=t.
\]

It is smooth. The exceptional divisor is the transverse chain

\[
E_1:\ a=0,
\qquad
E_2:\ b=0.
\]

The branch incidences are:

- \(C_X\) meets the outer point of \(E_1\);
- \(D_X\) meets a finite smooth point of \(E_1\);
- \(C_Y\) meets the outer point of \(E_2\);
- \(D_Y\) meets a finite smooth point of \(E_2\).

Each branch occurs with multiplicity one. No exceptional component is
inserted except those forced by resolving the frozen \(A_2\) surface
germ.

## The collapsing conductor cycle

In the edge ordering of entry 280,

\[
(n_{1a},n_{1b},n_{2a},n_{2b},P_+,P_-),
\]

the chosen integral top lift is

\[
g_{111}
=
(1,0,0,-1,-1,1).
\]

At \(\Lambda=0\), precisely the four supported edges in this vector
coalesce at the four-branch marked point. They form a primitive oriented
quadrilateral.

After resolution, its four branches attach in pairs to \(E_1\) and
\(E_2\). The cellular specialization boundary is therefore the oriented
difference of the two exceptional components:

\[
\operatorname{sp}(g_{111})
=
\pm(E_1-E_2).
\]

With the root-lattice identification

\[
[E_1]=\alpha,
\qquad
[E_2]=\beta,
\]

this is

\[
\operatorname{sp}(g_{111})
=
\pm(\alpha-\beta).
\]

The coefficient is primitive because the quadrilateral generator and all
four branch-incidence entries have coefficients \(\pm1\). Equivalently,
the relevant graph-incidence matrix is totally unimodular; its rank-one
image has torsion-free cokernel.

## Monodromy interpretation

The physical finite monodromy decomposes as

\[
A_2\otimes\mathbb Q
=
L_+\oplus L_-,
\]

where

\[
L_+=\mathbb Q(\alpha-\beta),
\qquad
L_-=\mathbb Q(\alpha+\beta).
\]

Entry 283 proves that the top graph line cannot extend into \(L_-\).
The log-resolution incidence now determines the remaining column. After
removing the order-two semisimple reflection, the finite relative
nilpotent operator satisfies

\[
N_{\rm rel}(g_{111})
=
\pm(\alpha-\beta),
\]

and vanishes on the finite absolute target. Hence

\[
N_{\rm rel}^2=0.
\]

This is the local finite part only. It does not include
\(N_{\rm ell}\) from the simultaneous nodal elliptic boundary.

## Integral parity audit

Entry 284 finds

\[
A_2/
\left(
\mathbb Z(\alpha-\beta)
\oplus
\mathbb Z(\alpha+\beta)
\right)
\simeq
\mathbb Z/2.
\]

The present map lands primitively in the invariant sublattice itself. It
does not require dividing \(\alpha-\beta\) by two. Therefore:

- the finite top specialization is integrally canonical up to sign;
- the index-two eigensplitting remains a real lattice-gluing datum;
- the conductor half-sum defect and the \(A_2\) eigensplitting defect are
  compatible but are not identified merely by the rank-one
  specialization map.

No post hoc parity correction is admitted.

## Classification

| Datum | Classification |
|---|---|
| exceptional chain \(E_1\cup E_2\) | resolved Cayley--Menger coefficient geometry |
| four branch attachments | frozen marked-denominator data |
| \(g_{111}\mapsto E_1-E_2\) | primitive relative specialization |
| finite rank-one \(N\) | Tate extension data |
| index-two eigensplitting | integral coefficient-lattice gluing |
| new carrier stratum | none |

## Deutsch--Popperian conclusion M2.28

For a generic \(\ell_1=0\) or \(\ell_2=0\) collision, the complete
finite marked nearby-cycle block is generated by the frozen
Cayley--Menger \(A_2\) resolution and the strict transforms of the two
source walls. Its only nonzero relative extension is the primitive map

\[
\mathbb Z_{\rm top}
\longrightarrow
L_+,
\qquad
1\longmapsto\pm(\alpha-\beta).
\]

The finite \(\Lambda\)-collision therefore closes without a new
cosmology-specific carrier datum.

This conclusion is narrow:

- it does not split the global rank-twelve system;
- it does not determine the elliptic extension column;
- it does not address the non-isolated \(E=0\) degeneration;
- it does not identify the home of \(\mathcal Q\).

## Next hostile test

The finite \(\ell_1/\ell_2\) block is closed. Move to the global
total-energy component

\[
E=\ell_4=0,
\]

where

\[
K_E=R^2
\]

and the affine surface splits. Construct the global semistable model of
the compactified pair, compute the dual complex and nearby-cycle weight
graded object, and determine whether the marked top extension remains
Tate/Kummer away from \(xy=0\). Keep the second Rees grade of
\(\mathcal Q\) visible throughout.
