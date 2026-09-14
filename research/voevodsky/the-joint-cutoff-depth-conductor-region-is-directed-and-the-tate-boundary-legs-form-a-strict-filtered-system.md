# The joint cutoff--depth--conductor region is directed, and the Tate boundary legs form a strict filtered system

## Conductor operator

On the angular Mellin carrier

\[
\mathscr H_S
=
\bigoplus_\chi
L^2
\left(
\mathbb R,
\frac{ds}{2\pi}
\right),
\]

define the nonnegative conductor multiplier

\[
\boxed{
\kappa_S(\chi)
=
\sum_{v\in S_f}
f(\chi_v)
\log q_v.
}
\]

Let

\[
K_S
=M_{\kappa_S}
\]

and define the conductor projections

\[
\boxed{
Z_F
=1_{[0,F]}(K_S).
}
\]

Their ranges

\[
\mathscr H_S^{(F)}
=Z_F\mathscr H_S
\]

form an increasing family.

## Commutation with the Tate connection

The Tate connection is diagonal in the same angular decomposition:

\[
A_S
=
\bigoplus_\chi
M_{w_\chi(s)}.
\]

Therefore

\[
\boxed{
[Z_F,A_S]
=0.
}
\]

By spectral calculus,

\[
\boxed{
[Z_F,A_{S,+}]
=[Z_F,A_{S,-}]
=[Z_F,|A_S|]
=0.
}
\]

Hence conductor truncation preserves the global positive and negative Tate legs exactly.

## Filtered observer domains

Set

\[
\mathcal D_S^{(F)}
=
Z_FD(|A_S|^{1/2}).
\]

For `F<=F'`, inclusion gives

