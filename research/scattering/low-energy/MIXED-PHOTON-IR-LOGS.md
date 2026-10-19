# Mixed c0*c1 photon cuts: odd-degree crossing and local scale mixing

[Contract](contracts/mixed-photon-ir-logs.v1.json) · [checker](check_mixed_photon_ir_logs.py) · [receipt](results/mixed-photon-ir-logs.v1.json)

## 1. Missing interference term, not a new positive channel

The [counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) treated the three leading monomial regimes separately. With both real subtraction coefficients present, the same conditional leading photon kernel has

    A=c0*s^2*A2+c1*s^3*A3+O(s^4),
    T=(b/2)*A+b^2*B+...,    Im B=A^dagger*A/8.

Here A2,A3 are dimensionless angular kernels, including their full Bose-helicity carriers, not scalar probabilities. The missing degree-five coefficient is

    Im B_23=(c0*c1*s^5/8)*(A2^dagger*A3+A3^dagger*A2).

On the common normalized Bose eigenbasis its coefficient is a2*a3/4. The denominator is **4**, not 8: both interference orderings contribute. This term is not an extra open channel and need not be positive by itself. The complete two-term cut remains the squared norm of c0*s^2*A2+c1*s^3*A3 divided by eight.

This is the pure g2^4 coefficient of the previous conditional density model below the charged threshold, with no added massless poles. Independent g3 contributions are outside this coefficient, not declared absent. No c0,c1 value or sign is selected. The two-term square is an algebraic positivity control, not a claim that truncation determines the full photon amplitude.

## 2. Full helicity and partial-wave reconstruction

Polarize the earlier monomial cut polynomials: replace a squared monomial eigenvalue by twice the product of its k=2 and k=3 values. In the notation of the [crossed-log audit](CROSSED-PHOTON-IR-LOGS.md), with q=5,

    D(z)=(37-z^2)/320,
    O=-13/96,
    M(x)=-x^2/48,    x=(1+z)/2.

With c0*c1*s^5 stripped, the physical right-cut matrix in (++ , -- , +- , -+) is

    [[D(z), O, 0, 0],
     [O, D(z), 0, 0],
     [0, 0, M(x), M(1-x)],
     [0, 0, M(1-x), M(x)]].

The scalar parity cut coefficients are kappa_minus=1/4 and kappa_plus=-1/48. The J=2 equal-parity coefficients are both -1/2400; the normalized Bose J=2 mixed coefficient is -1/120. The J=3 mixed interference vanishes because the k=2 amplitude has no such component; its k=3 squared contribution remains retained in the complete two-term control. J=1 is still absent.

For every Bose eigenwave the complete cut is

    [c0*s^2*a2+c1*s^3*a3]^2/8
      =c0^2*s^4*a2^2/8+c0*c1*s^5*a2*a3/4+c1^2*s^6*a3^2/8 >=0.

As a two-term algebraic control, c0=3,c1=4,s=1 gives zero J=0 plus-parity cut: its positive squared terms are 1/8+1/8 and its interference is -1/4. This is a coherence witness, not selected matching data or a cancellation claim for the untruncated spectral response.

In particular a negative interference coefficient in the plus scalar wave is compatible with positivity. The checker separately squares the summed amplitudes, reconstructs their angular polynomials and verifies the decomposition into the three homogeneous terms for signed and zero coefficients. It checks equal- and mixed-helicity projection moments with the normalized Bose factors, not a single ordered entry squared.

## 3. Cross before scalar projection: q is odd

Use the parent's pure-duality field-strength sections, now with the polynomials above and q=5. For two plus and two minus dualities, let S be the same-duality pairing invariant and W its pair-vertex product. The logarithmic section before -c0*c1/pi is

    (4*W/S^2)*[S^5*D((T-U)/S)*log(-S/nu)
               +T^5*M(-S/T)*log(-T/nu)
               +U^5*M(-S/U)*log(-U/nu)].

For four equal dualities it is

    -4*O*sum_pairings W_S*S^3*log(-S/nu).

The checker evaluates expanded polynomial coefficients only: the mixed S-channel coefficient uses S^3 and S*(T-U)^2; the crossed ones use S^0*T^3 or S^0*U^3, before multiplication by W. There are no added Mandelstam poles. The chiral field-strength projectors provide a multilinear Ward-compatible extension. Pairing sums and T<->U symmetry give Bose/crossing covariance. Three-plus/one-minus cut/log sections vanish here without excluding finite/rational terms in the full quartic amplitude.

On the physical upper section t=-s*alpha and u=-s*(1-alpha). **Now t^5 and u^5 are negative.** Reusing the even-q angular-log formulas without this sign would be wrong. If M(x)=sum_j m_j*x^j, the diagonal crossed-log and finite angular moments are

    L=2*(-1)^q*sum_j m_j/(q-j+1)=1/96,
    K=-2*(-1)^q*sum_j m_j/(q-j+1)^2=-1/384.

