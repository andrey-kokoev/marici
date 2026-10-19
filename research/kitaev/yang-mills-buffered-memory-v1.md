# Buffered full-box readers: controlled memory despite exact boundary nonclosure

## Question and disposition

Can fixed interior observables have a controlled approximate autonomous description even though every nontrivial finite cubic-box reader leaks at its boundary?

**Written actual-source upper bounds:** keep0<=r<27/262144, R=4096r/3<9/64, c=1/2-3R>5/64 and m=kappa*c. Let f be a real smooth cylinder with support K inside the full link reader of Lambda, let b=d(K,Lambda complement), and M(f)=sum_i||gradient_i f||_infinity. Define

\[
E_f(t,b)=\frac{2R}{c}(1-e^{-mt})(3/4)^b M(f).
\]

For the actual vacuum projection Pi=E_nu[ . |U_Lambda], Q=I-Pi, actual source P_t and actual free-boundary source P_t^Lambda,

\[
\|\Pi P_t f-P_t^\Lambda f\|_{L^2(\nu)}\le E_f(t,b),
\qquad\|QP_t f\|_{L^2(\nu)}\le E_f(t,b).
\]

For K_t=Pi P_t Pi on the full reader,

\[
0\le\langle f,(K_{2t}-K_t^2)f\rangle
\le E_f(t,b)^2.
\]

These bounds hold for every t>=0, not just a preassigned finite horizon. They improve the earlier growing propagator comparison by retaining the existing Ricci damping. The executable rational buffer criterion below covers any finite horizon or all source parameters. Independent analytic review of the analytic dependency chain remains open.

This is an observable-wise result for the FULL spatial reader. It is not a small operator-norm claim on its entire L2 unit ball, not an assertion about an incomplete two-trace reader, and not a physical-clock or continuum result.

## Issue-boundary conjecture and rivals

**Problem:** exact boundary nonclosure and fixed-bulk convergence have different quantifiers; qualitative convergence alone does not budget compressed-reader memory.

**Conjecture:** damped finite-product gradient transport makes the boundary Duhamel error saturate, and orthogonal projection converts that common-carrier comparison into actual-state reader and memory bounds.

**Rivals:** discard Ricci damping and obtain an unnecessarily growing horizon cost; silently identify free-boundary and infinite-marginal vacuum measures; assume Q is L-infinity contractive; infer a whole-reader operator norm from one smooth input; apply the result to a smaller reader that does not contain the finite-source output.

**Risky consequences:** the saturating2R/c boundary prefactor; squared equal-time memory budget and cross-time matrix-element budget; exact rational minimal-buffer calculations; explicit norm/measure/coarse-reader countercontrols.

## Retain damping in the actual propagator comparison

For Lambda inside Gamma, use the same independent exterior Brownian comparison extension as the actual propagator packet. The full drift discrepancy inside Lambda obeys

\[
\|\beta_{\Gamma,i}-\beta_{\Lambda,i}\|_\infty
\le2R a^{-h_i},\qquad
h_i=d(i,\Lambda^c),\quad a=4/3.
\]

The clustering packet retained the radius-two product Ricci damping in the finite-source gradient equation, giving

\[
\sum_i a^{d(i,K)}\|\nabla_i P_s^\Lambda f\|_\infty
\le e^{-ms}M(f).
\]

Duhamel and sup-norm contraction of the actual finite-source semigroups, with h_i>=b-d(i,K), now yield

\[
\|P_t^\Gamma f-P_t^\Lambda f\|_\infty
\le2\kappa R a^{-b}M(f)\int_0^t e^{-ms}\,ds
=E_f(t,b).
\]

All steps take place on finite compact products. The already established actual propagator limit Gamma increasing to infinity passes this scalar inequality to P_t. No limit of infinite sums of gradients is needed. Since the resulting bound holds for every t and is bounded by2R a^(-b)M(f)/c, it also supplies an all-parameter uniform comparison. At R=0 the discrepancy is exactly zero.

## Projection, measure discipline and memory

All norms in the claim use the ONE actual infinite state nu. The free-boundary propagator is evaluated as a bounded Lambda-measurable function in that space. Its own reversible measure is nu_Lambda, generally not the infinite-state marginal. No L2(nu) contraction property is assumed for P_t^Lambda.

Since Pi P_t^Lambda f=P_t^Lambda f,

\[
\Pi P_t f-P_t^\Lambda f
=\Pi(P_t f-P_t^\Lambda f),\qquad
QP_t f=Q(P_t f-P_t^\Lambda f).
\]

Pi and Q are orthogonal contractions in L2(nu), and the common-carrier sup-norm error bounds the L2 error because nu is a probability measure. This proves both estimates. Q need not have L-infinity norm1; no such assertion is used.

The actual source is self-adjoint. Therefore

\[
K_{2t}-K_t^2=(QP_t\Pi)^*(QP_t\Pi),
\]

