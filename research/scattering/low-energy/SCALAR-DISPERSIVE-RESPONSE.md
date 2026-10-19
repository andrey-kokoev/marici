# A Ward-compatible subtracted scalar response

[Contract](contracts/scalar-dispersive-response.v1.json) · [checker](check_scalar_dispersive_response.py) · [receipt](results/scalar-dispersive-response.v1.json)

## 1. Matched cut, not a complete scattering construction

The [complex-mass audit](COMPLEX-MASS-ANALYTICITY.md) separates real-axis unitarity from analytic continuation and finds a subthreshold open-photon obstruction for the eta=1 candidate. Here construct a **leading, right-hand-cut-only dispersive control** for the scalar photon elastic response. It matches the charged-pair absorption, adds the corresponding real forward data, and exposes the unfixed local subtraction terms.

Use m=1, s=M^2 and b=epsilon2^2. With S=I+i*T, the existing scalar Cayley entries have, for s>4,

    T_gamma_gamma=(i*b/2)*sigma(s)+O(b^2),
    sigma(s)=s^3*sqrt(1-4/s)>0.

Define the new leading response by T_gamma_gamma^(2)=(b/2)*R(s), requiring Im R(s+i0)=sigma(s). Superscript (2) denotes order lambda^2, not order b^2. This preserves the Born map's second-order Hermitian loss, not the special B=0 second-order forward phase used by both Cayley controls. The independent g2 and g3 dimensions remain -3 and -6; no equality of their coefficients is introduced.

**Assumptions:** use the contact density sigma(t) all the way to infinity as a comparison model, admit only the right-hand cut [4,infinity), and impose regular local Ward-compatible subtraction terms. This extrapolation is not licensed UV spectral data. A crossed-channel contribution is not zero by theorem: it is deliberately absent from this particular control and remains a separate gate. The construction is neither a full QFT loop renormalization nor an exact unitary S matrix.

## 2. Four subtractions before Ward factoring, two afterwards

For density asymptotic to a positive multiple of t^d, an n-times-subtracted integrand behaves as t^(d-n-1). Convergence needs n>d; n=d still diverges logarithmically. Thus sigma~t^3 requires **four** subtractions for R:

    R(s)=P3(s)+(s^4/pi)*integral_4^infinity sigma(t)/[t^4*(t-s)] dt.

The local two-photon pseudoscalar tensor contains two photon momenta. Two such vertices give a regular four-photon scalar response with an overall s^2 factor. For the declared local, IR-regular subtraction terms, Ward/soft scaling therefore forbids the constant and linear terms in P3, leaving

    P3(s)=c0*s^2+c1*s^3, c0,c1 real and unfixed.

Gauge invariance alone does not exclude arbitrary nonlocal IR poles; no such pole has been added here. Equivalently R=s^2*Pi and the Ward-factored response has density t*sqrt(1-4/t)~t, so **two** subtractions are necessary and sufficient:

    Pi(s)=c0+c1*s+(s^2/pi)*integral_4^infinity beta(t)/[t*(t-s)] dt,
    R(s)=c0*s^2+c1*s^3+(s^4/pi)*J(s).

These are the same construction, not contradictory subtraction counts. The coefficients are renormalization/matching data; setting them to zero defines a control, not a derived physical prescription. Additional UV growth assumptions could restrict the subtraction class, but are not supplied here.

## 3. Exact integral, threshold behavior and absorptive normalization

With u=sqrt(1-4/t),

    J(s)=integral_4^infinity beta(t)/[t*(t-s)] dt
        =integral_0^1 2*u^2/[4-s+s*u^2] du.

It is analytic off the declared right cut and real for real s<4. For 0<s<4,

    J(s)=(2/s)*[1-sqrt((4-s)/s)*atan(sqrt(s/(4-s)))],
    J(0)=1/6.

For s>4, on the upper rim and beta=sqrt(1-4/s),

    J(s+i0)=[2+beta*log((1-beta)/(1+beta))]/s+i*pi*beta/s,
    Im R(s+i0)=s^3*beta=sigma(s).

