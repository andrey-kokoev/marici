# Cross-ray half-power recovery within each double-margin branch sector

## Result and exact domain

[Contract](contracts/photon-branchwise-double-margin-v1.json) · [checker](checkers/check_photon_branchwise_double_margin_v1.py) · [tests](checkers/test_photon_branchwise_double_margin_v1.py) · [receipt](results/photon-branchwise-double-margin-v1.json).

The common-leading-ray assumption can be removed **within either fixed factorization-root sign sector**. Two positive normalized readout margins give an explicit uniform half-power cut bound for arbitrary leading rays. All h3 and quartic contacts remain present; no cubic single-minus margin is imposed. One-half is sharp on this stated domain. Comparisons between opposite root signs are not settled here and are not relabeled by convention.

The model is the imported real parity-even eight-leading-contact photon Born domain, retained quadratic two-photon degree-six order and fixed normalized joint13/cut13 max norms. All eighteen finite local matching directions remain free. Every box, margin, branch or noise assumption below is mathematical, not a native/UV/physical license.

For each actual source X=(g,f,p,q,h,K,L,M), write

    r=sqrt(g^2+f^2), s=sqrt(p^2+q^2), c=sqrt(p^2+q^2+h^2),
    d=g*q-10*f*p.

Fix a box radius Mbox>=1, 0<sigma<=1/2, 0<eta<=1 and one label epsilon=+1 or -1. Require each compared source to satisfy

    |all eight contacts|<=Mbox,
    d^2>=sigma^2*r^2*s^2, epsilon*d>=0,
    (6*g+f)^2>=eta^2*r^2.

These homogeneous inequalities include zero leading and zero (p,q) pairs without evaluating 0/0. For nonzero pairs they are the normalized discriminant and leading-trace margins. Nonzero leading rays with cancelled trace are excluded, even if h happens to vanish. The label is weak at d=0, which is possible only in the admitted zero strata. Stronger supplied margins may use these weaker capped values. There is no common-ray condition, and the trace signs need not agree.

## 1. Computable all-gap bound

Let delta be the complete joint-data max-norm gap. Set c0=49/7680 and k0=3821/36 from the [positive radius](photon-common-ray-modulus-v1.md). Define the following deliberately conservative rational constants:

    L=1+50/sigma, e=2*L, u=e+1, R=(14+u)/eta,
    a=c0*eta^2/37, b=eta^(-2),
    T=2/eta^2+74/eta^4, D=2+37*T,
    F1=4*k0*e*(1+R)*(R^2+1)/a,
    F2=28*k0*b*u*(1+R)*(R^2+1)/a^2,
    N=8*e*(400/a+D/a^2),
    S=1+(2+e)^2,
    A=13/3+max(k0/a,S)/224,
    B=max((F1+F2+N)/224,229/4200).

Then

    cut gap <=min((2713/3360)*Mbox^2,
                  A*delta+B*Mbox*sqrt(delta)).

For delta<=1 this is a Holder-1/2 estimate with coefficient A+B*Mbox. The constants are large but explicit and computable, not fitted or claimed optimal. The implementation encloses square roots rationally. For a nonempty compatibility set within one licensed mathematical sign sector and deterministic tolerance tau, its cut diameter is at most this bound evaluated at 2*tau. This is not a probability guarantee or an algorithm proving compatibility.

## 2. Stable recovery of the rank-one bilinear matrix

The lower data are u5=g*p, v5=f*q, w5=g*q+10*f*p, z5=h*(6*g+f). They satisfy

    w5^2-40*u5*v5=d^2.

Within the same weak root-sign sector, the difference of signed roots is bounded by 50*delta/sigma. Indeed |w5|<=10*r*s and |u5|,|v5|<=r*s, so the squared-discriminant gap is at most 50*(r*s+r'*s')*delta, while the sum of absolute roots is at least sigma*(r*s+r'*s'). If both products vanish, the corresponding bilinear matrices are zero and need no division.

Recover the four entries of

    V= [[g*p,g*q],[f*p,f*q]]

using g*q=(w5+d)/2 and f*p=(w5-d)/20. Their max-norm gap is at most L*delta; the Frobenius gap is at most e*delta. The five-coordinate auxiliary data U=(entries of V,z5) have Euclidean gap at most u*delta. This inversion is precisely where the common sign sector is used. It is not valid across opposite signs merely because both absolute margins are positive.

For nonzero leading pairs align their unit directions n,n' by a simultaneous entire-source sign reversal, leaving all data, margins and labels unchanged. Rank-one projection then gives

    ||n-n'|| <=2*||V-V'||_F/max(r*s,r'*s').

The radius weights, positive metric and leading-trace square have uniform direction gains 400, 2 and 74 respectively. These follow from the exact displayed coefficients, not from sampled directions.

## 3. Auxiliary ratio for the varying-radius comparison

Let P(n) be the positive cubic metric, W(n) the radius row, and C(n)=6*n_g+n_f. For auxiliary data U=(V,z5), put

    J_n(B)=W(n) dot B,
    A_U=||first column of V||_2^2,
    Q_n(U)=sum_(two rows v of V) v^T*P_pair(n)*v
              +P_hh(n)*z5^2/C(n)^2,
    F(n;B,U)=J_n(B)*A_U/Q_n(U).

At the source's actual direction, F equals p^2. At another direction it is only an algebraic comparison quantity; J_n(B) can be negative and is never assumed to be a realizable source radius. The denominator is positive on nonzero auxiliary data. This avoids the invalid step of taking a square root of an off-ray radius.

