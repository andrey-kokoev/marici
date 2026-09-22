# Native actual-letter source budgets preserve the calibrated attachment certificate

## End-to-end result

The calibrated finite-prime witness survives explicitly bounded perturbations in either its inherited actual-letter source norm or its native two-factor presentation norm. Use graph control s=1, native path radius R=1, and inherited path radius R=5.

Keep the original physical constants lambda and w_seam. Either of the following admissible perturbation budgets suffices:

    inherited source error <= 10^(-23) lambda sqrt(w_seam),
    native tuple error     <= 10^(-22) lambda^2 sqrt(w_seam).

Allow additionally at most 2*10^(-23) response measurement error in each selected feature sector. Then the total sector error is below the previously certified 10^(-22). At z=3i and prime cutoff 10000, the SAME rationally calibrated observer still gives

    Re(observation)>0.12 w_seam>0.

This result is restricted to the actual four-event, one-retained-feature homogeneous packet and its declared source ideal/presentations. It does not turn arbitrary response noise into an ideal perturbation or assert unchanged-radius equivalence.

Inputs:
- `../nima/theta-tail-dominance-controls-actual-letter-factorization-lifts.md`
- `../nima/an-explicit-residual-observer-detects-the-nonzero-attachment-class.md`
- `arb-calibrates-a-finite-prime-noise-certificate-for-the-attachment-witness.md`

## 1. Keep the source, homogeneous sector and physical weights fixed

Use the supplied retained diamond on primes 2,3 followed by the forgotten diamond on 5,7. Its endpoints are 2 and 420. The product v=ac has event length n=4, retained degree one, and lies in I^2; I^3 vanishes in this finite packet.

Let delta v belong to the SAME homogeneous I^2 sector. Alternatively perturb its native I tensor_D I presentation by an admitted one-feature, total-length-four tuple. Its multiplication is still in I^2. Perturbations outside these source conditions are not covered.

For a retained event e the actual weight is

    gamma_e=sqrt(w_seam)||f_e||_beta,
    Gamma(w)=product of retained gamma_e.

Use beta=4. No raw arithmetic-response kernel replaces I. The physical memory/seam parameters, including the prescribed lambda, are unchanged.

## 2. Explicit lift constant and radii

The theta-tail theorem applies because beta=4<=8pi-7. It supplies

    C_tail=2/sqrt(3),  kappa=4/sqrt(3),
    D=(kappa+1)/(kappa-1).

For the actual terminal-anchored lift H in the four-event sector,

    ||H(z)||_(Gamma,tuple)
      <=D(kappa^4-1)||z||_Gamma <70||z||_Gamma.

Multiplication returns z for z in I^2. This is the SOURCE lift on expanded marked-path tuples, not a tensor norm on independently completed ideals.

For reference, the all-radius comparison uses inherited radius 2kappa; choosing the integer radius 5 is sufficient because 2kappa<5. Thus the chosen radii are compatible with the existing completion theorem rather than an assertion of unchanged-radius equivalence.

On this homogeneous corner the exact scalar multipliers in the supplied native norms are

    nu_(1,1,5,Gamma)(z)=150000 lambda ||z||_Gamma,
    nu_(2,1,1,Gamma)(presentation)=4800 lambda^2 ||presentation||_(Gamma,tuple).

The second formula is for an expanded presentation; taking quotient infima gives the native element norm. The same lift bounds those infima.

## 3. A uniform per-letter response bound at the calibrated point

For the forcing norm ||f||_beta=||exp(beta x)(1+x)f||_2 and z=3i, beta=4, Cauchy--Schwarz gives

    |X_f(3i)|<=||f||_beta/sqrt(2),
    |iX_f'(3i)|<=||f||_beta/sqrt(2).

The factor (1+x) controls the moment trace. With receiver gamma=2 and the previously certified |L(7/2)|<1, this yields

    ||Psi(f)(3i)||_(D_2 direct_sum H_2)
      <=[sqrt(5)+sqrt(2)]||f||_beta <4||f||_beta.

We also need a bound for the actual five-label response, uniformly at finite prime cutoffs and at the limit. The supplied piecewise gamma regulator estimates, together with |f(0)|<=||f||_D2, give a graph bound below 20. An explicit upper expression checked by Arb is

    log(pi)+1+[9+4exp(-1/2)+exp(-2)]/[1-exp(-2)] <20.

For the prime response,

    sum_(n>=2) Lambda(n)n^(-5/2)
      <= log(2)2^(-5/2)
         +2^(-3/2)[(2/3)log(2)+4/9] <1.

Thus C_A=22 bounds the full Tate response on the graph domain. The supplied five-label bound is at most

    2C_A+sqrt(1/5+1/3)+1 <46.