\[
\boxed{
\mathcal D_S^{(F)}
\hookrightarrow
\mathcal D_S^{(F')}.
}
\]

The union

\[
\bigcup_{F<\infty}
\mathcal D_S^{(F)}
\]

is a form core for `|A_S|`: spectral truncation in the nonnegative multiplication operator `K_S` converges strongly to the identity and commutes with `|A_S|`.

## Boundary features

Define at conductor level `F`

\[
\boxed{
\Phi_{S,F}^{boundary}(g)
=
\left(
A_{S,+}^{1/2}g,
A_{S,-}^{1/2}g
\right),
\qquad
g\in\mathcal D_S^{(F)}.
}
\]

For `F<=F'`, the target inclusion is the ordinary orthogonal inclusion induced by

\[
Z_F
\le
Z_{F'}.
\]

Because all operators commute,

\[
\boxed{
\Phi_{S,F'}^{boundary}|_{\mathcal D_S^{(F)}}
=
\Phi_{S,F}^{boundary}.
}
\]

Thus conductor-successor cells commute on the nose.

## Lower bound on each level

The finite-place epsilon-factor estimate gives

\[
A_{S,-}|_{\mathscr H_S^{(F)}}
\preceq
(F+C_S)I
\]

for a fixed-place-set constant `C_S` after endpoint extraction.

Consequently the common Plancherel edge form

\[
\boxed{
C_{L,F}
=LI-A_{S,-}
}
\]

is positive on `H_S^(F)` whenever

\[
\boxed{
L
\ge
F+C_S.
}
\]

This is the admissibility inequality for positive reference-edge removal.

## Joint index set

Let

\[
\boxed{
\mathfrak I_S
=
\left\{
(L,n,F):
L\ge F+C_S,
\quad
n\in\mathbb N,
\quad
F\ge0
\right\}.
}
\]

Order it coordinatewise:

\[
(L,n,F)
\preceq
(L',n',F')
\]

when

\[
L\le L',
\qquad
n\le n',
\qquad
F\le F'.
\]

## Directedness

Given two admissible indices

\[
i_1
=(L_1,n_1,F_1),
\qquad
i_2
=(L_2,n_2,F_2),
\]

set

\[
F_3
=
\max(F_1,F_2),
\]

\[
n_3
=
\max(n_1,n_2),
\]

and

\[
L_3
=
\max
\left(
L_1,
L_2,
F_3+C_S
\right).
\]

Then

\[
i_3
=(L_3,n_3,F_3)
\in
\mathfrak I_S
\]

and

\[
i_1\preceq i_3,
\qquad
i_2\preceq i_3.
\]

Therefore

\[
\boxed{
\mathfrak I_S
\text{ is directed}.
}
\]

## Depth transitions

At fixed `(L,F)`, dyadic depth transitions are the exact defect-splitting isometries

\[
J_n:
\mathcal K_{L,n,F}
\to
\mathcal K_{L,n+1,F}.
\]

Since the conductor projection acts on angular labels and every dyadic operator is functional calculus in the cutoff contraction `B_Lambda`, the two operations commute whenever the cutoff pair preserves angular character sectors:

\[
\boxed{
Z_FJ_n
=J_nZ_F.
}
\]

This angular invariance is exact for radial/module cutoffs.

## Common-edge removal at an admissible index

In the ideal common-Widom model, the two regulator Grams on level `F` decompose as

\[
\boxed{
G_{L,F}^{T}
=C_{L,F}
+A_{S,+}|_F,
}
\]

\[
\boxed{
G_{L,F}^{0}
=C_{L,F}
+A_{S,-}|_F.
}
\]

The common form `C_(L,F)` is positive by admissibility. Removing its feature leaves

\[
\boxed{
\left(
A_{S,+}^{1/2}|_F,
A_{S,-}^{1/2}|_F
\right),
}
\]

which is independent of `L` and dyadic presentation depth.

Thus after common-edge removal, all `(L,n)` variation disappears from the abstract Tate boundary; only the increasing conductor restriction remains.

## Cutoff enlargement before removal

For `L<=L'` at fixed `F`,

\[
C_{L',F}
=C_{L,F}
+(L'-L)I.
\]

The later regulator contains additional common positive edge mass. Hence the unremoved full features are not related by a norm-preserving label map.

This is expected: increasing cutoff adds bulk. The correct strict transition occurs after quotienting/removing the common edge feature, not on raw regulator features.

## Strict filtered boundary functor

Let `B_F` be the two-polarity boundary carrier

\[
\mathscr B_F
=
Z_F\mathscr H_S
\oplus
Z_F\mathscr H_S.
\]

For `F<=F'`, let

\[
I_{F'F}:
\mathscr B_F
\hookrightarrow
\mathscr B_{F'}
\]

be orthogonal inclusion. Then

\[
\boxed{
I_{F''F'}I_{F'F}
=I_{F''F},
}
\]

and

\[
\boxed{
I_{F'F}
\Phi_{S,F}^{boundary}
=
\Phi_{S,F'}^{boundary}|_{\mathcal D_S^{(F)}}.
}
\]

Therefore the boundary defines a strict functor

\[
\boxed{
(\mathbb R_+,
\le)
\longrightarrow
\mathsf{Hilb}_{isom}
\]

through the conductor coordinate.

Pulling this functor back along the projection

\[
\mathfrak I_S
\to
\mathbb R_+,
\qquad
(L,n,F)
\mapsto F
\]

gives the strict boundary functor on the full admissible index set.

## Inductive limit

The Hilbert inductive limit is

\[
\boxed{
\varinjlim_F
\mathscr B_F
=
\mathscr H_S
\oplus
\mathscr H_S.
}
\]

On the form-domain union, the compatible features converge graph-norm-wise to

\[
\boxed{
\Phi_S^{boundary}
=
(A_{S,+}^{1/2},
A_{S,-}^{1/2}).
}
\]

Thus unbounded conductor does not prevent existence of the limiting Tate boundary. It prevents realizing every conductor sector by one finite-cutoff positive common-edge subtraction.

## Cofinal paths

A cofinal sequence may be chosen by any functions

\[
F_k\to\infty,
\qquad
n_k\to\infty,
\]

with

\[
\boxed{
L_k
\ge
F_k+C_S
}
\]

and whatever additional observer-weighted plunge condition determines `n_k`.

For example,

\[
L_k
=F_k+C_S+k
\]

is automatically admissible. It does not assert the correct prolate depth; that remains a separate spectral input.

## Place-set enlargement

For `S subset S'`, define

\[
\kappa_{S'}(\chi)
=
\kappa_S(\chi|_S)
+
\sum_{v\in S'\setminus S}
f(\chi_v)
\log q_v.
\]

An admissible transition must increase `F` by the added conductor budget and increase `L` enough to preserve

\[
L\ge F+C_{S'}.
\]

This gives an explicit place-enlargement condition, though an isometric comparison of the different semilocal Hilbert carriers still requires the source Sonin/Tate transition map.

## What remains analytic

The strict filtered construction assumes the ideal positive decompositions

\[
G_{L,F}^{T,0}
=LG_{edge,F}
+
\text{finite Tate/reference term}.
\]

For exact cutoff regulators one still needs:

1. observer-weighted common Widom asymptotics on each conductor level;
2. form-order remainder bounds sufficient for positivity;
3. compatibility of the physical polar transports with conductor inclusion;
4. the source-derived dyadic depth/plunge scale.

The present result solves the indexing and abstract transition problem once those analytic estimates hold.

## Disposition

The admissible positive region

\[
\boxed{
\mathfrak I_S
=
\{(L,n,F):
L\ge F+C_S\}
}
\]

is directed. Conductor projections commute with the Tate connection and its Jordan parts, so common-edge-removed boundary legs restrict and compose exactly. The positive completion is therefore a strict conductor-filtered inductive system, with prolate depth and cutoff retained as analytic presentation coordinates.
