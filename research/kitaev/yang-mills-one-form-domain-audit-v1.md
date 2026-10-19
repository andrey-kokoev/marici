# R3 audit: identifying the actual Banach one-form generator

Owner: `marici.Kitaev`. Post-audit iteration1/10. Selected issue: `issue-tree:f57ade80940345418b04f880:one-form-generator-identification:v1`.

## DPC and verdict

**Problem.** The earlier force-regularity argument compressed the inclusion of a proposed cylinder differential operator in the actual one-form semigroup generator. Continuous Hilbert-Schmidt derivatives alone do not prove a generator domain.

**Conjecture.** Uniform finite-source generator identities, strong convergence on the actual continuous-field Banach space, and a small resolvent perturbation establish that inclusion and then equality of domains. No derivative of the Hessian multiplier is needed.

**Rivals.** Infer a domain from HS regularity; confuse pointwise multiplier convergence with strong convergence on B; apply strong convergence to uncontrolled moving inputs; omit the first-order connection; reverse the order of a noncommuting resolvent factorization; infer a C(X) operator core merely from a form core.

**Risky consequence.** A standalone conditional identification theorem, an explicit source-hypothesis ledger and a justified zero-resolvent gradient application. The source-specific interaction and path/parallel-transport construction remain upstream analytic inputs, not independently certified here.

**Falsification.** A genuine free-SU2 gradient-mode resolvent loses1/20 at kappa=alpha=1 if the connection curl is omitted. A noncommuting finite control changes the inverse coefficient by1/18 if factor order is reversed. Bounded pointwise-convergent multipliers without column-tail control retain norm defect1. An actual disjoint-plaquette character series has continuous HS Hessian but infinite generator difference quotient at the identity.

**Verdict.** The conditional domain/extension argument is established below at written-proof scope. No failed implication was found in this part once its upstream hypotheses are explicitly retained. This is local proof expansion, not independent external review of the complete source construction. R4 parameterized strong-map measurability remains executable next.

## 1. Abstract identification lemma

Let B be a Banach space, -A the generator of a contraction C0 semigroup P, and D a linear operator core for A. Suppose:

(H1) A closed fibre-derivative operator partial has (alpha+A)^-1 B in its domain, with ||partial(alpha+A)^-1||<=d_alpha.

(H2) J:D(A)->B satisfies ||Ju||<=c_J||partial u||, and Z is bounded on B. For some alpha>0,

q:=||(J+Z)(alpha+A)^-1||<1.

(H3) T_n,T are C0 semigroups, T_n(t)F->T(t)F uniformly on bounded time intervals for each FIXED F in B, and sup_n sup_(0<=t<=T0)||T_n(t)||<=C_T0. Let G be the generator of T and assume alpha belongs to its resolvent set (injectivity plus the needed growth bound would suffice for the final comparison).

(H4) For each F in D, finite-source generator vectors g_n(F) converge in B to (-A+J+Z)F, and

T_n(t)F-F=integral_0^t T_n(s)g_n(F)ds.

Then G equals G0=-A+J+Z on D(A), and D is an operator core for G.

### Proof A: closedness, graph core and full range

Write R_alpha=(alpha+A)^-1 and B_alpha=(J+Z)R_alpha. On D(A),

alpha-G0=(I-B_alpha)(alpha+A).

The order is essential. Since ||B_alpha||<=q<1, I-B_alpha is boundedly invertible. This factorization proves closedness and full range directly, without invoking a perturbation theorem with unspecified hypotheses. Its inverse is

(alpha-G0)^-1=R_alpha*(I-B_alpha)^-1.

Moreover,

(1-q)||(alpha+A)u||<=||(alpha-G0)u||<=(1+q)||(alpha+A)u||.

These norms are equivalent to the respective graph norms: the contraction resolvent gives ||u||<=alpha^-1||(alpha+A)u|| and ||Au||<=2||(alpha+A)u||. The inverse factorization gives the corresponding bounds for G0. Therefore the A-core D is also a G0-core.

### Proof B: the actual extension, with moving inputs controlled

Fix F in D and put g=G0F. For0<=s<=T0,

