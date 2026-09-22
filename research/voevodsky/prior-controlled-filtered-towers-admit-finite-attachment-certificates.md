# Prior-controlled filtered towers admit finite attachment certificates

## Result

A realized actual-letter tower whose degree-one quotient vanishes admits a finite certificate for the fixed nonzero attachment observation. There is an explicit forward error budget combining source truncation, retained source-coefficient error, finite prime cutoff, and response noise.

For this PARTICULAR observer there is a sharper fact: it has finite corner support. Depth two and retention of its full labelled four-event packet make its depth and endpoint omission errors exactly zero. Infinite-tower approximation priors are necessary for global source recovery, but not for observing coordinates that have already stabilized.

The statement concerns genuine realized sources and a known positive observation margin. Priors alone do not imply nonvanishing, and arbitrary noisy quotient data are not asserted to be realizable.

Inputs:
- `../nima/uniform-actual-letter-budgets-characterize-realizable-infinite-filtered-towers.md`
- `../nima/endpoint-tightness-completes-finite-packet-approximation-of-filtered-towers.md`
- `native-actual-letter-source-budgets-preserve-the-calibrated-attachment-certificate.md`
- `arb-calibrates-a-finite-prime-noise-certificate-for-the-attachment-witness.md`

## 1. Source assumptions and a fixed finite observable

Let t be a compatible tower with the uniform actual-letter quotient budgets at EVERY radius required for realization. Let x in X_Gamma be its unique source. Assume t_1=0, so x belongs to J_(2,Gamma). Its joint attachment therefore factors through I^2/I^3 in the already declared completion.

Use the fixed rationally calibrated observer from the finite certificate:

    z=3i, gamma=2, beta=4,
    Xhat_1=0.00056, Xhat_2=10^(-18), Lhat=0.13668993.

Let F_* be the finite complete source corner packet whose four-event, one-feature records can reach its two selected balanced sectors. Retain every background/type label in that packet, not merely the numerical endpoint 420. Let pi_* denote this finite corner projection followed by the one-feature homogeneous projection.

All relevant source derivatives, terminal lifts, and forward balancing operations preserve endpoints, total event length and retained feature degree. Thus the selected response maps Y_P and Y_infinity, and the scalar observation Lambda, satisfy

    Y_P=Y_P pi_*,   Y_infinity=Y_infinity pi_*,
    Lambda=Lambda pi_*.

Here Y collects the two UNscaled selected feature responses with their sum norm; the scalar observation restores w_seam as before. These maps are not observations of all completed receiver coordinates.

Fix a proper labelled corner height h, with finite sublevels F_H, and put h_*=max_(c in F_*) h(c). A concrete permissible exhaustion can take F_1=F_* before enumerating the remaining corners. No multiplicativity of these projections is required.

## 2. Uniform forward constants in the source Q_5 norm

Write rho=sqrt(w_seam)>0. The preceding native-source certificate gives, on the selected length-four packet,

    ||Y_P z|| <= (14/rho) Q_5(z),

uniformly over finite prime sets and at the limit. Explicitly, 2944*70/15000<14: the factors account for response substitution, derivative choices, the actual theta-weighted lift, and the homogeneous factorial/path norm.

Before applying the response, the sum of the selected strong port norms is bounded by

    (0.3/rho)Q_5(z),

since 16*4*70/15000<0.3. Therefore, when P contains every prime <=N,

    ||(Y_infinity-Y_P)z|| <= (0.9 T_N/rho)Q_5(z),
    T_N=N^(-3/2)[(2/3)log N+4/9].

These estimates extend to x by the finite contractive projection pi_*. They do not require a global derivative estimate with the same constants on all event lengths.

The scalar response functional for the rational observer has norm at most

    4*10^18 w_seam

on the two-sector sum space: its test norm is below four and max(1/Xhat_1,1/Xhat_2)=10^18. This deliberately conservative constant is sufficient for a finite existence/certification theorem; the calibrated witness admits much sharper constants.

## 3. Finite approximation with a source prior

Suppose, in addition to realization, that

    Q_(10,eta,h)(x)<=M,  eta>0.

The finite source A_(m,H)(t) is determined by the stabilized corners in t_m of length <=2m+1 and height <=H. The supplied approximation theorem gives

    Q_5(x-A_(m,H)(t))
      <=M[2^(-2m-2)+(H+1)^(-eta)].

Let a_tilde be a genuine finite source candidate in J_2, supported in these stabilized coordinates, with

    Q_5(a_tilde-A_(m,H)(t))<=epsilon_Q.

This is a SOURCE coefficient/quotient-data error. It is not a response norm. Finite source constraints must be respected or independently verified; no arbitrary noisy data lift is assumed.

