# Packet weak-coupling errors and an unbounded incoming mass tail

[Contract](contracts/packet-weak-coupling-tail.v1.json) · [checker](check_packet_weak_coupling_tail.py) · [receipt](results/packet-weak-coupling-tail.v1.json)

## 1. Scope and reduced strengths

Following the [on-shell unitary controls](ON-SHELL-UNITARY-COMPLETION.md), certify packet-level Born errors and an explicit nonuniformity. This concerns **postulated imported on-shell models and declared preparations**, not source-selected photon branching, a native encounter or a local UV completion. Ordinary weak-coupling/cutoff limits commute in the example; the noncommutation occurs after a specified weak-coupling rescaling.

Keep g2 and g3 independent, of mass dimensions -3 and -6, and lambda the dimensionless common bookkeeping parameter. In units m=1 (M means M/m), define separate dimensionless strengths

    epsilon2=|lambda*g2|*m^3/(sqrt(128)*pi),
    epsilon3=|lambda*g3|*m^6/(sqrt(207360)*pi^2).

No equality of these strengths or of the dimensionful coefficients is imposed. The squared bright-channel arguments are exactly

    y2(M)=epsilon2^2*beta(M)*M^6,
    y3(M)=epsilon3^2*beta(M)*M^10*(M^2+2),
    beta=sqrt(1-4/M^2).

The phase volumes, factorials and current normalization are in these constants; beta has not been removed. For eta=0,1 write

    q2=y*(1+eta*y)^2,
    F_eta(y)=q2/(1+q2/4)^2, 0<=F_eta<=1.

Let w2=|alpha|^2 and w3=||jS*cS+jD*cD||^2/N^2 be the coherent source bright projections at each mass. Both lie in [0,1] for a unit angular-spin vector. For a pure S-wave triplet, w3=B(M)=2*(M+1)^2/[3*(M^2+2)], whereas w2=0. It is incorrect to replace w3 by separate S/D probabilities. For a normalized mass density rho, the exact model conversion strength is P_eta,n=integral rho*w_n*F_eta(y_n)*dM; its Born term is W_n=integral rho*w_n*y_n*dM when that integral is finite. Boost normalization is still one and the full photon profiles are retained.

## 2. Compact-packet certificate

For 0<=y<=delta=1/16,

    0<=y-F_0(y)<=y^2/2,
    |F_1(y)-y|<=3*y^2,
    0<=F_1(y)-F_0(y)<=(2+delta)*y^2.

These are analytic inequalities, not conclusions from a mesh. For the first, y-F0=y^2*(1/2+y/16)/(1+y/4)^2, and half its denominator minus the numerator factor is 3*y/16+y^2/32>=0. For the second put z=y*(1+y)^2: |F0(z)-y|<=|z-y|+z^2/2, bounded by y^2*[2+delta+(1+delta)^4/2]<3*y^2. For the third, z<=delta*(1+delta)^2<4 and F0'(v)=(1-v/4)/(1+v/4)^3 is between zero and one on [0,4].

Thus whenever sup y_n<=delta on the packet support,

    0<=W-P_0<=delta*W/2,
    |P_1-W|<=3*delta*W,
    0<=P_1-P_0<=(2+delta)*delta*W.

These hold also for a current-null state with W=0; no division by W is needed. On 3<M<4 sufficient separate conditions are epsilon2^2*4^6<=delta and epsilon3^2*18*4^10<=delta. For example epsilon2<=1/256 and epsilon3<=1/32768 suffice. They are mathematical smallness conditions, not calibrated physical couplings. The same bounds sum over the two orthogonal photon-number sectors without deleting their coherent amplitudes or survival.

## 3. A normalizable incoming packet outside the Born domain

Keep the prior boost envelope, coherent S-wave angular preparation and incoming coarea half-density, but choose

    a(M)=sqrt(30)*(M-2)/(M-1)^3, M>2,
    rho(M)=|a|^2=30*(M-2)^2/(M-1)^6.

Restoring units means a(M)=m^(-1/2)*sqrt(30)*t/(1+t)^3 with t=(M-2m)/m. The beta integral gives integral rho*dM=30*B(3,3)=1. Its first two mass moments are 7/2 and 16. The retained boost cube has u0<=19/13, so the lab-energy mean and second moment are finite as well. Merely finite energy, even finite energy variance, therefore does not ensure the Born-domain condition below. This is a full normalizable free Dirac pair packet, not a sharp CM state or a physical source selection. Its Born image is not an L2 photon state: being in the incoming Fock space is not the same as being in the contact/Born operator's domain. No finite point-current norm is assumed for this tail; field matrix elements can require distributional interpretation.

For M>=4, rho>=15/(2*M^4) and beta>=1/2. Also 2/3<=B(M)<=1. Consequently the scalar Born integrand is bounded below by (15/4)*epsilon2^2*M^2 and the pure S-triplet one by (5/2)*epsilon3^2*M^8. Both integrals diverge for any nonzero corresponding strength. In contrast every exact on-shell P_eta,n is finite and <=1.

For later domination rho<=1920/M^4 for all M>2. This follows from M-1>=M/2 and M-2<=M, not a sampled tail fit.

## 4. Nonanalytic weak-coupling asymptotics

Treat each sector's independent epsilon as tending to zero. Set p=3 for a pure singlet's two-photon output and p=6 for a pure S-triplet's three-photon output. With s=epsilon^(1/p) and M=t/s,

    rho(t/s)/s^4 -> 30*t^(-4),
    y_n(t/s) -> t^(2p),
    w_n(t/s) -> b_infinity, b_infinity=1 or 2/3.

