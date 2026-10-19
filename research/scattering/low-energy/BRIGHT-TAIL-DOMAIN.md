# Coherent bright-tail domains and low-mass-preserving source damping

[Contract](contracts/bright-tail-domain.v1.json) · [checker](check_bright_tail_domain.py) · [receipt](results/bright-tail-domain.v1.json)

## 1. Sharp domain: project coherently first

The [packet-tail audit](PACKET-WEAK-COUPLING-TAIL.md) showed that finite norm, mean energy and energy variance do not ensure a finite Born image. Here classify the **coherent bright** mass tails for the imported kernel K, then construct two source preparations restoring controlled Born recovery. Neither is source-selected, an interaction form factor, or a local UV theory. All statements about completions refer to the declared polynomial-in-K Cayley family, not arbitrary higher-order controls that could lift its dark states.

For fixed nonzero corresponding g2,g3 and m>0, the active singular values are

    kappa2^2=|g2|^2*beta*M^6/(128*pi^2),
    kappa3^2=|g3|^2*beta*M^10*(M^2+2*m^2)/(207360*pi^4).

In the transported source basis write the singlet coefficient f_s and the triplet bright coefficient f_B=(jS*cS+jD*cD)/N, retaining their complex phases. The orthogonal dark coefficient is f_D=(-jD*cS+jS*cD)/N. Measure below is dM*dmu(u); these are full normalized coefficient functions, including any mass/boost envelope. For source-only states and integer k>=1, the exact maximal domain condition is

    f in D(K^k) iff integral [kappa2^(2k)*|f_s|^2
                             +kappa3^(2k)*||f_B||^2] < infinity.

Dark states and all remaining kernel complements require only their original L2 norm. If a coupling vanishes, omit its term. Near threshold the multipliers are bounded and vanish, so the extra condition is at large mass, not a new threshold delta prescription. Since kappa2 grows as M^3 and kappa3 as M^6, raw spin norms cannot replace this coherent projection. The old heavy S/D dark packet has raw M^-2 amplitudes but Kf=0 and belongs to every D(K^k). This does not make dark retention universal under other higher-order interactions.

### Critical power and logarithmic tails

For a nonzero asymptotic bright amplitude M^(-r)*(log M)^(-s), meaning its squared boost-integrated norm is asymptotic to a positive constant times M^(-2r)*(log M)^(-2s), set p=3 or 6. Then D(K^k) holds precisely when

    r>p*k+1/2,
    or r=p*k+1/2 and s>1/2.

Below the power boundary no finite logarithmic exponent repairs it. At the boundary, s=1/2 still diverges as log(log M). This is the integral test after t=log M, not a numerical tail fit. Ordinary L2 membership is the analogous k=0 test.

| requirement | scalar bright amplitude | triplet bright amplitude |
|---|---|---|
| Born/first strong coefficient, k=1 | r>7/2 | r>13/2 |
| second strong coefficient / finite quartic moment, k=2 | r>13/2 | r>25/2 |
| K^3 domain, k=3 | r>19/2 | r>37/2 |

Each equality case uses the same strict logarithmic condition s>1/2. These are componentwise asymptotic criteria; an actual integral condition above applies when no such tail law exists.

## 2. Controlled Born recovery, without a hard mass cutoff

For either completion, the source's strong first-order expansion exists **iff f is in D(K)**:

    (S_eta(lambda)-I)f/lambda -> i*Kf.

Given the first coefficient, the second strong Taylor coefficient exists **iff f is in D(K^2)**, and is -K^2*f/2. To prove sufficiency, for a real spectral argument x put q=x+eta*x^3. The scalar Cayley multiplier satisfies

    |S_eta(x)-1|<=2*|x|,
    |S_eta(x)-1-i*x|<=3*x^2.

For |x|<=1 use |q|<=2|x|, |q-x|<=|x|^3 and |Cayley(q)-1-i*q|<=q^2/2. For |x|>=1 use |S-1|<=2. Spectral dominated convergence then gives the coefficients. Necessity follows from the pointwise coefficients and Fatou applied to a strongly convergent subsequence. The expansion is not uniform over unrestricted mass states.

The conversion probability has a finite Born coefficient exactly when the corresponding first bright moment is finite: F_eta(y)/y->1 and 0<=F_eta(y)<=4*y give sufficiency; Fatou gives divergence of the rescaled coefficient otherwise. Finite quartic bright moments yield global, not only compact-window, error bounds:

    0<=W-P_0<=epsilon^4*H2/2,
    |P_1-W|<=11*epsilon^4*H2,
    H2=integral bright_weight*h(M)^2*|a(M)|^2*dM,
    y=epsilon^2*h(M), W=epsilon^2*integral bright_weight*h*|a|^2.

For eta=0, 0<=y-F0(y)<=y^2/2 globally. For eta=1, if y<=1 the earlier estimate is bounded by y^2*[2+y+(1+y)^4/2]<=11*y^2; if y>=1 then |F1-y|<=y<=y^2. This fourth-moment condition is sufficient for both probability error bounds. The sharp necessity claims here concern K-power domains and the strong coefficients, not every possible signed eta=1 probability remainder. A finite moment must not be promoted to an all-orders convergent series.

## 3. Two normalized source controls preserving the low-mass wavefunction

Use the preceding a0(M)=sqrt(30)*(M-2)/(M-1)^3 in m=1 units, and retain the same boost function, phases and spin preparation. For any R>=4 leave a0 **exactly unchanged for 2<M<=R**. Its tail norm is

    tau(R)=10/(R-1)^3-15/(R-1)^4+6/(R-1)^5.

