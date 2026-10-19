# On-shell unitary controls: forward correction, dark states and completion freedom

[Contract](contracts/on-shell-unitary-completion.v1.json) · [checker](check_on_shell_unitary_completion.py) · [receipt](results/on-shell-unitary-completion.v1.json)

## 1. What is constructed

The [Born maps](OUTGOING-BORN-MAP.md) now extend to two **postulated on-shell unitary controls**. They agree at first and second order but have different finite conversion strengths. Source survival, inverse conversion, coherent S/D dark states and photon-profile complements are retained. These are operators on the imported asymptotic coefficient Hilbert space, **not** a constructed spacetime scattering Hamiltonian, local QFT or native encounter law.

This is more restrictive than merely changing the independent leading couplings: the two controls have the **same** leading couplings, Born amplitudes and second-order elastic term. Their difference starts in higher orders. It exhibits a freedom that first-order norms and the optical theorem do not remove.

## 2. Physical-current channel kernel and second order

For M>2m the selected incoming relative space has dimension seven: the singlet S wave s, triplet S waves S_j and normalized triplet D waves D_j. The full outgoing candidate profiles are the normalized two-photon scalar chi2 and three-photon triplet chi3j, dimension four. All other incoming angular states and all other photon profiles remain in orthogonal complements. The full carrier retains M and u; it is not restricted to the fixed boost cube after a Lorentz transformation.

In the declared amplitude convention define real mass multipliers

    r2(M)=g2*M^3*sqrt(Phi_in*Phi2/2!),
    r3(M)=g3*M^4*sqrt(2/45)*sqrt(Phi_in*Phi3/3!),
    jS=2*sqrt(2)*(M+m)/3, jD=-2*(M-2m)/3,
    N^2=jS^2+jD^2=4*(M^2+2*m^2)/3.

Here the separate dimensionful coefficients, threshold and phase volumes are exactly those of the Born calculation. The source-to-photon block A is

    A(s)=-i*r2*chi2,
    A(S_j)=-r3*jS*chi3j, A(D_j)=-r3*jD*chi3j.

Thus the Born output is i*A applied to the incoming coefficient; its scalar and vector phases match the previous full Fock amplitudes. Define K=[[0,A^dagger],[A,0]], self-adjoint on the eleven active coefficients, zero on both complements. It is an auxiliary **dimensionless on-shell kernel**, not the lab-time Hamiltonian. Its adjoint includes the inverse channels and their D-wave source component.

The source block of K^2 is A^dagger*A. In particular its vector S/D multiplicity block is

    r3^2 * [[jS^2,jS*jD],[jS*jD,jD^2]] tensor I3.

The off-diagonal entry is coherent interference; it must not be replaced by averaged S/D probabilities. With S(lambda)=I+i*lambda*K+lambda^2*D+..., unitarity requires

    D+D^dagger=-K^2,
    D=-K^2/2+i*B, B=B^dagger.

The Born data fix the Hermitian loss term, not the Hermitian phase operator B (subject to any additional symmetry/domain requirements). The following two controls both choose B=0. This is not a calculation of renormalized QFT loops or their real counterterms.

## 3. Two exact completions with the same first two orders

For eta=0 or 1 set

    H_eta(lambda)=lambda*K+eta*lambda^3*K^3,
    S_eta=(I+i*H_eta/2)*(I-i*H_eta/2)^(-1).

Every fiber is unitary because H_eta is Hermitian. Both have

    S_eta=I+i*lambda*K-lambda^2*K^2/2+O(lambda^3).

This expansion is fiberwise and uniform on compact mass windows, not an operator-norm expansion on the unrestricted mass carrier.

For T_eta=(S_eta-I)/i the exact optical theorem is T_eta-T_eta^dagger=i*T_eta^dagger*T_eta. The checker verifies both inverse-sided unitarity and this identity, rather than renormalizing only the outgoing photons.

For either scalar channel or a normalized bright triplet channel, let kappa be the magnitude of its off-diagonal K entry: |r2| or |r3|*N. Put q=lambda*kappa+eta*(lambda*kappa)^3. Bright survival and conversion have strengths

    R_eta=[(1-q^2/4)/(1+q^2/4)]^2,
    C_eta=q^2/(1+q^2/4)^2, R_eta+C_eta=1.

The kernel's fixed complex phase is retained in the conversion amplitude; only this norm formula uses kappa's magnitude. At the same reduced lambda*kappa=1, eta=0 gives C=16/25 and eta=1 gives C=1. These are mathematical control values, not observed rates, and are unrelated to the earlier controller herald probabilities. The two completions agree through the second-order forward term but their conversion strengths first differ at fourth order. Their parameter has not been source-selected.

### Full carrier, domain and covariance

Globally K grows with mass and is not bounded. The measurable direct integral of its finite Hermitian matrices is self-adjoint on the maximal domain {f: integral ||K(M)f(M,u)||^2 dM*dmu<infinity}; compact-mass sections give a dense core. H_eta is defined by spectral functional calculus, not by assuming every L2 packet belongs to the K^3 domain. Its Cayley transform is a bounded unitary on **all** coefficient packets. This cures a norm deficit within this on-shell prescription, not the local EFT's UV/domain problem.

