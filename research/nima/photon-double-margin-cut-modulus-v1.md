# Sharp half-power cut recovery on the unlabelled double-margin sector

## Result and scope

[Contract](contracts/photon-double-margin-cut-modulus-v1.json) · [checker](checkers/check_photon_double_margin_cut_modulus_v1.py) · [tests](checkers/test_photon_double_margin_cut_modulus_v1.py) · [receipt](results/photon-double-margin-cut-modulus-v1.json).

The shared factorization-label condition is removed. **Both signs, opposite-sign comparisons and arbitrary leading rays** satisfy a uniform half-power cut bound under the two stated normalized margins and a conditional finite source box. One-half is sharp on the stated margin range. Independent h3, all quartics, zero strata and all eighteen free finite local matching directions are retained. No cubic single-minus margin or physical branch selection is used.

This resolves the sole admitted bounded mathematical question in [frontier v4](photon-eft-frontier-v4.md), not the physical programme. The imported real parity-even eight-leading-contact Born model, fixed joint13/cut13 coefficient norms and retained quadratic two-photon degree-six order remain the scope. Physical source/noise/margin licensing, measured matching, native dynamics, full physical IR inventory and UV inputs remain unearned. C1–C12, C12's exhausted/not-renewed budget and the high-energy pause do not change.

## 1. Full source class and explicit modulus

For X=(g,f,p,q,h,K,L,M), set r^2=g^2+f^2, s^2=p^2+q^2 and d=g*q-10*f*p. Fix Mbox>=1, 0<sigma<=1/2 and 0<eta<=1. Require only

    |all eight contacts|<=Mbox,
    d^2>=sigma^2*r^2*s^2,
    (6*g+f)^2>=eta^2*r^2.

There is no sign condition. The homogeneous inequalities include zero leading and zero (p,q) pairs without 0/0 conventions or discarded h3. Nonzero leading pairs must satisfy the leading-trace margin even when a cubic mode vanishes. Any stronger supplied positive margin can be weakened to these capped values; sharpness is asserted for the displayed range, not every stronger sub-sector.

Let delta be the complete joint-data gap. Use the explicit rational constants from the [branchwise theorem](photon-branchwise-double-margin-v1.md):

    c0=49/7680, k0=3821/36,
    L=1+50/sigma, e=2*L, u=e+1, R=(14+u)/eta,
    a=c0*eta^2/37, b=eta^(-2),
    T=2/eta^2+74/eta^4, D=2+37*T,
    F1=4*k0*e*(1+R)*(R^2+1)/a,
    F2=28*k0*b*u*(1+R)*(R^2+1)/a^2,
    N=8*e*(400/a+D/a^2), S=1+(2+e)^2,
    A=13/3+max(k0/a,S)/224,
    B=max((F1+F2+N)/224,229/4200).

Then, **without a branch prior**,

    cut gap <=omega(delta)
      :=min((2713/3360)*Mbox^2, A*delta+B*Mbox*sqrt(delta)).

For delta<=1 this is Holder-1/2 with coefficient A+B*Mbox. The constants are deliberately conservative, not optimized or experimentally calibrated. The checker computes rational upper enclosures of square roots. For any nonempty compatibility set satisfying the box and both margins, including candidates on both root signs, deterministic tolerance tau gives cut diameter at most omega(2*tau). No actual physical noise budget or compatibility-set nonemptiness is supplied by this result.

## 2. New opposite-root lemma

For opposite discriminants, a sharper separate bound holds:

    cut gap <=min(diameter,
                  (439/84)*delta+[229/(70*sigma)]*Mbox*sqrt(delta)).

This lemma needs the discriminant margin and box, but **does not need the leading-trace margin**. That does not remove the latter from the full theorem: the known same-sign cancelled-trace family still obstructs a discriminant-only full-sector half-power estimate.

### Leading Gram controls projective direction

For nonzero leading vectors write them r_X*n and r_Y*m. Entire-source sign reversal aligns n dot m>=0 without changing data, discriminants, cuts or box membership. Put r=max(r_X,r_Y). The measured leading Gram entries give

    |r_X^2-r_Y^2|<=2*delta,
    ||G_X-G_Y||_F<=2*delta,
    ||n-m||<=4*delta/r^2.

For the last inequality project the larger rank-one Gram matrix orthogonally to the other's direction: r^2*sin(angle)<=||G_X-G_Y||_F. Aligned unit-vector distance is at most twice that sine. This is a statement about projective source directions, not a selection of a physical source sign.

### Opposite roots cannot remain large far from the leading origin

