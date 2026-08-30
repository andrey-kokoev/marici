# No finite scalar port can be faithful on the completed prime-labelled wall--jump carrier

## Completed reciprocal carrier

After primewise construction, the minimal completed output is

\[
\mathcal Y
=
\ell^2(\mathbb P,w)
\widehat\otimes
\mathbb C^2,
\]

where the two coordinates are:

\[
e_{\mathrm{wall}},
\qquad
e_{\mathrm{jump}}.
\]

The valuation idempotents retain each prime fiber independently.

## Scalar augmentation

A two-port scalar Euler observer has the form

\[
\mathcal A(y)
=
\left(
\sum_p a_p y_{p,\mathrm{wall}},
\,
\sum_p b_p y_{p,\mathrm{jump}}
\right)
\in\mathbb C^2.
\]

Even if every \(a_p\) and \(b_p\) is nonzero and both sums are bounded,
\(\mathcal A\) cannot be injective on the infinite-dimensional carrier.

For two distinct primes \(p\ne q\), the wall vector

\[
y
=
a_q e_{p,\mathrm{wall}}
-
a_p e_{q,\mathrm{wall}}
\]

is nonzero but satisfies

\[
\mathcal A(y)=0.
\]

The same construction applies to the jump coordinate.

## No lower frame bound

Because \(\ker\mathcal A\ne0\), there is no \(\delta>0\) such that

\[
\|\mathcal A y\|
\ge
\delta\|y\|
\]

on the full completed carrier.

Adding finitely many scalar ports does not repair this: every map from an
infinite-dimensional prime carrier to a fixed finite-dimensional output has
a nontrivial kernel.

Thus global scalar pushforward cannot be the faithful comparison map required
to define the Adams edge.

## Correct hierarchy

Faithfulness is required before augmentation:

\[
\ell^2(\mathbb P,w)\widehat\otimes\mathbb C^2
\longrightarrow
\ell^2(\mathbb P,w)\widehat\otimes\mathcal H_{\mathrm{Green}},
\]

with the prime idempotents and both reciprocal ports retained.

The scalar observer is only a terminal readout:

\[
\text{faithful labelled Adams edge}
\longrightarrow
\text{complete Green block}
\longrightarrow
\text{scalar Euler augmentation}.
\]

It may intentionally have a kernel without invalidating the constructor,
provided no coercivity or spectral identification theorem treats that scalar
kernel as invisible source state.

## Local versus global faithfulness

Two distinct claims must be separated.

Local reciprocal faithfulness asks, for each fixed prime,

\[
\ker J_p\cap
\operatorname{span}
\{e_{\mathrm{wall}},e_{\mathrm{jump}}\}
=
\{0\}.
\]

This is a finite \(2\times2\) rank condition and may hold.

Global prime faithfulness asks whether scalar augmentation separates all
prime-labelled outputs. It cannot hold.

Therefore the valid theorem is:

\[
\text{primewise two-port faithfulness}
+
\text{label retention}
+
\text{bounded scalar readout}.
\]

It is not global faithfulness of the scalar pushforward.

## Consequence for the RH operator

The Birman--Schwinger or Green defect must be formed on the labelled completed
carrier, or on a source-authorized quotient that retains equivalent infinite
information. Forming it only after scalar Euler augmentation creates an
infinite dark sector.

Determinant or trace readout may occur downstream because those are
invariants of an already defined operator, not substitutes for its domain.

## Revised next gate

The pushforward problem contracts to the primewise system:

1. construct the \(2\times2\) wall--jump observer \(J_p\);
2. prove \(\det J_p\ne0\);
3. prove a uniform lower singular-value bound after source normalization;
4. assemble \(\bigoplus_pJ_p\);
5. apply scalar Euler augmentation only as observation.

The global no-go removes the impossible demand that finitely many scalar
ports identify the full prime carrier.

## Hostile

Take two individually visible prime wall packets whose weighted scalar outputs
cancel. Every local observer is faithful, yet the scalar total is zero. If
the scalar total is used as the operator domain, a genuine labelled state has
been erased.
