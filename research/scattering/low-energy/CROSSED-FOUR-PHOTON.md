# Leading crossed four-photon tensor and scalar partial-wave cuts

[Contract](contracts/crossed-four-photon.v1.json) · [checker](check_crossed_four_photon.py) · [receipt](results/crossed-four-photon.v1.json)

## 1. A conditional tensor construction, not exact dynamics

The [scalar dispersive control](SCALAR-DISPERSIVE-RESPONSE.md) gave R(s)=s^2*Pi(s), with

    Pi(s)=c0+c1*s+(s^2/pi)*J(s),
    Im R(s+i0)=sigma(s)=s^3*sqrt(1-4/s), s>4.

Here complete the **declared leading order-g2^2 tensor** by its three photon pairings. Retain the same imported Dirac/Maxwell fields, threshold m=1, free real c0,c1 and contact-density extrapolation. The extrapolation is not licensed UV input, and other allowed local operators or extra fields have not been excluded. This is not an all-orders crossing/unitarity construction or a native source identification.

Take all four momenta q_i outgoing, sum q_i=0, and define the symmetric pair vertex

    V_ij=det(q_i,e_i,q_j,e_j)=V_ji.

This is the earlier pseudoscalar photon tensor in its declared determinant convention. Define the reduced angular kernel

    M=2*[V12*V34*Pi(s12)+V13*V24*Pi(s13)+V14*V23*Pi(s14)],
    sij=(qi+qj)^2.

The factor 2 fixes the s-channel eigenvalue to the previously normalized R(s) in the pseudoscalar photon mode, as shown below. It is a reduced-kernel normalization with normalized angular measure dOmega/(4*pi); constant two-photon phase volume and Bose normalization are already in b=epsilon2^2. It does not identify or equate the independent g2 and g3. The leading scattering coefficient is (b/2) times this reduced kernel.

Each term satisfies all four Ward identities: replacing any e_i by q_i repeats a determinant column. Exchanging the two legs of a pair swaps two two-column blocks and introduces no sign. S4 permutes the three perfect matchings, and momentum conservation makes complementary-pair invariants equal. Thus one analytic Pi in all three terms supplies Bose/permutation and all-outgoing crossing consistency. This is not permission to conjugate Pi at complex momentum; physical incoming/outgoing polarization conventions are handled separately. Products of two pseudoscalars are proper Lorentz scalars and parity even.

## 2. Physical helicities and the normalization check

In physical 2->2 CM kinematics use q1=-k1,q2=-k2,q3=p3,q4=p4, incoming annihilation polarizations and outgoing conjugate creation polarizations. Let z=cos(theta),

    s=4*E^2, t=-s*(1-z)/2, u=-s*(1+z)/2.

Transport both outgoing helicity frames by the same spatial rotation from the incoming frames. On the equal-helicity pair basis (++ , --), the kernel is

    (1/2)*[[R(s), -(R(s)+R(t)+R(u))],
           [-(R(s)+R(t)+R(u)), R(s)]].

The normalized combinations chi_minus=i*(++ - --)/sqrt(2) and chi_plus=(++ + --)/sqrt(2) diagonalize it, with pointwise eigen-kernels

    F_minus(s,z)=R(s)+[R(t)+R(u)]/2,
    F_plus(s,z)=-[R(t)+R(u)]/2.

The s pairing alone has eigenvalue R(s) in chi_minus and zero in chi_plus, matching the old scalar Born-cut normalization. The other helicity assignments have not been dropped: the checker retains all sixteen physical configurations, although the displayed 2x2 block is the one needed for scalar J=0. Opposite pair helicities have helicity difference two and do not contribute to that scalar projection.

## 3. Scalar partial waves and the two cuts

The reduced J=0 projection uses (1/2)*integral_-1^1 dz. Define

    C(s)=integral_0^1 R(-s*x) dx
        =(1/s)*integral_-s^0 R(y) dy, s!=0.

Then the scalar parity channels are exactly

    A_minus(s)=R(s)+C(s), A_plus(s)=-C(s).

For physical s>0, C is real: its arguments are nonpositive and below the massive-pair right cut. Hence Im A_minus=sigma(s) for s>4 and Im A_plus=0 at this order. The old charged-pair absorptive cut is retained; the crossed terms supply additional real forward data, not a new photon multiplicity fraction.

R has its declared right cut [4,infinity). Since R(-s*x) reaches that cut only for s<=-4/x, C has a left cut (-infinity,-4]. For s=-v+i0, v>4, its argument approaches the R cut from **below**, so

    Im C(-v+i0)=-(1/v)*integral_4^v sigma(t) dt,
    Im A_minus(-v+i0)=-(1/v)*integral_4^v sigma(t) dt,
    Im A_plus(-v+i0)=+(1/v)*integral_4^v sigma(t) dt.