Let a=r_X*(p_X,q_X), b=r_Y*(p_Y,q_Y). The three lower degree-five products satisfy

    T5=A_n*a,  A_n=[[n_g,0],[0,n_f],[10*n_f,n_g]].

The smallest singular value of A_n is at least 1/15 and its direction gain is at most 11. Thus

    ||a-b||<=30*delta+165*||n-m||*||b||.

The discriminant is the functional ell_n(a)=n_g*a_q-10*n_f*a_p, with norm at most 10 and direction gain at most 10. If the roots have opposite signs, the margins imply

    sigma*(||a||+||b||)
      <=|d_X-d_Y|
      <=300*delta+1660*||n-m||*||b||.

This does not treat a root swap as a Lipschitz signed-root inversion. It instead uses the measured leading directions.

If r>120*sqrt(delta)/sigma, both leading magnitudes exceed r/2 and

    ||n-m||<=4*delta/r^2<=sigma/3320.

The displayed inequality then gives ||a||+||b||<=600*delta/sigma, hence

    s_X,s_Y<=1200*delta/(sigma*r)<=10*sqrt(delta),
    |p_X^2-p_Y^2|<=200*delta.

The exact augmented cut inverse has fixed-missing-coordinate gain 13/3 and missing-coordinate contribution |Delta p^2|/224. The far-leading cut gap is therefore at most (439/84)*delta.

If instead r<=120*sqrt(delta)/sigma, the existing general surrogate-bias bound applies directly:

    cut gap<=(13/3)*delta+(229/8400)*Mbox*r
            <=(13/3)*delta+[229/(70*sigma)]*Mbox*sqrt(delta).

This includes zero leading points and retains all h3/quartic effects. At delta=0 exact joint-data reconstruction supplies zero cut gap. No division by a zero cubic pair or zero leading vector is performed.

## 3. Joining signs without assuming a sign

When d_X*d_Y>=0, the sources belong to some common weak sign sector, including its homogeneous zero boundary; the established branchwise theorem applies. When d_X*d_Y<0, the new lemma applies. This is exhaustive mathematical case analysis, not a prior restricting possible physical roots.

The same A,B already dominate the new opposite-root constants. Indeed e>=202 and S>200 imply A>=439/84. Also k0>2, a<1, R>=0 and e>=100/sigma imply

    B>=F1/224>=800/(224*sigma)
      =25/(7*sigma)>229/(70*sigma).

Consequently one and the same modulus controls the entire unlabelled source class. Neither freezing a direction-dependent radius nor taking a square root of an off-ray possibly negative radius is used in the new step.

## 4. Sharpness and controls

The inherited bounded axis family has discriminant margin at least 23/37, leading trace margin six, data gap of order v^2 and cut gap of order v. It is in this unlabelled class for every displayed sigma,eta. The cubic-reflected family supplies the other sign as well. Thus no uniform exponent above one-half is possible; the argument does not claim the opposite-root lemma alone has an optimal exponent or optimal constants.

Exact controls sample both same-sign and opposite-sign comparisons without a label argument, include zero strata, and accept a nonzero-h3/all-quartics cross-ray pair excluded by the earlier label gate. Three small-scale opposite-root pairs explicitly exercise the **far** regime and its small-cubic-pair consequence, not merely the coarse diameter cap. A cancelled-leading-trace opposite-root control demonstrates the standalone lemma's scope; the full theorem still rejects that control because its leading-trace margin fails. The inherited cubic-trace-zero and six sharpness controls remain present.

Eight tests, scoped SCC, a fresh headless receipt and unchanged net/coverage/planner checks are implementation controls. The real norm and spectral argument above is documented mathematics with exact rational coefficient certificates, not proof-assistant formalization or a fresh full-suite/physical-evidence claim.

## 5. Bounded frontier disposition

The opposite-sign constructor closes the admitted double-margin question. There is no remaining branch, common-ray or h3 restriction to remove from this theorem beyond its stated model/order, box and two margins. Removing the discriminant-only obstruction's leading-trace cancellation by fiat would still be false; source/noise/margin licensing and native/UV/matching data are not outputs of an inverse-modulus proof.

No additional mathematical card, C12 budget, scored conjecture, task/tree claim, commit or push is admitted by this completion. The registered planner's null recommendation is not programme completion. Further physical application requires concrete licensed source-box, margin, normalization/noise and native matching input objects; those are not currently supplied. Hold at the requested scoped theorem rather than inventing another mathematical queue or promoting it to physics.

```text
python -S research/nima/checkers/check_photon_double_margin_cut_modulus_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_double_margin_cut_modulus_v1.py
```
