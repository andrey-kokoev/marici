# Arb calibrates a finite-prime noise certificate for the attachment witness

## Certified result

For the actual two-window, four-event attachment witness, use

    z=3i, gamma=2, delta=1/2, forcing beta=4,
    prime cutoff p<=10000 (1229 primes, all their powers retained).

There is an explicitly rationally calibrated observer for which per-feature labelled-response errors at most 10^(-22) still certify

    Re(observed witness)>0.12 w_seam>0.

The certificate encloses theta summation, window integration, calibration, and omitted prime-place error. It uses rigorous Arb ball arithmetic, not sampled quadrature or floating-point sign inference.

Files:
- `checkers/certify_finite_prime_attachment_noise.py`
- `results/finite-prime-attachment-noise-certificate.json`

Input theorem: `the-nonzero-attachment-observer-has-a-linear-labelled-noise-certificate.md`.

## 1. Freeze the actual source normalization

Use the completed theta convention explicitly recorded in Nima's `completed-theta-autocorrelation-has-an-explicit-double-dirichlet-kernel.md` and Grothendieck's `the-dilation-coordinate-turns-each-theta-label-into-a-positive-length-three-jordan-packet.md`:

    Phi(x)=exp(x/2) sum_(n>=1) (4 a_n^2-6 a_n)exp(-a_n),
    a_n=pi n^2 exp(2x).

The present positive-half-line estimates do not use any unrestricted autocorrelation-series interchange. An older first-atom convention with coefficients 2 and 3 is not silently substituted for this completed normalization.

Keep the actual windows [log 2,log 4] and [log 4,log 12]. Define

    X_i=integral_window cosh(3x)Phi(x)dx,
    J_i=integral_window x sinh(3x)Phi(x)dx,
    mu_i=J_i/X_i.

All constants below concern these windows and the existing selected balanced sectors. No edge or source relation is changed.

## 2. Rigorous theta and integration enclosure

Each window is divided into 4096 equal cells. The exact logarithmic endpoints and each whole cell are enclosed by Arb balls at 160-bit precision. On every cell the integrand is evaluated over the ENTIRE interval and multiplied by its enclosed width. Summing these interval integrals encloses the true integral without a quadrature remainder assumption.

The first two theta atoms are evaluated explicitly. Write c=pi exp(2x). For n>=3, positivity and

    0<(4c^2 n^4-6c n^2)exp(-c n^2)
      <=4c^2 n^4 exp(-c n^2)

hold on both windows. Successive majorants have ratio at most

    r=(4/3)^4 exp(-7c)<1.

Thus the omitted atom sum is enclosed between zero and

    exp(x/2) 4c^2 3^4 exp(-9c)/(1-r).

The implementation adds this nonnegative enclosure on every cell. It bounds the completed sum, not just a finite theta approximation.

The resulting rigorous balls include

    X_1 = [0.00056 +/- 2.54e-6],
    X_2 = [1e-18 +/- 3.81e-20],
    mu_1 = [0.72 +/- 5.13e-3],
    mu_2 = [1.4 +/- 0.0450].

The actual Arb comparisons certify mu_2-mu_1>0.6. Displayed balls are intentionally coarse printed enclosures; no midpoint is treated as exact source data.

## 3. Calibrate the operator and observer independently

At s=7/2 compute

    L(s)=1/s+1/(s-1)-log(pi)/2+psi(s/2)/2-P(s).

Arb evaluates the elementary constants and digamma. P(s) is enclosed using actual Mangoldt prime powers n<=4096 and the omitted bound

    sum_(n>N) Lambda(n)n^(-s)
      <=N^(1-s)[log N/(s-1)+1/(s-1)^2].

Here s>1 and the integral majorant is decreasing beyond the chosen cutoff. This gives

    L(7/2) = [0.13668993 +/- 5.00e-9].

The exact-observer test norm from the preceding theorem is enclosed by

    C_test = [3.62804495 +/- 2.90e-9].

The stronger prior is admissible because y-gamma-delta=1/2. Its explicit port bounds are

    P_i=sqrt(2)X_i[sqrt(91)+|mu_i-L(7/2)|],