Consequently

    ||O_P Psi(f)(3i)||_response <=184||f||_beta

uniformly in P, including the all-prime response. This is a forward bound and uses no analytical inverse.

## 4. Two-factor differentiation and the selected normalization

Apply D tensor D to an expanded marked-path tuple of total length four. Each derivative chooses an event position; there are at most 4^2=16 resulting terms. This loose bound avoids any dependence on a special cancellation of path coefficients.

Project to the two balanced sectors of the fixed observer: the retained feature lies in its feature seam, the selected second seam is forgotten, and all spectators carry unit vacuum values. Any term with its retained feature elsewhere is discarded by this projection.

On these selected sectors, forward balancing is concatenation of the forgotten interface histories. Each input term gives at most one normalized term; identifying several terms is bounded by the coefficient l1 triangle inequality. Its norm is at most one in this selected presentation. No reverse-cut adjoint, sum over newly chosen cuts, or arbitrary chamber refinement is included in this estimate.

The selected response is measured in the UNscaled feature norm used in the calibrated certificate. Since Gamma carries sqrt(w_seam) for its unique retained event, the response bound for the sum of the two selected sector errors is

    ||selected O_P D2(presentation)||
      <= (16*184/sqrt(w_seam)) ||presentation||_(Gamma,tuple)
      =2944 ||presentation||_(Gamma,tuple)/sqrt(w_seam).

No memory multiplier is missing: the selected retained feature is in the seam, and all retained-memory sectors are projected out. The later observation restores the SAME w_seam multiplier as before.

The supplied actual balancing identities ensure this selected map annihilates the source presentation kernel. The bound therefore passes to quotient infima. It is not an arbitrary claim that every analytical tensor functional descends through every balancing quotient.

## 5. Translate source errors to the certified response tolerance

For inherited error eta_inh=nu_(1,1,5,Gamma)(delta v), lift with H. Sections 2--4 give

    epsilon_source
      <=2944*70 eta_inh/[150000 lambda sqrt(w_seam)].

With eta_inh<=10^(-23)lambda sqrt(w_seam), this is at most

    1.3738666667*10^(-23).

For native tuple error eta_nat in nu_(2,1,1,Gamma), no lift is needed:

    epsilon_source<=2944 eta_nat/[4800 lambda^2 sqrt(w_seam)].

With eta_nat<=10^(-22)lambda^2 sqrt(w_seam), this is at most

    6.1333333334*10^(-23).

These bound the SUM of the selected sector errors, hence each error individually. Adding at most 2*10^(-23) independent measurement error per selected sector keeps either case below 10^(-22).

All powers of lambda and w_seam are retained explicitly. Setting them numerically to one is not part of the theorem.

## 6. Compose with the same finite-prime certificate

Compare the measured finite-place response of v+delta v with the exact finite-place response of v. The source error just bounded and the additional response noise lie within the original certificate's measurement budget.

The original certificate already includes its separate finite-prime tail error for v, the complete theta window integrals, and rational observer calibration. It therefore applies without recomputing a prior for the perturbed source and proves the same lower margin >0.12w_seam.

The observer constants remain

    Xhat_1=0.00056, Xhat_2=10^(-18), Lhat=0.13668993.

The path source ideal, source derivative, finite-place residual convention, and prime cutoff remain unchanged. The identity comparison between native and inherited source completions does not change an observation at all; the estimates quantify the additional effect of an admissible perturbation of that source element or its presentation.

Because the perturbed source remains in I^2 in this finite packet, the exact source-equivariant nullhomotopy argument still annihilates it under any purported nullhomotopy. Its nonzero detected image therefore continues to witness the same obstruction. Arbitrary noisy data alone are not assigned a chain or derived class.

## 7. Boundary and relation to infinite towers

This is an end-to-end certificate for one finite homogeneous attachment witness, not a uniform perturbation theorem for every completed source tower. The supplied `../nima/uniform-actual-letter-budgets-characterize-realizable-infinite-filtered-towers.md` requires uniform quotient budgets at every radius for infinite realization; that condition is not inferred from the present finite certificate.

Nor are source-quotient errors interchangeable with response errors in reverse. Only the forward maps and their declared factorization lift are used here. Source instability, reduced-response kernels, and ordinary L2 cutoff escape remain unaffected.

## Verification

- `uv run --with python-flint python research/voevodsky/checkers/certify_native_attachment_source_budget.py`
- Fresh actual-letter factorization and nonzero-witness checkers pass.
- The supplied actual-letter filtered-limit checker also passes.

The new Arb artifact is `results/native-attachment-source-budget.json`. It verifies all displayed scalar constants and error budgets. Actual terminal retraction, later-start substitutions and source balancing are verified by the owning finite source checkers and used with their analytic theta-tail theorem, not inferred from these scalar computations.
