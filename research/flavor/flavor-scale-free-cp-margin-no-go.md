# Scale-free flavor symmetry cannot supply a positive CP margin: WP1020

## Question

Can representation, charge, support, CP, and rank-one portal data alone force
a positive physical transmission margin (|T|\ge\tau>0)?

## Admitted source ray

Start from the exact WP90 witness and rescale one real portal coupling:

\[
Y_d(\lambda)=Y_0+\lambda z ab,qquad \lambda>0.
\]

Every point on this ray has the same fields, gauge representations, charges,
CP action, portal support, and rank-one topology. The portal remains nonzero
and belongs to the same qualitative orbit for every finite (lambda>0).
Only its unnormalized magnitude changes.

## Exact obstruction

The checker obtains

\[
\det[H_u,H_d(\lambda)]=1152i\lambda^3.
\]

All finite positive points transmit CP, but their invariant margin has
infimum zero. Using the exact spectral discriminants, the normalized
Jarlskog invariant obeys

\[
J^2(\lambda)=O(\lambda^6),qquad
\lim_{\lambda\to0^+}J^2(\lambda)=0.
\]

The endpoint has nondegenerate diagonal up and down spectra, so this collapse
is not caused by a spectral degeneracy.

## Consequence

Any proposed source constraint invariant under positive portal rescaling
cannot establish a uniform (	au>0). It can classify a nonzero portal,
exclude a literal missing edge, or rigidify an orbit, but it cannot normalize
the physical CP response.

This is stronger than the WP1018 aligned counterexample. Even after deleting
the exact blind hypersurface and retaining only transmitting portals, the
scale-free family has no positive margin.

## Contextual partition and instrument

The signed Jarlskog/CKM instrument separates the CP signs and resolves the
shrinking magnitude. It does not choose (lambda). The 1,210 fitted sheets
all have nonzero (J), but that empirical lower scale cannot be used to
normalize the source without circularity.

## Smallest exact falsifier

The family (lambda=1/n) preserves every listed qualitative source datum
while

\[
\det[H_u,H_d]=1152i/n^3.
\]

Thus any symmetry-only positive-margin claim is falsified by arbitrarily
large (n).

## Claim boundary

The theorem applies to homogeneous or otherwise scale-free source constraints
that admit the positive rescaling ray. A nonhomogeneous source equation,
quantized coupling, or independently normalized positive pairing could evade
it. Those are additional source resources, not consequences of the present
symmetry grammar. No implicit time or causal interpretation is used.

## Disposition

Close coefficient-free scale symmetry as a route to the CP magnitude. Reopen
only with an independently derived nonconic normalization, its radiative
closure, and a physical calibration instrument.

Verification: uv run --with sympy python
research/flavor/checkers/wp1020_scale_free_cp_margin_no_go.py.
