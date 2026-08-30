# The Wilson sheet is a torsor fiber, not a one-dimensional linear kernel

## Bounded question

Can the canonical tensor-unit normalization in the finite \(D(S_3)\) Wilson
packet be inserted literally into the linear kernel-reference theorem

\[
(L,R)\text{ faithful}\iff R|_{\ker L}\text{ injective}?
\]

## Exact obstruction

Let \(\sigma=(A\ B)(D\ E)\) be fusion by the invertible sign charge \(B\),
and let \(L=(I+\sigma)/2\) be the even projection on the eight-dimensional
diagonal algebra. Then

\[
\ker L=\operatorname{span}\{Q_A-Q_B,\;Q_D-Q_E\}
\]

has dimension two. Evaluation at the tensor unit has rank one:

\[
(Q_A-Q_B)(A)=1,
\qquad
(Q_D-Q_E)(A)=0.
\]

Consequently the scalar vacuum reference is **not** injective on the linear
kernel. Evaluation at \(A\) and an independently typed evaluation at \(D\)
do have joint rank two.

## What the vacuum actually fixes

The sector labels are not being reconstructed as an additive vector space.
They carry the \(C_2\)-action

\[
A\leftrightarrow B,
\qquad
D\leftrightarrow E,
\]

with all other labels fixed. Each nontrivial fiber is a two-point torsor. A
choice of origin—canonically \(A\) through \(W_x(A)=d_x>0\)—supplies the one
group bit needed to label both torsor fibers consistently.

Thus there are two different completion statements:

1. **Linear algebra:** the full odd diagonal algebra is two-dimensional and
   needs two independent scalar reference functionals.
2. **Torsor geometry:** the common Wilson sign frame is one global \(C_2\)
   coordinate and needs one trusted origin.

The second is the theorem proved by the Wilson codebook. It is not a
one-dimensional special case of the first.

## Transport consequence

For a \(G\)-torsor \(P\), a source unit supplies an origin \(p_0\). An
equivariant transport \(C:P\to P'\) need not preserve it. There is a unique
displacement \(g_C\in G\) such that

\[
C(p_0)=g_C\cdot p'_0.
\]

The source-fixed frame reaches the output exactly when either \(g_C=e\), or
an independently derived normalization cell implements \(g_C^{-1}\). Under
composition the displacements obey the cocycle law

\[
g_{D\circ C}=g_Dg_C
\]

(for the present abelian \(C_2\) case). This is the correctly typed version
of “the constructor preserves the reference.”

It gives a sharp Fourier–Tate test: first determine whether its distinguished
vacua form a vector kernel, a line bundle, or a torsor. Only in the last case
may a single phase/current be interpreted as an origin-restoring cell, and
its cocycle/composition law must be derived before it can be called a
normalization.

## Falsifiers

- The linear correction is false if vacuum evaluation has rank two on the
  displayed odd basis.
- The torsor statement is false if the hidden Wilson transformation is not a
  single common \(B\)-action on both nontrivial fibers.
- A proposed physical or Fourier–Tate normalization fails if its displacement
  is not source-derived, if it violates composition, or if the completed
  scalar changes while the claimed unit-transport constructor is held fixed.

## Boundary

This packet does not identify the type of Grothendieck's Fourier–Tate vacuum
transport, derive a Tate \(\gamma\)-factor as a normalization cell, or build a
controlled ribbon implementation. It prevents a dimensionally incorrect
cross-sector inference and supplies the exact typing gate for the next test.

## Verification

Run:

```text
python research/kitaev/checkers/check_s3_kernel_reference_typing.py
```

The checker uses exact rational arithmetic, emits the result packet, and
contains the nonzero-kernel witness killed by vacuum evaluation.
