# Tail-localized diamond cycles obstruct stable inversion at fixed event length

## Result

The completed receiver is injective in the specified endpointwise cut-l1 construction, but stable inversion fails even when **event length and relation depth remain fixed**.

Translate a two-event diamond to increasingly large arithmetic endpoints. Its singly retained relation has the same source coefficient norm at every location, while its function-valued seam image tends to zero exponentially in the logarithmic starting endpoint. After normalization these are source unit vectors whose images tend to zero in every seminorm of the all-depth seam scale.

Thus weights depending only on path length and depth cannot repair this obstruction. The family also gives a continuous source functional that is not the pullback of any continuous functional on the completed target. Finite endpoint observers still separate every source vector, as Voevodsky proved.

This strengthens, rather than replaces, the existing forgotten-suffix nonclosed-range example. It produces no nonzero source vector with zero image and changes none of the prescribed finite weights or Green forms.

## 1. Completed results used, not reproved

Use:

- `../voevodsky/weighted-theta-tails-and-path-length-domains-give-uniform-seam-bounds.md`;
- `../voevodsky/the-relative-normalization-pentagon-extends-to-the-cut-l1-completion.md`;
- `../voevodsky/endpointwise-separation-and-bounded-differentials-close-the-fixed-depth-l1-receiver.md`;
- `../voevodsky/the-completed-receiver-has-nonclosed-range-but-separating-finite-observers.md`;
- `../voevodsky/an-all-depth-seam-scale-has-bounded-differential-and-continuous-balanced-tensoring.md`;
- `../voevodsky/holomorphic-feature-closure-retains-completed-cross-spectral-packets.md`.

Those results provide the continuous injective endpointwise layer map, its bounded differential, relative currents, finite-observer separation, and the complete all-depth scales X_s and Y_s. The present task is the conditioning of that map, not another proof of finite faithfulness.

Keep the same forcing Phi, spectral region Omega, beta, memory multiplier tau, and positive seam-feature weight w_seam. Put

`epsilon=beta-Y>0`,

`C_feature=||A_Cl|| sqrt(mu(Omega)/(epsilon eta))`,

`h=max(tau,sqrt(w_seam))`,

`A=max(1,h C_feature B_0)`.

Here B_0 is the already proved bound on the full weighted theta forcing. A is Voevodsky's uniform letter bound, not a new parameter chosen to improve conditioning.

## 2. A localized feature estimate

For a forcing f supported in [R,infinity), put

`u(x)=exp(beta x)(1+x) f(x)`.

For sigma=+/- and j=0,1, Cauchy--Schwarz and x^j/(1+x)<=1 give

`|h_(sigma,j)(f;z)|
 <= exp(-epsilon R)/sqrt(2 epsilon) ||f||_beta`.

Indeed the squared kernel integral is bounded by

`integral_R^infinity exp(-2 epsilon x) dx
 = exp(-2 epsilon R)/(2 epsilon)`.

Integrating the half-line feature in t gives the factor 1/(2 Im z). Summing the four raw ports, integrating over Omega, and applying the existing normalized Clark matrix yields

`||Lhat(f)|| <= C_feature exp(-epsilon R) ||f||_beta`.

In particular every event window lying beyond R satisfies

`||g_e|| <= C_feature B_0 exp(-epsilon R)`.

No spectral points are sampled. This is an estimate on the full function-valued norm, including the first-moment tails.

The same integral estimate makes the raw one-letter map from the weighted forcing Hilbert space to the four-port feature space Hilbert--Schmidt. This observation is about that coefficient map; it is not a claim that the entire typed all-depth receiver is compact.

## 3. Fixed old packets remain stable

For genuine chamber refinement, an old forcing function is unchanged: its old indicator is the sum of its new subchamber indicators. Its weighted forcing norm and actual feature function therefore remain unchanged. The checker verifies the corresponding additive shell-mass identity.

A fixed finite endpoint interval contains only finitely many monotone paths and is not enlarged by new primes outside that interval. Its finite injective map consequently retains its own positive inverse bound on its image. The counterexample below uses **new outer endpoint corners**, not deterioration of a fixed old finite subspace.

