# Scaled theta calibration makes cubic template certificates robust

## Certified results

The exact-normalizer assumption is removed for the original cubic gap witness at y=3, receiver gamma=1 and forcing beta=4. Rigorous scaled theta integration supplies fixed rational normalizers and bounded moment errors, including the window starting at 60 whose amplitude is approximately 3.33e-4902.

Two finite certificates now give

    Re(observation)>0.05 w_seam^2.

1. **Original four sectors:** calibration, common/mismatched template errors, moment errors and independent labelled noise are enclosed. Common absolute tolerances of 10^(-4906) per feature and 10^(-4926) per two-feature sector suffice, with the other budgets specified below.
2. **Voevodsky's newly supplied private sectors:** a rationally calibrated residual-only observer permits total independent full-output noise 10^(-544), with the same positive margin. This certificate uses the additional EXISTING private sector and is not available from only the original four measurements.

All comparisons are Arb interval assertions. These tiny absolute tolerances are reported explicitly; a manageable relative calculation does not make independent absolute noise harmless.

The first certificate is for the original positive witness's shared-template structure. The second also bounds calibration errors on both visible source basis directions, including the crossed product. Neither supplies uniform tolerances over translated backgrounds.

## 1. Integrate late windows without underflow or unresolved boundary layers

For an actual window [log A,log(pA)], use the completed theta convention

    Phi(x)=exp(x/2) sum_(n>=1)(4q_n^2-6q_n)exp(-q_n),
    q_n=pi n^2 exp(2x).

Put t0=pi A^2, v=pi exp(2x)-t0 and D=t0 A^(7/2). At y=3 write

    X(A,p)=D exp(-t0) I(A,p).

The normalized density for I is

    cosh(3x)exp(x/2)/(2tD)
      *sum_(n>=1)(4n^4t^2-6n^2t)
                      exp(-(n^2-1)t0-n^2v),
    t=t0+v, x=log(t/pi)/2.

This density is of order one near v=0 even for the latest windows. Its physical upper endpoint is t0(p^2-1), which exceeds 32 for every window used here.

On [0,32], divide v into 8192 equal cells. Arb encloses each WHOLE cell, evaluates the density interval, and multiplies by its exact cell width. The first two theta atoms are explicit; the remaining scaled atom sum is bounded by

    4t^2*81 exp(-8t0-9v)
       /[1-(4/3)^4 exp(-7t)].

For v>=32, all atoms together give the normalized bound

    2(1+v)^3 exp(-v)/[1-16exp(-3t0)].

This follows from cosh(3x)<=exp(3x), the geometric atom-ratio bound, and (1+v/t0)^(11/4)<=(1+v)^3. Thus the omitted integral is at most

    2exp(-32)[32^3+6*32^2+15*32+16]
       /[1-16exp(-3t0)],

approximately 1e-9. Integrating the bound to infinity overestimates the finite window tail.

For the moment, integrate the CENTERED quantity x tanh(3x)-log A against this density and reconstruct

    mu=log A+I_centered/I.

On the actual window its absolute centered value is at most log A+log(Ap), so that constant times the density-tail bound encloses the missing centered integral. Centering prevents a large constant log A from magnifying interval dependency.

No sampled quadrature or asymptotic PNT constant enters these window enclosures. The scale exp(-t0) is retained by Arb's arbitrary exponent representation.

## 2. Explicit rational calibration of the original four sectors

The window starts and multiplicative lengths are (2,2), (4,3), (12,5), (60,7). The following exact rational decimal normalizers are certified:

    Xhat_A1=5.591534e-4,
    Xhat_A2=9.763347e-19,
    Xhat_B1=9.197196e-191,
    Xhat_B2=3.327794e-4902.

Every ratio r_F=X_F/Xhat_F obeys |r_F-1|<0.005. Rational moment representatives

    0.720647, 1.395946, 2.486015, 4.094389

all have certified errors below 0.001. Floating point only proposes these rationals; Arb independently verifies every error bound.