The off-diagonal crossed-log coefficient is 2*(-1)^q*O/(q+1)=13/288. With sign=-1 for minus parity and +1 for plus parity,

    kappa=d0+sign*O,       d0=11/96,
    lambda=L+sign*2*(-1)^q*O/(q+1),
    Gamma=kappa+lambda.

Thus the scalar interference response is

    B_23,parity^log=-(c0*c1*s^5/pi)*[kappa*log(-s/nu)
                                   +lambda*log(s/nu)+angular_constant].

All coefficients below have c0*c1 stripped; the physical interference changes sign if that product changes sign and vanishes if the product is zero.

| parity | right cut kappa | crossed log lambda | surviving real log Gamma | angular constant |
|---|---:|---:|---:|---:|
| minus | 1/4 | -5/144 | 31/144 | 17/3456 |
| plus | -1/48 | 1/18 | 5/144 | -35/3456 |

For s>0, log(-s/nu)=log(s/nu)-i*pi. Absorption therefore remains c0*c1*kappa*s^5, while the real momentum-log coefficient is -(c0*c1/pi)*Gamma. **Neither scalar interference log cancels completely.** Endpoint integrals are finite: their crossed diagonal power is alpha^3 and the off-diagonal power is alpha^5. The finite angular constants are not complete matching constants.

## 4. Three local representatives and off-diagonal running

At q=5 the parity-even polynomial classes used in the parent have the basis

    all equal:       P_all*e2*e3,
    two plus/two minus: P_mixed*S^5, P_mixed*S^3*T*U,
    e2=ST+TU+US, e3=STU.

The phases are P_all=-4*W_S/S^2 and P_mixed=4*W_S/S^2 only for classification; no such division is evaluated. Since p5=S^5+T^5+U^5=-5*e2*e3, the all-equal representative is -A5/5, with A5=-4*sum W_S*S^3. The mixed representatives are 4*W_S*S^3 and 4*W_S*S*T*U. All are polynomial in the momenta and contain all four field strengths. Their contact operator dimension is fourteen.

The invariant-ring arguments of the parent give one all-equal and two mixed representatives, independent on these polynomial classes. They do not classify omitted helicity sectors or a complete off-shell EFT basis. The phase-stripped all-equal and mixed sections of H=sum_a H_a are

    H_same=O*p5=(65/96)*e2*e3,
    H_mixed=(2/15)*S^5-(1/20)*S^3*T*U.

Equivalently H=sum_i h_i*O_i, with

    h=(65/96, 2/15, -1/20).

The source checks the exact rational polynomial decomposition and the tensor identity in all physical helicities, including forward kinematics, as well as Ward, Lorentz and all-outgoing permutation witnesses. For scalar projection the basis moments are (-2/15,1,1/6); mixed minus/plus all-equal combinations reproduce 31/144 and 5/144 independently.

Use **unfactored**, independent local coefficients,

    B_local^(q5)=sum_i C_i(nu)*O_i.

Then

    d B_log/d log(nu)=+(c0*c1/pi)*H,
    d C_i/d log(nu)=-(c0*c1/pi)*h_i.

The beta coefficient of c0*c1/pi is therefore (-65/96,-2/15,1/20). This is the first audited mixed-subtraction contribution, not a full EFT anomalous-dimension matrix. Hold the leading c0,c1 fixed at this order; no running of g2 or g3 is inferred. Nu is a positive squared-mass logarithm reference, not a selected source scale or finite IR-window endpoint; a mass-scale derivative would have an additional factor of two.

For nu'=exp(ell)*nu, the log change +(c0*c1/pi)*ell*H cancels the local shift delta C_i=-(c0*c1/pi)*ell*h_i. Finite real constants C_i(nu0) remain arbitrary, including when c0*c1=0. Vanishing interference then means zero contribution to running, **not** zero finite contact coefficients. Counterterms do not remove the physical momentum logarithms or alter right-cut absorption.

## 5. Boundaries and executable successor

This adds one missing homogeneous coefficient to the existing conditional construction. It is not the full quartic cut spectrum, an all-orders S matrix, a complete renormalized EFT, a UV completion or native preparation. C1-C12, exhausted C12 effort, the high-energy pause and historical owner/hash warnings are unchanged. Physical couplings, rates and branching ratios remain unselected. General tensor, invariant-ring and logarithmic arguments are documented mathematics, not machine-formalized proofs.

The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected.

The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence.

The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded.

The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds.

The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free.

The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected.

**Next:** construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Do not infer all-subthreshold convergence from the right-cut response series.

```sh
python -S research/scattering/low-energy/check_mixed_photon_ir_logs.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_mixed_photon_ir_logs.py
```
