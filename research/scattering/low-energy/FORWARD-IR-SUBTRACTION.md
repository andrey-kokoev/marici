# Whole-window forward IR subtraction and matching transport

[Contract](contracts/forward-ir-subtraction.v1.json) · [checker](check_forward_ir_subtraction.py) · [receipt](results/forward-ir-subtraction.v1.json)

## 1. Subtract an amplitude, not a signed density power

The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) found that positive right-cut moments do not imply positive crossed matrices. The [moment audit](FORWARD-PHOTON-MOMENTS.md) also found indefinite moments after subtracting a leading IR density power. Here remove the **entire known cut in a finite window at the amplitude level**. This is a conditional pure-g2^4 forward construction, not a completed physical amplitude or native preparation.

Use the same normalization F(s)=Im B(s,forward), T=(b/2)*A+b^2*B+..., and the same Gamma partial-transpose/helicity-flip crossing map. Retain r2=c0, r3=c1 free and r_(n+4)=n!*(n+1)!/[pi*(2n+3)!] only in the conditional spectral comparison, not as source-selected UV matching. Choose an artificial window 0<tau<1 within the certified response domain. Define the twice-subtracted paired Cauchy representative

    D_tau(z)=(z^2/pi)*integral_0^tau
                  [F(x)/(x-z)+Gamma(F(x))/(x+z)]/x^2 dx.

F starts at degree at least four, so this integral is IR convergent off the cuts. It obeys D_tau(-z)=Gamma(D_tau(z)) and Hermitian analyticity. On the upper rim its discontinuity coefficient is

    Im D_tau(s)=F(s),                 0<s<tau,
    Im D_tau(-s)=-Gamma(F(s)),        0<s<tau,
    Im D_tau(z)=0,                   real |z|>tau.

The I_tau(-z) Cauchy factor is on its **lower** rim when z is on the upper rim. Missing that sign would add rather than remove the left cut. Endpoints +/-tau are artificial, not physical thresholds; the representative does not assert that the true photon cut ends there. This forward prescription differs from the earlier full-tensor symmetric-flow prescription by a forward analytic matching shift, not by its retained cut.

## 2. Explicit analytic difference from the logarithmic kernel

Write F(z)=sum_(q>=4) F_q*z^q. In this frame the generated forward logarithm is

    B_log,nu(z)=-(1/pi)*sum_q z^q
          [F_q*log(-z/nu)+(-1)^q*Gamma(F_q)*log(z/nu)].

Let I_tau(z)=log(tau-z)-log(-z). Polynomial division gives

    pi*D_tau=sum_q [F_q*z^q*I_tau(z)
                    +Gamma(F_q)*(-z)^q*I_tau(-z)] + P_tau(z),
    P_tau(z)=sum_(q>=4) sum_(n=2..q-1)
             [F_q+(-1)^n*Gamma(F_q)]*tau^(q-n)*z^n/(q-n).

Thus E_tau,nu=D_tau-B_log,nu is explicit and analytic near zero:

    pi*E_tau,nu=P_tau
       +sum_q z^q*[F_q*log((tau-z)/nu)
                    +(-1)^q*Gamma(F_q)*log((tau+z)/nu)].

Its coefficient at **every** degree n>=2, including the first logarithmic degree, is finite:

    pi*E_n(tau,nu)=sum_(q!=n) [F_q+(-1)^n*Gamma(F_q)]*tau^(q-n)/(q-n)
                    +[F_n+(-1)^n*Gamma(F_n)]*log(tau/nu).

The q<n terms are negative inverse-window powers from expanding the analytic logarithms; they are not divergent bare cut moments. For n below the first cut degree this reduces to the usual finite IR moment shift. At and above that degree, computing an unsubtracted moment from zero instead would be incorrect.

If a candidate full forward germ is B=B_log,nu+H_nu with an independently specified IR-regular matching part H, define B_hat_tau=B-D_tau=H_nu-E_tau,nu. It is analytic inside the smaller of the matching domain and |z|<tau. The generated difference E is constructed here; **regularity and values of an arbitrary physical H are not derived**. Equality of discontinuities alone would not exclude an additional pole, essential singularity or unretained IR cut. The conditional improved amplitude requires those inventory/regularity assumptions explicitly.

## 3. Normal convergence and a remainder certificate

For the declared real response family, with A=16+16*|c0|+64*|c1|, the parent's coefficient majorant gives

    ||F_q||, ||Gamma(F_q)|| <= (9/4)*A^2*(q-3).

This uses the fixed Bell/mixed forward eigenbasis and the N_kl bounds for each ordered pair; it is not an assertion that Gamma is norm-contracting. Both coefficient series converge normally on every |z|<1. On |z|<=a<tau, write r=a/tau. Bounding the two analytic logarithms and the division polynomial gives an input-degree tail after q<=Q:

    ||delta E|| <=(2/pi)*[U_Q(a)*(|log(tau/nu)|+r/(1-r))
                           +r^2*U_Q(tau)/(1-r)].

Here U_Q is the bilinear audit's majorant. This proves analyticity of the generated E on |z|<tau and justifies coefficient extraction. For any fixed degree n, Cauchy's estimate also bounds its input-degree coefficient tail by the displayed operator bound divided by a^n. It says nothing about convergence of an arbitrary independent matching series.