||T_n(s)g_n(F)-T(s)g||
<=C_T0*||g_n(F)-g||+||(T_n(s)-T(s))g||.

The right side tends uniformly to0. This is where norm convergence of the generator vectors is used; strong convergence alone would not handle arbitrary moving inputs.

Pass the finite-source integral identity to get

T(t)F-F=integral_0^t T(s)g ds.

Strong continuity now yields (T(t)F-F)/t->g as t decreases to0. Hence F belongs to D(G), and GF=G0F. Since G is closed and D is a graph core for G0, this proves G0 subset G on ALL of D(A), not merely agreement on test fields.

### Proof C: no hidden extension

For z in D(G), full range supplies y in D(G0) with

(alpha-G0)y=(alpha-G)z.

The inclusion just proved gives (alpha-G)(z-y)=0. Injectivity implies z=y, proving D(G)=D(A) and G=G0. QED.

No claim here says two operators sharing a differential expression must agree. Both the core extension identity and full range were needed.

## 2. The vector core and the closed derivative

In the source application B=C(X;ell2(E;C3)), with compact metrizable X. Output projections Q_N onto finitely many link components converge uniformly on each continuous field: its image is compact in ell2. They commute with the componentwise scalar semigroup P_t^B and hence with its generator/resolvent. Thus for F in D(A_B), Q_N F->F and A_B Q_N F=Q_N A_B F->A_B F uniformly. On each finite output, the scalar C(X) operator core approximates every component in graph norm. Finite-output smooth cylinder fields are therefore an A_B operator core.

Define partial as the maximal continuous flat fibre derivative with values in C(X;HS), not as a formal trace of the Hessian. It is closed: uniform limits of fields and derivative matrices pass the fundamental theorem of calculus along each one-link frame curve, identifying every derivative entry. The entries reconstruct the stated HS-valued matrix.

Tracing the scalar reverse-Poincare VARIANCE inequality over finite output components gives

||partial P_t^B F||_(C(HS))^2
<=(P_t|F|^2-|P_t^B F|^2)/(2kappa t)
<=||F||_B^2/(2kappa t).

Uniform approximation and closed fibre differentiation extend this estimate. There is no number-of-output-components factor. To integrate it in the resolvent, first integrate over epsilon<=t<=T. Derivative continuity for t>0 follows by writing partial P_t=partial P_(epsilon/2) P_(t-epsilon/2), with the first factor bounded. Then let epsilon decrease to0 and T increase to infinity using the integrable t^-1/2 bound and exponential factor. Closedness gives

||partial(alpha+A_B)^-1||<=sqrt(pi/(2kappa alpha)).

This proves the derivative property ON D(A_B), since every domain element is a resolvent image. It does not infer that domain from an arbitrary derivative bound in the opposite direction.

## 3. Source multiplier bounds and actual norm convergence

Retain the source regime kappa>0,R<9/64,delta<=m/8,m=kappa*(1/2-3R), and g=m-2delta>0. Source logarithmic potentials are V_n=2 sum Phi_A, with beta_n=DV_n and M_n=kappa*Hess V_n. The actual Fourier norm is

W(Phi_A)=sum_pi d_pi*(1+C_pi)*||Phi_hat_A(pi)||_trace,
C_pi=sum_i j_i(j_i+1).

### Block beta bound, not a component/block substitution

Each of the three frame derivatives has representation-generator norm at most j_i. Thus ||D_i Phi_A||<=sqrt(3) sum_pi d_pi*j_i*||Phi_hat||_trace. Since sqrt(3)*j<=2j<=1+j(j+1)<=1+C_pi, this is at most W(Phi_A). Consequently

||beta_(n,i)||<=2 sum_(A containing i)W(Phi_A)<=2R.

This independently justifies the block bound used in the earlier b constant. No sqrt(3) factor is lost by confusing a component estimate with a block estimate.

### Strong Hessian multiplication on B

Use the common symmetric nonnegative Hessian block majorant h from the retained global interaction; its weighted rows and columns obey sum_i a0^d(i,j)h_ij<=3R, a0=4/3. Finite retained-label majorants are dominated by it. Schur gives ||M_n||,||M||<=3kappa R.

