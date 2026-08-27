# Source diagonal spectral comparison does not horizontalize the scalar readout

## Native labelled connection

On the doubled valuation module, logarithmic scale is a source-derived
generator. For a labelled mode at scale \(q\), let

\[
Le_q=qe_q.
\]

Spectral displacement acts by

\[
\psi(s)=e^{-sL}\psi(0),
\qquad
\frac{d\psi}{ds}=-L\psi.
\]

At every finite cutoff this parameter action is invertible. On the critical seam it
is a product of unit rotors on the reciprocal \(q\) and \(-q\) modes. This is
an authentic source connection; it uses no divisor information.

## Scalar readout is not horizontal

Let \(\ell\) be the augmentation or boundary covector and define

\[
\sigma(s)=\ell\psi(s).
\]

For a fixed covector,

\[
\frac{d\sigma}{ds}
=
-\ell L\psi(s).
\]

A rank-one scalar connection

\[
\frac{d\sigma}{ds}=a(s)\sigma(s)
\]

would require \(\ell L\) to be proportional to \(\ell\) on the complete
admissible state family. The augmentation sees many distinct logarithmic
frequencies, so it is not an eigen-covector of \(L\).

Thus invertible source comparison of the labelled state does not induce a
horizontal scalar readout.

## Exact reciprocal two-mode witness

Take reciprocal modes with frequencies \(+1\) and \(-1\). Along the seam,

\[
\psi(t)=
\left(e^{it},e^{-it}\right),
\qquad
\ell=(1,1).
\]

The state remains nonzero and its spectral comparison remains unitary, while

\[
\ell\psi(t)=2\cos t
\]

vanishes at \(t=\pi/2\). The missing quadrature is read by

\[
\ell L=(1,-1).
\]

The smallest parameter-action-closed output space is therefore two-dimensional. A
single scalar line is not closed under the source connection.

## Why covector co-comparison is not the answer

One can force the pairing to remain constant by evolving the covector through

\[
\frac{d\ell_s}{ds}=\ell_sL.
\]

Then the state and covector transports cancel exactly. But this produces a
constant conserved pairing, not the completed theta section. It changes the
readout apparatus along with the state and therefore does not prove
nonvanishing of the fixed source-authorized determinant readout.

## Consequence for the rotor programme

The native diagonal connection supplies phase comparison and preserves the
full labelled state. It does not supply the determinant-line connection needed
for RH. To obtain one, the source must construct a parameter-action-closed boundary
module containing the complete covector orbit

\[
\ell,
\ell L,
\ell L^2,
\ldots
\]

and then derive a determinant or exterior invariant whose nonvanishing controls
the original scalar section. For unrestricted distinct labels this orbit is
generically infinite.

This recovers the earlier infinite boundary-jet phenomenon from the rotor
side. Compressing the orbit to one scalar line is precisely where destructive
interference re-enters.

## DPC verdict

The source already supplies an invertible rotor connection on labelled states,
but its scalar augmentation is not horizontal. Therefore state comparison
alone contains no RH explanation. The next candidate must be a source-derived
invariant of the full parameter-action-closed covector module, with a proven bridge to
the completed determinant section.

## Verification

`check_rh_source_rotor_readout_no_go.py` verifies unitary reciprocal transport,
nonzero transported states, exact scalar cancellation, failure of the
eigen-covector condition, and rank two of the smallest covector orbit.