These comparisons use a common capacity, or the admitted untruncated carrier. Inclusions of different truncated memory caps are not silently treated as all-state module intertwiners.

## 4. The translated two-event family

Fix the event primes 2 and 3. Let Q_n be the product of an increasing sequence of other distinct primes, all at least 5. The packet contains those background primes together with 2 and 3.

Consider the convex diamond with arithmetic vertices

`2 Q_n, 4 Q_n, 6 Q_n, 12 Q_n`.

Its source interval always has event length two. All four event forcings are supported beyond

`R_n=log(2 Q_n)`.

Let r1_n be its singly retained relation

`e1^0 e2^1+e1^1 e2^0-f1^0 f2^1-f1^1 f2^0`.

It has four coefficients of modulus one. At this interval I^2=0 by event length, so it represents a nonzero conormal vector without an additional quotient ambiguity. Its source coefficient norm is independent of n.

The derivative has eight feature-bearing terms: each of the four event features occurs once in memory and once in a seam-letter slot. The cut-l1 triangle inequality and section 2 give

`||D(r1_n)||_cut-l1 <= 8 h C_feature B_0 exp(-epsilon R_n)`.

All terms are actual source-generated seam records. The endpoints remain labelled, and the finite function-valued injection ensures each image is nonzero.

## 5. Normalization in the existing all-depth scale

At depth one and event length two, the existing source path weight is

`W_2=3 A^2`.

The graph multiplier is b_s(1)=2 lambda s, where lambda=max(1,tau/sqrt(w_seam)). Define

`u_n=r1_n/[4 b_1(1) W_2]`.

The local conormal has the two disjoint retained-degree basis patterns r0 and r1. Its coefficient norm is W_2(2|a|+4|b|) on a r0+b r1, before the graph multiplier. Thus

`||u_n||_(X_1)=1`, `||u_n||_(X_s)=s`.

The image satisfies

`||j(u_n)||_(Y_s)
 <= s [2 h C_feature B_0/W_2] exp(-epsilon R_n)`.

Therefore j(u_n)->0 in every Y_s, while u_n does not tend to zero even in X_1. The sequence is bounded in every source seminorm.

The all-depth receiver is consequently not a topological embedding on its image. This failure persists for any further fixed weights depending only on event length and relation depth: both remain 2 and 1 throughout the sequence. Such weights merely multiply these estimates by constants at that fixed pair of indices.

This conclusion does not prohibit every possible stronger target topology. It says precisely that path-length and depth controls alone cannot supply stable reconstruction uniformly in the outer arithmetic location.

### The additional feature-degree scale does not remove this family

The subsequent holomorphic-closure theorem strengthens the target by b^m, where m counts retained feature slots, and the source by replacing A^n with (b A)^n. This family has exactly one retained feature and exactly two events. Thus, with the same X_(1,1)-normalized u_n,

`||u_n||_(X_(s,b))=s b^2`,

`||j(u_n)||_(Y_(s,b)) <= s b [2 h C_feature B_0/W_2] exp(-epsilon R_n)`.

The source sequence stays bounded in each specified seminorm and the target sequence still converges to zero in their full intersection. The nonclosed-range construction and continuous-dual obstruction below therefore also hold on this stronger holomorphic feature-degree scale.

For every fixed compact spectral interior K, choose b at least its evaluation constant. The new theorem then transfers this decay to the evaluated slot family uniformly on K. Bounded compact-interior spectral observations do not restore a uniform inverse. This does not dispute their continuity or finite-observer separation, and it says nothing about observation families approaching the spectral boundary without a uniform margin.

## 6. A missing range point in the scale intersection

Because Q_n>=5^n,

`exp(-epsilon R_n) <= 2^(-epsilon) 5^(-epsilon n)`.

Thus the series

`y=sum_n j(u_n)`

converges absolutely in every Y_s and defines an element of the complete scale intersection Y_infinity. Its partial sums lie in the receiver image.

The endpoint corners of the u_n are distinct. A source preimage of y would have coordinate u_n at each of these corners by endpointwise injectivity. Its X_1 norm would therefore be at least sum_n 1, which is infinite.

Hence y is a literal point in the closure of the receiver range but not in that range, even in the all-depth scale topology. This is not an inverse-limit phantom or a nonzero completed kernel element.

