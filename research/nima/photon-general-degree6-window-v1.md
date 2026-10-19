# Generic degree-six photon logarithmic/window tensor

## Question and result

Can every retained degree-six cut coordinate be lifted regularly, with its full local scale transport and analytic window difference rather than a forward fit?

[Contract](contracts/photon-general-degree6-window-v1.json) · [checker](checkers/check_photon_general_degree6_window_v1.py) · [tests](checkers/test_photon_general_degree6_window_v1.py) · [receipt](results/photon-general-degree6-window-v1.json).

**Result:** twelve quadratic source coordinates, including both Born2-by-Born4 and the cubic square, admit explicit regular crossed channel tensors. Their common-log transport has rank six in the [new six-generator local block](photon-local-degree6-v1.md), while their full cut has rank seven. Scale transport consequently loses a linear cut direction. This is a statement about bookkeeping coordinates, not yet a different-physical-source/same-running witness. All eighteen finite local matching coefficients remain free.

The generic log/window construction, identity derivations and convergent generated difference are scoped to the imported real parity-even on-shell photon contact ansatz and quadratic two-photon order. They do not provide native dynamics, physical preparation, measured matching, full IR inventory or UV bounds. They are not proof-assistant formalizations.

## 1. Explicit regular crossed lift

Use the [complete degree-six cut](photon-general-degree6-cut-v1.md), in source order

    (g2*g4,g2*g4prime,g2*f4,f2*g4,f2*g4prime,f2*f4,
     g3^2,g3*f3,g3*h3,f3^2,f3*h3,h3^2).

Resolve its diagonal sections as D0*P0+D2*P2 and O0*P0+O2*P2, and its mixed section as M2*d22^2+M3*d22^3. These coefficient vectors are exactly extracted from the independently projected Bose matrices, not fitted coupling values. Set

    A=-(D0+D2), B=6*D2,
    C=-(M2+M3), D=-6*M3,
    AO=-(O0+O2), BO=6*O2,
    H=(10*g3*h3+f3*h3)/960.

The last expression is a linear form in the declared monomials. For each mixed pair I use its old regular field-strength product P_I, same-pair invariant x and crossed product w. Put P_I*(A*x^4+B*x^2*w) in its own channel. For each of its four crossed label pairs with invariant y put

    (P_I/2)*[C*y^4+D*y^3*(-x-y)]

in that crossed channel. Summing the six mixed subsets is Bose/parity covariant. The factor one-half accounts for the two label pairs in each crossed channel, not a fitted normalization.

In each of the three same-pair channels add the regular forms

    AO*(F2*x^4/2+F3*x^3)+BO*F3*x^3+H*H3*x^3.

Here F2,F3,H3 are the inherited covariants, not scalar helicity phases. The all-same projection equals chi*(AO*x^6+BO*x^4*tu), using x^3=(S2/2)*x+S3. The global F2/F3 representative also ensures exact local transport on arbitrary polarization components, not just transverse-helicity evaluations. There are no kinematic denominators; every summand contains one field strength per leg. Ward identities and Bose/Lorentz/parity covariance follow algebraically and are supplemented by exact controls.

Call the resulting channel tensors C_s,C_t,C_u. With ell_x=Log(-rho*x) and rho=mu^(-2),

    pi^2*M6_log = sum_x C_x*ell_x.

Its right-cut normalization is pi*Im M6_log=-C_s. All five physical helicity sections match the independently projected cut at four CM configurations, and an independent spinor oracle checks all sixteen sectors. The two archived R-family sectors restrict with their unchanged source weights and normalization. No inactive Born waves, h3 square or unknown quartic inputs were removed.

## 2. Full local transport and the additional scale kernel

Define T=sum_x C_x. Direct invariant identities give

    T=(A+C)*G6+(B-4*C+D)*G6prime+(2*C-2*D)*G6doubleprime
      +(AO/4)*F6+3*(AO+BO)*F6prime+3*H*H6.

For the mixed sector use y^4+z^4=x^4-4*x^2*w+2*w^2 and y^3*z+z^3*y=x^2*w-2*w^2. For the same sector use sum x^4=S2^2/2 and sum x^3=3*S3. The checker verifies the entire tensor identity on all 256 matrix-unit polarization tuples.

