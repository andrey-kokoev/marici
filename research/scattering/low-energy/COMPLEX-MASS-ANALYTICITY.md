# Scalar complex-mass continuation: an open-channel obstruction, not a general QFT no-go

[Contract](contracts/complex-mass-analyticity.v1.json) · [checker](check_complex_mass_analyticity.py) · [receipt](results/complex-mass-analyticity.v1.json)

## 1. What is continued, and which assumptions are added

The [on-shell controls](ON-SHELL-UNITARY-COMPLETION.md) are real-mass unitary direct integrals, with an identity prescription in the photon sector below the charged-pair threshold. The [bright-tail domain audit](BRIGHT-TAIL-DOMAIN.md) controls source domains, not analyticity of their scattering kernels. Here audit the **scalar two-photon elastic entry** of the declared controls. This is not an assertion that their analytic germ is the source's QFT amplitude, nor a classification of every complex pole of the scalar or triplet sectors.

Set m=1 and b=epsilon2^2>0, retaining its origin in the independent dimensionful g2 and the bookkeeping coupling. Use the upper continuation

    w(M)=sqrt(M-2)*sqrt(M+2), w(M)~M at infinity,
    beta(M)=w(M)/M,
    Y(M)=b*M^6*beta(M)=b*M^5*w(M).

The roots are continued from w>0 for real M>2 through Im M>0; equivalently w is the branch of sqrt(M^2-4) on C\[-2,2] asymptotic to M. Consequently

    w(x+i0)=i*sqrt(4-x^2), 0<x<2,
    w(i*gamma)=i*sqrt(gamma^2+4), gamma>0.

The scalar kernel is continued as [[0,i*r],[-i*r,0]], with r^2=Y and its positive real branch above threshold (the sign of the original coupling does not affect this elastic entry). Continue the coefficient functions, **not pointwise complex adjoints**: a complex-mass kernel need not be Hermitian. Off-diagonal square-root normalization may have additional kinematic branching; the photon elastic entry needs only Y. In particular beta's apparent pole at zero is canceled in Y. Its branch endpoints include +/-2; channel-coordinate branching must not be confused with a physical pole.

Writing H=K*(1+eta*Y), H^2=Z*I, the elastic entry is

    E_eta(M)=(1-Z/4)/(1+Z/4), Z=Y*(1+eta*Y)^2.

This agrees with the real-mass Cayley matrix above threshold. The two-photon mode remains normalized and open for all real M>0; its massless two-body phase volume is constant. No imaginary-flux normalization or positive-norm closed charged channel is introduced below 2.

The added analytic test is conditional: interpret this expression as the upper analytic germ of that same photon elastic entry, in a connected first-quadrant domain reaching the real intervals above and below 2, with regular continuous boundary values away from endpoints. Exact boundary agreement on an open interval fixes a continuation in such a domain: their difference vanishes on that interval, Schwarz reflection of the zero boundary values and the identity theorem give uniqueness. Poles/cuts or absent boundary regularity must be stated if they prevent that domain. A first-quadrant requirement in M is not an unqualified holomorphy axiom for the entire upper M half-plane.

## 2. Below threshold: test the open photon entry, not a fictitious two-channel unitary

For 0<M<2 put v=b*M^5*sqrt(4-M^2)>0. Then Y=i*v. For eta=0,

    E_0=(1-i*v/4)/(1+i*v/4), |E_0|^2=1, E_0!=1.

It is a nontrivial elastic phase, not the original identity patch. This one-channel norm condition is necessary, not sufficient, for local/causal dynamics.

For eta=1,

    Z=-2*v^2+i*v*(1-v^2),
    |E_1|^2-1=2*v^2/|1+Z/4|^2 > 0.

The denominator never vanishes for real v>0: its imaginary part can vanish only at v=1, where its real part is 1/2. Thus the failure is not a numerical pole artifact. Any positive-norm unitary scattering matrix requires an open-channel diagonal entry to have magnitude at most one. Adding other open channels cannot repair a diagonal entry already larger than one. No unitarity requirement is imposed on the analytically continued **closed charged channel**.

An exact reduced witness is M=sqrt(2), b=1/8, giving Y=i:

    E_0=(15-8*i)/17, norm_squared=1,
    E_1=3, norm_squared=9.

This is a model control, not a calibrated coupling or physical measurement. The excess is strictly positive for every b>0 and 0<M<2, even when small: it begins at order b^2, beyond the shared second-order bookkeeping expansion.