For any actual source Y and either admissible comparison direction n,

    Q_n(U_Y)>=a*r_Y^2*c_Y^2,
    ||Q_n||<=b,
    |Q_n(U_Y)-Q_n'(U_Y)|<=D*r_Y^2*c_Y^2*||n-n'||.

Here the scalar coefficient P_hh/C^2 has direction gain at most T. Its denominator uses only the leading-trace margin, not a cubic-trace margin. The projected transport rows also give the universal source estimate

    ||B_Y||<=c_Y^2+r_Y*Mbox,

because their cubic and quartic row gains are at most 1/16 and 9/10. These estimates explicitly account for direction-dependent radius weights and arbitrary quartic interference.

## 4. Quantitative near/far and small/large pair proof

For delta>0 let rho=sqrt(delta), and let r=max(r_X,r_Y).

**Near leading:** if r<=2*rho, the general surrogate-bias estimate gives cut gap<=(13/3)*delta+(229/4200)*Mbox*rho. This includes zero leading sources.

**Far leading:** if r>2*rho, both leading magnitudes exceed r/2 because their squared norms differ by at most 2*delta.

If min(s_X,s_Y)<=rho, the stable bilinear-matrix estimate gives the other pair norm at most (2+e)*rho. Therefore |p_X^2-p_Y^2|<=S*delta, including zero cubic-pair strata, and the cut gap is at most (13/3+S/224)*delta.

It remains that both pair norms exceed rho. The full cubic norms are then nonzero. Since

    eta*r_i*c_i<=||U_i||<=7*r_i*c_i,

the auxiliary data estimate gives c_Y/c_X<=R and c_X/c_Y<=R. Compare F first at fixed n_X with changing data, then at fixed Y data with changing direction. This is a comparison identity, not interpolation through unrealizable source states.

For the fixed-direction step, |J_n(B_X)-J_n(B_Y)|<=k0*delta. The elementary fraction difference

    |A_X/Q_X-A_Y/Q_Y|
      <=|A_X-A_Y|/Q_X+(A_Y/Q_Y)*|Q_X-Q_Y|/Q_X

uses |A_X-A_Y|<=r*(c_X+c_Y)*e*delta, |Q_X-Q_Y|<=7*b*r*(c_X+c_Y)*u*delta, Q_X>=a*r^2*c_X^2/4, A_Y/Q_Y<=s_Y^2/(a*c_Y^2), and |J_n(B_Y)|<=k0*(c_Y^2+r*Mbox). Substitution yields

    fixed-direction p^2 gap <=k0*delta/a+(F1+F2)*Mbox*rho.

For the direction step, the radius-row gain 400 and denominator gain D give

    direction p^2 gap
      <=(400/a+D/a^2)*[s_Y^2+r*Mbox*s_Y^2/c_Y^2]*||n_X-n_Y||
      <=N*Mbox*rho.

The last inequality uses the rank-one direction bound, r_i>r/2 and s_Y>rho. It does not replace a varying radius by a fixed one or suppress a small-pair singularity; the small-pair case was handled separately.

Finally the exact augmented cut inverse has fixed-M3 data gain 13/3 and missing-coordinate contribution |Delta p^2|/224. Combining these cases gives the displayed A,B bound. At delta=0 the established exact joint-data reconstruction supplies zero cut gap. This real-inequality proof is documented mathematics with exact rational coefficient certificates, not proof-assistant formalization.

## 5. Sharpness, controls and remaining cross-sign question

The bounded axis family already has both margins (discriminant>=23/37 and leading trace=6) and gives data gap of order r^2 with cut gap of order r. It lies in the negative root-sign sector. Negating all three cubic contacts in both members, leaving leading and quartic contacts unchanged, constructs an actual positive-sector pair with the same gap orders and margins. Thus no exponent greater than one-half can hold uniformly in either sector for the stated sigma<=1/2,eta<=1 range. This is a constructed comparison, not a physical identification of source signs.

Exact controls include both sign sectors, multiple leading rays, an explicit fractional cross-ray pair with nonzero h3/all quartics, a nonzero-h3 cubic-trace-zero comparison, homogeneous zero strata, and six bounded sharpness pairs. Eight tests, scoped SCC and a fresh headless receipt accompany them. Each pair also checks the signed-root gap, bilinear/Frobenius data gains, rank-one projection inequality, off-ray denominator coercivity and the actual-source p^2 ratio identity, rather than only the coarse diameter cap. Coefficient-gain certificates are independent of the numerical controls; no fresh full-suite or native physical-evidence claim is made.

The result removes the common-ray assumption but **not** the shared factorization-label assumption. Opposite-sign pairs satisfying the same absolute margins are deliberately rejected by this sector checker. Their comparison remains a separate live constructor; they must not be assigned a common sign based on noisy data or convention. An unlabeled compatibility set may still require the full-box one-third bound across components until that cross-sign case is resolved.

All eighteen finite local matching coefficients remain free. Source box, margins, branch/noise licensing, physical preparation/matching, native dynamics and UV inputs are unearned. C1–C12, C12's zero/not-renewed budget and the high-energy pause are unchanged. See [frontier v4](photon-eft-frontier-v4.md).

```text
python -S research/nima/checkers/check_photon_branchwise_double_margin_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_branchwise_double_margin_v1.py
```