Local polynomial subtractions do not alter these discontinuities. The left-cut onset and signs are derived from the declared crossed tensor, not assigned by calling an arbitrary imaginary-M pole physical. The left-cut magnitude begins as (16/3)*(v-4)^(3/2), from sigma(t)~32*sqrt(t-4). The checker encloses two positive spectral integrals using t=4/(1-u^2): sigma(t)*dt=512*u^2/(1-u^2)^5 du. Positive-series remainder bounds, not floating-point quadrature, certify their signs.

## 4. Selected-sector invariance is not an identity complement

Using the preceding exact a_n=n!*(n+1)!/(2*n+3)!,

    R(s)=c0*s^2+c1*s^3+(1/pi)*sum_(n>=0) a_n*s^(n+4),
    C(s)=c0*s^2/3-c1*s^3/4
         +(1/pi)*sum_(n>=0) a_n*(-1)^n*s^(n+4)/(n+5).

Consequently

    A_minus=4*c0*s^2/3+3*c1*s^3/4+s^4/(5*pi)+s^5/(72*pi)+...,
    A_plus=-c0*s^2/3+c1*s^3/4-s^4/(30*pi)+s^5/(360*pi)+....

A_minus is analytic for |s|<4 with cuts starting at +/-4; A_plus has only the left cut at this order. No choice of these two local coefficients makes A_plus identically zero: its s^4 coefficient remains nonzero. Thus the old photon complement cannot be treated as globally unchanged by a crossing-completed leading interaction. A function only of the old K, which annihilates that complement, cannot supply this extra phase. Here the complement is relative to the current-selected chi_minus mode of K, not the older band-limited eight-profile projector.

**But no J=0-to-J=2 leakage has been inferred.** Rotational invariance preserves J, and parity keeps chi_minus versus chi_plus separate within the scalar photon-elastic block. This does not remove the already retained inverse charged-pair channel of the full scattering problem. The orthogonal photon channel has its **own** nontrivial scattering. A beam with a fixed incoming axis contains other partial waves. Nonconstant z dependence indicates their scattering, not mixing of an already projected J=0 state.

For a monomial R(s)=r_k*s^k, the crossed contribution's reduced J=0 and J=2 moments are

    r_k*s^k*(-1)^k/(k+1),
    r_k*s^k*(-1)^k*k*(k-1)/[(k+1)*(k+2)*(k+3)].

These follow by integrating the binomial in z, or x^k*P_J(1-2*x). In the zero-subtraction control the chi_minus J=2 kernel starts at +s^4/(105*pi), with the opposite sign for chi_plus. These J=2 values are equal-helicity subblock matrix elements, not a diagonalization of the full J=2 helicity carrier. They indicate additional complement dynamics, not a charged-source annihilation channel or a higher-photon branching prediction. Dark source statements remain scoped to their owning completion family.

## 5. A sharper, explicitly scoped Cayley comparison

At leading order in b, both original zero-forward-phase Cayley controls have the same normalized photon response on the upper physical interval: R_C(s)=i*sigma(s). Its earlier upper germ gives, for 0<s<4,

    R_C(s)=-s^(5/2)*sqrt(4-s),

which is nonanalytic at s=0: its third s derivative begins as -15/(4*sqrt(s)). By contrast the leading crossed **massive-pair-loop plus regular local counterterms** construction is analytic there. Finite local subtraction polynomials cannot remove a fractional power. Therefore these zero-phase Cayley germs are not the leading massive-pair-only local response under the declared analytic continuation and interaction assumptions. They retain their mathematical real-axis unitarity as piecewise on-shell prescriptions.

This is not an exclusion of all local UV completions. Extra massless dynamics at the same order, other interactions, a different forward phase or a different asserted analytic domain change the comparison and must be exposed. Massless photon cuts are also expected at **higher order** from photon intermediate states; no all-orders analyticity at zero is claimed. Their order matters: a later cut is not a derivation of this leading-order fractional germ.

## 6. Executable successor and evidence boundary

The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ. The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum. The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Exact unitary dynamics remain unconstructed.

The tensor, projection and analytic arguments are documented mathematics, not machine-formalized proofs. Exact checks cover 64 physical helicity configurations, 1536 cached all-outgoing permutation identities, 48 pair Ward identities, four Lorentz witnesses, sixteen equal-helicity matrices, monomial projections and two signed left-cut certificates. C1-C12, exhausted C12 effort, high-energy pause and historical owner/hash warnings remain unchanged. No native preparation, UV spectral density, subtraction data, physical rates or branching ratios are selected.

```sh
python -S research/scattering/low-energy/check_crossed_four_photon.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_crossed_four_photon.py
```
