# Domain-Wall Inflow and Flavor-Overlap Fiber

## Question

Can a chiral domain-wall history realize WP794's required
non-mirror-completable constructor while fixing the flavor portal, its RG
basin, thresholds, and readout?

## Claim boundary

The admitted source is a five-dimensional fermion coupled to a scalar wall
whose ordered asymptotic vacua are fixed. Near its zero crossing,

\[
\Phi(y)=2\mu^2y.
\]

The normalizable four-dimensional zero mode is

\[
f_\ell(y)
=\left(\frac{2\mu^2}{\pi}\right)^{1/4}
e^{-\mu^2(y-\ell)^2}.
\]

It solves one first-order chiral equation and not the opposite one. Reversing
the wall reverses the trapped chirality. Bulk Chern--Simons inflow cancels the
boundary anomaly, so the chirality and anomalous current are tied to one
source construction and persist across massive-mode thresholds.

This realizes the architecture demanded by WP794 only conditionally. The
ordered endpoint vacua prepare the orientation. A symmetric double-well theory
also admits the antikink unless that boundary history has independent source
authority.

## Exact flavor fiber

A bulk fermion mass \(M_i\) shifts the localization center to

\[
\ell_i=-\frac{M_i}{2\mu^2}.
\]

For two normalized zero modes, their overlap is

\[
\int_{\mathbb R}f_{\ell_i}(y)f_{\ell_j}(y)\,dy
=e^{-\mu^2(\ell_i-\ell_j)^2/2}.
\]

The effective four-dimensional Yukawa therefore has the form

\[
y_{ij}
=\rho e^{-\mu^2(\ell_i-\ell_j)^2/2}.
\]

Topology fixes neither \(\rho\), \(\mu\), nor the masses \(M_i\). The exact
hostile pair

\[
|\ell_i-\ell_j|=\frac1\mu,
\qquad
|\ell_i-\ell_j|=\frac2\mu
\]

has identical wall orientation, zero-mode chirality, and anomaly coefficient,
but gives \(\rho e^{-1/2}\) and \(\rho e^{-2}\). Assigning the near overlap to
\(g_n\) and the far overlap to \(g_m\) gives one sign of \(g_n-g_m\); swapping
the assignments reverses it without changing the inflow packet.

## RG, threshold, and instrument typing

Anomaly matching makes the quantized inflow coefficient robust under RG and
massive thresholds. It does not make the flavor overlap an anomaly
coefficient. The first paired heavy wall modes occur at a scale controlled by
\(\mu\), which is continuous source data.

The anomalous current is a genuine physical response channel. Fermion masses
and CKM elements are genuine flavor readouts. But the split-fermion
construction chooses localization positions to reproduce those observables;
it does not provide an independently calibrated source perturbation map into
physical16. A readout of the fitted overlap is not a selector of its source.

## Classification

- The oriented wall is a relative chirality selector.
- Anomaly inflow is a quantized RG and threshold rigidifier.
- The wall theory does not select its own ordered boundary history.
- The continuous overlap data are numerical flavor selectors only after
  \(M_i\), \(\mu\), and \(\rho\) are supplied.
- The anomaly instrument does not measure the full flavor portal.

This is the closest constructive template so far: one physical history
co-generates chirality, topological response, and threshold robustness.
Nevertheless, its flavor values remain tunable presentation data on that
history.

## Smallest exact falsifier

The two separations \(1/\mu\) and \(2/\mu\) preserve every topological and
anomaly datum while changing the Yukawa. Interchanging which species receives
which separation reverses the portal contrast. Therefore anomaly inflow cannot
be the missing numerical selector without a further source rule for
localization geometry.

## Disposition

Retain oriented anomaly inflow as the first physically coherent template for
WP794's boundary-history constructor. Reject it as a complete flavor selector.
The successor must derive the ordered endpoints and the complete set of
localization masses and wall scales from the same source, then calculate the
RG transport, finite threshold response, and calibrated physical16 Jacobian.

Verification:

- checker:
  research/flavor/checkers/wp795_domain_wall_inflow_overlap_fiber.py
- generated result:
  research/flavor/results/wp795_domain_wall_inflow_overlap_fiber.json
- exact invocation:
  uv run --with sympy python research/flavor/checkers/wp795_domain_wall_inflow_overlap_fiber.py
- domain-wall source:
  [Kaplan](https://arxiv.org/abs/hep-lat/9206013)
- anomaly-inflow source:
  [Fukaya et al.](https://arxiv.org/abs/2001.03318)
- split-flavor source:
  [Mirabelli and Schmaltz](https://arxiv.org/abs/hep-ph/9912265)
