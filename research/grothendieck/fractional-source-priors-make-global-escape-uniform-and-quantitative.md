# Fractional source priors make global escape uniform and quantitative

## Result

The global two-profile escape law becomes uniform on EVERY positive fractional Sobolev prior ball. No zero trace is required for its half-line application.

Let T_P be the unchanged full finite-place response, retaining all powers of primes p<=P. Put L=log P, and define

    E_P h(u)=J_-h(u+L)+J_+h(u-L),
    J_-h(t)=integral_0^infinity exp(-a/2)h(t-a)da,
    J_+h(t)=integral_0^infinity exp(-a/2)h(t+a)da.

For 0<r<=1 there is the operator estimate

    ||P^(-1/2)T_P h-E_P h||_2
      <= [C K(P)^r+C_r(1+log P)/sqrt(P)] ||h||_H^r(R),

where K(P) is the explicit prime-counting discrepancy functional below and tends to zero. Constants can be chosen independent of P>=2 and h. With a classical quantitative PNT bound, this gives

    <= [C_r exp(-c_r sqrt(log P))
         +C_r(1+log P)/sqrt(P)] ||h||_H^r.

The latter rate uses constants from that PNT theorem; it is not advertised as a numerically calibrated error budget. The discrepancy-functional estimate can instead be used with independently certified prime-counting bounds.

For r>1 use the r=1 result and the continuous inclusion H^r->H^1. For each M, these bounds are uniform on ||h||_H^r<=M.

At r=0 uniform convergence fails even for the BOUNDED first-prime part: its normalized two-profile remainder has operator norm bounded below by a quantity tending to four. Thus the positive-regularity threshold is sharp for this Sobolev scale.

## 1. A quantitative distance for the prime measures

Use the same finite positive measures as the global escape theorem:

    m_P=P^(-1/2) sum_(p<=P) log(p)p^(-1/2) delta_(log(P/p)),
    dm(a)=exp(-a/2)da, a>=0.

Write W(X)=sum_(p<=X) log(p)/sqrt(p), with W(X)=0 for X<2. Except at irrelevant tail endpoints,

    m_P([a,infinity))=P^(-1/2)W(P exp(-a)),
    m([a,infinity))=2exp(-a/2).

Define

    d_P(a)=P^(-1/2)W(P exp(-a))-2exp(-a/2),
    K(P)=|d_P(0)|+integral_0^infinity |d_P(a)| da.

This includes the total-mass discrepancy. It is finite; Chebyshev's bound gives a uniform integrable majorant C exp(-a/2). PNT gives pointwise convergence d_P(a)->0. Dominated convergence therefore proves K(P)->0.

Equivalently, an explicit form useful for estimates is

    K(P)=|W(P)/sqrt(P)-2|
         +(1/sqrt(P)) integral_0^P |W(x)-2sqrt(x)| dx/x.

The integral from zero to two is finite under the stated convention. This formula measures actual first-prime data against the limiting measure, not an invented arithmetic counterterm.

## 2. Operator estimates at regularities zero and one

Let nu_P=m_P-m. For either sign define the convolution error

    B_P^sign h=integral h(.+sign a)dnu_P(a).

Its L2->L2 norm is at most m_P([0,infinity))+2, hence uniformly bounded by Chebyshev. This bound does not tend to zero.

For h in H^1, use the strongly differentiable translation orbit

    h(.+sign a)=h+sign integral_0^a h'(.+sign t)dt.

Bochner integration and Fubini give

    B_P^sign h=d_P(0)h
                 +sign integral_0^infinity d_P(t)h'(.+sign t)dt.

The measures have finite first moments, which justifies this identity absolutely before cancellation. Consequently

    ||B_P^sign h||_2
      <=|d_P(0)| ||h||_2
         +integral |d_P(t)|dt ||h'||_2
      <=K(P)||h||_H^1.

Endpoints of tail intervals do not affect the dt integral. The mass at a=0 is accounted for by the first term.

Interpolating the L2 and H^1 bounds on the Bessel-potential Sobolev scale gives, for 0<r<1,

    ||B_P^sign||_(H^r->L2) <=C^(1-r)K(P)^r.

The endpoint r=1 is already proved. Translations of the OUTPUT are unitary, so summing the two centered errors proves the C K(P)^r bound for the normalized first-prime response minus E_P.

## 3. The complete finite-place response obeys the same estimate

The higher-prime-power response has L2 operator norm O(1+log P), as proved by summing log(p)/(p(1-p^(-1/2))) over p<=P. Its normalized H^r->L2 norm is therefore O((1+log P)/sqrt(P)).

The prescribed archimedean multiplier has at most logarithmic growth. For every r>0,

    A_r=sup_xi |a_infty(xi)|/(1+xi^2)^(r/2)<infinity.

