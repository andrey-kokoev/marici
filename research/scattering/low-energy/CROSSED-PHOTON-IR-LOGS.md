# Crossed leading photon infrared logs: surviving scalar parity terms

[Contract](contracts/crossed-photon-ir-logs.v1.json) · [checker](check_crossed_photon_ir_logs.py) · [receipt](results/crossed-photon-ir-logs.v1.json)

## 1. Scope and input from the Bose optical theorem

The [photon-cut audit](PHOTON-UNITARITY-CUT.md) fixed Im B=A^dagger*A/8 for T=(b/2)*A+b^2*B+..., b=epsilon2^2, in the pure g2^4 coefficient below the charged threshold. It deliberately left the crossed infrared contributions open. Here reconstruct the **leading IR logarithmic kernel**, not the entire order-g2^4 cut spectrum or amplitude.

In each preceding subtraction regime the leading term is R(s)=r*s^k:

- k=2, r=c0, if c0 is nonzero;
- k=3, r=c1, if c0=0 and c1 is nonzero;
- k=4, r=1/(6*pi), in the c0=c1=0 spectral control.

These are the preceding comparison model's regimes, not an exhaustive classification of possible UV matching data. The contact spectral density extrapolation remains unlicensed. Extra same-order massless interactions or poles would change the cuts. Independent g3 contributions are not identified with g2 or included in this pure-coefficient calculation. Set q=2*k. All log coefficients below multiply b^2*r^2 in the full T.

## 2. Reconstruct helicity cuts before crossing

Write e_J and h_J for the monomial moments E_kJ,H_kJ from the prior audit, with r*s^k stripped off. Let a_minus=1+e_0, a_plus=-e_0. Define the polynomials

    D_k(z)=(a_minus^2+a_plus^2)/16
           +sum_(even J>=2)^k (2*J+1)*e_J^2*P_J(z)/8,
    O_k=(a_plus^2-a_minus^2)/16,
    M_k(x)=sum_(J=2)^k (2*J+1)*h_J^2*x^2*P_(J-2)^(0,4)(2*x-1)/16.

D is even in z; M starts at x^2. The ordered mixed-helicity denominator is 16, not 8: its physical Bose eigenvalue has been distributed over its two ordered components. Both even and odd allowed J are included.

For physical s>0, z=cos(theta), x=(1+z)/2, the right-cut coefficient in the (++ , -- , +- , -+) basis is r^2*s^q times

    [[D_k(z), O_k, 0, 0],
     [O_k, D_k(z), 0, 0],
     [0, 0, M_k(x), M_k(1-x)],
     [0, 0, M_k(1-x), M_k(x)]].

This reconstructs all helicity sums of the normalized Bose carrier. In particular the constant off-diagonal O is not obtained by guessing a scalar crossing rule for one parity wave. At k=2, D=17/144+P2(z)/1440, O=-5/48, M=x^2/80. The checker also constructs the k=3,4 polynomials and verifies their mixed-channel projections against the optical coefficients.

## 3. Crossed logarithmic sections and a Ward/Bose tensor

Use all-outgoing momenta and the preceding gauge-invariant pair vertices V_ij=det(q_i,e_i,q_j,e_j). Resolve each external field strength into its two Hodge-duality components. The +/- names of those components are conventional; in the transported physical frames their labels are (h1,h2,-h3,-h4). Applying chiral projectors before the bilinear V gives V_ij^h: on a pure-duality configuration it equals V_ij if both fields have that duality, and is zero otherwise.

For two-plus/two-minus dualities there is one same-duality pairing, with invariant S and vertex product V=V_ij^+*V_kl^- (or the reverse). The other two invariants T,U obey S+T+U=0. Its logarithmic coefficient section, before the common factor -r^2/pi, is

    (4*V/S^2)*[S^q*D_k((T-U)/S)*log(-S/nu)
               +T^q*M_k(-S/T)*log(-T/nu)
               +U^q*M_k(-S/U)*log(-U/nu)].

For four equal dualities, sum the three pairings with section

    -4*O_k*sum_pairings V_ij^h*V_kl^h*S^(q-2)*log(-S/nu).

Sum the two dualities in each class. The three-plus/one-minus **leading cut/log** sections vanish; cut-free rational/local terms are not thereby excluded from the full quartic amplitude. These sections extend multilinearly through the field-strength projectors.

The displayed divisions are bookkeeping, **not poles**. D has degree <=k and is even, so the first mixed coefficient is a sum of S^(q-j-2)*(T-U)^j, with nonnegative powers. M starts at degree two, so the other coefficients are sums of S^(j-2)*T^(q-j) and S^(j-2)*U^(q-j). The checker evaluates these polynomial forms directly, including forward kinematics. Every term contains all four external field strengths; replacing a polarization by its momentum kills a pair vertex. Pair permutations, and symmetry under T<->U, give all-outgoing Bose/crossing consistency. Proper Lorentz covariance follows from the vertices and invariant polynomials, not from a chosen helicity probability average.

