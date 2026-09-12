# Finite Green realizations form a coherent ind/pro system

## Finite stages

Let \(D\subset\mathbb R\) be the admitted displacement set and let \(S\subset D\) be finite. Define

\[
E_S=\operatorname{span}\{k_x:x\in S\}
\subset H^1(\mathbb R),
\qquad
k_x(t)=e^{-|t-x|}.
\]

Strict positive definiteness implies

\[
\dim E_S=|S|.
\]

The Gram matrix in the kernel-section basis is

\[
K_S=(e^{-|x-y|})_{x,y\in S}.
\]

## Covariant state direction

For \(S\subset T\), literal inclusion of kernel spans gives an isometry

\[
i_{S,T}:E_S\hookrightarrow E_T.
\]

These maps satisfy

\[
i_{T,U}i_{S,T}=i_{S,U}.
\]

Thus finite state realizations form a directed system. If \(D\) is dense, its directed union is dense in the full Green RKHS:

\[
\overline{\varinjlim_{S\Subset D}E_S}=H^1(\mathbb R).
\]

## Contravariant observation direction

Let

\[
p_{T,S}:E_T\to E_S
\]

be orthogonal projection. In kernel coordinates its matrix is

\[
P_{S,T}=K_S^{-1}K_{S,T},
\]

where \(K_{S,T}\) is the rectangular cross-Gram matrix.

For \(S\subset T\subset U\), nested orthogonal projection gives

\[
p_{T,S}p_{U,T}=p_{U,S}.
\]

Therefore the finite observable shadows form an inverse system.

The formula also has an interpolation meaning: \(p_{T,S}f\) is the unique element of \(E_S\) whose residual against every section \(k_x\), \(x\in S\), vanishes.

## The graded/pro residual type

The correct finite-depth object is not a sequence of unrelated full-rank matrices. It is the paired system

```text
states:       E_S -> E_T                 for S subset T
observations: E_T -> E_S                 by orthogonal projection
compatibility: projection o inclusion = identity on E_S
```

This is the finite-depth graded/pro realization requested by the context-rank audit. The infinite RKHS is its Hilbert completion, not an additional guessed primitive.

## Relation to rank growth

Every new distinct context adds one independent kernel state, so

\[
\dim E_T-\dim E_S=|T\setminus S|.
\]

The transition is therefore an exact rank-one extension when one context is added. This parallels breakpoint recollement, but the quotient direction is now a Green-orthogonal innovation rather than a seam jump. Connecting these two extension classes is the next comparison problem.

## Verification

The exact-rational checker uses nested displacement sets in \(\log 2\,\mathbb Z\), where

\[
k(i\log2,j\log2)=2^{-|i-j|},
\]

and verifies every projection triangle through seven states:

```text
python research/coherence/check_green_gram_pro_system.py
```

Artifacts:

- `check_green_gram_pro_system.py`
- `green-gram-pro-system.v1.json`