**Narrow disposition:** the eta=1 analytic candidate fails open-photon contractivity under the declared continuation/domain interpretation. The original piecewise real-axis operator remains mathematically unitary because it separately sets E=1 below threshold; that patch is **not** the analytic continuation of either above-threshold germ. Hence neither patched prescription has already supplied a causal analytic scattering realization. This excludes that interpretation, not EF1 as a whole or all higher-order completions. Repair may change higher-order dynamics, forward dispersive data or the asserted analytic domain; silently replacing the below-threshold values is not such a derivation.

## 3. Nonremovable imaginary-mass poles, with exact interval certificates

On M=i*gamma, Y=-a with

    a=b*gamma^5*sqrt(gamma^2+4)>0.

The diagonal denominator is zero when

    eta=0: a=4,
    eta=1: a*(1-a)^2=4.

The second has exactly one positive solution a1>1. On [0,1] its maximum is 4/27<4; above 1 its derivative (a-1)*(3*a-1) is positive. Its root lies strictly between 2 and 5/2. Both controls therefore have an imaginary-mass pole for every b>0; choosing eta=1 does not remove this pole family.

For t=gamma^2, a^2=b^2*t^5*(t+4). The latter is strictly increasing for t>0, since its derivative apart from b^2 is 2*t^4*(3*t+10)>0. The checker first encloses a1 using rational bisection and then encloses t. It records six certified t boxes: two eta values at b=1,1/16,1/65536. Target and coordinate bounds are checked with exact fractions, not floating root residuals. At equal b the eta=1 pole has smaller gamma; as b decreases both poles move outward. They escape to infinity as b->0, rather than spoiling fixed compact-mass weak-coupling convergence.

At a denominator zero Z=-4, the elastic numerator is **2**, not zero. The relevant derivatives are nonzero, so the poles are simple and nonremovable in this specified germ. This pole test uses an open photon entry, not a potentially singular charged-channel coordinate.

### Squaring introduces extraneous solutions

Eliminating square roots gives an equation such as b^2*M^10*(M^2-4)=16 for eta=0. It loses the sign of Y. A positive real solution has Y=+4 and denominator 2, **not a pole**. The exact witness M=sqrt(5), b=4/(25*sqrt(5)) satisfies the squared equation but not the unsquared pole condition. Branch/sign checks are mandatory; this audit does not label every polynomial root a physical-sheet pole.

## 4. Why these poles are not a general causal-QFT exclusion

Under s=M^2, M=i*gamma maps to s=-gamma^2, on the **negative real s axis**. The first M quadrant maps to the upper s half-plane; its imaginary edge maps to a possible crossed-channel/left-hand-cut boundary. Thus a pole in the entire upper M half-plane is not automatically a pole strictly inside the upper s half-plane. It is not a positive-mass bound state and is not, without more information, a tachyonic physical-state claim.

A physical exclusion requires the actual analytic domain, crossed-channel singularities, sheet conventions and appropriate boundedness/positivity assumptions. None is supplied by the native source or by this algebraic kernel. The certified pole family falsifies entire-upper-M holomorphy of the specified germ, **not a universally assumed QFT domain**. Other complex poles and triplet-sector continuation remain unclassified. The subthreshold eta=1 contractivity failure is the separate, narrower obstruction established in section 2.

Damping the incoming packet leaves this operator germ unchanged. A specially selected matrix element can mask a singularity; that is not a repair of the scattering kernel. The earlier zero-radius **coupling** series and the present **mass-plane** statements are different issues.

## 5. Executable successor and scope

The [scalar dispersive response](SCALAR-DISPERSIVE-RESPONSE.md) now matches the charged-pair cut with four full-response subtractions (two after Ward factoring), retaining free s^2 and s^3 terms and a nonzero dispersive phase. It is a right-cut control, not an exact unitary or crossing-complete amplitude. The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ. The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom.

The branch, uniqueness and causal-scattering arguments are documented mathematics, not machine-formalized proofs. Checks cover exact real-axis matrices, subthreshold entries and a norm-nine witness, six rational pole boxes, nonremovable numerators and an extraneous squared-root witness. All photon complements, survival channels and coherent dark states of the original family remain. C1-C12, exhausted C12 effort, high-energy pause and historical owner/hash warnings remain unchanged. No physical preparation, form factor, rate, branching ratio or native source license is admitted.

```sh
python -S research/scattering/low-energy/check_complex_mass_analyticity.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_complex_mass_analyticity.py
```