Fix the rational observer coefficient Lhat=0.13668993. The actual window residual still uses the unchanged all-prime L(7/2), enclosed near 0.13668993 with radius below 5e-9 by an Euler-line Mangoldt sum and its analytic tail. Finite prime cutoffs never refit that residual.

The test norm at gamma=1 is enclosed near 2.70939020392. Denote its bound by C_test. Keep all four ordered sector labels and the physical factor w_seam^2.

## 3. Common error and mismatch enter differently

Let a be the correlation of the already certified shared residual template with exp(-3u): a is enclosed near 0.16665416774446. A normalized one-feature observation is allowed to have the form

    z_F=sqrt(2) r_F
          [C+delta C_F+(mu_F+delta mu_F-L)(a+delta a_F)]
          +zeta_F.

Here C is COMMON to all four windows. The independent deviations have TOTAL budgets

    |C|<=0.05,
    |delta C_F|<=0.0001,
    |delta mu_F|<=0.001,
    |delta a_F|<=0.00002,
    |zeta_F|<=0.0001.

For example, the difference between the exact residual correlation 1/6 and a is already charged against the delta a_F budget; it is not free additional error. Moment errors represent numerical residual data, not a change to the exact window-residual convention.

With d_A defined by

    d_A=sqrt(2)a[r_A2(mu_A2-L)-r_A1(mu_A1-L)],

and similarly d_B, the pair errors satisfy

    e_A <=sqrt(2)|r_A2-r_A1|*0.05
       +sum_(F=A1,A2) {sqrt(2)|r_F|
          [0.0001+|mu_F-L|*0.00002
                   +0.001|a|+0.001*0.00002]+0.0001}.

The first term is the important cancellation: common error is multiplied by a CALIBRATION DIFFERENCE, not by the sum of two calibration magnitudes. Independent terms do not cancel. The moment/correlation cross term remains included.

For the four-sector product, error per w_seam^2 is bounded by

    |d_A|e_B+|d_B|e_A+e_A e_B.

Arb verifies both reference gaps are positive. An optional additional independent two-feature error of 0.00001 after normalization in EACH sector adds 0.00004. With all these errors present, the remaining real margin is still greater than 0.05.

The sufficient unscaled labelled-response tolerances are

    epsilon_F <=0.0001 Xhat_F/C_test,
    epsilon_ij<=0.00001 Xhat_Ai Xhat_Bj/C_test^2.

The checker verifies the common absolute choices 10^(-4906) and 10^(-4926), respectively. These norms are the existing one-feature and ordered projective two-feature response norms, not source norms.

## 4. Both exact finite-prime data and the finite field fit the common budget

Take p<=100000, including every power. Let L_P be the actual finite-place Euler eigenvalue. With the rational observer the exact finite response has common even scalar

    C_actual=(L_P-Lhat)/3,

enclosed near -7.045e-10.

For the finite escape field with R=8, S=16 and the shared cell template g, direct integration against exp(-3u) gives

    C_field=ell_-(g) exp(-(y+1/2)(R+S-log P))/(y+1/2)
       +P^(1/2-y)a/(y-1/2)-2Lhat a.

The hypotheses R<log P<S and log P<R+S hold. This expression is enclosed near -0.04555989305. Both common scalars therefore satisfy the 0.05 budget, despite differing much more than the permitted INDEPENDENT mismatch.

This is an observer-adapted calculation, not a claim that the coarse global field norm implies tiny independent scalar errors. A direct actual finite-prime scalar cross-check also retains a margin greater than 0.05.

## 5. The additional private sector gives a far stronger absolute-noise certificate

Voevodsky's `alternative-balanced-sectors-reduce-cubic-response-amplification-to-sharp-gaussian-order.md` proves that two existing balanced rows separately detect the original positive product v_0 and the crossed product v_x, with zero on the other 268 source basis products. At background A=2 they use retained windows

    row_0: 2->4 and 12->60,
    row_x: 2->4 and 20->60,

with the same forgotten seam 420->4620. We use that exact source enumeration; it is not inferred from numerical amplitudes.

Let kappa test only the weak residual coordinate by

    kappa(w)=sqrt(8) integral_0^infinity exp(-5u)w_res(u)du.

