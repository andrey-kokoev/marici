# Uniform actual-letter budgets characterize realizable infinite filtered towers

## Result and attribution

Voevodsky's `../voevodsky/the-bounded-filtered-limit-recovers-the-source-and-its-faithful-fox-jets.md` already proves the bounded inverse-limit theorem for the COMMON-PATH domain. This note extends that theorem to the actual-letter factorial domain and its summed forcing-resolved Fox map. It also gives quantitative finite-depth reconstruction and distinguishes the two source requirements.

A compatible tower is realized in the actual-letter source exactly when its actual-letter quotient seminorms are uniformly bounded in depth, at EVERY radius. Compatibility alone is insufficient. The bounded tower carries supremum seminorms, not the inverse limit's weaker product topology.

An actual-letter-realizable tower need not be common-path-realizable. If both source requirements are retained, both uniform budgets are required.

## 1. The actual domain and the precise quotients

Use the fixed positive actual letter weights and source from

`../grothendieck/actual-letter-weights-characterize-marked-fox-summability.md`:

`Q_R(x)=sum_c n(c)! R^(n(c)) ||x_c||_Gamma`,

`||x_c||_Gamma=sum_(w in c)|x_w|Gamma(w)`, `R=1,2,...`.

Let S_Gamma be their common domain. Let

`J_(r,Gamma)={x in S_Gamma : x_c belongs to (I^r)_c for every corner c}`,

`X_Gamma=J_(1,Gamma)`, `E_(m,Gamma)=X_Gamma/J_(m+1,Gamma)`, for m>=1.

These ideals are closed. Endpoint truncation shows they are precisely the inherited closures of the finite-source powers. The recent `theta-tail-dominance-controls-actual-letter-factorization-lifts.md` identifies the corresponding native presentation intersections with these inherited spaces. Here depth-uniform bounds are stated in the specified AMBIENT Q_R quotient seminorms, not in seminorms independently rescaled at each depth.

Write q_(R,m) for the quotient seminorm induced by Q_R. In each finite corner it is computed using the distance in ||.||_Gamma to (I^(m+1))_c. Thus

`q_(R,m)(x mod J_(m+1,Gamma))
 =sum_c n(c)! R^n dist_Gamma(x_c,(I^(m+1))_c)`.

Indeed a minimizing representative exists in each finite-dimensional corner. All radii multiply its norm by scalars, so one choice of corner minimizers works simultaneously for every radius. Their sum lies in X_Gamma whenever the quotient family is in E_(m,Gamma). This justifies the quotient formula in the Frechet domain, not only at a single Banach stage.

## 2. Exact inverse-limit criterion

Let t=(t_m) be compatible, with t_m in E_(m,Gamma). A relation consumes at least two events. Hence (I^(m+1))_c=0 when n(c)<2(m+1). Every corner of the tower therefore stabilizes to a unique actual vector x_c in I_c.

For each corner its quotient distances increase with m and eventually equal ||x_c||_Gamma. Monotone convergence over the countable corner set gives, allowing infinity,

`B_R(t):=sup_m q_(R,m)(t_m)
       =sum_c n(c)! R^n ||x_c||_Gamma=Q_R(x)`.

Consequently t comes from a UNIQUE x in X_Gamma if and only if B_R(t)<infinity for every integer R>=1. Reconstruction is an isometry for each pair B_R,Q_R. This identifies the bounded tower with a complete Frechet source when the tower is given its supremum seminorms.

There is no nonzero source in the kernel of the tower map. The issue is existence of a summable preimage and the topology of recovery, not injectivity.

## 3. Compatibility does not imply summability

Choose distinct primes and form the product a_r of r consecutive FORGOTTEN diamond relations in its minimal 2r-event corner. There are 2^r distinct paths, all with coefficient magnitude one and Gamma=1. Distinct r have distinct terminal corners. Put

`z_r=a_r/[2^r (2r)!]`.

Then z_r belongs to I^r and exactly

`Q_R(z_r)=R^(2r)`.

The tower

`t_m=sum_(r=1)^m z_r mod J_(m+1,Gamma)`

is compatible and each level has finite source support. In those first m corners the quotient ideal vanishes, so

`q_(R,m)(t_m)=sum_(r=1)^m R^(2r)`.

In particular B_1=infinity. No actual-letter summable source realizes it.

The image of X_Gamma is nevertheless dense in the ordinary inverse-limit topology: lift a prescribed finite level, which automatically matches every lower level. It is proper by this example. Individual z_r tend to zero at every fixed filtration level but Q_1(z_r)=1. Hence the inverse on the realized image is not continuous for the product subspace topology. The supremum topology in section 2 is essential.

## 4. Quantitative recovery from finite depth and a radius budget

Level m determines every stabilized corner of length n<=2m+1. Let x^[m] be those corners, with all longer corners set to zero. It need not have FINITE endpoint support: there can be infinitely many short corners. Its coefficient family is summable when the budgets in section 2 hold. It is a length-truncated reconstruction, not necessarily a lift of the entire quotient t_m.

