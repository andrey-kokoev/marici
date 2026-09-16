# The finite absolute-Gram closure is conditional on one exact positive-regulator alignment

## Correction

The common-Widom-edge argument proves a complete finite-packet theorem once its
input matrices are the positive Tate and reference Grams of one physically
aligned regulator. Prior exact transport of the ordered signed product does not
by itself establish that positive-Gram alignment.

Therefore the previous statement “finite-packet absolute Gram is closed” must
be read conditionally. One finite-cutoff identity remains before the common-edge
argument applies to the physical prolate feature.

## Required aligned objects

For the same regulator tuple

\[
\alpha=(\Lambda,R,N,n,F),
\]

construct physical positive features

\[
X_\alpha^T:E\to\mathcal H_\alpha^T,
\qquad
X_\alpha^0:E\to\mathcal H_\alpha^0
\]

using identical:

- physical and outer windows;
- two-copy channelwise bulk projection;
- dyadic filter depth;
- observer localization;
- angular and conductor truncations;
- endpoint/index splitting convention.

Set

\[
G_\alpha^T=(X_\alpha^T)^*X_\alpha^T,
\qquad
G_\alpha^0=(X_\alpha^0)^*X_\alpha^0.
\]

The exact missing alignment is

\[
\boxed{
G_\alpha^T-G_\alpha^0=D_\alpha^{centered},}
\]

where \(D_\alpha^{centered}\) is the same Hermitian centered regulator whose
matrix coefficients are already known to converge to the Tate--Weil form.

Without this identity, one may have a correct signed trace comparison and two
correct positive features but no reason that their Gram difference is the
centered matrix used by common-edge removal.

## Why ordered-product transport is insufficient

The exact physical-to-Hardy unitary transports

\[
P_\Lambda(Q_\Lambda^T-Q_\Lambda^0)A_g
\]

to the corresponding ordered Hardy expression. This controls a cross/signed
readout. Positive Grams contain diagonal squares of complete regulated feature
legs. Equality of a cross readout does not determine those diagonal squares.
The one-dimensional hidden-equal-mass hostile from the absolute-Gram audit
applies again.

## Exact finite algebra after alignment

Once alignment holds, the remaining argument is formal. If

\[
D_\alpha^{centered}\to W
\]

and the pure-reference Widom law gives

\[
a_\alpha^{-1}G_\alpha^0\to G_{edge}>0,
\]

then the Tate positive Gram has the same leading edge. For large regulator,

\[
C_\alpha
=G_\alpha^T-(D_\alpha)_+
=G_\alpha^0-(D_\alpha)_-
\succeq0.
\]

Removing the common feature \(C_\alpha^{1/2}\) leaves residual Gram

\[
|D_\alpha|\to|W|.
\]

Thus there is no further finite-dimensional analytic mystery after the boxed
alignment identity.

## Minimal executable target

For one noncommuting finite projection fixture, construct both complete
positive regulator features directly from the same rows and verify:

1. both Gram matrices are positive;
2. their difference equals the independently assembled centered Hermitian
   matrix entrywise;
3. the two-copy bulk blocks cancel in the difference;
4. changing one regulator placement makes the identity fail;
5. common-edge removal returns \(|D_\alpha|\).

Such a checker would validate the algebra and placement convention but would
not prove the semilocal analytic identity. The analytic proof must establish
the same equality before regulator removal on the source carrier.

## Updated channel-2 frontier

The gate now has three ordered layers:

1. **positive-regulator alignment:** open exact finite-cutoff source identity;
2. **finite-packet absolute-Gram theorem:** formal and closed conditional on 1;
3. **completed packet-natural Mosco convergence:** open after 1 and 2.

This ordering prevents use of the common-edge theorem with mismatched positive
features.

## Repository dependencies

- `exact-regulator-transport-aligns-the-physical-product-cutoff-with-the-eight-leg-hardy-readout.md`
- `bounded-relative-gram-convergence-transfers-the-reference-widom-law-to-the-tate-regulator.md`
- `common-widom-edge-removal-closes-the-absolute-gram-gate-on-every-coercive-finite-packet.md`
- `the-regulated-positive-gram-block-requires-a-two-copy-channelwise-bulk-counterterm-not-one-outer-window-bulk.md`