Replace only M>R by either

    a_R,power(M)=sqrt(tau*27/R)*(R/M)^14,
    a_R,exp(M)=sqrt(tau*27/R)*exp[-27*(M-R)/(2*R)].

Each new tail has norm tau, so each full state has norm one without rescaling the low-mass core. They share the same boundary tail amplitude (any jump from the core at R is harmless in L2). These are modifications of incoming preparation only; the vertices, dimensionful couplings, incoming threshold measure and outgoing photon profiles remain unchanged.

The normalized tail moments are exactly

    E_power[M^k]=27*R^k/(27-k), k<27,
    E_exp[M^k]=R^k*sum_(j=0)^k binomial(k,j)*j!/27^j.

The power integral diverges at k=27 and above. At R=4, tau=17/81. The power control is in D(K^2), but not D(K^3) for a nonzero triplet bright component of a pure S preparation; the exponential control is in every K-power domain. Coherent dark controls remain in the kernel regardless of these raw tail comparisons.

### Explicit moment and error certificates

The total k-th mass moment is bounded above by (1-tau)*R^k+tau*E_tail[M^k], since the core has M<=R. The exponential moments are smaller than the power moments. Hence both preparations satisfy

    H2_scalar <= R^12*(1+4*tau/5),
    H2_triplet <= (9/4)*R^24*(1+8*tau).

The second uses h3=beta*M^10*(M^2+2)<=(3/2)*M^12 for M>2 and bright_weight<=1. Combined with the previous global inequalities these are explicit finite O(epsilon^4) probability-error controls; no supremum of y over the unbounded support is assumed. The checker stores exact rational bounds at R=4,8,16.

Both preparations approach the original heavy packet in Hilbert norm as R grows. With the chosen nonnegative mass phases, their squared input-state distance from the original is <=2*tau(R). At each fixed mass the unchanged on-shell operator is unitary, so the same norm bound holds for their full outputs. Moreover, because the conversion projector is mass-diagonal and both tails have norm tau,

    |P_damped(lambda)-P_original(lambda)|<=tau(R),

uniformly in lambda and eta. This particular bound is for total conversion strengths, not arbitrary coherent observables.

Nevertheless their Born coefficients diverge as R->infinity: the unchanged core alone contains the original growing M^2 or M^8 Born integrand up to R. Hilbert-norm closeness does not control the unbounded operator's graph norm. At each fixed R both damped controls recover the quadratic Born law; taking R->infinity first recovers the earlier nonanalytic heavy-packet strengths. Damping does not select one of these limits as a physical rate.

### Same core and tail norm do not select the Born strength

The power tail survival function is (R/M)^27, while the exponential one's is exp[-27*(M-R)/R]. The former is strictly larger for M>R: its hazard 27/M is smaller than 27/R, or equivalently log(M/R)<(M-R)/R. Therefore it has strictly larger expectation of any strictly increasing mass function with finite moments. Both scalar beta*M^6 and pure S-triplet beta*M^10*(M+1)^2 are strictly increasing. With a nonzero corresponding coupling, the power preparation has strictly larger **Born** strength than the exponential one, despite identical low-mass wavefunctions and tail norms. This does not impose a global ordering of their exact finite-coupling conversion strengths.

## 4. All moments still do not imply an analytic coupling series

For the exponential preparation every moment exists. For eta=0 the formal coefficient of epsilon^(2n) in the conversion strength is (-1)^(n-1)*n*E[bright_weight*h^n]/4^(n-1). In the active scalar or pure S-triplet tail the moments are bounded below by a positive constant times 2^(-n)*(2*p*n)!*(R/27)^(2*p*n), p=3 or 6. This follows from beta>=1/2 for M>=R, the positive tail norm, and exponential moments of (M-R). Their coefficient roots grow without bound, so the Taylor series has **zero radius** even though every finite-order coefficient is well-defined. Finite-order differentiation is justified by the finite corresponding moments of the smooth rational Cayley functions.

This is a smooth/nonanalytic coupling dependence in a postulated model, not a locality no-go. It must not be confused with analyticity in complex invariant mass, which is a separate scattering constraint.

## 5. Next executable gate and evidence limits

The [complex-mass audit](COMPLEX-MASS-ANALYTICITY.md) now finds that the eta=1 scalar analytic candidate fails subthreshold open-photon contractivity, while both identity patches differ from their upper germs. Certified imaginary-mass poles map to negative s, not a general local-QFT exclusion. The [scalar dispersive response](SCALAR-DISPERSIVE-RESPONSE.md) now matches the charged-pair cut with four full-response subtractions (two after Ward factoring), retaining free s^2 and s^3 terms and a nonzero dispersive phase. It is a right-cut control, not an exact unitary or crossing-complete amplitude. The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ. The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. A leading dispersive response is not a full unitary local QFT.

General spectral-domain, integral-test and stochastic-order arguments are documented mathematics, not machine-formalized proofs. The checker verifies forty power/log boundary cases, global multiplier witnesses, coherent dark cancellation, 72 exact tail-moment comparisons, normalization and finite-moment bounds. The old band's comparisons remain mass-restricted (above 4 the selected overlaps are 1/2 and 1/64), not one global compact-window projection. C1-C12, exhausted C12 effort, paused high-energy execution and historical owner/hash warnings remain unchanged. No source-selected preparation, interaction form factor, physical rate or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_bright_tail_domain.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_bright_tail_domain.py
```
