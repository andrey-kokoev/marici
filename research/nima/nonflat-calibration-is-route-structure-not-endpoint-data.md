# Nonflat calibration is route structure, not endpoint data

## Question

Does nonzero calibration holonomy always invalidate a multi-setting
experiment?

## Claim boundary

No. It invalidates an endpoint-only calibration model. A source-derived
nonflat connection can remain lawful when route labels are retained and each
route uses its own transport. This is transport on setting space, not an
assertion about physical time.

## Flat endpoint model

If each setting has one nuisance frame \(\kappa_i\), then

\[
\eta_{ij}=\kappa_i\kappa_j^{-1}
\]

is pure gauge and flat. Transport depends only on endpoints. On a triangle,

\[
\eta_{01}\eta_{12}=\eta_{02}.
\]

Nonzero holonomy proves that no such endpoint-frame family realizes the
declared connectors.

## Route-dependent model

A general connection assigns transport to an ordered route. Let \(p\) and
\(q\) be two routes with the same endpoints. Their transports may differ:

\[
\eta_p\neq\eta_q.
\]

The comparison

\[
h_{p,q}=\eta_p\eta_q^{-1}
\]

is curvature or holonomy. It is not an inconsistency when the source apparatus
distinguishes \(p\) from \(q\).

For a source response \(\omega\), route-specific observations satisfy

\[
z_p=\eta_p\omega,
\qquad
z_q=\eta_q\omega.
\]

Each route recovers the same source response after applying its own inverse
transport. Erasing the route label makes the two observations appear
contradictory.

## Exact \(C_4\) triangle

Write phase transport additively modulo four. Direct and indirect transports
from setting \(2\) to setting \(0\) are

\[
\eta_{\mathrm{direct}}=\eta_{02},
\qquad
\eta_{\mathrm{indirect}}=\eta_{01}+\eta_{12}.
\]

The curvature is

\[
F=\eta_{01}+\eta_{12}-\eta_{02}.
\]

Among the \(4^3=64\) edge assignments, sixteen are flat and forty-eight are
curved. Every curved assignment remains internally correct as a route-labelled
instrument: subtracting the corresponding route transport recovers the same
source phase.

## Typing correction

Three cases must remain distinct:

1. endpoint calibration claimed, nonzero holonomy: defect;
2. route-dependent calibration source-derived, holonomy retained: explained
   behavior;
3. route dependence introduced after observing disagreement: fitted escape.

The second case requires route preparation, route identity, ordered
composition, and a readout preserving the route label until correction.

## Cross-sector consequences

- Optical paths can carry genuine geometric or apparatus phase. Calibration
  must be path-indexed when that phase is source-derived.
- Flavor threshold routes may differ by ordered matching operations; endpoint
  equality is not automatic.
- Software middleware and migrations naturally carry ordered route effects;
  flattening them to endpoint bytes erases curvature.
- Boundary completion along different admissible factorization routes may
  retain a comparison phase; it may be structural only if the routes and
  transport are source-defined.

## DPC

When calibration holonomy is nonzero:

1. check whether endpoint-only transport was claimed;
2. identify the ordered routes producing the competing transports;
3. verify source authority for route distinction;
4. correct each observation with its own route transport;
5. test agreement of the recovered source response;
6. delete route labels and confirm the predicted ambiguity;
7. classify unexplained or retrospectively added route dependence as a
   failure, not curvature.

## Disposition

Flatness is the criterion for descent from routes to endpoints. It is not a
universal validity condition for transport. Nonflat calibration is lawful only
as a route-labelled connection whose holonomy remains observable.

## Verification

The checker check_route_dependent_calibration.py exhausts all 64 \(C_4\)
triangle connections, classifies flat and curved assignments, verifies
route-specific recovery for every source phase, and demonstrates the
endpoint-erasure contradiction on a curved hostile.
