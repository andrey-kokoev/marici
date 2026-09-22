# Arb certifies a minimum source lift and an all-depth realizable tail

## Certified result

This is a worked source-realization certificate, not another abstract criterion.

For the actual six-event cubic packet at A=2, with forcing beta=4, prescribe the two existing normalized private-row readings to be exactly 1 and 1/2. Among genuine J_3 sources, their unique minimum-Q_R lift is

`x_0=v_0+(1/2)v_x`.

Arb encloses its actual Q_1 cost per physical seam weight near 1.2*10^(-185); the upper/lower enclosure ratio is below 1.2. The calculation includes the completed theta series and analytic integral tails.

An explicitly specified infinite continuation then gives a source x in BOTH the actual-letter and common-path domains, with

`Q_1(x)<10^(-4) w_seam`.

Its finite depth-four prefix contains 192 actual marked paths and satisfies

`Q_1(x-x^(4))<3*10^(-8) w_seam`.

All source-radius budgets have an explicit finite-sum/geometric formula. Thus this specified observer tower passes the all-depth lift-budget criterion with a finite-description proof.

The tail specification is essential. The same finite observations admit a different, internally consistent continuation with no summable source. No finite data test alone certifies arbitrary unseen future observations.

## 1. Exact finite data and the source constraint

Keep the actual two-private-row protocol from Voevodsky's cubic calibration, at spectral point 3i and receiver gamma=2. Its norm-one residual test kappa has positive values on the relevant actual windows. Let E_0,E_x be its exact positive evaluations on the private rows for v_0 and v_x, respectively.

Divide each row reading by its own exact E value. Call the resulting admitted source functionals P_0 and P_x. Their source coefficients are exactly

`P_0(v_0)=1`, `P_x(v_x)=1`,

with both zero on the other relevant basis products. The prescribed data are

`P_0(x)=1`, `P_x(x)=1/2`, with `x in J_3`.

These are exact NORMALIZED observer constraints, not a claim that finite response noise gives exact source coefficients. The positivity/nonvanishing of E_0,E_x at this point is supplied by the existing Arb private-row calibration. That normalization and its measurement error budget remain separate from the source-cost integration here.

For a full tower protocol, explicitly retain P_0,P_x and their source-action translates from stage three onward, alongside the existing saturated observers. This is a finite-support admissible augmentation, not an assumption that the previous single scalar cubic observer already recovered two coefficients. Both added rows kill J_4, so the tower construction applies unchanged.

## 2. Why the minimum source lift is exact

The actual two-feature I^3 corner has 270 disjoint-support basis products. The two private rows isolate v_0 and v_x among ALL of them. Consequently the constraints force their coefficients to be 1 and 1/2. Every other basis coefficient contributes a nonnegative additional Gamma path norm and cannot cancel their supports.

Other corners and retained degrees do not affect these selected data and only add source norm. Therefore x_0 is the unique minimum lift within the declared J_3 domain, simultaneously for every R. This assertion would not follow on an enlarged J_1 domain without a new optimization; the J_3 constraint is retained explicitly.

Write g(a,p)=||1_[log a,log(pa)] Phi||_H4 and put

`S(a;p,q)=g(a,p)+g(pa,q)+g(a,q)+g(qa,p)`.

Since each source product has two retained features, its physical Gamma weight contains w=w_seam. Exactly,

`||v_0||_Gamma/w=2 S(2;2,3)S(12;5,7)`,

`||v_x||_Gamma/w=2 S(2;2,5)S(20;3,7)`.

Thus

`Q_R(x_0)/w=6!R^6 [2 S(2;2,3)S(12;5,7)
                           +S(2;2,5)S(20;3,7)]`.

This is an exact minimum formula in the SOURCE norm. It is not the full-response observer-norm optimization, recently solved separately by Grothendieck.

## 3. Rigorous actual theta norm enclosures

Use the completed convention

`Phi(x)=exp(x/2) sum_(n>=1)(4q_n^2-6q_n)exp(-q_n)`,

`q_n=pi n^2 exp(2x)`.

For a starting arithmetic value a>=2 set q_0=pi a^2, v=pi exp(2x)-q_0, and x=(1/2)log((q_0+v)/pi). Define P(v)=exp(q_0-x/2)Phi(x). The first two atoms are

`(4q^2-6q)exp(-v)+(64q^2-24q)exp(-3q_0-4v)`,

where q=q_0+v. The omitted positive atoms are bounded by

`4q^2*81 exp(-8q_0-9v)/[1-(4/3)^4 exp(-7q)]`.

The SCALED squared H4 norm integrand is

`exp(9x)(1+x)^2 P(v)^2/(2q)`.

The checker integrates its interval enclosure on 2048 complete cells through v=32 at 192-bit precision. Since every event multiplier is at least two, its finite window extends past this core: 3q_0>32. The same per-start core and tail enclosures therefore apply to all needed actual upper endpoints, without replacing their true integrals by equal values.

For the tail put

`H_0=1+16 exp(-3q_0)/[1-(3/2)^4 exp(-5q_0)]`.

Positivity gives P(v)<=4q^2 exp(-v)H_0. Since 1+x<=q and q>=1, the scaled norm integrand is bounded by

`8pi^(-9/2)H_0^2 q^10 exp(-2v)`.

Its integral from V to infinity is exactly bounded using

`exp(-2V) sum_(k=0)^10 binomial(10,k)(q_0+V)^(10-k) k!/2^(k+1)`.

After restoring exp(-2q_0) and taking square roots this encloses each actual forcing norm. The nine required starting values are 2,4,6,10,12,20,60,84,140. No asymptotic substitution, underflowed amplitude or sampled quadrature sign is used.

