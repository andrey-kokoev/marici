# Uniform observer-lift budgets certify actual source realization

## Result

A compatible corrected observer-state tower has a source in the actual-letter domain if and only if its MINIMUM SOURCE LIFT costs are uniformly bounded in depth at every source radius.

This is not a bound on the numerical size of the observations. It measures the least admissible source cost of realizing them. The criterion supplies existence, generally not uniqueness. Coherent frame observations can fail it, and an explicit internally consistent tower does fail it.

The proof uses source-bimodule corner decomposition, finite support at each observer stage, and finite-dimensional stabilization of the constraints in each corner. It applies to the original saturated tower and to the admitted corrected/common-refinement towers, provided each stage is a finite source-invariant subspace of E_m^* as already constructed.

## 1. Exact observations after the frame checks

First require the corrected frame tuples to synchronize at each rung and to respect restriction across rungs, as in `frame-discrepancy-observers-form-a-compatible-consistency-tower.md`. Choose the resulting reference state

`y=(y_m)`, `y_m in O_m`, `pi_m(y_(m+1))=y_m`.

Let X_Gamma=J_(1,Gamma), with

`Q_R(x)=sum_c n(c)! R^n ||x_c||_Gamma`, `R=1,2,...`.

Write Obs_m:X_Gamma->O_m for source evaluation. It is onto at each finite stage. Because the observer spaces are source bimodules with finite support, their vertex-idempotent decompositions give finite corner components O_(m,c), and evaluation acts cornerwise from I_c. This module property is important; unrelated scalar constraints mixing infinitely many corners would not justify the proof below.

If a particular attachment requires x in J_q rather than just J_1, replace I_c throughout by (I^q)_c and first require y_m to lie in the corresponding finite image Obs_m(J_q). The same proof then applies. Vanishing of the selected first observer alone does NOT imply x belongs to J_2; the selected tower is not assumed faithful on the first source quotient.

Define the observable lift norm

`nu_(R,m)(y_m)=inf {Q_R(x): x in X_Gamma, Obs_m(x)=y_m}`.

Every finite-stage state has a finite-support source lift. Thus the infimum is finite, and is attained as described next. No source coefficient is inferred by simply equating a response norm with Q_R.

## 2. Cornerwise feasibility and its eventual stabilization

For every corner c let

`A_(m,c)={u in I_c: Obs_(m,c)(u)=y_(m,c)}`.

Outside the support of stage m, this is all of I_c. Each A_(m,c) is a nonempty finite-dimensional affine subspace. Compatibility of the tower makes these affine spaces decreasing in m.

Their direction spaces K_(m,c)=ker Obs_(m,c) also decrease. In finite dimension there are only finitely many strict dimension drops, so for each c there is some index m_c after which K_(m,c) is constant. Nested nonempty affine spaces with that same direction are equal. Hence A_(m,c) eventually becomes one fixed nonempty affine space A_(infinity,c).

This stabilization index is NOT automatically bounded by n(c)/2. Future higher-depth detectors can introduce new context observations on an earlier source corner. Finite dimension bounds the number of rank increases, not how late the last one occurs.

Let

`d_(m,c)=min_(u in A_(m,c)) ||u||_Gamma`,

`d_(infinity,c)=min_(u in A_(infinity,c)) ||u||_Gamma`.

The minima exist by finite-dimensional coercivity. The numbers increase with m and eventually equal d_(infinity,c).

## 3. Exact lift-budget identity

All source radii multiply the same Gamma corner norm by a scalar. Therefore one choice of minimum-Gamma representatives at each finite stage minimizes EVERY Q_R simultaneously, and gives

`nu_(R,m)(y_m)=sum_c n(c)! R^n d_(m,c)`.

Only finitely many terms are nonzero at that stage. Monotone convergence now proves, allowing infinity,

`B_R(y):=sup_m nu_(R,m)(y_m)
       =sum_c n(c)! R^n d_(infinity,c)`.

Choose a minimum-Gamma representative x_c in each A_(infinity,c). If B_R(y)<infinity for every integer R, then x=(x_c) lies in X_Gamma, realizes every y_m, and satisfies EXACTLY

`Q_R(x)=B_R(y)` for every R.

Conversely every realizing source has Q_R(x)>=B_R(y). Consequently:

`y is realized by an actual-letter source
 iff B_R(y)<infinity for every R`.

Without these bounds, the stabilized corner representatives still define a formal coefficient family. Formal cornerwise realization is not a summable source realization, or a claim that every completed filtered source quotient is admissible.

## 4. The source is only determined modulo the invisible module

Put

`K_infinity={x in X_Gamma: Obs_m(x)=0 for all m}`.

It is a closed source submodule. All realizing sources form the affine fiber x+K_infinity. The theorem does not assert that this kernel is zero.

The bounded observer tower, with seminorms B_R, is isometrically the quotient X_Gamma/K_infinity with its induced Q_R quotient seminorms. Indeed the simultaneous corner minimizer attains all quotient infima. This supplies completeness and a precise topological realization statement, but no preferred linear or source-equivariant lifting section.