For a field supported on a finite output set I, let J_b be its finite b-neighborhood. Weighted columns give, uniformly in n,x,

||(I-Q_(J_b))M_n F||_ell2
<=3kappa R*a0^-b*sum_(j in I)|F_j(x)|
<=3kappa R*a0^-b*sqrt(|I|)*||F||_B.

The same holds for M. On J_b by I, entrywise UNIFORM-in-x convergence gives convergence of the finite matrix action. First choose b for the common tail, then n for the finite head. Hence M_n F->MF in B. General fields follow by finite-output approximation and the uniform multiplier bounds. This also proves that the multiplier maps B into B, without requiring operator-norm continuity of x->M(x).

The diagonal multipliers C(beta_n) converge strongly by fixed-component uniform convergence and the same output truncation. With E_n->E and fixed U, so do

Z_n=kappa*C(beta_n)-kappa*I+M_n-U+E_n.

## 4. Geometry, finite identity and semigroup input ledger

In the declared radius-two invariant frame C_a z=(1/2)e_a cross z. The covariant derivative is X_a+C_a, sum_a C_a^2=-I/2 and Ric=I/2. Expanding the connection Laplacian plus drift and subtracting Ric gives on a localized smooth field

gen(S_n)=-A_(B,n)+J+Z_(0,n),
(JF)_i=2kappa sum_a C_a X_(ia)F_i,
Z_(0,n)=kappa*C(beta_(n,i))-kappa*I.

The two contributions to -kappa*I are connection-square and Ricci. The sign can be checked on exact gradients: J(Df)=kappa*Df at the free source, cancelling Z0=-kappa rather than adding to it.

The finite-source connection transport semigroup satisfies the generator integral identity by finite-dimensional Ito/Dynkin on smooth fields. Adding continuous bounded M_n-U+E_n preserves that identity by bounded perturbation. Once the box contains all input/output supports of F and support(U), this is a finite-dimensional computation; M_n F may spread through the box but has only finite output. C2 log potentials give C1 drift; the Hessian is used ONLY as a bounded continuous multiplier. No differentiation of it is involved.

The actual source input from the pointwise-core construction is strong convergence of the connection transport semigroups S_n on B uniformly on bounded intervals. Its construction uses original synchronous path comparison and fixed-link parallel-transport stability, NOT tilted force uniqueness. Strong convergence of M_n just verified and uniform bounds pass the bounded-perturbation Dyson series. For each fixed vector this yields

T_n(t)=exp(tE_n)H_(n,U,t) -> T(t)=exp(tE)H_(U,t)

strongly uniformly on bounded intervals, with ||T_n(t)||,||T(t)||<=exp(-gt). Moving vectors in Dyson terms are controlled by compact time images and finite nets, or one-at-a-time splitting as in Proof B.

For F in the cylinder core, A_(B,n)F->A_BF follows from the fixed finite derivative support and local uniform beta recovery. JF is unchanged, and Z_nF->ZF by the preceding multiplier argument. Thus g_n(F)->G0F in B. All of H3-H4 now reduce to the stated original-path/parallel-transport input and finite generator calculation, not an assumed identity for the limiting generator.

### Upstream assumptions retained, not silently certified

| Hypothesis | Source argument checked/mapped | Remaining status |
|---|---|---|
| Retained interaction and uniform C2/Hessian bounds | Fourier norm and global h; beta block bound expanded above | Actual interaction fixed-point theorem remains an upstream analytic candidate |
| Original scalar C(X) operator core | Finite resolvents u_n, residual <=2kappa R/(alpha-3kappa R)*a0^-distance*M(f), then finite C2 smoothing | Requires the existing original gradient comparison; not derived from form-core density |
| Scalar reverse Poincare | Finite weighted curvature and closed derivative passage | Original semigroup/curvature input retained |
| Strong connection semigroup convergence | Original path comparison and linkwise parallel-transport BDG stability | Analytic input of the pointwise-core construction; not an independent external review here |
| Bounded multipliers on B and convergence | Finite-head/weighted-column-tail argument above | Conditional proof supplied here |
| Finite generator and limiting extension identity | Frame calculation, Dynkin/bounded perturbation and Proof B | Conditional proof supplied here |
| Ground-vector and first derivative | Weighted log-filter localization and the convergent one-form integral | Existing input, not inferred merely from a spectral gap |

