# Degree-six photon logs: coupled subtraction data and cancellation loci

[Contract](contracts/degree6-photon-ir-logs.v1.json) · [checker](check_degree6_photon_ir_logs.py) · [receipt](results/degree6-photon-ir-logs.v1.json)

## 1. Complete the homogeneous coefficient, not the full amplitude

The [degree-five audit](MIXED-PHOTON-IR-LOGS.md) exposed interference missing from separate monomial controls. For the same conditional photon kernel, write

    R(s)=c0*s^2+c1*s^3+r4*s^4+O(s^5),
    A=c0*s^2*A2+c1*s^3*A3+r4*s^4*A4+O(s^5),
    T=(b/2)*A+b^2*B+...,    Im B=A^dagger*A/8.

Then degree six has exactly two input monomials in this model:

    X=c1^2 >=0,    Y=c0*r4,
    Im B6=(s^6/8)*[X*A3^dagger*A3+Y*(A2^dagger*A4+A4^dagger*A2)].

The prior c1-only calculation gives the X column, not the general coefficient. This audit supplies the Y column, crosses both and combines their scale dependence. This is complete at homogeneous degree six **for the declared leading kernel and retained pure g2^4 photon cut**, not for generic photon EFT interactions or the entire quartic spectrum. Independent g3 contributions are outside this coefficient, not declared absent. Additional leading tensor structures or massless poles require a new calculation.

Keep r4 symbolic. Its value 1/(6*pi) belongs only to the preceding contact-spectral-density control, whose UV extrapolation is not source-licensed. No UV matching, subtraction value, dimensionful coupling relation or physical preparation is selected here.

## 2. Reconstruct the missing c0*r4 interference

On the normalized Bose eigenbasis the Y cut coefficient is a2*a4/4, including both interference orderings. In the parent D,O,M notation it gives

    D24(z)=29/140+z^2/280,
    O24=-23/120,
    M24(x)=x^2/56,    x=(1+z)/2.

With Y*s^6 stripped, insert these in the full right-cut matrix

    [[D24(z), O24, 0, 0],
     [O24, D24(z), 0, 0],
     [0, 0, M24(x), M24(1-x)],
     [0, 0, M24(1-x), M24(x)]].

The scalar parity coefficients are 2/5 and 1/60. The two J=2 equal-parity coefficients are 1/2100 and the normalized Bose J=2 mixed coefficient is 1/140. J=3,4 interference coefficients vanish because A2 has no such components. This does not erase their nonzero components in A3 or A4: the full three-term square retains all allowed channels through J=4.

The checker independently forms the polynomial in s for every Bose eigenamplitude c0*s^2*a2+c1*s^3*a3+r4*s^4*a4, squares it and extracts its s^6 coefficient. Angular reconstruction agrees with X*(D33,O33,M33)+Y*(D24,O24,M24). The complete polynomial square is nonnegative on real controls. Signed test inputs are algebraic controls, not declarations of admissible positive-spectral UV matching. Its individual s^6 coefficient need not be nonnegative. A positivity conclusion about a complete norm cannot be transferred to a signed homogeneous Taylor coefficient or an uncontrolled truncation.

## 3. Crossed tensor and scalar logarithms

Apply the field-strength construction of the [crossed IR-log audit](CROSSED-PHOTON-IR-LOGS.md) with q=6 separately to each column. For two plus and two minus dualities the section, before its common -X/pi or -Y/pi factor, is

    (4*W/S^2)*[S^6*D((T-U)/S)*log(-S/nu)
               +T^6*M(-S/T)*log(-T/nu)
               +U^6*M(-S/U)*log(-U/nu)].

For four equal dualities it is -4*O*sum_pairings W_S*S^4*log(-S/nu). These apparent divisions are classification notation only. The implementation expands polynomial coefficients; the Ward, Bose/crossing and Lorentz properties are retained, including at forward kinematics. Three-plus/one-minus logarithmic cuts vanish here, without excluding finite/rational quartic amplitudes in those sectors.

On the upper physical section the scalar response is

    B6,parity^log=-(s^6/pi)*[(X*kappa33+Y*kappa24)*log(-s/nu)
                            +(X*lambda33+Y*lambda24)*log(s/nu)
                            +angular_constant].

The angular constant is the corresponding linear combination of the parent integrals, not a complete matching constant. For log(-s/nu)=log(s/nu)-i*pi, absorption is s^6*(X*kappa33+Y*kappa24). The real momentum-log coefficient is -(s^6/pi)*(X*Gamma33+Y*Gamma24), where

