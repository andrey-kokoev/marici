# Arb calibrates the improved cubic observer on the original six-event witness

## Certified result

At the actual background A=2, spectral point 3i and receiver weight gamma=2, the improved private-sector observer has a rigorous finite calibration.

With TOTAL independent noise at most 10^(-550) in the two selected unscaled projective-response sectors, the measured positive witness has a certified margin

    >0.04 w_seam^2,

including rational-coefficient calibration error. The same lower bound remains after allowing for the calibration discrepancy from the ORIGINAL source functional on this witness.

On the SAME full labelled response norm, both the ideal same-functional observer and its recorded rational calibration improve on the original four-sector test norm by a factor greater than 10^4000. This comparison is an Arb inequality at A=2, not an inference from asymptotic exponents.

Prime cutoff 10000 may be used, retaining all powers. For THIS test its cutoff error is exactly zero because it reads only the unchanged residual response coordinates. This does not say that the full Tate response is cutoff-independent.

Inputs:
- `alternative-balanced-sectors-reduce-cubic-response-amplification-to-sharp-gaussian-order.md`
- `two-residual-gaps-detect-the-adjacent-cubic-attachment.md`

## 1. Fix the actual windows and private rows

Use the completed theta convention

    Phi(x)=exp(x/2) sum_(n>=1) (4q_n^2-6q_n)exp(-q_n),
    q_n=pi n^2 exp(2x).

The old window endpoints in the arithmetic coordinate exp(x) are

    A1: [2,4], A2: [4,12], B1: [12,60], B2: [60,420].

The private crossed window is [20,60]. All are existing event windows of the same six-prime source packet. The private rows use (A1,B1) and (A1,CROSS), with the same forgotten third seam.

Write X_F=integral cosh(3x)Phi(x)dx and mu_F=(integral x sinh(3x)Phi(x)dx)/X_F. The old functional values on its only two visible cubic basis products are

    S0/w_seam^2=(mu_A2-mu_A1)(mu_B2-mu_B1)/18,
    Sx/w_seam^2=-(mu_A1-L)(mu_B2-L)/18,
    L=L(7/2).

The previous exact checker verifies that the two private rows isolate these two basis products among all 270 actual cubic products.

## 2. Boundary-scaled interval integration

A uniform mesh in x is poorly conditioned for the late windows. Instead, for a window starting at arithmetic a put

    q0=pi a^2, v=pi exp(2x)-q0,
    x=(1/2)log((q0+v)/pi).

Integrate the SCALED amplitudes exp(q0)X and exp(q0)J. The density Phi(x)dx after this scaling has first two atom terms

    exp(x/2)[(2q-3)exp(-v)+(32q-12)exp(-3q0-4v)],
    q=q0+v.

The n>=3 tail is bounded by

    exp(x/2) 2q*81 exp(-8q0-9v)
        /[1-(4/3)^4 exp(-7q)].

The checker evaluates the full intervals of 8192 cells up to min(64,v_max), not just cell centers. Thus there is no sampled quadrature assumption.

If the window continues past v=64, its scaled X-integrand is bounded by C(q0+v)^3 exp(-v), and its scaled J-integrand by C(q0+v)^4 exp(-v), where

    C=2pi^(-7/4)[1+16exp(-3q0)/(1-(3/2)^4exp(-5q0))].

These follow from cosh(3x)<=exp(3x), x<=q, and q^(11/4)<=q^3. Their tails have elementary exponential-polynomial integrals, evaluated by Arb. Extending the majorant to infinity bounds the finite omitted window tail as well.

Finally multiply by exp(-q0), retaining the enclosure. Small amplitudes are never replaced by underflowed floating-point numbers.

## 3. Certified source and calibration enclosures

Representative printed Arb balls are

    X_A1 = [0.00056 +/- 2.41e-6],
    X_A2 = [9.8e-19 +/- 7.69e-21],
    X_B1 = [9.2e-191 +/- 3.90e-193],
    X_B2 = [3.3e-4902 +/- 4.09e-4904],
    X_CROSS = [8.0e-539 +/- 3.84e-541].

The actual computations use their enclosing balls at 192-bit precision. The logarithmic derivative is enclosed by the same independent finite Mangoldt sum, analytic prime-tail bound and Arb digamma calculation used in the earlier certificate:

    L(7/2)=[0.13668993 +/- 5.00e-9].

