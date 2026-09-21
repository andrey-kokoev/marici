# The actual four-prime route theta decoder has an exponential noise barrier

## Result

The previous full-atom conditioning warning can be strengthened to the actual full-route source. Let A(c)=(Theta_2(c),Theta_4(c)), with orthonormal route coefficients and the direct-sum raw L2 tensor-history norm. Every bounded linear left inverse of A has norm greater than 10^9236. A nonlinear exact inverse has at least the corresponding Lipschitz lower bound on the admitted image.

This directly affects the proposed route reconstruction, not just an irrelevant full tensor coordinate. It does not apply unchanged to a different independently justified measurement metric.

## Column bounds

The preceding analytic estimate gives, for an edge spanning [log a,log b],

||H_[a,b]||_2 <= 4 pi^4 log(b/a) a^9 exp(-2 pi a^2) / sqrt(4 pi a^2-9).

All cube edges lie between labels 2 and 420. Thus log(b/a)<6, and 3<pi<4 implies

||H_[a,b]||_2 < 6144 a^9 exp(-6a^2).

The logarithmic derivative 9/a-12a is negative for a>=2. The bound at a=2 is less than one, as certified by a positive partial sum for exp(24). Hence every edge response has norm less than one.

For a>=60 the bound is at most 6144*60^9 exp(-21600). Since 6144*60^9<10^20 and log 10<7/3, it is strictly less than 10^-9237. These are entire-half-line bounds, not sampled or truncated numerical norms.

## The actual source direction

Use prime-index words and the four-route vector

h=0123+1032-0132-1023.

Its coefficient norm is 2. The exact interval-signature checker establishes K_2 h=K_3 h=0, hence Theta_2 h=Theta_3 h=0.

Each of its four routes first adds primes 2 and 3, in some order, and then primes 5 and 7, in some order. Starting at label 2, the first two steps end at 12. The final step therefore starts at 60 or 84. Each fourth-degree response is a tensor product of its four edge responses, with one factor of norm less than 10^-9237 and the others less than one. Consequently

||Theta_4 h||_2 < 4 * 10^-9237,

||A(h/2)|| < 2 * 10^-9237.

If R A=I, then 1=||R A(h/2)|| <= ||R|| ||A(h/2)||. Therefore

||R|| > (1/2)*10^9237 > 10^9236.

The two positive mixtures on either side of h also give this inverse Lipschitz obstruction by comparing their input and output distances. Normalizing both to probability mixtures changes both differences by the same factor and does not remove the ratio.

Adding the third-degree response does not help on this direction. Using amplified dual-atom probes may change the output norm, but then their measurement gains and noise must be accounted for. The coefficient matrix determinant one is not a bound on those gains.

## Source audit and decision

The reviewed Nima source-pattern audit explicitly separates NNMHV insertion/reflow histories from RH theta histories. Its finite four-chart cycle model uses a source-pulled norm and explicitly declines an actual theta/amplituhedron comparison. Voevodsky's four-prime observer assumes the free route source and states that physical theta instrumentation remains open. The fixed-forcing Evans graph is injective in its admitted history input, not in an undeclared upstream route space.

Thus no physical pre-aggregation adapter is established by these reviewed records. This is a bounded audit, not a proof that none exists elsewhere. It would be incorrect to call the route-counting norm a physical norm or to declare a source-pulled norm to be measured noise without an independent calibration model.

The immediate route-theta branch should stop here pending new source input. Its achievements are exact finite reconstruction and a now explicit measurement contract; its missing input is genuine route access plus a justified norm. Further scalar inversion or raw Gram numerics do not supply that input.

## Verification

`python research/grothendieck/checkers/check_route_theta_conditioning_barrier.py` passes the exact rational constants and checks the existing collision certificate. The analytic inequalities above supply the continuum argument.

Related records:
- `the-raw-theta-inverse-is-severely-conditioned-and-fixed-forcing-does-not-restore-route-correlations.md`
- `four-point-theta-interval-signatures-recover-the-four-prime-route-mixture.md`
- `research/nima/two-polarity-four-presentation-source-patterns-for-determinant-construction.md`
- `research/nima/a-source-cycle-selector-makes-the-two-polarity-four-chart-seam-faithful.md`
- `research/voevodsky/four-prime-correlation-observer-realization-and-minimality.md`
