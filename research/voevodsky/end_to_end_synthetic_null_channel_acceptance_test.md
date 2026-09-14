# End-to-end synthetic null-channel acceptance test

## Question

Does the complete encoder, noisy detector response, exact calibration inverse, and parity decoder recover every conductor syndrome class?

## Claim boundary

This is a synthetic exact-arithmetic acceptance test of the specified channel. It is not experimental evidence and does not test whether the conductor quotient occurs in an optical apparatus.

## Channel

For each logical class

\[
(a,b)\in(\mathbb Z/2)^2,
\]

the encoder prepares

\[
|a,b,0\rangle.
\]

Each mode passes independently through the calibrated number-resolving response with

\[
\eta=9/25,
\qquad
d=1/10.
\]

The resulting measured distribution has 64 possible count triples. Applying the exact tensor-product left inverse reconstructs the source distribution on the 27 occupations in \(\{0,1,2\}^3\).

The decoder then evaluates

\[
\langle O_1\rangle
=
\sum_n(-1)^{n_1+n_3}p_n,
\qquad
\langle O_2\rangle
=
\sum_n(-1)^{n_2+n_3}p_n.
\]

## Acceptance test

For all four encoded basis classes, exact inversion recovers the original point distribution with zero residual. The decoded parity signs are

\[
\bigl((-1)^a,(-1)^b\bigr),
\]

so the reconstructed bits equal \((a,b)\).

The vacuum codeword \(|0,0,0\rangle\) is recovered as the trivial syndrome, while each of the three nontrivial conductor classes gives its distinct two-bit result.

## Calibration falsifier

Generate measured distributions with \(\eta=9/25\) but decode them using the incorrect efficiency \(\eta'=2/5\). The reconstructed source vectors have nonzero residual relative to the prepared source vectors. Thus exact recovery is calibration-dependent rather than an identity that survives arbitrary response assumptions.

## Acquisition acceptance criterion

A physical run would pass this finite channel test only if:

1. calibration data support a full-column-rank response on the declared occupation cutoff;
2. held-out prepared codewords reconstruct within a preregistered error bound;
3. inferred source probabilities satisfy normalization and positivity within uncertainty;
4. the two syndrome estimators distinguish all four prepared classes;
5. channel exchange swaps the two inferred bits within uncertainty.

## Disposition

The complete finite null-channel architecture passes end-to-end exact synthetic testing for every conductor class and fails under a deliberately mismatched calibration. The remaining blocker is material physical preparation and acquisition, not an undefined mathematical decoder.
