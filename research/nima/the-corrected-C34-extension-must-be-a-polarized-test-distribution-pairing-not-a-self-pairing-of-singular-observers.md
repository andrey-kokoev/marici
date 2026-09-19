# The corrected C34 extension must be a polarized test--distribution pairing, not a self-pairing of singular observers

## Question

Does splitting a meromorphic observer into regular, principal-value, and residue
coordinates suffice to extend the `C34` sesquilinear form to its self-pairing?

## Claim boundary

No. The original observation contains the product

\[
\overline{m_h(t)}m_g(t).
\]

If both observers have a simple physical-line pole, this product has a
nonintegrable double-pole term. Distributional notation does not define
products such as `pv(1/x)^2`, `delta(x)pv(1/x)`, or `delta(x)^2` canonically.
A three-coordinate split records the singular data but does not define their
self-product.

Any finite-part self-pairing requires a subtraction prescription and generally
a scale. Unless that prescription is derived from the source meromorphic
family and sewn to the endpoint packet, it is an observer-fitted extension.

## Polarized source type

The corrected state is not an arbitrary singular observer squared with itself.
It is the fixed-forcing pair

\[
\Delta_\Xi(z)=\Phi\otimes u_z,
\]

where `Phi` is a rapid anchor and `u_z` carries the meromorphic response. This
selects an asymmetric pairing type

\[
E_{C34}^{\rm test}
\times E_{C34}^{\rm dist}
\longrightarrow \mathbb C,
\]

not a quadratic form on `E_C34^dist`.

For one regular multiplier `m_Phi` and one simple-pole multiplier `m_u`, the
singular contribution can be defined by principal-value action and residue
evaluation on the smooth coefficient

\[
\overline{m_\Phi}(Q^T-Q^0)m_u,
\]

provided the corresponding boundary values and trace estimates are proved.
No product of two singular distributions is then required.

## Required constructor

The next admissible object is a polarized extension

\[
q_{C34}^{\rm pol}:
E^{\rm test}\times E^{\rm pole-res}
\to\mathbb C
\]

that:

1. agrees with `q_F` when both inputs are regular;
2. uses the source-defined principal value and diagonal residue in the singular
   leg;
3. preserves reciprocal exchange between the two ordered placements;
4. retains the rapid forcing leg explicitly;
5. does not promote the polarized pairing to a singular self-norm.

## Disposition

A symmetric rigged observer space with an everywhere-defined self-pairing is
not justified. The fixed-forcing structure narrows the viable interface to a
polarized test--distribution pairing, whose first remaining check is continuity
of the `C34` cross kernel against one principal-value leg.