The original finite resolvents need not be smooth for merely C2 coefficients. Approximate them in C2 on their finite compact products, with errors chosen small enough for each finite graph residual. The graph-range proof, not the phrase 'elliptic smoothing', supplies the scalar operator core. Nothing in this new lemma replaces that upstream obligation.

## 5. Apply the abstract range theorem

Pointwise Cauchy-Schwarz gives ||JF||<=sqrt(3)*kappa*||partial F||. From the block bound and Schur estimate,

||Z||<=b=kappa*(1+4R)+2delta.

Let x=b/kappa and alpha=64kappa*(1+x)^2. Then

q<=sqrt(3pi*kappa/(2alpha))+b/alpha
<=5/[16(1+x)]+x/[64(1+x)^2]
<=81/256<1/2.

The rational envelope uses pi<4,sqrt(6)<5/2 and x/(1+x)^2<=1/4. T is exponentially stable, so alpha is in its resolvent set. All premises of the identification lemma are now accounted for, conditional on the explicitly retained upstream inputs. Therefore

D(G)=D(A_B), G=-A_B+J+Z,

and localized smooth cylinder fields form its graph core.

For v=Dpsi, the already constructed Bochner identity is

v=-integral_0^infinity T(t)(psi DU)dt.

Since G is exponentially stable, the integral is minus its zero-resolvent. Therefore v belongs to D(G), Gv=psi DU, and hence v belongs to D(A_B). Only after this conclusion use partial(alpha+A_B)^-1 to infer partial v in C(HS). Product differentiation gives partial r=psi^-1 partial v-r tensor r. This is the claimed legitimate order of reasoning.

## 6. Actual-source HS/domain guard

The audit's counterexample can be made explicit on the same free SU2 lattice. Choose disjoint plaquettes p_n and normalized spin-n characters phi_n=chi_n(W_(p_n))/(2n+1). Let

f=sum_(n>=1)(1-phi_n)/n^3.

Uniform convergence follows from |phi_n|<=1. Frame derivatives of normalized representations give ||Dphi_n||<=4n and ||Hess phi_n||_HS<=12n^2. Disjoint supports imply uniformly convergent ell2 gradient and HS Hessian tails, so these fields are continuous in the product topology. At the identity, the exact Hessian block has HS square16[n(n+1)]^2/3; after the coefficient n^-3 its squares are summable.

But P_t phi_n=exp[-4kappa*n(n+1)t]phi_n, and f(identity)=0. Hence

(P_t f(identity)-f(identity))/t
=sum_n (1-exp[-4kappa*n(n+1)t])/(n^3*t) -> infinity

by nonnegativity and divergent sum4kappa sum_n(1/n+1/n^2). Thus f is not in D(A_C). This validates the audit's guard while showing why the resolvent-domain proof above does extra work. The counterexample is not an actual tilted ground vector and does not falsify the just-proved conditional inclusion.

## 7. Finite controls and continuation

The checker freshly replays the v2 net/scaling controls, checks rational Neumann envelopes, actual free-SU2 constant/plaquette-gradient mode identities and zero-resolvent signs, a noncommuting inverse/graph factorization, moving-input and missing-column-tail rivals, and dyadic harmonic divergence controls. Exact arithmetic does not certify the infinite-dimensional lemma or its upstream source inputs.

Next: the already open R4 parameterized compatible-disintegration lemma. No new localization or perfect-flow task is manufactured. Independent external R1-R4 review and the continuum/physical/reviewed-root gates remain open; the conditional retained-window physical obstruction and nonconstant infinite-horizon density obstruction stay closed in their stated scopes.

Contract: `contracts/yang-mills-one-form-domain-audit.v1.json`.
Checker: `checkers/check_yang_mills_one_form_domain_audit.py`.
Receipt: `results/yang-mills-one-form-domain-audit-v1.json`.
Frozen predecessor notes and v1/v2 programme snapshots are unchanged.
