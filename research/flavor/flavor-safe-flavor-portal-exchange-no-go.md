# Safe flavor-portal exchange no-go: WP727

## Question

Do the anomaly-free asymptotically safe flavor-portal models of Hiller,
Hormigos-Feliu, Litim, and Steudtner realize the WP724 source principle by
fixing a nonzero ordered portal contrast on the admitted real-triplet flavor
quotient?

## Source boundary

The audited source is arXiv:2008.08606v1. Its BSM matter consists of three
generations of vector-like leptons and a complex matrix scalar (S). The
vector-like assignment avoids a chiral-anomaly obstruction and the completed
two-loop system supplies genuine gauge–Yukawa and scalar RG dynamics.

The scalar potential contains one Higgs portal,

\[
V_p=\delta (H^\dagger H)\operatorname{Tr}(S^\dagger S).
\]

The paper's flavor assumptions reduce the relevant new Yukawa tensors to
universal couplings. At the matching scale its BSM couplings, including
\(\alpha_\delta\), are input coordinates. The reported BSM critical surface is
a viable region obtained by varying matching-scale couplings, not a singleton
prediction.

## Exact exchange obstruction

Restrict the trace norm to two ordered real norm coordinates (R_n,R_m). Then

\[
V_p=\delta h^2(R_n+R_m).
\]

The ordered portal pair is

\[
(g_n,g_m)=(\delta,\delta),
\]

so its contrast vanishes:

\[
g_n-g_m=0.
\]

Equivalently, the source image lies in the exchange-even line spanned by
\((1,1)\), whereas the required contrast is the exchange-odd covector
\((1,-1)\). This is not repaired by the existence of an interacting fixed
point: RG evolution respecting the same flavor symmetry preserves the even
subspace.

The smallest hostile extension adds an exchange-odd source coordinate

\[
\epsilon h^2(R_n-R_m).
\]

It produces (g_n-g_m=2\epsilon). Unless a larger source theory makes
\(\epsilon\) an irrelevant coordinate with a unique nonzero fixed value, this
only renames the tunable contrast.

## Fixed-point and matching audit

Asymptotic safety constrains irrelevant eigendirections, but it does not make
every coupling predicted. Relevant and marginally relevant amplitudes remain
free coordinates on the UV critical surface. In the audited study the BSM
matching values are explicitly treated as free parameters, and the numerical
critical surfaces are regions of viable initial conditions. The portal is
also assigned exemplary matching values in those scans. Consequently the
paper does not derive a unique portal magnitude, matching scale, or ordered
contrast.

The models do exhibit representation-dependent Clebsch factors in fermion
mixing and collider channels. Those factors can rigidify labelled responses,
but the paper supplies no map from them to a nonzero (n/m) portal contrast on
the Marici `physical16` quotient.

## Disposition

This known anomaly-free source class does not realize WP724. With its admitted
flavor symmetry it predicts zero ordered contrast. Breaking that symmetry by
an independent coefficient restores a contrast only as a free source
coordinate. The result is a sharp exchange no-go for this model class, not a
no-go against asymptotic safety in a representation-asymmetric theory.

The surviving candidate must satisfy a stronger condition: non-isomorphic
source representations must explicitly orient the two portal channels, so
exchange is not an automorphism of the source theory. The fluctuation about
the resulting nonzero fixed portal coordinate must then be irrelevant. An
exchange-symmetric fixed point cannot have a unique nonzero odd coordinate.
The same theory must fix the relevant clock deformation, preserve the contrast
through finite thresholds, and generate two calibrated physical response
channels. WP728 proves this correction.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp727_safe_flavor_portal_exchange_no_go.py`

Generated result: `results/wp727_safe_flavor_portal_exchange_no_go.json`.

Primary source: Hiller, Hormigos-Feliu, Litim, and Steudtner, *Model Building
from Asymptotic Safety with Higgs and Flavor Portals*, arXiv:2008.08606v1.