This invisible module is an observational kernel of the specified saturated tower. It does not replace the original terminal-record ideal or the raw arithmetic-response kernel.

## 5. Finite lifts can converge, without an automatic rate

Choose minimum-Gamma representatives consistently whenever the same affine constraint space recurs; for example break ties by a fixed strictly convex Euclidean norm on the minimum set in each corner. Let x^(m) be the resulting finite-support minimizing lift of y_m, and x^* the stabilized choice.

For each corner, x_c^(m)=x_c^* eventually. Also

`||x_c^(m)-x_c^*||_Gamma <=2 d_(infinity,c)`.

When B_R is finite, dominated convergence gives Q_R(x^(m)-x^*)->0 at every R. Thus compatible observer data satisfying the lift budgets possess convergent finite source lifts.

This is an existence/convergence theorem, not a finite algorithm for recognizing that no further constraint will appear in a corner. Arbitrary repeated equal ranks do not certify eventual stabilization.

If an extra source height-moment budget is desired, use the lift costs for Q_(R,eta)=sum_c n!R^n h(c)^eta||x_c||_Gamma. The same minimizers and identity apply, since height is scalar on a corner. Once all corners of height <=H have stabilized, the approximation error is at most

`2(H+1)^(-eta) B_(R,eta)(y)`.

The stabilization condition must still be justified, not guessed from the source event length.

## 6. A synchronized tower with no summable source

Use the all-depth actual witnesses v_r and their positive detector values d_r=ell_r(v_r). Their outer corners c_r are distinct. Let U_r be any finite positive bound for the Q_1-dual norm of ell_r restricted to I_(c_r). Such a bound exists from its finite-support actual test. Choose U_r at least that norm and put

`w_r=(U_r/d_r)v_r`, for r>=2.

Define

`y_m=Obs_m(sum_(2<=r<=m) w_r)`.

These states are compatible: every later w_r belongs to I^r and is killed by all rows in Omega_m when r>m. They produce zero frame discrepancy in every corrected frame presentation.

But ell_r(y_m)=U_r for 2<=r<=m, where this notation denotes the ell_r coordinate of the observer state. Any source lifting y_m must spend Q_1 cost at least one in EACH of those distinct corners, by the choice of U_r. Therefore

`nu_(1,m)(y_m)>=m-1`, and `B_1(y)=infinity`.

This internally consistent tower has no actual-letter summable source realization. The obstruction uses existing witnesses and finite functional bounds, not fabricated letters or arbitrary noisy records.

## 7. Additional common-path requirements and noisy feasibility

If the older common-path source is also required, its norm is not generally a scalar multiple of the Gamma norm WITHIN a corner. Separate minima for the two norms need not be achieved by the same source. Do not infer simultaneous realization merely from two independently bounded optimization problems.

A general joint criterion avoids this issue. Fix increasing positive coefficient seminorms N_k encoding all required source priors, for example N_k=Q_k+p_k, and prescribed finite budgets M_k. A source satisfying every budget and every observer equation exists if and only if, for each j, there is a source satisfying

`Obs_m(x)=y_m for m<=j`, and `N_k(x)<=M_k for k<=j`.

The candidates can be taken finite-support: keep the finitely many corners used by the first j observer stages, which preserves those equations and decreases the coefficient norms.

For sufficiency, N_1 bounds each coefficient in its finite corner. Extract a coordinatewise convergent subsequence of the finite candidates. All source-ideal corner conditions are closed, every fixed observer equation involves finitely many coordinates, and Fatou's inequality preserves each N_k budget. The limit is therefore the required jointly admissible source.

The same compactness proof permits closed finite-stage error constraints instead of exact equations, for example ||Obs_m(x)-y_m||<=epsilon_m, including separate corrected-frame data. This requires jointly feasible candidates with the SAME prescribed budgets. Arbitrary noisy data are not automatically feasible.

This is an infinite feasibility criterion, not a claim that one successful finite test proves all future conditions. Effective finite certification needs independently controlled tails or further structural information.

## 8. Scope and interpretation

The consistency observer checks whether frames agree; the lift-budget theorem checks whether their compatible state has at least one source in the declared domain. Neither establishes the external truth of that source or uniqueness of its invisible components.

The minimum lift costs are source-derived norms, not measured response norms and not backward error estimates for arbitrary analytical data. Existing large frame and observer conditioning constants remain in force.

No preservation of a particular extension class follows just from source realizability. The supplied splitting/nonsplitting and recalibration results retain their own source-marked comparison diagrams.

## Verification

`uv run python research/nima/checkers/check_observer_source_realization.py`

Exact fixtures check cornerwise minimum lift costs, their simultaneous radius scaling, delayed observer stabilization, and a compatible unbounded-cost tower. Infinite sufficiency uses the affine stabilization and monotone/Fatou arguments above, not finite tests or an analytical inverse assumption.