Both source gaps and all private-row residual factors are bounded away from zero. The two source values satisfy

    S0/w_seam^2=[0.06 +/- 3.73e-3],
    Sx/w_seam^2=[-0.13 +/- 3.55e-3].

## 4. Ideal coefficients, rational coefficients and their distinction

Use the norm-one residual response test

    kappa(w)=sqrt(10) integral_0^infinity exp(-7u)w_res(u)du.

For e=exp(-3u), kappa(e)=1/sqrt(10), so h^2=1/10. The private-row evaluations are

    E0=2h^2 X_A1 X_B1 (mu_A1-L)(mu_B1-L),
    Ex=2h^2 X_A1 X_CROSS (mu_A1-L)(mu_CROSS-L).

The IDEAL coefficients alpha0=S0/E0 and alphax=Sx/Ex give exactly the old functional on all 270 source basis products, as proved previously.

The checker records exact rational midpoint proposals for alpha0/w_seam^2 and alphax/w_seam^2, then evaluates them with Arb. They are not silently treated as exact ideal coefficients. The resulting errors on v0 and vx are enclosed, per seam-weight squared, by

    |alpha0_rat E0-S0|/w_seam^2 <0.00483,
    |alphax_rat Ex-Sx|/w_seam^2 <0.00489.

Both errors are checked to be below ten percent of the corresponding nonzero basis value. On the other 268 basis products both tests remain zero. For arbitrary linear combinations, calibration error must be combined with their coefficient budget; a uniform relative error on cancellation-prone combinations is NOT inferred.

On the original positive witness the crossed private row has coefficient zero. The calibrated signal is therefore alpha0_rat E0 alone. The script bounds this signal, the noise error and the discrepancy from the original S0 separately.

## 5. Finite norm comparison in one data topology

The old one-slot test has exact response norm 1/sqrt(2) here. Indeed its endpoint norm and its 2|L| residual-copy coefficient are smaller, as verified by interval inequalities. The old four-sector direct-sum test consequently has norm

    ||Lambda_old||/w_seam^2=1/(2X_A2 X_B2)
       =[1.5e+4919 +/- 5.14e+4917].

The new calibrated two-private-row test has norm equal to the larger absolute rational coefficient, because kappa tensor kappa has norm one and the rows are separate l1 sectors:

    ||Lambda_new,rat||/w_seam^2
       approximately 8.6094811475984e540.

The ideal coefficients have a separately enclosed norm of the same order. Arb checks BOTH ratios, old/new-rational and old/new-ideal, to exceed 10^4000. The latter is the finite comparison of two EXACT representatives of the SAME source functional.

Both tests are regarded on the full labelled balanced response space; the old test is extended by zero outside its four sectors. The improvement requires access to the existing CROSS private row. It is not available from a data protocol measuring only the original four sectors.

## 6. Independent noise and finite primes

Assume the sum of the two selected sector projective-response error norms is at most 10^(-550). The calibrated observer's scalar error, divided by w_seam^2, is at most

    8.6094811475985e(-10).

After this error the calibrated signal has positive margin >0.04w_seam^2. Subtracting its enclosed calibration discrepancy from the original S0 still leaves margin >0.04w_seam^2.

Unlike the original test, kappa uses only the residual coordinate. That coordinate is identical in O_P and O_infinity: it retains the fixed all-prime window residual. Thus the selected scalar cutoff error is EXACTLY zero for every finite prime set, including all primes <=10000 with all their powers. No residual is refitted to the cutoff.

Arithmetic fields, endpoints and the other response labels remain present. They are not discarded or redefined; this particular continuous test assigns them zero. If those ignored coordinates have larger numerical errors, they need not be charged to this scalar measurement. A full projective-response error bound as above is sufficient, not necessary.

All numerical evaluation error in the two tested residual tensors must still be included in the stated noise budget. The result specifies a certificate, not an experimental ability to achieve that extremely small absolute tolerance.

## Reproduction and boundary

    uv run --with python-flint python research/voevodsky/checkers/certify_private_sector_cubic_observer.py

Artifact: `results/certified-private-sector-cubic-observer.json`, including the exact rational observer coefficients.

All assertions pass. This calibrates the actual finite-background advantage without using asymptotic growth as a numerical remainder estimate. It does not establish a best finite-A norm, source reconstruction, or ordinary L2 response realization. The nonzero cubic attachment class remains the previously proved source-equivariant class.
