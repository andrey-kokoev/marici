# A positive factorization margin alone does not improve the cut exponent

## Result and scope

[Contract](contracts/photon-margin-only-obstruction-v1.json) · [checker](checkers/check_photon_margin_only_obstruction_v1.py) · [tests](checkers/test_photon_margin_only_obstruction_v1.py) · [receipt](results/photon-margin-only-obstruction-v1.json).

Even with normalized degree-five discriminant margin **at least two**, an exact unit-box source pair family excludes every uniform cut-reconstruction exponent above one-third. Both sources have the same factorization-branch sign, identical full degree-five data and nonzero degree-six transport, and uniformly bounded contacts. The obstruction uses nonzero h3 on the allowed leading single-minus cancellation locus 6*g2+f2=0, not coalescing factorization roots.

Together with the full-box upper estimate, one-third remains sharp on this stated positive-margin sector (and sectors with a weaker threshold). This does not classify all larger thresholds or the sector with an additional positive leading-trace margin. Nor does it contradict the [exact f2=0 half-power theorem](photon-axis-cut-modulus-v1.md): the new family is not on that face for any positive parameter.

The domain remains the imported real parity-even eight-contact photon Born model at retained quadratic two-photon degree-six order, with fixed normalized joint13/cut13 max norms. No UV assumptions are silently added to exclude the cancellation locus. Source box, margins, physical preparation/matching, native dynamics, full physical IR inventory and all eighteen finite local matching coefficients remain unearned or free as before.

## 1. Explicit actual real algebraic source family

Let theta be the unique root in (4,9/2) of

    588553*theta^2-475440*theta-9509250=0.

Define

    H=1065/3962+(75/1132)*theta^2,
    Kc=-5/12+(7/30)*H,
    Mc=-5/32-(7/192)*theta^2+(7/16)*H,
    P=1/10, s=1+r, T=-P^2*(2+r)/(1+r),

where 0<r<=1/100. The two sources, in the fixed order (g2,f2,g3,f3,h3,g4,g4prime,f4), are

    X=(r,-6*r,s*P,s*theta*P,P*sqrt(H),0,0,0),
    Y=(s*r,-6*s*r,P,theta*P,s*P*sqrt(H),Kc*T,(H/2)*T,-(Mc/6)*T).

H is positive and below two on the isolating interval, so the indicated positive radical is real. The independent single-minus contact is nonzero for both sources; it is not erased or fitted away. The quartic contacts in Y are explicit nuisance coordinates, not an assumption that those operators are absent. The zero quartics in X specify one member of the witness, not a restriction on the entire source model.

All sixteen contacts remain strictly inside the unit box over the entire interval. The checker uses rational bounds theta<5, sqrt(H)<2, |T|<=2*P^2, and explicit coefficient bounds on Kc,Mc. The resulting rational coordinate majorants are stored in the receipt. No contact diverges and no common physical EFT window is inferred merely from this coefficient construction.

## 2. Exact source factorization and equal transport

Put D=P^2*(1-s^2). Direct factorization gives the twelve-monomial difference Y-products minus X-products as D times

    (Kc, H/2, -Mc/6, -6*Kc, -3*H, Mc,
     1, theta, 0, theta^2, 0, -H).

The g3*h3 and f3*h3 differences vanish exactly: one source scales its (g3,f3) pair by s while the other scales h3 by s. The h3-square difference has the opposite sign to the g3-square difference. This is a difference of two actual sources, not a free monomial vector passed off as one source.

The critical polynomial for theta makes every one of the six transport rows annihilate this difference. Exact coefficient arithmetic in Q(r)[theta] with theta^2=(475440/588553)*theta+9509250/588553 verifies all twelve product identities and all transport equalities. The extra radical sqrt(H) is tracked independently, with its square reduced to H; no floating-point radical or numerical slope fit is used.

The common transport is nonzero. Its H6 component is

    P^2*s*(10+theta)*sqrt(H)/320 >0.

The cubic single-minus trace 10*g3+f3 is nonzero, so this is not a double-cancellation example. The specific failure is in the leading trace that controls the lower single-minus data.

## 3. Uniformly positive discriminant margin, same branch sign

Both sources have f2=-6*g2 and f3=theta*g3. Their normalized degree-five discriminant margin is therefore the same constant

    sigma=(theta+60)/(sqrt(37)*sqrt(1+theta^2)) >2.

For a rational interval certificate, sigma^2>4 is equivalent to

    -147*theta^2+120*theta+3452>0.

This concave polynomial is positive at both endpoints of [4,5], which contains the isolating interval. The unnormalized discriminant root g2*f3-10*f2*g3 is r*s*P*(theta+60)>0 for both sources. Thus even selecting the same sign of the factorization branch does not remove this witness.

The normalized leading single-minus trace |6*g2+f2|/sqrt(g2^2+f2^2) is exactly zero. Both leading and cubic pairs are nonzero for every r>0, so there is no undefined-margin or omitted-zero-stratum loophole. Adding or excluding zero strata does not eliminate this nonzero-pair obstruction. No conclusion is asserted for thresholds stronger than the proved positive-margin sector or for an additionally separated leading trace.

## 4. Data and cut orders

The complete degree-five coordinates agree:

    g2*g3=r*s*P,
    f2*f3=-6*r*s*theta*P,
    g2*f3+10*f2*g3=r*s*P*(theta-60),
    h3*(6*g2+f2)=0.

All six degree-six transport coordinates agree by section 2. The degree-four Gram difference is

    r^2*(s^2-1)*(1,36,-6).

Its middle coordinate dominates the actual max norm, giving the exact joint-data gap

    delta(r)=36*r^3*(2+r),  delta(r)/r^3 ->72.

The complete seven-coordinate cut difference, and independently the full thirteen polynomial coefficients, are D/4032 times the known transport-null direction (-3,-3,0,0,5,1,0). Hence

    cut_gap(r)=P^2*r*(2+r)/224,
    cut_gap(r)/r ->1/11200.

For every alpha>1/3, cut_gap/delta^alpha diverges as r->0. This rules out the proposed general-margin half-power estimate on the stated sector and establishes the sharp one-third power there. Both data and cuts still converge to common limits, consistent with bounded-source continuity and exact joint-data recovery.

## 5. Disposition and next test

The exact field-product, lower-data, transport and full-cut identities supply the universal algebraic certificate; rational interval inequalities certify reality, source size and margin. Three exact parameter controls and eight tests accompany scoped SCC and a fresh headless receipt. These are implementation controls, not proof-assistant formalization or independent physical evidence.

The normalized discriminant margin alone was insufficient because it did not separate the independent h3 readout cancellation. The axis theorem avoided this cancellation through its extra structural prior. Neither theorem licenses setting a small f2 or h3 to zero, choosing a physical branch, or imposing a native source margin.

Next test simultaneous positive normalized margins on the factorization discriminant and the leading trace 6*g2+f2, with explicit zero-stratum conventions and all cubic/quartic contacts retained. Establish a quantitative rate or a bounded actual-source obstruction on that double-margin sector. Physical priors, matching, native/UV inputs, C1–C12 dispositions and C12's exhausted budget remain unchanged. See [frontier v4](photon-eft-frontier-v4.md).

```text
python -S research/nima/checkers/check_photon_margin_only_obstruction_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_margin_only_obstruction_v1.py
```
