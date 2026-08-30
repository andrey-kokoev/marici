# 3023 — The Frozen Optical Source Supplies an Ideal Path but No Noisy Crossing

**Status:** source-provenance closure  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-c90a423f1dbe7fd023e39d1c`

## Scope

Entry 3020 derived the exact X-state support boundary

\[
|z|^2=bc.
\]

This entry asks whether the frozen optical source supplies a physical trajectory through that boundary.

## Source-authorized ideal trajectory

White et al. derive the two-crystal output

\[
|\psi(\epsilon,\phi)\rangle
=
\frac{|HH\rangle+\epsilon e^{i\phi}|VV\rangle}
{\sqrt{1+\epsilon^2}},
\qquad
\epsilon=\tan\chi,
\]

where the pump half-wave plate controls \(\chi\) and the ultraviolet quarter-wave plate controls \(\phi\). In the labelled X-state coordinates,

\[
a=\frac1{1+\epsilon^2},
\qquad
d=\frac{\epsilon^2}{1+\epsilon^2},
\qquad
z=\frac{\epsilon e^{-i\phi}}{1+\epsilon^2},
\qquad
b=c=0.
\]

Consequently,

\[
|z|^2-bc
=
\frac{\epsilon^2}{(1+\epsilon^2)^2}.
\]

Every finite nonzero \(\epsilon\) lies strictly inside the NPT sewing region. The ideal path reaches the support boundary only at its two product-state endpoints:

\[
\epsilon=0,
\qquad
\epsilon=\infty.
\]

The phase \(\phi\) rotates the calibrated coherence but does not alter the invariant distance from the NPT boundary.

## What the source reports beyond the ideal path

The same paper observes small \(|HV\rangle\) and \(|VH\rangle\) components, even near maximal entanglement, and says that they become proportionally more important as the state becomes less entangled. It offers two possible origins:

- imperfect alignment between source and analyzer axes;
- nonorthogonal source optic axes.

This is not a source-defined stochastic channel or a parameterized X-state trajectory. In particular, the paper does not provide functions

\[
b(\chi),\qquad c(\chi),\qquad z(\chi)
\]

for the imperfect source.

The proposed future access to mixed states cites depolarization technology but supplies no two-photon map connecting its control parameter to the labelled X-state coefficients. The cited Schwindt–Kwiat–Englert work concerns a single-photon interferometer and does not fill this two-photon provenance gap.

## Exact boundary along any future source trajectory

If a later source construction supplies

\[
\tau\longmapsto
(z(\tau),b(\tau),c(\tau)),
\]

its orientation-sewing transition is already fixed:

\[
|z(\tau_*)|^2=b(\tau_*)c(\tau_*).
\]

The source trajectory may cross this hypersurface, approach it asymptotically, or remain on one side. Those are physical predictions of the trajectory, not choices in the support calculus.

## Narrow conclusion

The frozen source authorizes:

1. a tunable pure path that is NPT at every nonproduct point;
2. qualitative evidence for leakage outside that path;
3. complete tomography capable of measuring the resulting state.

It does not authorize a noisy trajectory or a finite noisy crossing parameter. Therefore no depolarizing threshold may be reported from this source without importing an additional model.

This is not a failure of the Carrier or the quantum lens. The support boundary and the required readout are already defined. The missing datum is source dynamics.

## Experimental constructor

Aspect's finite-count constructor is correctly matched to the invariant boundary: estimate \(b\), \(c\), \(\operatorname{Re}z\), and \(\operatorname{Im}z\) in one calibrated phase frame and evaluate

\[
\Delta_{\rm NPT}
=
|z|^2-bc.
\]

This separates asymmetric leakage from handedness and avoids interpreting a linear witness as the full boundary away from \(b=c\).

## Next falsifier

Use a primary two-photon source paper that implements a declared decoherence or depolarization element and reports enough control-to-density-matrix data to derive \((z(\tau),b(\tau),c(\tau))\). Freeze that map before evaluating \(\Delta_{\rm NPT}\). If no such map is available, the physical crossing remains experimentally measurable but not source-predicted.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-c90a423f1dbe7fd023e39d1c`, value 3023.
- Primary source: White, James, Eberhard, and Kwiat, arXiv:quant-ph/9908081, especially Eq. (1), the pump controls, and the reported \(HV,VH\) leakage.
- Upstream tomography source: James et al., arXiv:quant-ph/0103121.
- Epistemic-graph admission: `ev-000000005849-baf7aa64-ab0d-40f3-870b-58a00184eadb`.