Under log(rho)->log(rho)+delta the loop tensor changes by delta*T/pi^2. In particular its H6 common-log coefficient is

    +h3*(10*g3+f3)/320.

Equivalently d/dlog(mu) of the loop coefficient is -h3*(10*g3+f3)/160, divided by pi^2. A fixed total amplitude needs the opposite local compensation; no finite integration constant or actual h6 is selected. Conventions distinguish log(rho) transport from log(mu) running.

The twelve-to-six transport matrix has rank six, whereas the twelve-to-angular-cut matrix has rank seven. Their kernels have dimensions six and five. Every cut-kernel vector annihilates each channel tensor, but an explicit transport-kernel vector in the receipt has nonzero cut and nonzero channels despite sum C_x=0. Thus a nonlocal logarithmic ratio may remain when common-log transport vanishes in this linear coordinate space.

This extra vector is **not automatically a realizable real Born source**: the twelve monomials obey eight-coupling factorization constraints. Nor is either kernel the ten-dimensional forward kernel of eighteen local matching coefficients. No Born-source equivalence or physical identifiability is inferred from these linear kernels.

## 3. Whole-window representative and generated analytic difference

For 0<tau<1 choose the minimal forward-visible polynomial extension J_tau, leaving invisible additions as representative freedom. Its nonzero coefficients are

    G2: -(A+C)*tau^4/4,  F2: -AO*tau^4/4,
    G3: (-A+C)*tau^3/3,
    G4: -(A+C)*tau^2/2,  F4: -AO*tau^2/4,
    G5: (-A+C)*tau.

Set

    pi^2*D6_lift = sum_x C_x*[ell_x-Log(1-x/tau)-log(rho*tau)]+J_tau.

The physical forward coefficients obey C_u=Gamma(C_s), the even-degree crossing law. Exact polynomial division, logarithmic coefficients, generated series and both rims reproduce the entire prescribed twice-subtracted degree-six Cauchy window. The retained cuts agree inside the artificial window; outside it the window cuts vanish as prescribed. The endpoint tau is not a physical threshold, and no global equality of the window and full-cut amplitude is claimed.

Subtracting M6_log gives

    pi^2*(D6_lift-M6_log)
      =J_tau-log(rho*tau)*T+sum_(n>=1,x) C_x*x^n/(n*tau^n).

The series starts at degree seven. For u=-s-t and |s|,|t|<=a with 2*a<tau it converges absolutely and uniformly in two complex variables; the covariant polynomial prefactors preserve holomorphy on compact momentum/polarization charts. This is the generated difference's analyticity, not analyticity of the full threshold-log amplitude at zero.

For the normalized physical helicity scalars, a conservative source-coordinate l1 bound on the three channel prefactors together is K*r^6, r=2*a, with K=107/80, obtained directly from the coefficient vectors A,B,C,D,AO,BO,H. After degree N>=6 the generated tail is bounded by

    K*r^6*(r/tau)^(N-5)/[(N-5)*(1-r/tau)].

This is not a norm bound on arbitrary boosted tensors, unknown matching, unretained light channels or all-order remainders. The finite matching directions and the independent quartic source inputs remain retained.

## Verification and next test

Eight tests accompany all-helicity and Bose controls, 9216 scalar component Ward constraints, 256 full-component transport identities, archived source restrictions and per-monomial Cauchy polynomial/series/rim comparisons. Scoped SCC and a fresh headless receipt are implementation controls, not independent physical evidence. C1–C12, C12's zero remaining budget and the high-energy pause are unchanged.

Next test the actual real factorization locus: can vanishing degree-six transport coexist with a nonzero degree-six cut for an eight-coupling source, or is the extra linear kernel excluded by the source constraints? A bookkeeping null vector does not answer that question. Zero transport must in no case be conflated with zero entire interaction: the already classified zero-leading pure-quartic sources remain unseen through these cut orders. Physical preparation/matching and native/UV gates remain separate and unearned.

```text
python -S research/nima/checkers/check_photon_general_degree6_window_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_general_degree6_window_v1.py
```
