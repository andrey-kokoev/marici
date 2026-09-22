# Signed fixed-hat pairings resolve the frozen middle case

## Result

The conjecture succeeded: a direct, source-anchored enclosure of the signed pairing resolves both frozen middle cases WITHOUT enlarging the projection.

The answer is **CERTIFIED_INFEASIBLE**, relative to the unchanged source family, raw intervals and order-16 prior. It is not a newly measured source, nor a claim about sources outside that model.

Approximate certified bounds are

    C_bin in [1.9721802517665386, 1.9721846168572132],
    positive gain in [6.280441788911149, 6.280464194187088] * 1e-193.

The gain upper bound is below the frozen decision threshold by about 4.04005e-199. The normalized necessary source cost is about

    40.000025679423985 > 40

in both private and reuse modes. Exact rational inequalities, not rounded displays, certify the contradiction.

The new C interval is about 20.25 times narrower than the 272-dimensional projection enclosure. Existing feasible/infeasible cases and nonvacuous positive-task certificates are preserved. Ten portable refinement chains pass isolated verification.

## 1. The missing information was a signed functional, not a whole state

The projection proof bounded

    <g-Pg, b-Pb>

by a product of residual norms. The actual response g is not an arbitrary Hilbert-space vector with those moments and that norm. Its analytic definition imposes additional structure.

This calculation pushes the fixed hat b through that definition and evaluates the resulting scalar functional directly. It does not reconstruct the full residual or claim a lossless replacement for it. The fixed filters and response definitions remain the authoritative inputs.

For orientation, the resulting signed corrections to the two old projected pairing centers are approximately

    plus:  [-4.26e-9,  1.390e-6],
    minus: [-1.995e-6, 9.763e-7].

Their sum cannot bridge the gap to the critical C interval. Finite contributions are kept signed. The last uncomputed tails still use conservative absolute bounds; the result does not depend on claiming an optimal joint tail estimate.

## 2. Exact anchor to the existing response transforms

Set

    s=7/2, beta=3/2,
    a=s-1=5/2, lambda=s+beta-1=4, d=s-beta=2,
    D(q)=psi(q/2)/2-log(pi)/2+zeta'(q)/zeta(q).

The OLD bulk responses, in their existing sign convention, have Laplace pairings at q=beta+r

    G_plus(r)  = (D(q)+D(s))/(q+s-1),
    G_minus(r) = (D(s)-D(q))/(q-s).

Substituting L(q)=1/q+1/(q-1)+D(q) into the original response formulas proves these identities by rational cancellation. The checker verifies them symbolically. The q=s singularity is removable.

For real q,s>1, introduce the positive measure

    nu(du)=du/(1-exp(-2u)) + sum_(n>=2) Lambda(n) delta_(log n)(du).

The digamma difference integral and the absolutely convergent logarithmic Euler product give

    D(q)-D(s)=integral [exp(-s*u)-exp(-q*u)] nu(du).

These are identities for the completed response, not a finite-prime replacement for it.

## 3. Pull the observable through the response

For the fixed plus hat define

    B0=integral_0^64 b_plus(t) exp(-4t) dt,
    T(u)=integral_u^64 b_plus(t) exp(-4t) dt,

with T(u)=0 for u>64. For the minus hat define

    J(u)=integral_0^min(u,64) b_minus(t) exp(2t) dt.

The exact pairings are

    <g_plus,b_plus> = 2 D(s) B0 + integral K_plus(u) nu(du),
    <g_minus,b_minus> = integral K_minus(u) nu(du),

where

    K_plus(u)=B0 exp(-s*u)-exp(a*u) T(u),
    K_minus(u)=-exp(-s*u) J(u).

Testing these formulas on b(t)=exp(-r*t) reproduces the two response transforms exactly; the symbolic checker verifies the kernel identities. Laplace uniqueness identifies the same responses used by the existing projection proof.

There is also a useful structural consequence:

    g_minus(t)=-exp((s-beta)*t) integral_[t,infinity) exp(-s*u) nu(du).

Thus this response is nonpositive (up to immaterial endpoint conventions at atoms). Its rescaled magnitude is a tail of a positive measure. Norm bounds alone do not retain that information.

The paired kernels vanish linearly at u=0, cancelling the measure's 1/u singularity. For bounded compactly supported hats the combined integrals are absolutely convergent, permitting the interchange used above. One must keep the cancelling terms together rather than separately integrate divergent origin terms.

## 4. Archimedean calculation and the origin

For a linear hat segment, T and J have exact elementary exponential primitives. Consequently K_plus and K_minus are explicit exponential-polynomial expressions on each segment.

On [epsilon,64], epsilon=2^-28, every cell lies within a single hat segment. Exact rational cell boundaries prevent crossing a slope discontinuity silently. The same whole-cell fourth-derivative Taylor bound used in the theta refinement encloses

    integral K(u)/(1-exp(-2u)) du.

The baseline calculation uses 2679 cells. No endpoint sampling is substituted for the derivative bound.

