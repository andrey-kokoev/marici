# A conditional two-data modulus for photon-cut reconstruction

## Result and domain

[Contract](contracts/photon-box-cut-modulus-v1.json) · [checker](checkers/check_photon_box_cut_modulus_v1.py) · [tests](checkers/test_photon_box_cut_modulus_v1.py) · [receipt](results/photon-box-cut-modulus-v1.json).

On the explicitly assumed source box S_M={|g2|,|f2|,|g3|,|f3|,|h3|,|g4|,|g4prime|,|f4|<=M}, M>=1, the exact joint-data cut map has a computable uniform Holder-1/3 modulus. A separate unit-box family excludes every uniform two-data exponent greater than 1/2, including Lipschitz recovery. **Neither endpoint is claimed optimal:** a gap between 1/3 and 1/2 remains.

This is the imported real parity-even on-shell eight-leading-contact Born model, retained quadratic two-photon degree-six sector, fixed amplitude frames and normalized coefficient units. The source box and any noise budget are conditional assumptions, not native/UV bounds or physical calibration. All eighteen finite local matching coefficients and the source sign ambiguities remain retained.

Let D(X) be the thirteen coordinates consisting of the calibrated seven degree-four/five cut coordinates J and six degree-six common-log coefficients B. Let C(X) be the thirteen coefficients of the four independent D/O/M/single-minus angular cut polynomials, padded to lengths (3,3,4,3). All norms below are max norms in these fixed coordinates; they are not scattering-rate or arbitrary boosted tensor norms.

## 1. Explicit modulus

For X,Y in S_M set delta=||D(X)-D(Y)||. The [exact joint-data reconstruction](photon-joint-transport-v1.md) makes C a well-defined function on this realizable image, even though sources need not be unique. Define

    L(M)=13/3+(45/7)*M^2,
    D_M=(2713/3360)*M^2.

Then

    ||C(X)-C(Y)|| <= omega_M(delta),
    omega_M(0)=0,
    omega_M(delta)=min(D_M,L(M)*delta^(1/3))   for 0<delta<=1,
    omega_M(delta)=D_M                        for delta>1.

D_M is a source-box cut diameter bound from the independently projected monomial coefficient rows. The implementation computes rational upper enclosures of the cube root with a scaled dyadic bracket and controlled relative precision; no floating-point fit or precision floor at zero is used. It also accepts the equivalent certificate delta<=rho^3,0<rho<=1, yielding the bound L(M)*rho.

## 2. Quantitative proof across all leading strata

Write leading vectors ell=(g2,f2) and k, and cubic pairs z=(g3,f3). Choose a simultaneous sign for the second entire source so ell dot k>=0; this leaves all data and cuts unchanged and is not physical sign selection. Exchange X,Y if necessary so r=||ell||_2>=||k||_2.

### Leading Gram alignment

The data contain the three entries of ell*ell^T. Their matrix Frobenius gap F obeys F<=2*delta. The aligned vector gap d obeys d<=2*F/r<=4*delta/r for r>0. One algebraic verification puts s=||k||/r and c equal to the nonnegative alignment cosine (take c=0 when k=0). The expression (F^2-r^2*d^2/4)/r^4 is concave in c, and its endpoint values are nonnegative for s in [0,1]:

    c=0: 3/4-s^2/4+s^4 >=1/2,
    c=1: (1-s)^2*(s^2+2*s+3/4) >=0.

The factorization is checked exactly, not inferred from sampled alignment angles.

### Cubic sensing away from the zero-leading boundary

The three lower degree-five data (u,v,w) obey

    (u,v,w)^T=A(ell)*z,
    A(g,f)=[[g,0],[0,f],[10*f,g]].

Its squared singular values have trace 2*g^2+101*f^2<=101*r^2 and determinant g^4+g^2*f^2+100*f^4>=r^4/2. Thus its smallest singular value is at least r/15. Also ||(A(ell)-A(k))*z_Y||_2<=11*M*d. Hence

    ||z_X-z_Y||_2 <=30*delta/r+660*M*delta/r^2,
    |g3_X^2-g3_Y^2| <=1440*M^2*delta/r^2,

using r<=2*M. This uses all three mixed degree-five coordinates, and is valid on either leading chart and both cancellation loci. It does not divide by a single-minus trace.