The sign follows from 1/(t-s-i0)=PV[1/(t-s)]+i*pi*delta(t-s). The cut normalization agrees with the original forward loss exactly, while its real principal-value part is generally nonzero. For the zero-subtraction control, Re R0/s^3=(2+beta*log((1-beta)/(1+beta)))/pi. It is positive at beta=1/2 and negative at beta=7/8, as certified by rational atanh-series bounds. More generally it grows as -log(s)/pi plus a constant at high energy. No fixed c0*s^2+c1*s^3 can cancel this real part on the whole positive cut. That statement is conditional on this right-cut spectral extrapolation; additional crossed input or UV changes may change it.

Below the charged cut the leading response is real and yields a real elastic phase coefficient, unlike the original identity patch. It does **not** yet repair eta=1's order-b^2 contractivity failure. In particular, the truncation S=1+i*b*R/2 has a norm error at order b^2; it must not be read as an exact probability map. An all-orders unitarization and its analytic tests remain unconstructed.

## 4. Analytic low-energy series and subtraction freedom

For |s|<4 the exact series is

    J(s)=sum_(n>=0) a_n*s^n,
    a_n=n!*(n+1)!/(2*n+3)!,
    a_0=1/6, a_1=1/60, a_2=1/420,
    a_(n+1)/a_n=(n+1)/[2*(2*n+5)] -> 1/4.

Thus the series radius in **s** is 4. This differs from the earlier zero-radius **coupling** series for an unbounded exponential source packet. The coefficients follow either from the spectral moments or by integrating u^2*(1-u^2)^n; no fitted tail quadrature is used. With only the right cut, R has

    R(s)=c0*s^2+c1*s^3+s^4/(6*pi)+...,
    R^(4)(0)=4/pi.

The positive higher coefficient does not determine c0 or c1. For example c0=+1 and -1, both with c1=0, retain the same cut and Ward scaling, but give opposite signs at s=1 because 0<R0(1)<1. This is freedom within the stated subtraction model, **not proof that both signs have a full causal UV completion**. A positivity claim about the s^2 coefficient would need stronger high-energy/crossing assumptions or matching information absent here.

For 0<=s<4, a partial sum through n=N-1 has a positive remainder bounded by a_N*s^N/(1-s/4). Exact rational boxes are recorded at s=0,1/2,1,2,3. The identity J(2)=1-pi/4 also gives a rational pi enclosure from the same positive series, allowing certified boxes for R0=s^4*J/pi without floating-point constants. These boxes are implementation certificates for the formulas, not physical evidence.

## 5. A scoped UV comparison bound

Suppose two spectral controls share c0,c1 and the density below a squared-mass cutoff L>4, while above L one damps it by 0<=d(t)<=1. For 0<=s<4,

    0<=R_original(s)-R_damped(s)
      <=s^4/[pi*(L-s)].

Indeed beta<=1 and integral_L^infinity 1/[t*(t-s)] dt <=1/(L-s). This bounds a **spectral** modification of the response, not the source-packet damping of the earlier audit. It does not cover arbitrary UV additions, sign-changing spectral changes, altered subtraction constants or altered high-energy growth. None of these envelopes is a selected physical interaction form factor.

For L=4/(1-u0^2), the tail's n-th Taylor coefficient is exactly

    [1/(2*4^n)]*sum_(j=0)^n (-1)^j*binomial(n,j)
                         *(1-u0^(2*j+3))/(2*j+3).

Its consecutive-coefficient ratio is at most 1/L. The checker certifies 36 tail moments and nine bounds using u0=1/2,3/4,7/8 and s=1,2,3, with geometric remainder bounds rather than numerical tail truncation.

## 6. Executable successor and unchanged limits

The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ. The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Do not promote a leading crossing construction to exact unitary or native local dynamics.

The analytic/dispersive and Ward-subtraction arguments are documented mathematics, not machine-formalized proofs. All old photon complements and source-preparation caveats remain; the scalar response is not a three-photon branching calculation. C1-C12, exhausted C12 effort, the high-energy pause and historical owner/hash warnings remain unchanged. No physical preparation, UV spectral density, form factor, rate, branching ratio or native source license is selected.

```sh
python -S research/scattering/low-energy/check_scalar_dispersive_response.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_scalar_dispersive_response.py
```
