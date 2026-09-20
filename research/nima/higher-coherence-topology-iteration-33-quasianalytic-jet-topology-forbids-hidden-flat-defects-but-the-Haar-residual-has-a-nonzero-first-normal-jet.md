# Higher-coherence topology iteration 33: quasianalytic jet topology forbids hidden flat defects, but the Haar residual has a nonzero first normal jet

## Candidate topology

Place the parameter-dependent higher-cone packet in a quasianalytic
Denjoy--Carleman class. Its defining weight sequence satisfies the
quasianalyticity criterion, so the Borel jet map is injective:

\[
\partial^nF(z_0)=0\ \forall n
\quad\Longrightarrow\quad
F\equiv0
\]

on the connected domain.

Holomorphic compact-open topology already has this property locally; the
Denjoy--Carleman version permits selected real-analytic and boundary variables
while excluding nonzero flat functions.

## Potential infinite-cone mechanism

If the `n`th higher coherencer killed the residual through order `n`, then a
compatible infinite tower could produce

\[
j_{z_0}^\infty r=0.
\]

Quasianalyticity would force `r=0` globally. This is a jet analogue of the
Rees separated-intersection mechanism: successive cones improve vanishing
order rather than norm.

## Haar normal jet

Take normal coordinate

\[
a=\operatorname{Re}z
\]

and

\[
r_p(a,t)
=(1-p^{-2a})E_p(b_{a+it}).
\]

At the seam,

\[
r_p(0,t)=0,
\]

but its first normal derivative is

\[
\partial_a r_p(0,t)
=2(\log p)E_p(b_{it}),
\]

because the derivative of the energy term is multiplied by the vanishing
factor. Since the retained state energy is positive,

\[
\partial_a r_p(0,t)>0.
\]

Therefore the Haar residual is not flat at the seam. Its complete jet records
the transverse confinement obstruction immediately at first order.

## What higher jets do and do not do

The flat spectral-jet connection detects every zero and multiplicity, but the
same connection exists for reciprocal hostile sections with off-seam zeros.
Jet completeness provides determination, not orientation.

To make the Haar residual flat, a higher cone must cancel the explicit positive
first normal jet above. Its coefficient is source-fixed. Choosing a compensator
from that derivative would be a fitted counterterm unless an independent
source operation supplies it.

Tangential jets along the seam are even weaker: they do not determine the
normal modulus responsible for `p^(-2a)`.

## Completion consequence

Quasianalytic topology is conservative. It prevents a residual from hiding as
an infinitely flat but nonzero completion class. Hence it strengthens the
obstruction rather than absorbing it: any proposed infinite coherence tower
must account for every normal jet, beginning with the positive first one.

## Verdict for topology 33

An infinite order-improving cone tower could force vanishing in a
quasianalytic carrier, but the actual Haar residual has a nonzero first normal
jet equal to `2 log(p) E_p(b_it)`. No current higher operation cancels this jet
independently.

The next nonredundant topology to test is a Gevrey/resurgent topology, where
factorially growing higher fillers may be Borel-summed even when the formal
coherence series does not converge ordinarily.