The sole missing response is m3=g3^2/4032. The fixed-m3 linear map from B to cut coefficients has max-norm gain 13/3, and the m3 direction has cut norm eighteen. Therefore, for r>=rho,

    cut gap <=(13/3)*delta+(45/7)*M^2*delta/r^2.

### Near the zero-leading boundary

For r<=rho use the [universal surrogate bias identity](photon-joint-transport-stability-v1.md). For each source its missing-coordinate bias is

    b=-g2*g4/1680+g2*g4prime/7200-f2*g4prime/43200.

The two biases together are bounded by 2*M*r*(37/50400+1/43200). With the surrogate gain 13/3 and cut-line norm eighteen,

    cut gap <=(13/3)*delta+(229/8400)*M*r.

This includes r=0 and both leading sources zero. It is a cut bound, not a unique source inverse.

For delta<=rho^3 and rho<=1, both regimes give cut gap<=L(M)*rho: the near coefficient 229*M/8400 is smaller than 45*M^2/7 for M>=1. Taking rho=delta^(1/3) proves the stated modulus. At delta=0 use exact image/fibre equivalence. The independent diameter bound handles larger gaps. All constants come from explicit inequalities and coefficient rows, not compactness alone or a Jacobian nullspace. The documented real-inequality argument is not proof-assistant formalization.

## 3. A bounded obstruction to exponents above 1/2

Continuity does not make the inverse Lipschitz. Use the rational p(v),q(v) from the [equal-transport curve](photon-equal-transport-v1.md), with q^2+(30/7)*p^2=1. Put p0=p(1)=14/37,q0=q(1)=-23/37. For 0<r<=1 write p1=p(1+r),q1=q(1+r), Delta=p1^2-p0^2 and Z=p1*q1-p0*q0. Set

    X_r=(r,0,p0,q0,0,0,0,0),
    Y_r=(r,0,p1,q1,0,-7*Delta/(16*r),-5*Delta/(56*r),-5*Z/(84*r)).

All coordinates of both sources lie in [-1,1]. To certify the quartic bounds, on v in [1,2] use |p'|<=14/37, |q'|<=1680/1369 and |p|,|q|<=1; the resulting mean-value bounds on each displayed quartic coefficient are strictly below one. The apparent divisions by r have removable finite limits; no nuisance contact diverges.

The two actual sources have the same nonzero B. Their monomial difference decomposes into Delta and Z directions, both annihilated exactly by all six transport rows. The Delta direction has cut response (-3,-3,0,0,5,1,0)/4032; the Z direction has zero cut. Their joint-data and cut gaps are exactly

    delta_r=r*max(|p1-p0|,|q1-q0|),
    cut_gap_r=|Delta|/224.

Exact derivatives at v=1 give

    delta_r/r^2 ->840/1369 >0,
    cut_gap_r/r ->161/202612 >0.

Thus cut_gap_r/(delta_r^alpha) diverges for every alpha>1/2. No uniform two-data estimate with such an exponent, including Lipschitz, can hold even on the unit source box. This does not refute bounded-source continuity: the cuts approach the same limit, and the obstruction concerns pairs of nearby data, not merely a fixed-basepoint continuity limit. It also does not prove the half-power upper bound. The earlier unbounded-source discontinuity is not used as a substitute bounded witness.

## 4. Deterministic uncertainty consequence and limits

If a supplied datum has one or more compatible actual sources in S_M within a deterministic coefficient tolerance epsilon, then any two compatible joint data differ by at most 2*epsilon. Their cut coefficient set therefore has diameter at most omega_M(2*epsilon). This is not a probability or coverage guarantee, does not establish nonempty compatibility, and does not choose one source or matching coefficient. Native licensing of M, epsilon and the imported observable frame remains separate.

Eight tests and exact controls check the algebraic certificates, 178 two-point box comparisons, scaled source boxes, rational cube-root enclosures, and four bounded sharpness pairs. Scoped SCC and a fresh headless receipt accompany the packet; no fresh full-suite or physical evidence claim is made. C1–C12, C12's exhausted budget and the high-energy pause are unchanged.

Next close the exponent gap: prove a uniform half-power cut modulus on the conditional source box, or exhibit a bounded-source obstruction below one-half. Until then neither the conservative one-third estimate nor the half-power ceiling is optimality. Physical matching, native dynamics and UV/source-bound inputs remain unearned. See [frontier v3](photon-eft-frontier-v3.md).

```text
python -S research/nima/checkers/check_photon_box_cut_modulus_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_box_cut_modulus_v1.py
```
