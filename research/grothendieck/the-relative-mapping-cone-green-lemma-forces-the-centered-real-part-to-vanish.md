# The Relative Mapping-Cone Green Lemma Forces the Centered Real Part to Vanish

## Two oriented sector identities

Let `z=s-1/2`. Suppose a nonzero boundary state has two reciprocal
realizations with Green packets

\[
(E_+,B_+,F_+),
\qquad
(E_-,B_-,F_-).
\]

The direct sector has centered Green identity

\[
2\operatorname{Re}(z)E_+=B_+-2F_+.
\]

After reciprocal spectral reversal and opposite boundary orientation, the dual
sector has

\[
2\operatorname{Re}(z)E_-=-B_-+2F_-.
\]

The signs are not chosen to obtain cancellation: they are respectively the
spectral sign reversal `z -> -conjugate(z)` and the outward-orientation
reversal of the common seam.

## Relative sewing

Assume the final seam mate is isometric on the full typed packet:

\[
E_+=E_-=E,
\qquad
B_+=B_-=B,
\qquad
F_+=F_-=F.
\]

Adding the two Green identities gives

\[
4\operatorname{Re}(z)E=0.
\]

Therefore, if `E` is finite and strictly positive,

\[
\operatorname{Re}(z)=0.
\]

This is the finite relative mapping-cone zero-confinement lemma.

## Why the doubled architecture matters

Neither sector alone confines the state: its endpoint and forcing terms can
balance off seam. The theorem works only because the two complete packets are
retained until their oppositely oriented Green identities are combined.

The earlier normalization anomaly is now reinterpreted. It arose when the two
states were normalized into one frame before the forcing packets were sewn.
The relative mapping cone instead compares the entire triples `(E,B,F)` and
therefore exposes exactly which mate must be proved.

## RH-bearing gate

The algebraic theorem is complete. Its application to the completed theta/Tate
source remains conditional on four source statements:

1. a scalar zero produces a nonzero admissible state in both sector packets;
2. Fourier–Tate sewing identifies their full energies, endpoint currents, and
   forcing currents—not only scalar readouts;
3. the primitive, square, and archimedean channels are included in `B` and `F`;
4. the common energy remains finite and nonzero after restricted-product
   completion.

Failure of any equality `E_+=E_-`, `B_+=B_-`, or `F_+=F_-` is a typed
falsifier. No scalar cancellation may substitute for these packet-level mates.