For the comparison c0=c1=0, tau=nu=1/2, a=1/4, the rational pi>3 certificate is twice the earlier window-tail comparison bound: <10^(-8) at Q=40 and <10^(-10) at Q=48. This is an operator-norm truncation bound on E, **not** an uncertainty bound on physical matching. General normal-convergence and contour arguments are documented mathematics, not machine-formalized proofs.

## 4. All-degree window transport and reference compatibility

For 0<tau1<tau2<1 the difference D_tau2-D_tau1 integrates only the shell [tau1,tau2], and is analytic for |z|<tau1. If C_hat_n(tau) are the improved analytic coefficients, then for every n>=2,

    C_hat_n(tau2)-C_hat_n(tau1)=-W_n(tau2,tau1),
    W_n=(1/pi)*integral_tau1^tau2
                   [F(x)+(-1)^n*Gamma(F(x))]*x^(-n-1) dx.

There is **no** n<2*k0 restriction for a shell separated from zero. In a finite polynomial control, each q contributes tau2^(q-n)-tau1^(q-n) divided by q-n, or log(tau2/tau1) at q=n. The checker represents these logarithms formally, rather than rounding them to test cocycle equality.

    W_n(tau3,tau1)=W_n(tau3,tau2)+W_n(tau2,tau1),
    d C_hat_n/d log(tau)=-[F(tau)+(-1)^n*Gamma(F(tau))]/(pi*tau^n).

Reference changes in E_n are -[F_n+(-1)^n*Gamma(F_n)]*delta log(nu)/pi. The same reference running in H cancels them in C_hat. Shell transport is nu independent and commutes with these reference changes while the leading r_k are held fixed. Artificial window flow mixes higher input degrees into lower analytic powers; it is not identical to physical scale running or a source-selected RG trajectory. No running of the independent leading couplings is supplied.

Unknown cut-free matching polynomials shift the initial C_hat values but not these transport differences. The construction fixes a transport law, not initial physical matching data.

## 5. Positive shells and preparation-dependent ordering

The right-shell moment integral F(x)/x^(n+1) is positive for any n on a window away from zero. For even n, W_n has nonnegative expectation on the preparation cones of the crossing audit. Consequently the improved coefficient decreases as tau increases in those preparations. It is **not** a Loewner-monotone matrix law: Gamma need not preserve positivity, and odd sums have no general sign.

For R=s^2, n=2, tau1=1/4 and tau2=1/2, the unnormalized shell S_n=pi*W_n has expectations

    Bell_plus: -37/5120,
    product ++: 63/5120.

At n=4 its transport is a finite log(2) matrix even though the original zero-based moment diverges.

The checker also certifies the infinite spectral c0=c1=0 control at **n=8**, its first divergent bare moment index. With K=16 it forms the whole response square, integrates the shell without an IR density subtraction and bounds the omitted spectral coefficients by the parent's operator error. All three right-shell eigenvalues have positive lower endpoints. The paired Bell-plus shell has a negative upper endpoint, while the product ++ shell has a positive lower endpoint. Logarithms have outward rational enclosures. Values are normalized as pi^2 times the unnormalized shell; coefficient transport divides by one additional pi.

For the right-shell error use epsilon from the parent's full-minus-truncated moment bound over [0,tau2], which bounds the smaller shell error. This use is valid at n=8 because the *difference* is IR integrable even though the individual zero-based moments are not. For the paired Bell-plus expectation the dual matrix rho+Gamma(rho) has trace norm three, giving error 3*epsilon; for product ++ it is positive with trace norm two, giving 2*epsilon. No assumption that Gamma is positive or contractive is inserted.

## 6. Conditional IR-improved dispersion, not a physical bound

If the **whole** retained IR cut of a same-scope amplitude is subtracted, its remaining right cut above tau is unchanged. Unlike removing a signed leading-density polynomial, this does not alter the positive UV density. Assuming an exhaustive IR inventory and regular remainder, its improved coefficients exist at all degrees.

The paired finite-window D_tau grows at most O(z) at large |z|. Thus for n>=2 it does not spoil a previously assumed vanishing large contour at degree n. If pole/forward-limit terms are accounted for, the large contour vanishes, the remaining cut is positive at the scope of the coefficient, and a valid N-subtracted law is supplied, then for n>=max(2,N)

    C_hat_n(tau)=(1/pi)*integral_tau^infinity
                  [F(x)+(-1)^n*Gamma(F(x))]*x^(-n-1) dx.

Even n and globally valid preparation cones give conditional nonnegative expectations. Moving to a larger certified window gives a calculable shell lower-bound shift. Neither a pole/arc term nor an independent subtraction coefficient below N may be silently dropped. These conditional statements are not admitted physical hypotheses: in particular a subthreshold pure-g2^4 positive cut does not establish positivity of every UV perturbative coefficient. The audit does not select finite matching, a UV completion, a physical preparation or a rate.

This construction is forward only. A Ward/Bose off-forward lift of this particular paired prescription has not yet been constructed, nor is its forward-to-off-forward uniqueness implied. C1-C12, exhausted C12 effort, the high-energy pause, independent dimensionful couplings and historical owner/hash warnings remain unchanged.

**Next:** construct a Ward/Bose off-forward lift of this subtraction, compare its analytic shift with the symmetric-flow representative, and expose the remaining forward-invisible matching ambiguity.

```sh
python -S research/scattering/low-energy/check_forward_ir_subtraction.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_forward_ir_subtraction.py
```