Both S and D source triplets have the same total-J=1 transformation law in the transported CM spin basis, as does the full photon triplet. K's multiplicity matrices tensor I3 commute with the common Wigner rotation. Its mass-only coefficients and fixed total u also commute with free four-momentum. Hence these controls intertwine the imported proper Poincare actions on the full carrier. Transforming an envelope still transforms its boost and spin records. For photon masses below 2m there is no charged-pair channel and S is identity. Threshold endpoints are null sets. No native Lorentz action has been derived.

This functional-calculus argument does not produce wave operators for a spacetime Hamiltonian, locality, cluster separability, analyticity or crossing. In particular choosing the free Hamiltonian would give identity scattering, not these nontrivial on-shell operators. No regulator, form factor or Wilson coefficient has been source-selected by writing a Cayley transform.

## 4. Dark retention and complete photon profiles

For each triplet component define the orthonormal source combinations

    bright_j=(jS*S_j+jD*D_j)/N,
    dark_j=(-jD*S_j+jS*D_j)/N.

K annihilates dark_j, so **both chosen completions** act on it as identity at every coupling. This all-order dark statement is a property of these polynomial-in-K prescriptions, not a theorem for every completion or QED. For an explicit reduced countercontrol in (bright,dark,photon) order, let K couple bright to photon with unit magnitude and let L couple dark to photon with unit magnitude. Cayley(lambda*K+lambda^3*L) still has the same first two terms, but at lambda=1 the old dark state converts with strength 4/9. Such an independent higher-order operator, with appropriate mass/coupling dependence, is not prohibited by the Born data alone. It is not a new interaction derived from the Wick density.

A pure S-wave triplet has dark weight

    d(M)=jD^2/N^2=(M-2m)^2/[3*(M^2+2*m^2)].

Its exact conversion strength in these models is (1-d(M))*C_eta, not C_eta itself. The surviving charged pair can acquire a D-wave component; survival is not simply a scalar rescaling of the initial S wave. For the declared m=1, 3<M<4 packet, d grows from 1/33 to 2/27 (its derivative is 4*(M-2)*(M+1)/(3*(M^2+2)^2)>0). Thus a normalized pure S-wave triplet retains at least **1/33** charged norm in this family, irrespective of coupling. This bound is preparation- and completion-class-specific, not a physical survival prediction.

Each converted three-photon state remains in the **full** chi3 triplet, with coherent old-normal/added-normal/residual coordinates (-i*sqrt(15)/8,i/8,sqrt(3)/2). Its selected weight 1/4 and orthogonal remainder 3/4 are both retained. The checker also tests a nonzero photon vector orthogonal to this coherent profile and verifies it is unchanged, rather than deleting the complement. Above M=4 the earlier dynamical old-band comparison still has selected fractions 1/2 and 1/64 for the two-/three-photon sectors. This new on-shell operator is not asserted to be the scattering operator of that old escape Hamiltonian.

## 5. Next executable gate

The [packet weak-coupling audit](PACKET-WEAK-COUPLING-TAIL.md) now certifies compact errors and an unbounded finite-energy packet outside the Born domain. Its scalar/triplet strengths scale as epsilon2 and sqrt(epsilon3), with completion-dependent leading constants. Ordinary cutoff/weak limits commute; the specified rescaled limits do not. The [bright-tail domain audit](BRIGHT-TAIL-DOMAIN.md) now classifies the critical power/log conditions and constructs two normalized damping controls preserving the low-mass wavefunction and tail norm. They restore finite-order Born recovery but not a selected form factor or a convergent all-orders series. The [complex-mass audit](COMPLEX-MASS-ANALYTICITY.md) now finds that the eta=1 scalar analytic candidate fails subthreshold open-photon contractivity, while both identity patches differ from their upper germs. Certified imaginary-mass poles map to negative s, not a general local-QFT exclusion. The [scalar dispersive response](SCALAR-DISPERSIVE-RESPONSE.md) now matches the charged-pair cut with four full-response subtractions (two after Ward factoring), retaining free s^2 and s^3 terms and a nonzero dispersive phase. It is a right-cut control, not an exact unitary or crossing-complete amplitude. The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ. The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Source preparation remains distinct from an interaction form factor or a local UV derivation.

Independent physical preparation, native source/operation licensing and local/cluster dynamics remain open evidence gates. General direct-integral, representation and scattering arguments are documented mathematics, not machine-formalized proofs. The checker has 72 exact reduced-block unitarity/optical-theorem cases, 18 forward-term checks, 36 dark-state identities and coherent photon-complement checks. Its rational reduced coupling samples are algebraic tests, not calibrated EFT coefficients. C1-C12, exhausted C12 effort, historical owner/hash warnings and paused high-energy execution are unchanged. No physical outcome or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_on_shell_unitary_completion.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_on_shell_unitary_completion.py
```