## 7. A continuous source observation that has no continuous target lift

For each selected endpoint corner choose its norm-one conjugate-linear functional ell_n with ell_n(u_n)=1. In the local r0,r1 coordinates it is explicitly the scaled r1 coefficient functional. Define ell on X_1 by summing these coordinate functionals, and zero on the other corners and depths.

Absolute summability gives

`|ell(x)| <= ||x||_(X_1)`.

Thus ell is continuous on X_infinity and ell(u_n)=1 for every n.

If ell were the pullback of a continuous target functional psi, continuity and j(u_n)->0 in Y_infinity would give

`ell(u_n)=psi(j(u_n))->0`,

a contradiction. Therefore the pullback from the full continuous target dual to the continuous source dual is **not surjective** in this specified scale. Giving those duals their strong topology does not change this failure at the level of their underlying continuous functionals.

In particular no ambient finite-norm paired observer realizes ell. For a finite observer y_n realizing the individual condition ell_n(u_n)=1, the prescribed pairing bound gives

`1 <= ||j(u_n)||_(Y_1) ||y_n||_(Y_1)`.

Its norm is therefore bounded below by a fixed positive constant times exp(epsilon R_n). Signature-transformed observer channels do not remove this estimate: their involution has norm one.

Finite endpoint observers still separate every source vector, and their finite-support functionals remain weak-star dense as in Voevodsky's theorem. Uniformly bounded observer lifts and surjectivity onto the full source dual are stronger properties, and fail here.

## 8. The same phenomenon at a fixed higher relation depth

Fix 2r event primes and translate their face by background primes outside that set. Take a critical product with one local r1 relation and r-1 local forgotten r0 relations. Its source coefficient l1 norm is 2^(r+1), independent of the background. There is no positive-length balancing ambiguity at the minimal 2r-event interval.

Every derivative tensor term contains exactly one retained feature supported beyond R_n. Before contractive normalization there are at most 8*4^(r-1) such terms. With the existing path weight

`W_(r,2r)=(1+2r)^r A^(2r)`

and normalization to X_1 norm one, the same estimate becomes

`||j(u_n)||_(Y_s)
 <= s^r [2^r h C_feature B_0/W_(r,2r)] exp(-epsilon R_n)`.

Thus the obstruction is not special to depth one. It applies at fixed depth to the balanced associated-layer cycles and their shifted attachment observations. This statement is about the coefficient-layer receiver; it does not replace a full module receiver by copies of a root corner.

## 9. A separate raw-Hilbert obstruction, already avoided by cut-l1

The checker also records exact all-state memory-joining norms under the unchanged exponential Hilbert weights. On a fixed typed branch, joining two memories with output cap N has

`||mu_N||=sqrt(N+1)`.

Every degree-d output word has d+1 orthogonal splitting preimages. Multiplicative weights cancel on each normalized preimage. Joining k memory slots similarly has norm sqrt(binomial(N+k-1,k-1)). At r seam factors, the r-1 independent two-slot joins give fixed-branch norm (N+1)^((r-1)/2).

For an even-degree word in a signature eigenletter, the normalized coherent sum of its N+1 splits has fine pairing one and collision current N. These collisions are counted directly, not defined by a desired Gram discrepancy.

This explains why fixed exponential degree weights alone do not bound raw cut-l2 all-state sewing. Voevodsky's cut-l1 completion already addresses this obstruction. It is separate from the fixed-event tail obstruction above, which persists in that cut-l1 completion and its graph-norm scale.

## Verification and disposition

`uv run --with sympy python research/nima/checkers/check_completion_stability_obstructions.py`

Artifact: `results/completion-stability-obstructions.json`.

The checker verifies shell-refinement norm identities, localized trace-bound constants, the existing Clark row normalization, critical product coefficient counts, graph-scale ratios, exact word-splitting Gram matrices, and collision growth. It also records actual translated diamond endpoints. These are not numerical Clark samples or an experimental proof of the infinite statements.

The main result is the analytic fixed-length approximate-null family and its consequences for the already specified completed receiver. Finite and completed injectivity remain intact. No topology or finite pairing has been changed to repair the failed inverse bound.