with enclosures near 0.0080 and 1.5e-17 respectively. These bounds control the finite-place operator error on the actual inputs.

## 4. Quantitative finite-place and noise budgets

For gamma=2 the response-tail exponent is sigma=5/2. At N=10000,

    T_N=N^(-3/2)[(2/3)log N+4/9]
       = [6.5846713590952329351590883236027489980473817474e-6
          +/- 6.54e-53].

The existing labelled cutoff estimate is ||O-O_P||<=3T_N. For the exact source-normalized observer, the resulting witness error per w_seam is enclosed by [0.0021 +/- 6.46e-5]. Per-feature response noise of 10^(-22) contributes [0.00037 +/- 7.16e-6].

The exact witness and its certified remaining real margin are both positive; the script verifies a remaining margin greater than 0.14 per w_seam. These comparisons are performed on intervals, not their displayed midpoints.

## 5. Rational calibration removes reliance on exact unknown normalizers

For an implementable fixed observer use the exact rationals

    Xhat_1=0.00056,  Xhat_2=10^(-18),
    Lhat=0.13668993,
    ohat=(exp(-3u),-2Lhat exp(-3u)).

Normalize its two selected sectors by -1/Xhat_1 and +1/Xhat_2. The true full-response signal of this observer, per seam weight, is

    S=sqrt(2)/6 [ (X_2/Xhat_2)(mu_2+L-2Lhat)
                 -(X_1/Xhat_1)(mu_1+L-2Lhat) ].

The term L-2Lhat follows from the unchanged arithmetic form and the changed fixed observer. Calibration error is therefore INCLUDED in the enclosing ball for S, rather than ignored or estimated from sampled source amplitudes.

Let Chat_test be the displayed test-norm formula with Lhat in place of L. Its total cutoff-plus-measurement error is bounded by

    E=Chat_test [ (10^(-22)+3T_N P_1)/Xhat_1
                +(10^(-22)+3T_N P_2)/Xhat_2 ].

The script encloses S-E and checks directly

    S-E>0.12.

This is the announced certificate for a completely specified rational calibration. The exponentials and prescribed test/dual integrals are still the analytic measurement functional; numerical error in evaluating those integrals must be covered by the stated response/error budget.

## 6. A direct finite-prime scalar cross-check

The finite-place scalar can also be evaluated directly, independently of the coarse operator-tail error. On this Euler fibre all powers of each included prime sum geometrically:

    P_included(7/2)=sum_(p<=10000) log(p)/(p^(7/2)-1).

Let L_P use this finite-place prime term and the unchanged gamma and endpoint terms. Keep the window residual at its FIXED all-prime value mu_i-L. Then the rationally calibrated finite observation is

    S_P=sqrt(2)/6 [ (X_2/Xhat_2)(mu_2+2L_P-L-2Lhat)
                  -(X_1/Xhat_1)(mu_1+2L_P-L-2Lhat) ].

The checker sums these 1229 prime contributions using Arb, subtracts the measurement-noise budget, and independently verifies a remaining margin greater than 0.12. No cutoff-dependent residual was fitted to obtain this agreement.

## 7. Scope and compatibility

The conclusion certifies the existing nonzero attachment observation from finite-place labelled responses in the declared weighted-dual topology. It does not assume arbitrary noisy data are cycles, prove existence of a reconstruction from every noisy vector, or promote responses to ordinary L2.

The archimedean response is held fixed analytically. A further numerical approximation to it must contribute to the declared error budget; no full response-field discretization is claimed here.

The first omitted theta tail and the omitted prime powers are analytically enclosed. Thus the certificate is about the completed theta source and the all-prime comparison, not just an isolated finite sampled model.

The newly supplied actual-letter factorization theorem preserves the same source ideal and allows its justified native/inherited comparison; it changes none of these observation constants. The independently supplied escaping-cutoff theorem concerns raw kernel sources in ordinary L2, not these bounded test/dual observations, and does not invalidate this certificate.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/certify_finite_prime_attachment_noise.py

The run writes the JSON artifact with rigorous balls, calibration values, and checked inequalities. All certificate assertions pass.
