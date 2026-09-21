# Raw theta inversion is severely conditioned; fixed forcing does not restore route correlations

## Disposition

Two checks limit the preceding finite reconstruction proposal:

1. In the unweighted interval coefficient / raw half-line L2 theta metric, every left inverse of the full fifteen-atom theta synthesis has norm greater than 10^113376. Algebraic unimodularity does not address this metric obstruction.
2. The reviewed fixed-forcing joint graph cannot recover route correlations if its input is the already aggregated interval history. Its injectivity retains that input, not a finer source that was previously quotiented out.

These are precise restrictions, not a claim that every independently enriched physical source is impossible. In particular the inverse bound below does not prove that every restricted twenty-four-route decoder has the same lower bound.

## 1. Analytic column estimate

Let I=[log a,log b), a>=2, ell=log(b/a), and use the recorded atom

Phi_1(u)=exp(u/2)(2 pi^2 exp(4u)-3 pi exp(2u)) exp(-pi exp(2u)).

On u>=log 2 it is positive and bounded above by

2 pi^2 exp(9u/2) exp(-pi exp(2u)).

For s>=0, the product of the two upper bounds, as a function of v>=log a, has logarithmic derivative

9-2 pi exp(2v)(1+exp(2s)) < 0.

Thus the interval column H_I(s)=integral_I Phi_1(v)Phi_1(v+s)dv satisfies

0 <= H_I(s) <= 4 pi^4 ell a^9 exp(9s/2) exp[-pi a^2(1+exp(2s))].

Squaring and using exp(2s)>=1+2s yields

||H_I||_2 <= 4 pi^4 ell a^9 exp(-2 pi a^2) / sqrt(4 pi a^2-9).

This is an analytic bound on the entire half-line, not a quadrature cutoff estimate.

## 2. The last atom

For root 2 and primes (2,3,5,7), the final consecutive labels are 210 and 420. Hence a=210 and ell=log 2<1. Using 3<pi<4 and sqrt(4 pi a^2-9)>1 gives

||H_last||_2 < 1024 * 210^9 * exp(-264600).

The exact rational checks establish 1024*210^9<10^24 and log 10<7/3. The latter follows from the first nine terms of the positive exponential series at 7/3 exceeding 10. Therefore

||H_last||_2 < 10^-113376.

If L is any bounded left inverse of the full atom synthesis H, then L H_last=e_last, whose Euclidean norm is one. Consequently

||L|| > 10^113376.

The canonical Gram inverse is subject to the same lower bound. H^{tensor 4} likewise has a column H_last^{tensor 4}, so a left inverse on the entire coefficient tensor space has norm greater than 10^453504. This tensor bound concerns the full tensor space, not automatically the much smaller route image.

Column normalization can move these large factors between synthesis, extraction, source coefficients, and measurement noise. It cannot be declared a physical cure without specifying which metric and absolute noise model the source actually supplies. Arbitrary-precision arithmetic by itself is not an experimental stability certificate.

## 3. Source contract audit

The reviewed source map is

F_Ev(u)=(C_Phi u, Phi tensor u),

with a fixed nonzero forcing vector Phi. The tensor coordinate is injective as a function of u. Let W map route mixtures to the aggregate interval history (or to all linear edge marginals). The established collision h satisfies Wh=0 but Bh != 0 for the desired correlation readout B.

Then F_Ev(W(c+h))=F_Ev(Wc). Every deterministic operation on that joint graph has the same value on those inputs. Correlation, tensor insertion, translation, or differentiation applied after W cannot change this equality when defined on the common input. This conclusion does not require the downstream operation to be linear or bounded.

Likewise the reviewed Adams-two/separation-history packet retains specified ordered shell-pair labels. That declaration alone is not a map from the four-prime free-route source, and it does not establish access to the required route-conditioned four-event products. Those are different typed source contracts.

The route-aware Volterra and interval tensor implementations remain valid enrichment constructions. They have not shown that the existing physical Evans or theta carrier contains their inputs.

## 4. Updated action boundary

Do not invest in a brute-force raw theta Gram inversion as the next step. First specify either:

- a physically justified weighted/normalized measurement model, with its noise and source norm, followed by conditioning on the actual route image; or
- a source retaining route-event labels before additive aggregation, with an independently defined adapter to the joint theta/correlation channel.

If the prescribed source is only Wc, the adapter is ruled out by the positive-mixture collision. If a finer source is available, identify it and its operations explicitly rather than infer them from injectivity of F_Ev on its own input.

## Verification and evidence

`python research/grothendieck/checkers/check_theta_inverse_conditioning_barrier.py` passes. It checks rational constants and interval endpoints; the continuum proof is the estimate above.

Sources inspected:
- `research/nima/evans-to-joint-response-source-map-and-fixed-marginal-hostile.md`
- `research/voevodsky/the-minimal-faithful-pair-to-cyclic-square-target-is-adams-two-tensored-with-separation-history.v1.json`
- `research/voevodsky/the_completed_theta_correlation_is_injective_on_the_arithmetic_interval_range_20260912.md`
- `research/nima/the-arithmetic-interval-diamond-has-a-source-derived-theta-cycle-reconstruction-and-determinant-line.md`

This is a bounded audit of the listed interfaces, not a repository-wide assertion that no finer physical source exists.