Arb proves

`0<Q_1(x_0)/w<10^(-170)`,

with an actual enclosing ball near 1.2*10^(-185) and upper/lower ratio below 1.2.

## 4. A uniform bound for every later actual event

The same tail majorant integrated from V=0, at q_0=4pi, bounds the COMPLETE admitted forcing tail:

`||1_[log 2,infinity) Phi||_H4^2
 <=8pi^(-9/2)H_0^2 exp(-2q_0)
   sum_(k=0)^10 binomial(10,k)q_0^(10-k) k!/2^(k+1)`.

Its Arb enclosure is approximately 0.0443258843, strictly below one. Hence every actual event window in our packets satisfies g_e<1, and gamma_e<sqrt(w). This is a uniform bound on the true theta source, not an assignment of artificial letter weights.

## 5. A finite-description, visible all-depth continuation

Let v_r be the actual r-seam detector witness from the all-depth theorem, with r-1 mixed diamonds and one forgotten diamond. For r>=4 define

`c_r=w^((3-r)/2)/[2^(r^2)(2r)! 2*4^(r-1)]`,

`x=x_0+sum_(r>=4)c_r v_r`.

The physical w>0 remains fixed; the displayed powers are explicit source coefficients, not a redefinition or numerical setting of w. Since v_r has 2*4^(r-1) paths and r-1 retained letters, section 4 gives

`Q_R(c_r v_r)<=w R^(2r)2^(-r^2)`.

For integer R>=1 set k_R=max(4,ceil(log_2 R)). The successive majorant ratio at r is R^2/2^(2r+1), at most one half for r>=k_R. Therefore

`Q_R(x)/w
 <=10^(-170)R^6
   +sum_(r=4)^(k_R-1) R^(2r)2^(-r^2)
   +[R^(2k_R)2^(-k_R^2)]/[1-R^2/2^(2k_R+1)]`.

This is finite and explicit for EVERY radius. It proves actual-letter summability without querying infinitely many numerical stages.

The same source belongs to the common-path domain. Its tail path mass is exactly

`||c_r v_r||_path=w^((3-r)/2)/[(2r)!2^(r^2)]`.

At any fixed common-path radius and polynomial order, the ratio of successive weighted terms tends to zero. Thus both domain requirements are met by this ONE source, not by two independently minimizing lifts.

## 6. The observer tower and the finite approximation certificate

Let x^(m)=x_0+sum_(4<=r<=m)c_r v_r for m>=3, and use zero at stages one and two. Define

`y_m=Obs_m(x^(m))`.

These are compatible because v_r belongs to I^r and every stage-m row annihilates I^(m+1). The private readings remain exactly 1 and 1/2. Every finite-stage source lift has cost at most the explicit all-radius bound in section 5. The source-realization criterion therefore applies, and the convergent series already gives its constructive realization.

At R=1,

`sum_(r>=4)2^(-r^2) <=1/65408`,

so Q_1(x)<10^(-4)w. Keeping just the depth-four source prefix gives

`Q_1(x-x^(4)) <=w/33538048 <3*10^(-8)w`.

The artifact records its 192 distinct actual marked paths: 32 from v_0, 32 from v_x and 128 from v_4. Each coefficient is specified by an exact rational multiplier and a recorded power of w. The tail is specified by the formula in section 5, rather than a list of unchecked floating-point samples.

For another requested radius the same geometric argument supplies its finite cutoff and tail budget. Existing forward observer/receiver estimates can then be applied with their stated norms; the Q_1 error is not silently interpreted as an arithmetic response error.

## 7. Why the declared tail information cannot be omitted

The data through depth four alone do not force this good continuation. Beyond r=4, replace c_r v_r by (U_r/d_r)v_r, where d_r=ell_r(v_r)>0 and U_r bounds the Q_1-dual norm of the actual detector in its corner. Each future stage still has a finite genuine source lift, and the resulting observer states agree with our good tower through stage four.

But the later detector coordinates require at least one unit of Q_1 source cost in every new distinct corner. Their minimum lift costs diverge. The alternative continuation has no summable actual-letter source, by `uniform-observer-lift-budgets-certify-actual-source-realization.md`.

Thus the finite certificate here consists of the exact finite observer constraints, a verified minimum lift, AND a specified tail rule with a proved uniform majorant. It does not claim that finite agreement alone settles arbitrary unobserved data.

## 8. Relation to the new response and coherence results

Grothendieck's `../grothendieck/matched-private-corrections-attain-the-full-cubic-observer-norm.md` solves a different minimum: the full continuous-response dual norm of the cubic functional. This note minimizes source Gamma cost for prescribed private data. Those norms must not be exchanged.

Voevodsky's `../voevodsky/common-flag-models-supply-coherent-nullhomotopies-at-every-finite-horizon.md` supplies compatible finite-horizon vertical defining systems. The present certificate addresses the remaining analytical realization question for one explicit all-depth source. Neither finite coherence nor a full-response optimum alone provides its summability bound.

## Reproduction

`uv run --with python-flint --with sympy python research/nima/checkers/certify_observer_source_lift.py`

Artifact: `research/nima/results/certified-observer-source-lift.json`.

Fresh checks cover all 270 actual cubic basis columns, their private pivots and disjoint supports; completed-theta norm enclosures; the uniform forcing-tail bound; exact rational all-radius majorants; and the 192-term finite source artifact. This is a source-realization certificate for the specified inputs, not an experimental acquisition claim or a calibrated inverse from arbitrary response noise.