For integer R'>R>=1,

`Q_R(x-x^[m]) <= (R/R')^(2m+2) B_(R')(t)`.

Only lengths at least 2m+2 remain. This is a direct geometric radius comparison and gives a quantitative depth-tail budget. A genuinely finite endpoint implementation needs, in addition, a bound on the omitted short-corner tail; this estimate does not supply one automatically.

More generally, let x,y be genuine source candidates with Q_(R')(x),Q_(R')(y)<=M. Their short-corner difference is measured exactly in the level-m quotient, while their long-corner difference is bounded by the prior. Therefore

`Q_R(x-y)
 <= q_(R,m)([x]_m-[y]_m)+2 M (R/R')^(2m+2)`.

This is a linear level-data error plus a geometric truncation error. In particular equal finite-depth data determine candidates to that accuracy on the radius-bounded prior class. The data norm is a SOURCE QUOTIENT norm, not an arithmetic response noise norm.

## 5. Equivalence with summed forcing-resolved jets

Keep Grothendieck's existing forcing-resolved receiver F_(s,b), with lambda=max(1,tau/sqrt(w_seam)). Its actual-letter theorem gives

`Q_R(x)<=||D(x)||_(F_(R,1))`,

`||D(x)||_(F_(s,b))<=2 Q_(ceil(2 lambda s b))(x)`.

Finite jets factor through the corresponding finite ideal quotients. Thus a compatible tower has its coherent finite-jet family. Those jets are summable at every forcing-resolved receiver scale if and only if B_R(t)<infinity at every source radius. The necessity uses labelled top-jet coefficient detection, not an inverse to an analytical transform.

With R_0=ceil(2 lambda s b) and integer R'>R_0, section 4 gives

`||D(x)-D(x^[m])||_(F_(s,b))
 <=2 (R_0/R')^(2m+2) B_(R')(t)`.

For two candidates with the prior Q_(R')<=M it also gives

`||D(x)-D(y)||_(F_(s,b))
 <=2 q_(R_0,m)([x]_m-[y]_m)
   +4 M (R_0/R')^(2m+2)`.

These are forcing-resolved summability statements. No reverse estimate from Clark or arithmetic output alone is inferred.

## 6. The old common-path requirement is genuinely additional

Write the old common-path seminorms as

`p_b(x)=sum_c (1+n)^p (b a)^n ||x_c||_path`, with p>=0 and a,b>=1.

On a tower whose finite levels are admitted in both systems, reconstruction belongs to X_common intersect X_Gamma exactly when BOTH sets of supremum quotient seminorms are finite. Do not replace the intersection by X_Gamma silently.

There are actual towers separating them. For each r choose an admitted starting arithmetic vertex sufficiently far out that every event in a selected 2r-event corner has gamma_e<=2^(-r^2). This uses the existing theta H_beta tail, not invented letters or weights. Choose distinct corners.

Let a'_r be the product of r consecutive MIXED-MARK diamond relations. It has 4^r distinct marked paths, each with r retained events. Set v_r=4^(-r)a'_r. Then

`v_r in I^r`, `||v_r||_path=1`,

`Q_R(v_r)<=(2r)! R^(2r) 2^(-r^3)`.

The last bounds sum for every R. Thus x=sum_r v_r is in X_Gamma, with summable all-order forcing-resolved jets. But p_1(x)>=sum_r 1=infinity, so x is not in the common-path source. Its finite tower levels are represented by the finite sums sum_(r<=m)v_r, which are admitted in BOTH systems. This is an actual failure of common-path realization of that tower, not failure of finite-level compatibility.

The construction uses the same type of late-window choices as the earlier marked Fox summability-domain witness, now with increasing relation depth. All arrows and windows remain prescribed source objects. Root states are not multiplied or adjoined.

## 7. Disposition

The unrestricted infinite filtered limit is larger than the actual-letter summable source. Its exact realizable part is characterized by uniform ambient quotient budgets. With those budgets, finite-depth recovery has an explicit geometric radius-loss estimate, and full forcing-resolved jet summability follows.

This extends, rather than replaces, the earlier common-path bounded-limit theorem. It does not identify arbitrary inverse-limit families with attachment realizations, change the terminal-record ideal, or supply an output-only inverse. Voevodsky's separate calibrated attachment measurement uses its own response norm and noise budget.

## Verification

`uv run --with sympy python research/nima/checkers/check_actual_letter_filtered_limit.py`

Finite checks use the existing actual forgotten and mixed diamond relations. They verify product coefficients, the factorial normalization, compatibility of the hostile tower, and the exact finite-depth radius/error inequalities on controlled coefficient fixtures. Infinite monotone convergence and existence of late theta windows are proved above, not inferred from finite fixtures.