Its norm on the prescribed response space is one. Put h^2=1/8. The two row values are

    E_0=2h^2 X_A1 X_B1 (mu_A1-L)(mu_B1-L),
    E_x=2h^2 X_A1 X_D (mu_A1-L)(mu_D-L),

where D is the actual window 20->60. Its amplitude is enclosed near 7.99e-539 by the same scaled integration.

Write the original source-functional values per w_seam^2 as

    S_0=(mu_A2-mu_A1)(mu_B2-mu_B1)/18,
    S_x=-(mu_A1-L)(mu_B2-L)/18.

The exact coefficients would be S_0/E_0 and S_x/E_x. Instead fix the rational coefficients

    khat_0=3.421149e192,
    khat_x=-6.882147e540.

The observer is w_seam^2 times their two private-row kappa-tensor evaluations. Arb verifies

    |khat_0 E_0-S_0|<0.002,
    |khat_x E_x-S_x|<0.002.

Thus the rational observer is not silently declared identical to the exact whole-corner functional. For a general source expansion its calibration error is at most

    0.002 w_seam^2 (|coefficient of v_0|+|coefficient of v_x|).

The other basis values remain exactly zero by the private-row support theorem. This is an explicit finite basis-coefficient statement, not a new source-norm identification.

## 6. Independent full-output noise and shared-template error on the private rows

The two-sector sum norm gives the rational observer norm per w_seam^2 exactly

    max(|khat_0|,|khat_x|)=6.882147e540.

Thus total independent full-output noise 10^(-544) causes scalar error at most 0.0006882147 w_seam^2. Noise in untested coordinates contributes nothing; projecting from the full response space is contractive.

For the finite shared residual template, the private-row signal factor is now

    rho=[8 integral_0^8 exp(-5u)g(u)du]^2,

because the unit residual test differs from the old exp(-3u) test. Arb encloses rho near 0.99975005462, strictly between 0.9997 and 1. Calibration-plus-template errors on each of v_0,v_x remain below 0.002.

On the original positive witness, row_x is exactly zero before noise. Both

    khat_0 E_0 - max(|khat|)10^(-544),
    khat_0 E_0 rho - max(|khat|)10^(-544)

are certified greater than 0.05. The bound remains greater than 0.05 after subtracting the corresponding enclosed calibration discrepancy from the original source-functional value. This covers either actual finite-prime residual outputs or the specified coherent finite residual template, with the independent noise budget applied around the chosen reference.

There is no omitted prime error in this private-row scalar: the test reads only the fixed window-residual coordinate, which is unchanged with P. The full output still retains all arithmetic labels. This is not a fitted cutoff-dependent residual.

The improvement from the original sector tolerances depends on access to the additional admitted row_x. It is consistent with the distinct Gaussian orders in the supplied observer-optimization theorem and does not give an improved four-sector norm.

## 7. Scope

These are certificates for the fixed original cubic witness, with explicit calibration and measurement conventions. The first is robust under stated common/mismatched factor errors and optional independent sector noise. The second uses a different, already proved source-equivalent observer on a larger measured carrier, and explicitly budgets its rational calibration error.

Voevodsky's concurrent `arb-calibrates-the-improved-cubic-observer-on-the-original-six-event-witness.md` independently calibrates the private observer at gamma=2. The present gamma=1 response norm and its noise tolerance are different; their numerical tolerances must not be compared as if they were the same data norm.

No calibration is reused for arbitrarily translated backgrounds, no noisy response is assigned a derived class, and no arbitrary source perturbation is inferred from a response norm. Actual source identities and the nonzero adjacent attachment remain supplied by their owning proofs.

## Reproduction

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_robust_cubic_template_measurement.py
    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_private_sector_cubic_noise.py

The second command freshly recomputes the first certificate, the shared template, and its extra window. Artifacts:

- `research/grothendieck/results/robust-cubic-template-measurement.json`;
- `research/grothendieck/results/private-sector-cubic-noise.json`.

The JSON records full Arb balls, exact rational calibration specifications and checked strict inequalities. Coarse printed balls are not used as midpoint source data.