| input monomial | parity | right cut kappa | crossed log lambda | real log Gamma |
|---|---|---:|---:|---:|
| X=c1^2 | minus | 9/128 | 17/1344 | 223/2688 |
| X=c1^2 | plus | 1/128 | -1/192 | 1/384 |
| Y=c0*r4 | minus | 2/5 | 13/210 | 97/210 |
| Y=c0*r4 | plus | 1/60 | -1/21 | -13/420 |

The X column is reproduced exactly, including its full helicity tensor, rather than re-normalized. Both columns are verified against physical cut entries, normalized mixed-helicity projection moments and an independent local-basis scalar projection.

## 4. Cancellation classification and what a zero means

For X>0, the two real-log zero loci are

    Gamma6_minus=0  iff Y/X=-1115/6208,
    Gamma6_plus =0  iff Y/X=35/416.

They differ. The determinant of the map (X,Y)->(Gamma6_minus,Gamma6_plus) is -473/125440, so **both degree-six scalar real logs vanish only when X=Y=0**. This statement also covers X=0 without dividing by it. Vanishing degree-six logs does not mean that lower- or higher-degree logs or the full amplitude vanish.

Each individual locus is an allowed conditional cancellation relation, not a source-selected ratio. Restoring the spectral-control r4 merely translates it into a relation among still-unselected matching data. Finite local counterterms cannot impose or remove these physical momentum-log coefficients.

A real-log zero is also not an absorptive zero. At the minus locus the degree-six right-cut coefficient is -19*X/12416; at the plus locus it is 23*X/2496. The negative coefficient at the first locus is not negative probability: the complete three-term squared amplitude, including other homogeneous degrees, stays nonnegative. The checker includes both loci as signed parameter controls and retains the higher-J squared components even where their degree-six coefficient is zero.

## 5. Two input columns in a five-dimensional local basis

Use the parity-even log-supported on-shell basis of the [counterterm audit](PHOTON-COUNTERTERM-RUNNING.md), in this order:

    P_all*e2^3, P_all*e3^2,
    P_mixed*S^6, P_mixed*S^4*T*U, P_mixed*S^2*(T*U)^2.

The parent supplies manifestly local field-strength representatives, with no Mandelstam division, of contact dimension sixteen. This is not a complete off-shell EFT basis or a classification of omitted helicity sectors. Decompose the sum of logarithm coefficients as

    H6=sum_i (X*h33_i+Y*h24_i)*O_i,
    h33=(1/16, -3/32, 111/2240, -293/6720, 5/336),
    h24=(23/60, -23/40, 8/35, -3/35, 1/28).

For independent, unfactored real local coefficients B_local^(6)=sum_i C_i(nu)*O_i,

    d C_i/d log(nu)=-(X*h33_i+Y*h24_i)/pi.

Nu is the arbitrary positive squared-mass logarithm reference, not the finite IR-window endpoint or a physical source scale. A mass-scale derivative has an additional factor of two. At this order the leading c0,c1,r4 are held fixed; these are new quartic-order photon coefficients, not a running of g2 or g3. The finite change nu'=exp(ell)*nu shifts the logarithms by +(ell/pi)*H6 and the local coefficients by -(ell/pi)*(X*h33+Y*h24), cancelling for all external configurations in the declared tensor classes.

The two-input running map has rank two: the minor using rows 0 and 4 is -1/288. Consequently it has three independent **input-independent invariant linear combinations** of the five C_i. The receipt constructs three explicit covectors annihilating both columns; one example is C1+(3/2)*C0. Their values remain arbitrary. All five finite coefficients at a reference point remain matching data, not just the invariant combinations. For fixed X,Y, running with a single scale follows one straight direction; the rank-two statement concerns variation of the two independent input monomials, not a two-dimensional trajectory in one scale.

## 6. Boundaries and executable successor

The result completes one homogeneous photon-cut/log coefficient and its reference-scale running in the conditional model. It is not the full order-g2^4 spectrum, a full EFT anomalous-dimension matrix, all-orders scattering or an interacting local UV completion. It derives no physical rate, branching ratio or native preparation. C1-C12, exhausted C12 effort, the high-energy pause and historical owner/hash warnings remain unchanged. General tensor, invariant-ring and logarithmic arguments are documented mathematics, not machine-formalized proofs.

The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence.

The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded.

The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds.

The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free.

The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected.

**Next:** construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. Do not infer all-subthreshold convergence from convergence of the right-cut response series, and keep finite matching and source licensing separate.

```sh
python -S research/scattering/low-energy/check_degree6_photon_ir_logs.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_degree6_photon_ir_logs.py
```
