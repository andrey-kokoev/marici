# The undilated spline tail variation is 5184, not 81 over 2

## Eighth-derivative measure

For the centered degree-seven cardinal spline,

`D^8 k_7=sum_(j=0)^8(-1)^j binom(8,j) delta_(j-4)`.

Its total variation is

`sum_j binom(8,j)=2^8=256`.

For a finite shifted profile

`phi=sum_m c_m k_7(.+m a)`,

a triangle-inequality bound is

`||D^8 phi||_TV<=256 sum_m |c_m|`.

Both the baseline five-shift coefficients and the symmetric lag-one seven-shift coefficients have

`sum_m |c_m|=81/4`.

Therefore the undilated `c=1` bound is

`||D^8 phi||_TV<=256*(81/4)=5184`.

## Relation to the old value

For `D_c phi(x)=phi(cx)`, an eighth distributional derivative measure has total variation scaling `c^7`, not `c^8`, because the Dirac mass contributes one inverse scale. At `c=1/2`,

`5184*(1/2)^7=81/2`.

Thus the old checker’s variation `81/2` is consistent only with its dilated archimedean test `phi(x/2)`. Reusing it for the undilated repair would understate the tail variation by a factor of `128`.

## Signed atomic alternative

The coarse value `5184` may widen the Hurwitz tail but remains multiplied by an eighth-order remainder. A sharper enclosure should retain the signed atoms at

`x=j-4-m a`

and sum their kernel values directly. Baseline and cross packets have cancellation not visible in total variation.

## Acceptance tests

1. The undilated implementation must report `5184` as its coarse variation bound.
2. A deliberate reuse of `81/2` must fail.
3. The signed-atomic interval must lie inside the coarse `5184` enclosure.
4. Dilation regression must verify `TV(D_c phi)=c^7 TV(phi)` at `c=1/2`.

## Disposition

The c=1 moment prefix is ready, but interval tail regeneration must update both atom locations and variation scaling. The old `81/2` constant is not admissible.