Let the measured selected output y be within epsilon_R, in the sum response norm, of Y_P a_tilde. Forward linearity then gives

    ||y-Y_infinity x||
      <= (14/rho){epsilon_Q+M[2^(-2m-2)+(H+1)^(-eta)]}
         +(0.9 T_N/rho)M+epsilon_R.

The prime term is evaluated on the exact x and Q_5(x)<=M. Source perturbations are handled separately by the uniform finite-P forward bound, so there is no need to refit the residual or recalibrate the observer on the perturbed source.

## 4. Scalar certificate and explicit finite choices

Denote the bracketed response bound in section 3 by E. If d_hat is the measured scalar observation, then

    |d_hat-Lambda(x)|<=4*10^18 w_seam E.

Thus an observed interval with Re(d_hat)>4*10^18 w_seam E certifies nonzero Lambda(x). Conversely, if a genuine source family is known to satisfy

    Re Lambda(x)>=d_0 w_seam,  d_0>0,

and 4*10^18 E<=d_0/2, the measured real part is at least d_0 w_seam/2.

One sufficient, finite choice is obtained by putting b=d_0/(40*10^18) and requiring

    epsilon_Q <= b rho/14,
    M 2^(-2m-2) <= b rho/14,     m>=2,
    M(H+1)^(-eta) <= b rho/14,  H>=h_*,
    N >= max(3,ceil(M/(b rho))),
    epsilon_R <= b.

Indeed log N<=sqrt(N) implies T_N<=10/(9N), so the prime contribution is at most b. The five contributions to E are then each at most b, and the total scalar error is at most d_0/2 per seam weight.

For example, the depth can be the smallest integer m>=2 satisfying its displayed geometric inequality; the height can be max(h_*,ceil((14M/(b rho))^(1/eta))). These are finite choices, not claims of optimal practical sizes. The exact rational checker includes a parameter fixture illustrating their conservative size; it is not a claimed measurement of an unspecified tower's prior.

## 5. The sharper finite-support certificate

For this fixed observer, once

    m>=2,   H>=h_*,

every corner it can see is already retained: its length four is below 2(m+1). Consequently

    Y_P A_(m,H)(t)=Y_P x,
    Lambda A_(m,H)(t)=Lambda(x).

Thus BOTH omission terms in the observation bound are exactly zero. No height or radius prior is needed to control omitted coordinates for THIS observation. Such priors remain necessary if the goal is approximation of the full source or an unbounded family of observers.

Let M_*=Q_5(pi_*x), or a certified upper bound from the finite quotient data. The sharper response error is

    E_*=(14/rho)epsilon_Q+(0.9 T_N/rho)M_*+epsilon_R.

For a known positive margin d_0, choose b_*=d_0/(24*10^18), epsilon_Q<=b_*rho/14, epsilon_R<=b_*, and N>=max(3,ceil(M_*/(b_*rho))). Then the three terms are at most b_*, and the same half-margin conclusion follows.

With an exhaustion starting at F_*, depth m=2 and height H=1 suffice. For the original witness and its calibrated source perturbation ball, use the much sharper previously verified N=10000 budgets instead of the very conservative universal N formula.

This is a finite certification theorem for an entire class of realized towers: arbitrary additional source components outside F_* do not affect this fixed labelled observation. It is not a reconstruction theorem for those unobserved components.

## 6. Calibration and algebraic integrity

The observer calibration is exactly the rational triple fixed in section 1. Its discrepancy from the ideal source-normalized observer was enclosed in the existing Arb proof. A known margin d_0 here must refer to THIS fixed functional; it cannot be borrowed from another observer without its calibration error bound.

If numerical evaluation introduces an additional scalar enclosure radius kappa_cal*w_seam, add kappa_cal to the normalized error. For a half-margin guarantee, one can apply section 4 with d_eff=d_0-2kappa_cal>0 in place of d_0; the combined error is then at most d_0/2. Interval evaluation need not introduce such a point-rounding error if its radius is retained in the reported observation enclosure.

The finite candidate must retain exact ideal, derivative and balancing identities. The certificate does not declare a noisy vector to be a cycle. Nonzero detection of the genuine J_2 source image uses the existing finite source-equivariant nullhomotopy obstruction; components outside the observed packet cannot cancel the selected typed sectors.

No arithmetic-response kernel replaces the terminal-record ideal. No inference runs backward from response error to source error. Common-path requirements, if separately imposed, require their own source budgets and endpoint tails.

## Verification

`uv run python research/voevodsky/checkers/check_finite_tower_attachment_budget.py`

The exact rational checks verify the forward constants, five-term allocation, and depth-two stabilization. The supplied endpoint-tightness checker also passes. Source realization and localization use the actual cornerwise constructions; the calibrated response margin remains the independently checked Arb theorem.