so its quadratic value on f is exactly||QP_t f|| squared. More generally, for reader-supported real smooth f,g,

\[
|\langle g,(K_{s+t}-K_sK_t)f\rangle|
=|\langle QP_sg,QP_tf\rangle|
\le E_g(s,b_g)E_f(t,b_f).
\]

The mixed defect need not be declared positive; the equal-step defect is positive. The quadratic bound on a chosen f is not a norm-squared bound for the whole defect operator.

## An executable finite-horizon or all-parameter buffer rule

For a step horizon T>=0, meaning0<=t<=T, use the rational majorant below. The equal-step defect reaches parameter2T; for a total two-step horizon H choose T=H/2.

\[
A_T=\frac{2R}{c}\min\{\kappa cT,1\}M(f),
\]

from1-exp(-x)<=min{x,1}. For all t>=0 use A_infinity=2RM(f)/c. Given positive tolerances epsilon for L2 amplitude and delta for the equal-step quadratic memory, choose the smallest nonnegative integer b such that

\[
A_T(3/4)^b\le\epsilon,\qquad
A_T^2(9/16)^b\le\delta.
\]

The checker exposes a fraction-only `plan_buffer` routine: multiply the amplitude by3/4 until both inequalities hold, and check minimality against the preceding integer. This is minimal for this rational sufficient budget, not an assertion of the true optimal source error. R=0, M(f)=0 or T=0 need buffer0 for these error budgets. The actual box must still contain the observable support.

Uniformly over the ENTIRE admitted source-coupling window,

\[
2R/c<18/5.
\]

Thus the conservative all-parameter choice A=(18/5)M(f) works without specifying r or kappa. For a plaquette trace M(f)<=4, epsilon=1/100 and delta=1/10000, buffer26 satisfies this worst-case all-parameter rule. For R=9/128,kappa=1,M=4, the corresponding rational budgets need buffer15 at T=1 or buffer19 for all parameters. All these integer statements are exact fraction checks, not floating-point exponentials or estimates of the actual error.

## Exact controls and named failures

The checker freshly replays the box-boundary-leakage receipt. It checks768 rational planner cases, including zero and near-cutoff parameters, horizon0 and the all-parameter option. It checks the saturating-prefactor algebra, the universal18/5 bound, and each declared minimal-buffer fixture. The analytic exponential/gradient inequalities remain written inputs. The first run under freeze02e79826b54aae30 failed the coverage guard because its kappa grid contained two values, giving384 rather than the declared768 cases. The original checker is retained at `scc-failures/yang-mills-buffered-memory.coverage384.py.txt`. Expanding that grid to four positive kappa values corrects the coverage without changing any analytic budget, tolerance fixture or guard; the corrected inputs are refrozen before rerunning.

A reversible rational three-state kernel and a two-block conditional projection regress cross-time compressed-defect factorization and Cauchy–Schwarz over several discrete times and reader inputs. This is a finite-law control, not an evaluation of the SU2 exponential. Constants have zero memory defect although other reader vectors do not: one observable's zero budget is not a whole-reader operator bound. Replacing the reader by the full three-state algebra eliminates that toy leakage; an incomplete reader on the same carrier cannot inherit the spatial full-reader guarantee.

Two further exact failures guard the norm discipline. With Pi the uniform average on three points and f=(1,-1,-1), ||Qf||_infinity=4/3>||f||_infinity while Q is L2-contractive. A uniform-reversible Markov kernel I/4+3J/4 increases the squared norm of(1,0,1) from1/3 to17/48 under the different measure(1,4,1)/6. A free source's own-measure contraction cannot be transferred just by copying coordinates.

## Reconcile the boundary lower bound; surviving scope

The previous lower bound uses a plaquette that stays on each box boundary, so its buffer does not grow. The present error tends to zero for a fixed smooth bulk observable with growing buffer. Both hold simultaneously. Exact nonclosure therefore does not forbid approximate finite-volume dynamics or small compressed memory for a specified interior probe.

No conclusion is made about all L2 reader vectors, incomplete internal readers, arbitrary repeated insertion words, spatial continuum refinement, a physical clock or continuum Yang–Mills. Independent analytic review and parent/root gates remain open. No commit or publication authority is inferred from the exact controls.

**Next executable issue:** control accumulation in actual multi-insertion words under increasingly fine source-parameter partitions, with a declared insertion/gradient budget and spatial buffer. The older multi-time packet proves convergence for each fixed finite word but supplies no mesh-uniform quantitative error budget. Two-step bounds alone do not control arbitrary composition with changing intermediate inputs; retaining weighted gradient locality through multiplication and propagation is the next constructor.

Contract: `research/kitaev/contracts/yang-mills-buffered-memory.v1.json`.
Reproduce: `python research/kitaev/checkers/check_yang_mills_buffered_memory.py`.
Receipt: `research/kitaev/results/yang-mills-buffered-memory-v1.json`.
