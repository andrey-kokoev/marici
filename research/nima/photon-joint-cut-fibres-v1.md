# Real source fibres of joint degree-four/five photon cuts

## Question and result

Does the joint coherent cut data identify the five real leading Born couplings, after respecting source factorization rather than treating six monomials as independent physical inputs?

[Contract](contracts/photon-joint-cut-fibres-v1.json) · [checker](checkers/check_photon_joint_cut_fibres_v1.py) · [tests](checkers/test_photon_joint_cut_fibres_v1.py) · [receipt](results/photon-joint-cut-fibres-v1.json).

**Complete scoped classification:** away from cancellation and a zero leading pair, each realizable datum has exactly two sources related by overall sign. On the nonzero-leading cancellation stratum, h3 is a free real parameter. With zero leading pair, all three degree-three couplings are unseen. An exact inverse on the ordinary stratum need not be uniformly well conditioned near its boundary.

This is identifiability in the declared real imported contact-EFT model and fixed coherent amplitude frames, not measured matching, a selected physical sign, UV positivity or native dynamics. Generic uniqueness below means uniqueness **modulo a data-invisible sign**, not a physical identification of the two Born interactions.

## 1. Data coordinates really come from the cut

Write source (g,f,p,q,h)=(g2,f2,g3,f3,h3). Fixed rational calibrations of the independently checked degree-four beta coefficients and degree-five helicity polynomials give

    J(g,f,p,q,h)=(g^2,f^2,g*f,g*p,f*q,g*q+10*f*p,h*(6*g+f)).

For example the degree-four coordinates are -80*B13, 240*B12 and -(48/5)*B2, with B=pi^2*beta. Degree-five coordinates are -48 times the forward mixed cut, -240 times the alpha^2 coefficient of D, 96 times O, and 480 times the alpha coefficient of Phi5. The checker compares these calibrations against the independent cut constructor on 243 sources. These are formal observable coordinates, not supplied experimental numbers.

Set data (a,b,c,u,v,w,t)=J(source). The common sign reversal of all five source couplings leaves J unchanged.

## 2. Necessary and sufficient real image conditions

First require

    a>=0, b>=0, a*b=c^2.

These are the rank-one PSD conditions of the leading **data Gram**, not a physical sign condition on g or a UV bound on f/g.

- If a>0, require a*v-c*w+10*b*u=0. If 6*a+c=0, also require t=0.
- If a=0,b>0, then c=0 already and require u=0.
- If a=b=0, require u=v=w=t=0 (and c=0 already).

There are no additional image conditions. The charts below explicitly construct all sources, proving sufficiency as well as necessity. Invalid data must be rejected, not forced into a fitted inverse.

## 3. All source fibres, with valid chart domains

For a>0 put r=sqrt(a)>0. The leading pair is either (r,c/r) or its negative: the Gram data allow no other pair. Fix the positive-g chart only as a mathematical orientation. Its remaining coefficients are forced to be

    p=u/r,
    q=w/r-10*c*u/r^3.

The image condition above is exactly the requirement f*q=v.

If 6*a+c!=0, then

    h=t*r/(6*a+c).

This is a single source on the oriented chart; simultaneous negation gives the other, and no other real source is possible. Equivalently 6*g+f!=0.

If 6*a+c=0, nonzero leading data force f=-6*g and t=0. Now **h is arbitrary**, not zero. The fibre consists of two affine lines exchanged by the common sign; modulo that sign one real parameter remains.

For a=0,b>0 use a separate positive-f chart, r=sqrt(b):

    g=0, f=r, p=w/(10*r), q=v/r, h=t/r.

It is again unique up to the simultaneous sign. A universal formula dividing by g would incorrectly omit this ordinary stratum.

For a=b=0 the unique datum is J=0 and the whole fibre is

    (g,f,p,q,h)=(0,0,p,q,h),    (p,q,h) in R^3.

The sign acts antipodally on this R3, with a fixed origin. It is not a two-sheet covering there. The zero-leading fibre is three-dimensional before the discrete quotient, even at points where its Jacobian has much larger nullspace.

These cases exhaust all real sources: the leading Gram determines its two possible nonzero lifts, linear equations then determine p,q, and the remaining equation either fixes h or vanishes. No unadmitted g>0 physical condition is used to select a sheet.

## 4. Exact implementation without spurious rational-root restrictions

For rational data the code stores a source as sqrt(d) times five rational coefficients, with free real chart parameters on exceptional strata. This is an exact algebraic description, not a requirement that the reconstructed source be rational. Homogeneity gives J(sqrt(d)*x)=d*J(x), so verification needs no approximate square roots or restricted radical library. The nonsquare d=7 control is retained explicitly. The same chart formulas and proof apply to real data; exact executable controls exercise rational/algebraic instances, not a machine-formalized theorem over all reals.

The checker covers 3000 ordinary rational sources, 54 cancellation sources and 125 zero-leading sources, with exact recovery of each source on its appropriate chart. It also rejects independent Gram, factorization and exceptional-response violations.

## 5. Nontrivial invisible sources and singular linearization

The sources

    (1,-6,2,3,0), (1,-6,2,3,7)

have identical complete J data and are not related by sign, but their Born single-minus amplitudes differ by 1008/625 at the existing exact angular control. Likewise (0,0,1,2,3) and (0,0,4,5,6) have identical zero data despite different degree-three Born tensors.

Jacobian ranks on representative strata are 5 (ordinary), 4 (nonzero cancellation), 2 (zero leading with nonzero g3), 1 (pure h3 with zero leading), and 0 (origin). At the origin a first-order variation of g lies in the Jacobian kernel but produces nonzero g^2 data at second order. Rank-nullity is therefore not a substitute for the actual singular-fibre calculation.

Even ordinary exact inversion is not uniformly stable near cancellation. Keep g=1,f=-6+epsilon,p=2,q=3 and compare h=0 with h=1. Both sources are ordinary for epsilon!=0. Their source separation is one but the maximum data separation is |epsilon|. The required inverse error-amplification factor is at least 1/|epsilon|. Exact epsilon=1/10,1/100,1/1000 controls certify this failure of a uniform inverse; uniqueness is not a noise-robust physical matching claim.

## Boundary and next constructor

The joint-cut fibre question is resolved within this five-leading-coupling model. The six-monomial linear kernel and the twelve-coefficient local forward kernel remain different constructions. Higher matching coefficients, actual measurements/preparations, native licensing and UV hypotheses remain unearned; no C1–C12 disposition or budget changes.

To test whether additional cut order resolves the blind directions, next compute the **complete degree-six quadratic two-photon cut** with independent leading degree-four g4,g4prime,f4. It requires both degree-two-by-degree-four interference and the degree-three Born square, including h3. The isolated square is not the full degree-six cut when leading degree-four contacts are allowed; do not claim identifiability by silently setting those unknown coefficients to zero.

```text
python -S research/nima/checkers/check_photon_joint_cut_fibres_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_joint_cut_fibres_v1.py
```
