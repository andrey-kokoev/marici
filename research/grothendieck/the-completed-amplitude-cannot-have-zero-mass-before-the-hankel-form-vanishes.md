# The completed amplitude cannot have zero mass before the Hankel form vanishes

## Question

Can the gamma and endpoint sectors canonically balance the prime amplitude to total mass zero, thereby removing the anchor from its order-space lift?

## Exact mass identity

For a fixed Hankel polynomial `p`, each sector of the Fourier-cosine formula can be encoded by an amplitude packet whose coefficient sum equals that sector's quadratic value, up to the fixed normalization convention. Therefore the sum of the completed endpoint-free amplitude is

\[
A_{t,h}(p)=Q_{\Gamma+P}(t,h;p).
\]

Including the known endpoint restores the corresponding full completed Hankel value, not zero.

This is structural: summing the amplitude is evaluation of its cosine synthesis at frequency zero. The gamma term can cancel part of the prime mass, but a zero-total-mass identity for every `p` would assert

\[
Q_{\Gamma+P}(t,h;p)=0
\]

for every `p`.

That assertion is false. Prior work proves strict rank-one positivity in a small-heat region and fixed-rank positivity in a full small-heat corner. Hence the completed amplitude has nonzero mass for explicit admissible probes.

## Consequence for the anchored lift

For an amplitude packet `a` of mass `A`, the order-space lift requires an anchor:

\[
\iota_{\lambda_*}(a)=-A e_*+\sum_i a_i e_i.
\]

Changing the anchor changes the order vector by

\[
A(e_*-e_*'),
\]

with squared order norm

\[
2|A|^2|\lambda_*'-\lambda_*|.
\]

Since `A=Q_(Gamma+P)(p)` is generally nonzero and depends quadratically on `p`, neither gamma completion nor endpoint subtraction makes the lift anchor-independent. Choosing the anchor at zero simply recovers the earlier quadraticized construction.

## Independent multiplier obstruction

At finite prime cutoff,

\[
W_{P,N}(0)=-\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}
\longrightarrow-\infty,
\]

while the gamma multiplier remains finite near zero. Thus the joint pointwise multipliers have no cutoff-uniform lower bound on the full Gaussian `L2` space. Any surviving lower bound must use the restricted analytic probe core or a distributional regularization; ordinary multiplier semiboundedness is unavailable.

## Strongest falsification attempt

One might seek a continuous archimedean balancing packet of mass `-A`. But because `A` depends on `|p|^2`, this packet would itself be quadratic in `p`. Its order norm squared would again be quartic, so it would not define a linear factorization. A fixed balancing packet cannot cancel every probe-dependent value.

## Disposition

The gamma and endpoint sectors do not canonically supply a zero-mass amplitude before evaluation of the quadratic form. The order-completion route remains a diagnostic encoding after quadraticization, not a linear form factorization. The executable frontier is restricted-core or distributional semiboundedness of the coupled gamma–prime form; full-space multiplier and anchor-free order-lift routes are closed.