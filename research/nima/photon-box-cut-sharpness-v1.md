# The conditional one-third cut exponent is sharp

## Question and result

Can the conditional uniform cut exponent be improved from one-third to one-half on the full finite source box?

[Contract](contracts/photon-box-cut-sharpness-v1.json) · [checker](checkers/check_photon_box_cut_sharpness_v1.py) · [tests](checkers/test_photon_box_cut_sharpness_v1.py) · [receipt](results/photon-box-cut-sharpness-v1.json).

**No.** An exact real algebraic pair family lies uniformly in the unit source box, has identical degree-five data and identical nonzero degree-six transport, but has degree-four data gap of order r^3 and cut gap of order r. Every uniform exponent greater than one-third fails. Together with the [explicit one-third upper modulus](photon-box-cut-modulus-v1.md), this proves that one-third is the optimal **power exponent** on the declared conditional source box. The optimal constant or modulus shape is not determined.

The model remains the imported real parity-even eight-contact Born domain, fixed normalized coefficient frames and retained quadratic two-photon degree-six order. This does not license a physical source box, numerical matching, preparation, native dynamics, UV completion or a full physical IR inventory. All eighteen finite local matching directions remain free.

## 1. Explicit actual-source algebraic family

Let 0<r<=1/100 and set

    k=5*sqrt(14)/12, k^2=175/72,
    c=142/791, A=1-c*r, v=1+r.

Define leading and cubic contacts by

    gx=k*r*A*v, fx=r*A, px=k/(20*A*v), qx=1/(2*A),
    gy=k*r/v,   fy=r,   py=k*v/20,     qy=1/2.

Both h3 contacts are zero. Their complete degree-five data agree exactly:

    gx*px=gy*py=k^2*r/20,
    fx*qx=fy*qy=r/2,
    gx*qx+10*fx*px=gy*qy+10*fy*py=(k*r/2)*(v+1/v).

The single-minus lower datum vanishes for both. The leading ratios k*v and k/v are the two nearby roots of the same lower degree-five factorization equation. The family exploits their coalescence rather than keeping the leading ratio fixed.

All three quartic contacts remain explicitly available. To specify them, put

    Delta=py^2-px^2, E=qy^2-qx^2, Z=py*qy-px*qx,
    kx=k*v, ky=k/v,
    S=(355/224)*Delta+(25/64)*E,
    ell=S/(ky-kx),
    U=-(5/12)*Delta+(7/30)*S,
    W=-(5/32)*Delta-(7/192)*E,
    N=[-(7/40)*ky*W
        -(5/48)*((1/ky-1/kx)*r+U/ky)-Z/96]
        /[(7/40)*(ky-kx)].

Choose the quartics

    Kx=r/gx,       Lx=ell/fx, Mx=N/fx,
    Ky=(r+U)/gy,   Ly=ell/fy, My=(N+W)/fy.

The two actual sources are X=(gx,fx,px,qx,0,Kx,Lx,Mx) and Y=(gy,fy,py,qy,0,Ky,Ly,My). These are constructive mathematical source values, not physical matching choices. The apparent divisions by r and ky-kx have removable finite limits at r=0; the specific rational constants c and k^2 ensure the required numerator cancellations.

## 2. Exact factorization and uniform source bounds

The checker represents each coordinate as a rational function of r times either 1 or k. The parity pattern is

    (k,1,k,1,1,k,k,1).

All products are computed in the exact quadratic field k^2=175/72, with no floating point or restriction to rational sources. Rational functions are canonically reduced by exact polynomial gcd. After reduction every source-coordinate denominator has nonzero constant term.

For a reduced P(r)/Q(r), the entire interval [0,1/100] is certified using

    |P/Q| <= sum_i |P_i|*rmax^i /
             (|Q_0|-sum_(i>=1)|Q_i|*rmax^i),

with a strictly positive denominator bound. Multiplying k-coordinates by the rigorous bound k<2 gives rational upper bounds strictly below one for all sixteen coordinates. They are stored in the receipt. Thus no quartic contact diverges and this is not the earlier unbounded-source counterexample in disguise.

The source products are explicitly factorizable by construction. Projection of their differences through all six transport rows vanishes identically as a rational-function identity. The common transport is nonzero throughout the interval: qx is uniformly nonzero, and the previously proved real zero-transport source theorem excludes a nonzero cubic contact on that locus. Source signs, quartic inputs and source bounds are not selected by a native or UV assumption.

## 3. Data gap and full cut gap

All lower degree-five data and all degree-six transport coefficients are exactly equal. Only the three degree-four leading-Gram coordinates differ. Each difference has an exact factor r^3, with nonzero leading coefficient. The first, rational Gram component dominates even a rigorous bound on the k-valued component throughout the interval, so the actual joint-data max norm is evaluated exactly without approximating k.

In the established seven-response coordinates, exact projection gives

    R(Y)-R(X)=(Delta/4032)*(-3,-3,0,0,5,1,0).

Therefore the full independent-cut polynomial coefficient gap is |Delta|/224. The checker compares this entire response direction, not merely the source values or one forward amplitude. Rational interval bounds certify positive constants b,B,d such that, throughout 0<r<=1/100,

    b*r^3 <= joint_data_gap <= B*r^3,
    cut_coefficient_gap >= d*r.

The exact leading limits are

    joint_data_gap/r^3 ->1000/113,
    cut_coefficient_gap/r ->5/50624.

Hence cut_gap/(data_gap^alpha) diverges for every alpha>1/3. In particular the proposed uniform half-power upper estimate is false on the full conditional unit box. The already proved one-third estimate is attained in power order; no better uniform power can hold on any larger radius-M box containing this family.

This is pairwise uniform regularity, not a claim about a single fixed source's pointwise continuity exponent. Both data and cuts still approach common limits, so bounded-source continuity remains intact. The leading Gram data, although small, still distinguish the pair at every r>0; exact joint-data reconstruction is not contradicted. The two sources are not common-sign partners.

## 4. Verification and remaining boundary

Exact rational-function source products verify all degree-five equalities, all six transport equalities and all seven cut-response differences. Canonical cancellation and whole-interval rational bounds certify source size, vanishing orders and positive gap bounds. Three exact parameter controls supplement these universal identities. Eight tests, scoped SCC and a fresh headless receipt accompany the stored certificate; these are implementation checks, not independent physical evidence or proof-assistant formalization.

The earlier one-half obstruction remains true but was not optimal: it used a fixed leading branch, while this family compares coalescing factorization branches. The one-third theorem is sharp for the full box, not necessarily for quantitatively branch-separated subclasses.

Next test a **normalized degree-five factorization-branch separation condition**: derive an improved conditional cut modulus on that stated sector or construct an exact counterexample despite the separation. Any separation margin is an additional mathematical assumption requiring separate physical licensing. No statement about native preparations, UV source bounds or measured noise is earned. C1–C12, C12's exhausted budget and the high-energy pause are unchanged. See [frontier v3](photon-eft-frontier-v3.md).

```text
python -S research/nima/checkers/check_photon_box_cut_sharpness_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_box_cut_sharpness_v1.py
```