The origin is handled separately. For any real r,t,

    (exp(r*u)-exp(t*u))/u
      =(r-t) integral_0^1 exp((t+v*(r-t))*u) dv,

and for 0<=u<=epsilon,

    1/2 <= u/(1-exp(-2u)) <= exp(2epsilon)/2.

The code first rewrites each numerator to enforce its exact zero, then applies these interval bounds. It never divides an interval containing zero by another such interval.

Past 64, both kernels are constant multiples of exp(-s*u). Their integrals are bounded using

    integral_64^infinity exp(-s*u)/(1-exp(-2u)) du
      <= exp(-64s)/(s*(1-exp(-128))).

## 5. Complete prime-power sum and a proved tail

The finite part includes every prime power n=p^k<=N, with weight Lambda(n)=log p. The baseline uses N=1000000. The kernel values and sums use Arb arithmetic; floating-point interval lookup is followed by a rigorous check that log n lies in the chosen hat segment.

The tail uses an elementary, deliberately conservative bound for the Chebyshev function psi_0(x)=sum_(n<=x)Lambda(n):

    psi_0(x) <= 2 log(2)*x + log(x) + log(2),  x>=1.

To prove it, let m=ceil(n/2). Every prime power in (m,n] contributes to the valuation of binomial(n,floor(n/2)), while all other valuation contributions are nonnegative. Hence

    psi_0(n)-psi_0(m) <= n log(2).

Iterating n -> ceil(n/2) gives a sum bounded by 2n+ceil(log_2 n), and ceil(log_2 n)<=log_2 n+1. Monotonicity extends the bound to real x. The finite integer tests check the recurrence's implementation; they are not the universal proof.

Partial summation now yields, for p>1,

    sum_(n>N) Lambda(n)n^(-p)
      <= 2 log(2)*p/(p-1)*N^(1-p)
         +N^(-p)*(log N+1/p+log(2)-psi_0(N)).

The checker verifies the antiderivatives exactly for p=3/2 and 7/2.

Let M_plus and M_minus bound the absolute hats after log N. Their values follow from the remaining linear-segment endpoints. Then

    |K_plus(log n)| <= |B0| n^(-s) + (M_plus/4)n^(-beta),

    |K_minus(log n)|
      <= (|J(log N)|+M_minus*N^2/2)n^(-s)
         +(M_minus/2)n^(-beta).

The second inequality is intentionally looser than necessary but valid. Applying the two weighted-tail bounds gives remainder radii of approximately

    6.94941e-7 and 1.48219e-6.

All omitted prime powers remain covered. Neither a finite-prime source model nor an unproved prime-number estimate is introduced.

## 6. Reconstruction of C and the task contradiction

The two bulk pairings are combined with the unchanged endpoint contribution and weak-hat pairing. The latter is recomputed directly from the fixed manifest. No Gram solve or new projection is used in this calculation.

The existing Taylor-refined theta masses, moments and L enclosure then give the new positive-gain interval. Its upper endpoint lies strictly below the frozen threshold. Even the smallest possible required positive source coefficient therefore exceeds the remaining budget after paying for the measured b_2=1/100.

Additional unmeasured source coefficients have nonnegative cost and cannot repair this contradiction. The result concerns the declared 271-direction-per-background source family and its unchanged moment prior. It does not rule out a broader source or an invalid error/prior assumption, and it does not assert that these synthetic fixture observations physically occurred.

## 7. Reproduction and verification

Fresh direct pairing, a second cutoff/mesh computation and frozen-task replay:

    uv run --with python-flint python research/grothendieck/checkers/certify_signed_pairing_task.py

Symbolic identities, tail checks, exact task replay and portable export:

    uv run --with sympy python research/grothendieck/checkers/check_signed_pairing_task.py

Standalone verification of the resolved middle chain:

    python research/grothendieck/certificates/verify_source_task_transition.py research/grothendieck/results/portable-source-task-transitions/private-middle_threshold-signed-pairing.json

The independent numerical replay uses N=500000, 224 bits and a finer archimedean mesh. Its enclosure overlaps the baseline. This is a regression, not the justification for the infinite tails or transform identities.

Artifacts:

- `research/grothendieck/results/signed-fixed-hat-pairing.json`
- `research/grothendieck/results/signed-pairing-task-refinement.json`
- `research/grothendieck/results/signed-pairing-task-tests.json`
- `research/grothendieck/results/three-channel-source-task-calibration-signed-pairing.json`
- `research/grothendieck/results/portable-source-task-transitions/*-signed-pairing.json`

The standalone task verifier checks exact source obligations and identity-refinement edges; analytical validity of the supplied gain enclosure remains the owning calculation and proof's obligation. Corruption tests reject altered raw evidence, a weakened prior and an understated necessary cost.

## Understanding gained

The successful jump was to compute the relevant functional through the analytic response law, rather than approximate the entire response more accurately in an auxiliary Hilbert space. The old residual-norm bound was sound but discarded useful signed structure. Restoring enough of that structure closed the decision gate without new readings, changed filters, a larger projection, or a stronger prior.
