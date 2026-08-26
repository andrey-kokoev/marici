# Correlated neutral-kaon response constructor: WP455

## Question

Does a published source-to-readout map repair WP454's operator-interface failure for the vectorlike flavor-current ray?

## Admitted domain and convention

Use the colorless heavy-vector model of Aebischer, Bobeth, Buras, and Kumar, [SMEFT ATLAS of Delta F = 2 Transitions](https://arxiv.org/abs/2009.07276), in its down-basis convention at a matching scale of 5 TeV. Retain only the off-diagonal down-sector couplings

\[
z_q^{12}=z_d^{12}=z,
\]

and set every other coupling in their equation (121) to zero. Equality of the two couplings is the source restriction inherited from a vectorlike flavor current; it is not fitted from the kaon answer.

The tree-level matching in their equation (115) then creates LL, RR, and LR operators together. In the source normalization their leading kaon response is

\[
\frac{M_{Z'}^2}{(5\ {\rm TeV})^2}\Sigma^K_{Z'}
=\left(-5.3\mathbin{\cdot}10^6+1.8\mathbin{\cdot}10^4+1.8\mathbin{\cdot}10^4\right)z^2
=-5{,}264{,}000z^2.
\]

Here \(\Sigma^K_{Z'}\) is normalized to \(2[M_{12}^K]_{\rm BSM}/(\Delta M_K)_{\rm exp}\). The published coefficients incorporate SMEFT running, electroweak matching, low-energy QCD running, and hadronic matrix elements in the authors' declared scheme.

## What this repairs

The response does not project the source onto an isolated LL axis. It transports the correlated vectorlike source ray as one object. Its coefficient is nonzero, so the source ray is not in the response kernel. Relative to either same-chirality term alone, the correlated response has the exact ratio

\[
\frac{-5{,}264{,}000}{18{,}000}=-\frac{2632}{9}.
\]

Thus the LR channel reverses the sign and enhances the magnitude by nearly three hundred. WP454's LL-only diagnostic is not merely incomplete; it is parametrically misleading for this source.

## Authority boundary

This is a positive common-frame response constructor, not yet an experimentally calibrated exclusion likelihood. The cited formula maps a frozen UV coupling packet to a physical mixing-amplitude normalization, but it does not supply a covariance-bearing likelihood for the Standard Model long-distance contribution, experimental record, and new-physics interference. Consequently:

- the operation separates zero from nonzero points along this one-dimensional source ray;
- it constrains the ray once an independently declared acceptance interval for the complex mixing amplitude is supplied;
- it does not identify arbitrary UV current orientations;
- it does not select \(g_F f/v\) or any flavor vacuum;
- it is neither a presentation rigidifier nor a source-generated selector.

No reference port is added: neutral-kaon mixing is an ordinary physical experiment, and the changed information comes from retaining the source-correlated operator family through its full transport.

## Smallest exact falsifier

For the declared equal-coupling source restriction, cancellation would require the correlated coefficient to vanish. The exact evaluated coefficient is \(-5{,}264{,}000\), so that falsifier fails.

The remaining physical-instrument gate is a named likelihood or acceptance region for the complex kaon mixing amplitude, with Standard Model long-distance uncertainty and correlations, in the same normalization. Without it, no numerical exclusion on the WP447 scale is admitted.