Moreover F_eta(y)<=4*min(y,1) and y_n(t/s)<=2*t^(2p). The scaled integrands are bounded by the integrable function 7680*t^(-4)*min(2*t^(2p),1). Dominated convergence therefore proves the actual limits, not merely order estimates:

    P_eta,n(epsilon)/epsilon^(3/p) -> C_eta,p,
    C_eta,p=30*b_infinity*integral_0^infinity t^(-4)*F_eta(t^(2p))*dt.

Each constant is strictly positive and finite. Hence P2 is linear in epsilon2 to leading order, while P3 is proportional to sqrt(epsilon3). At fixed nonzero g2,g3 this means |lambda| and sqrt(|lambda|), not a common quadratic Born law. This is a domain/preparation effect, not a nonanalytic physical rate prediction.

For eta=0, substituting u=t^(2p)/4 gives B(1-a,1+a)=a*pi/sin(pi*a), a=3/(2p), so

    C_0,3=5*pi, C_0,6=5*pi/3.

The eta=1 constants are certified by rational interval quadrature, not estimated floats. At the dominant mass scale M of order epsilon^(-1/p), terms that were higher order at fixed M are no longer small; completion dependence at leading order does not contradict the common fiberwise expansion. In fact both constants differ already at leading order despite the completions sharing their first two fiberwise expansion terms:

| constant | rigorous rational enclosure |
|---|---|
| C_0,3 | [15.63,15.79] |
| C_1,3 | [15.23,15.44] |
| C_0,6 | [5.15,5.32] |
| C_1,6 | [3.93,4.08] |

Thus the tail reverses the compact-window ordering: for sufficiently small epsilon the tail packet has P_1<P_0, even though F_1>=F_0 on the compact small-argument window. The dominant high-mass region is outside that window.

For certification the integrand is N(t)/D(t), with N=t^(2p-4)*(1+eta*t^(2p))^2 and D=(1+t^(2p)*(1+eta*t^(2p))^2/4)^2. Both are nonnegative increasing polynomials. On each interval [a,b], N(a)/D(b)<=N(t)/D(t)<=N(b)/D(a). Use 2048 cells up to T=4 for eta=0 or T=2 for eta=1, rounding each rational contribution outward to multiples of 10^-8. The remaining tail is bounded above by 16/[(3+d)*T^(3+d)], d=2p or 6p, before multiplying by 30*b_infinity. Final rounding to hundredths is also outward. All 8192 cell bounds use exact rational arithmetic. No physical-data quadrature is performed.

## 5. Which cutoff limits commute

The discarded mass norm is exactly

    tau(L)=integral_L^infinity rho*dM
          =10/(L-1)^3-15/(L-1)^4+6/(L-1)^5.

For L>2 let a_L=a*indicator_(2,M<L)/sqrt(1-tau(L)). This is another normalized incoming preparation. Since every conditional conversion strength lies in [0,1],

    |P_infinity(epsilon)-P_L(epsilon)|<=tau(L),

uniformly in epsilon and eta. Thus the ordinary iterated limits epsilon->0 and L->infinity **commute**, both giving zero. The on-shell operators converge strongly to identity by dominated convergence; for any nonzero corresponding strength their unrestricted operator-norm distance from identity remains 2, since the active high-mass Cayley phase approaches -1.

For the specified rescaled observable P/epsilon^(3/p), however,

    lim_(L->infinity) lim_(epsilon->0) P_L/epsilon^(3/p)=0,
    lim_(epsilon->0) lim_(L->infinity) P_L/epsilon^(3/p)=C_eta,p>0.

At each fixed finite cutoff the ordinary Born expansion is controlled and starts at epsilon^2, which vanishes after this weaker rescaling. Removing the cutoff first accesses masses of order epsilon^(-1/p) and gives the nonanalytic coefficient. Do not describe the unscaled probabilities as having noncommuting limits, or the infinite Born coefficient as an infinite exact probability.

For the unbounded packet, the old band's comparison cannot use one global compact-window fraction: above 4 the selected overlaps are still 1/2 for two photons and 1/64 for three photons. The full output and orthogonal remainder are not discarded. No comparison identifies these new on-shell operators with the old escape Hamiltonian.

## 6. Next executable gate and evidence boundary

The [bright-tail domain audit](BRIGHT-TAIL-DOMAIN.md) now gives sharp power/log conditions after coherent projection and two normalized damping controls preserving the low-mass wavefunction and tail norm. They restore finite-order Born recovery, while an exponential source with all moments still has a zero-radius coupling series in the eta=0 model. A dark tail is not treated as a growing bright amplitude. The [complex-mass audit](COMPLEX-MASS-ANALYTICITY.md) now finds that the eta=1 scalar analytic candidate fails subthreshold open-photon contractivity, while both identity patches differ from their upper germs. Certified imaginary-mass poles map to negative s, not a general local-QFT exclusion. The [scalar dispersive response](SCALAR-DISPERSIVE-RESPONSE.md) now matches the charged-pair cut with four full-response subtractions (two after Ward factoring), retaining free s^2 and s^3 terms and a nonzero dispersive phase. It is a right-cut control, not an exact unitary or crossing-complete amplitude. The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ. The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Keep source preparation separate from an interaction form factor: neither the tail used here nor a chosen damping envelope is native evidence or a selected local UV theory.

General dominated-convergence, beta-integral and representation arguments are documented mathematics, not machine-formalized proofs; the checker certifies the stated algebraic/rational components and scope controls. C1-C12, exhausted C12 effort, historical owner/hash warnings and paused high-energy execution are unchanged. No native physical preparation, local/cluster dynamics, measured rate or branching ratio is supplied.

```sh
python -S research/scattering/low-energy/check_packet_weak_coupling_tail.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_packet_weak_coupling_tail.py
```
