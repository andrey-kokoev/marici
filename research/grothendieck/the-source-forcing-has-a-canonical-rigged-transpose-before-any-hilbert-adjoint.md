# The source forcing has a canonical rigged transpose before any Hilbert adjoint

## Forward incidence

Let `E` be the source test space and `E'` its continuous dual. For the fixed
theta forcing `f` in `E`, define

\[
B_f:\mathbb C\longrightarrow E,
\qquad
B_f(c)=cf.
\]

This is the source-to-tail arrow appearing in the triangular tail system.

## Canonical variance reversal

The topological transpose exists without choosing a Hilbert metric:

\[
B_f^\times:E'\longrightarrow\mathbb C,
\qquad
B_f^\times(\lambda)=\lambda(f).
\]

It is characterized by the duality identity

\[
\langle B_fc,\lambda\rangle
=c\,B_f^\times(\lambda).
\]

This is exactly the missing reversal of variance. It sends a distributional
tail state back to the scalar source channel and remains meaningful for the
weakest regularity grade, provided that grade acts continuously on `f`.

## Why the Hilbert adjoint looked noncanonical

Choose a Hilbert realization `H` between `E` and `E'`. The Hilbert adjoint is

\[
B_f^{*,H}(G)=\langle f,G\rangle_H.
\]

It is the shadow of `B_f^×` after embedding `H` into `E'` by the chosen
Riesz map. Change the Hilbert metric and that embedding changes, so the row
representing the adjoint changes as well.

For example, in a two-coordinate test space with `f=(1,1)`, the Euclidean
metric gives the adjoint row `(1,1)`, while the metric `diag(2,3)` gives
`(2,3)`. The algebraic transpose in the fixed test--dual pairing remains
`(1,1)`.

Thus the source does not canonically choose one Hilbert adjoint across all
regularity grades. It canonically chooses one rigged transpose whose Hilbert
realizations are metric-dependent shadows.

## Fourier covariance

Let `mathcal F:E->E` be the source Fourier transform and let its dual action
be

\[
(\mathcal F'\lambda)(g)=\lambda(\mathcal F^{-1}g).
\]

If the theta source is Fourier-fixed, `mathcal F f=f`, then

\[
B_f^\times(\mathcal F'\lambda)
=\lambda(\mathcal F^{-1}f)
=\lambda(f)
=B_f^\times(\lambda).
\]

So the return arrow is Fourier-covariant at the rigged level. Reflection did
not create it; dualization did.

## Three-grade interpretation

The test--Hilbert--distributional tower should carry one transpose
correspondence:

```text
C --B_f--> E
             |
             v
             H
             |
             v
             E' --B_f^times--> C
```

The primitive, square, and connected-tail grades need not be forced into one
Hilbert adjoint. They need continuous embeddings into `E'` on which evaluation
at the fixed test vector `f` is defined.

This retypes the desired full block as a rigged correspondence

\[
E\oplus\mathbb C
\longrightarrow
E'\oplus\mathbb C,
\]

not initially as a bounded selfadjoint operator on one Hilbert space.

## What remains

The transpose solves existence and variance typing of the lower incidence. It
does not yet show:

- that the reciprocal theta constructor realizes this transpose dynamically;
- that the primitive and square currents lie in its domain;
- that the resulting rigged block has a closed or selfadjoint Hilbert
  realization;
- that its characteristic section equals the completed theta transform;
- that its Green boundary flux vanishes on zero-states.

The next finite audit is therefore not to guess `B*`. It is to embed each
declared boundary grade into `E'` and test whether its evaluation on `f`
matches the independently derived reciprocal incidence.

## Exact falsifier

At any cutoff, reject a proposed lower incidence if it changes under a mere
choice of Hilbert metric while the source/test--dual pairing is fixed, or if it
fails the transpose identity on one labelled test packet.