Hence H^r is contained in its multiplier domain and its normalized contribution is at most A_r/sqrt(P). This is precisely where a positive source regularity is needed to control the full unbounded archimedean term uniformly. Combining the three terms proves the stated full-response estimate.

## 4. A quantitative PNT supplies a rate

For sufficiently large x, classical unconditional quantitative PNT and partial summation give constants C,c>0 such that

    |W(x)-2sqrt(x)| <= C sqrt(x) exp(-c sqrt(log x)).

A bounded initial range can be absorbed into the constants. Split the a-integral defining K(P) at (log P)/2. In its first part x=P exp(-a)>=sqrt(P), so

    |d_P(a)| <= C exp(-a/2)
                         exp(-(c/sqrt(2))sqrt(log P)).

In the second part use the Chebyshev majorant. Its integral is O(P^(-1/4)). The mass discrepancy obeys the same PNT estimate. Thus

    K(P)<=C exp(-(c/sqrt(2))sqrt(log P))+C P^(-1/4).

Raising this bound to r proves the displayed stretched-exponential rate, with constants adjusted for bounded P. No explicit numerical values for the classical PNT constants are inferred from asymptotic notation.

## 5. Why the zero-regularity threshold really fails

Consider only the first powers, so the relevant remainder is a bounded Fourier multiplier on ordinary L2. Its normalized prime multiplier is

    b_P(xi)=(2/sqrt(P)) sum_(p<=P) log(p)p^(-1/2)cos(xi log p).

The two-profile multiplier is

    e^(i xi log P)/(1/2+i xi)
      +e^(-i xi log P)/(1/2-i xi).

For each FIXED finite prime cutoff, simultaneous recurrence on the finite torus gives an unbounded sequence xi_j such that exp(i xi_j log p)->1 for every included prime. This follows from simultaneous Diophantine approximation and requires no quantitative recurrence bound.

Along that sequence the profile multiplier tends to zero, while

    b_P(xi_j)->2W(P)/sqrt(P).

Both multipliers are continuous, so the same lower bound holds for their essential supremum, not merely at isolated frequencies. Therefore

    ||P^(-1/2)T_(P,first)-E_P||_(L2->L2)
      >=2W(P)/sqrt(P) ->4.

Thus fixed-source strong convergence cannot be upgraded to uniform convergence on the L2 unit ball. The full response additionally has the unbounded archimedean multiplier, so no full L2 operator-norm assertion is available there in the first place.

This establishes sharpness at r=0 without pretending that a changing high-frequency hostile is a fixed source.

## 6. Half-line priors and zero-extension jumps

For 0<r<1/2, unrestricted zero extension satisfies

    ||E_+ f||_H^r(R) <= C_r ||f||_H^1(R_+).

For example, in the fractional seminorm the interaction across zero is a constant multiple of integral_0^infinity |f(x)|^2 x^(-2r)dx. Near zero the H^1 trace/supremum bound controls this integral exactly when r<1/2; away from zero ordinary L2 controls it. The same-side seminorm is bounded by the H^1 norm through a bounded half-line extension.

Consequently the quantitative theorem applies uniformly on unrestricted-trace D_gamma balls, using ||f||_H^1<=||f||_Dgamma. It does not falsely require E_+f to be globally H^1, and does not exclude actual exponential fibres with nonzero trace. Nima's stronger weighted H^2 even-port priors also bound this norm, so the same estimate applies to their receiver even inputs.

The theorem concerns the raw full response field. It neither reconstructs a forcing from its prepared amplitudes nor alters the source ideal or any retained label.

## 7. Scope of the estimate

The quantity E_P h describes moving leading profiles of the unchanged response. The difference in the theorem is an approximation error, not a newly declared all-prime operator or a new endpoint prescription.

The estimate is in ordinary L2 for normalized finite responses. It does not replace the weighted-dual convergence theorem or the separately calibrated bounded-observer noise certificate. A small global approximation error does not alone give a sharp relative estimate in a small moving window or a weighted remainder estimate.

The finite numerical gate is now closed in `arb-certifies-uniform-escape-on-unrestricted-half-line-prior-balls.md`: Arb encloses the finite discrepancy integrals and explicit operator constants at P=100000. A trace-aware estimate certifies normalized field error below 0.72M on unrestricted half-line H1 prior balls of radius M. For other cutoffs, either enclose K(P) using its explicit discrepancy integral or insert independently certified PNT bounds. The asymptotic PNT rate by itself supplies no Arb-certified tolerance. No numerical sharpness of its constants is claimed.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_fractional_uniform_escape.py`

The checks cover signed-measure tail integration, its mass term, Sobolev interpolation powers, the PNT split exponents, and the critical cross-boundary integral. The infinite uniform operator theorem uses the Bochner, interpolation, and PNT proofs above. The r=0 obstruction uses finite-torus recurrence, not a numerical frequency search.

Input: `research/grothendieck/global-prime-cutoff-escape-has-an-exact-universal-L2-law.md`.