Here nu is an arbitrary positive squared-mass reference for the logarithms, not a selected source scale or the endpoint of the prior finite IR window. Changing it shifts a local real polynomial. Finite-window matching and counterterm data remain necessary.

## 4. Project the crossed logs into scalar parity waves

In the physical equal-helicity block call the diagonal logarithmic section G and the off-diagonal one O. With t=-s*alpha, u=-s*(1-alpha),

    G=s^q*D_k(z)*log(-s/nu)
       +t^q*M_k(-s/t)*log(-t/nu)+u^q*M_k(-s/u)*log(-u/nu),
    O=O_k*[s^q*log(-s/nu)+t^q*log(-t/nu)+u^q*log(-u/nu)].

The physical parity combinations are G-O and G+O. Scalar projection uses dz/2, equivalently d alpha. Let d0=(a_minus^2+a_plus^2)/16 and M(x)=sum_j m_j*x^j. The exact crossed angular log coefficients are

    L_k=2*sum_j m_j/(q-j+1),
    K_k=-2*sum_j m_j/(q-j+1)^2.

The corresponding off-diagonal factors are 2*O_k/(q+1) and -2*O_k/(q+1)^2. These follow from integral_0^1 alpha^n d alpha=1/(n+1) and integral_0^1 alpha^n*log(alpha)d alpha=-1/(n+1)^2. All endpoint powers obey n>=2, so no collinear divergence was discarded.

Writing sign=-1 for minus parity and +1 for plus parity,

    kappa=d0+sign*O_k,
    lambda=L_k+sign*2*O_k/(q+1),
    Gamma=kappa+lambda.

The projected leading logarithmic response is

    B_parity^log=-(r^2*s^q/pi)*[kappa*log(-s/nu)
                              +lambda*log(s/nu)+local_angular_constant].

This formula describes the upper physical section, not an independent assertion about every complex sheet. For 0<s in the IR window, log(-s/nu)=log(s/nu)-i*pi, so

    Im B_parity=r^2*kappa*s^q,
    Re B_parity^log=-(r^2/pi)*Gamma*s^q*log(s/nu)+local terms.

The right-cut coefficient stays positive and agrees with the prior optical table. A crossed real-log coefficient is not constrained to have that sign.

## 5. Exact cancellation audit

All entries below have r^2 stripped off. For k=4 restore r^2=1/(36*pi^2), not one.

| k | parity | right cut kappa | crossed log lambda | surviving real log Gamma |
|---:|---|---:|---:|---:|
| 2 | minus | 2/9 | 1/20 | 49/180 |
| 2 | plus | 1/72 | -1/30 | -7/360 |
| 3 | minus | 9/128 | 17/1344 | 223/2688 |
| 3 | plus | 1/128 | -1/192 | 1/384 |
| 4 | minus | 9/50 | 127/5880 | 5927/29400 |
| 4 | plus | 1/200 | -61/3528 | -271/22050 |

**Neither scalar parity real log cancels completely in any of the three declared regimes.** Crossing partly cancels or reverses some coefficients: the k=3 plus coefficient is one third of its right-cut-only value; k=2 and k=4 plus coefficients change sign. This does not reverse absorption or violate positivity. Finite local real counterterms can change regular terms, not remove these nonzero logarithmic coefficients. Other leading interactions or matching assumptions would require a new calculation.

These are order-g2^4 integer-power logarithms. They do not repair the old order-g2^2 fractional Cayley germ at fixed perturbative order. They establish neither an all-orders amplitude nor native local dynamics. The finite constants displayed by angular integration are not full matching constants: unknown real analytic terms, window completion and higher-energy data are still absent.

## 6. Executable successor and scope boundary

The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix. The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square. The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected. The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence. The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded. The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds. The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free. The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected. Next construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Running does not select a source scale or UV completion.

General chiral-tensor, crossing and logarithmic arguments are documented mathematics, not machine-formalized proofs. Exact certificates check the right-cut helicity coefficients, all-outgoing permutations, Ward and Lorentz witnesses, Bose optical projections and the scalar rational table. The result is a leading-IR kernel, not the full quartic spectrum. C1-C12, exhausted C12 effort, the high-energy pause and historical owner/hash warnings remain unchanged. No finite counterterm, UV density, native preparation, physical rate or branching ratio is selected.

```sh
python -S research/scattering/low-energy/check_crossed_photon_ir_logs.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_crossed_photon_ir_logs.py
```
