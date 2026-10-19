# Clock-independent spatial-scaling criterion with explicit observer budgets

Owner: `marici.Kitaev`. Spatial-scaling batch iteration1/10. This is a conditional theorem about specified equal-time multiplication observables,not a continuum Yang-Mills or universal triviality theorem.

## DPC and disposition

**Problem.** An energy/time dictionary alone cannot decide whether the retained lattice vacua acquire a physical spatial scale. Which actual observables can have nonzero connected limits at fixed physical separation,including growing supports and normalization factors?

**Conjecture.** The source's uniform spatial covariance estimate forces such correlations to vanish whenever the product of single-link oscillation budgets is subexponential in inverse spacing. This is unaffected by rescaling the whole Hamiltonian's clock. Exponential extended-observable normalization lies on a distinct boundary and must not be dismissed by this theorem.

**Rivals.** Call decreasing spacing a continuum construction without specifying observables; rescue spatial correlations by changing only the clock; ignore support growth; assume a polynomial plaquette normalization is already a proven continuum field; extrapolate the theorem to arbitrary exponential loop renormalizations or electric/noncommuting observables.

**Risky consequence.** A quantitative support/budget criterion,an actual plaquette-smear class with polynomial-log normalizations,and an exponential budget necessary for nonzero separated correlations if the retained covariance premise survives.

**Falsification.** A positive binary Markov-chain analogue has exponentially small bare correlations but exponential endpoint normalization gives covariance1 at the selected physical separation. Its earlier-distance covariance diverges. This does not construct an admissible continuum theory; it refutes dropping the budget assumption. Source lattice geometry,plaquette incidence and exact rational tail planners are checked separately.

**Disposition.** The scoped criterion and plaquette application are proved below at written conditional scope. The genuine macroscopic Wilson-loop/perimeter-renormalization boundary remains a next executable source question. No physical source change is admitted,independent analytic review remains open,and old frozen proofs are unchanged.

## 1. Remove the overall clock without claiming a new physical matching

Write eta=lambda/kappa. At every finite box,

H_(kappa,eta)=kappa*Hhat_eta,
Hhat_eta=sum_e(-Delta_e)+eta*sum_p(1-(1/2)Tr W_p).

For kappa>0, multiplication of the WHOLE Hamiltonian by kappa changes energies but not its normalized positive ground vector. Thus the actual equal-time state nu_(Lambda,eta),and its thermodynamic cylinder limit nu_eta,depend on eta rather than the overall clock factor. No global infinite Haar ground density is used in this argument.

Changing kappa while holding lambda fixed changes eta and is NOT a pure clock change. Holding an auxiliary probe U fixed while scaling the other terms also changes a dimensionless source. This note concerns the original unperturbed magnetic vacuum family only.

The covariance result below contains neither kappa nor a physical-time convention. It therefore survives any rescaling of the entire Hamiltonian that preserves eta and the observable definitions.

## 2. Source spatial estimate retained as an explicit premise

Let h>0 denote physical spacing; a0=4/3 is the unrelated source weight. Let eta_h vary arbitrarily in0<=eta_h<27/262144. The written source interaction/clustering construction gives R_h=(4096/3)eta_h<9/64 and alpha_h=8R_h/9<1/8.

For real continuous cylinder F,G of disjoint link supports K,L,define

Delta_i(F)=sup{|F(x)-F(y)|: x and y differ only at link i},
Osc(F)=sum_i Delta_i(F).

The source Dobrushin estimate is

|Cov_(nu_eta)(F,G)|
<=alpha_eta/[4(1-alpha_eta)] * Osc(F)*Osc(G) * (3/4)^d(K,L)
<= [Osc(F)*Osc(G)/28]*(3/4)^d(K,L).

Its analytic inputs are the actual vacuum interaction and the source comparison theorem,not a gap or an arbitrary Gibbs surrogate. This note assumes that estimate rather than independently certifying its upstream proof. The same finite-free-box estimate follows from the same finite conditional influence majorants; alternatively one may use only the already defined thermodynamic state at each eta_h. No uniform convergence in eta or identification of different Hilbert measures is needed.

## 3. Physical support geometry

Embed each positive link by its midpoint in h*Z3. Two links in one elementary plaquette have midpoint Euclidean distance at most h: opposite edges attain h and adjacent edges have distance h/sqrt(2). Consequently

h*d(i,j)>=|mid_h(i)-mid_h(j)|.

For the ACTUAL link supports K_h,L_h,put r_h=dist(mid_h(K_h),mid_h(L_h)). If r_h>0 then d(K_h,L_h)>=r_h/h. With c0=log(4/3),

|Cov_(nu_eta_h)(F_h,G_h)|
<= [Osc(F_h)*Osc(G_h)/28] * exp(-c0*r_h/h).

Physical regions specified by plaquette CENTERS must first be thickened to include their edges. For disjoint fixed regions with positive limiting separation,one may choose any smaller fixed r>0 and obtain r_h>=r eventually. Center separation is not silently identified with support separation.

## 4. Budget theorem and its necessary converse

Fix reader amplitude units once,independently of h,and let

B_h=max(1,Osc(F_h)*Osc(G_h)).

Fixed changes of those units do not affect the following exponential rate. Assume liminf_(h->0)r_h>=r>0 and let gamma=limsup_(h->0) h*log B_h. If gamma<c0*r,then

Cov_(nu_eta_h)(F_h,G_h)->0.

Proof: choose epsilon>0 with gamma+2epsilon<c0*r. Eventually h log B_h<=gamma+epsilon and r_h>=r-epsilon/c0. The preceding bound tends to0 exponentially. Equivalently the logarithmic limsup is at most gamma-c0*r. Zero covariance values cause no problem and need not have a logarithm.

In particular,if h log B_h->0,all fixed positive support separations have vanishing connected two-point limits. Polynomial-log budgets B_h<=C*h^-p*(1+|log h|)^q with finite fixed p,q satisfy this condition. Supports may grow without bound in lattice units; their cost is counted in Osc.

Conversely,if along a sequence |Cov|>=epsilon>0,the same inequality forces

Osc(F_h)*Osc(G_h)>=28*epsilon*exp(c0*r_h/h).

Thus a nonzero separated limit requires at least an exponential oscillation budget,unless the source spatial estimate,physical support separation,or declared observer class changes. This is a NECESSARY condition,not a construction or a sufficient condition for a continuum theory. At gamma=c0*r the upper envelope need not tend to0; above that threshold the estimate is inconclusive,not evidence that the actual covariance grows or survives.

For fixed local readers and their translations,the estimate supplies a uniform exponential-decay envelope with a lattice correlation-length upper bound1/c0 (when that length is defined from the decay rate). It is not an exact physical mass measurement. The explicit varying-reader theorem,not that shorthand,is what controls refinement.

## 5. Actual gauge-invariant plaquette-smear class

Let w_p=(1/2)Tr W_p in[-1,1]. A square has four distinct links and changing one such link changes w_p by at most2. Consider

F_h=Z_h*h^3*sum_(p in P_h) f(x_p)*(w_p-nu_eta_h(w_p)),

with finite plaquette set P_h,real weights f and scalar normalization Z_h. Centering constants change no oscillations. The triangle inequality gives

Osc(F_h)<=8*|Z_h|*h^3*sum_(p in P_h)|f(x_p)|.

This counts actual plaquette incidences,not a continuum differentiability assumption. For unit cubic regions resolved by h=1/N,there are3(N+1)N^2 plaquettes,so h^3*|P_h|=3(1+1/N)<=6 and

Osc(F_h)<=48*||f||_infinity*|Z_h|.

Take two such physically separated regions. If Z_h and the analogous normalization for G have polynomial-log growth,these actual source readers lie in the vanishing class. In the illustrative Z_h=h^-4 case for both readers,the product budget is at most2304*||f||_infinity*||g||_infinity*h^-8. Exponential spatial decay beats that polynomial.

This proves a statement about that PLAQUETTE-BASED CANDIDATE. It does not identify it with a renormalized continuum Tr(F^2),nor prove that a continuum field must have precisely this normalization. More general smearings qualify whenever their stated sums and normalizations give the required budget. Contact terms and coincident-support limits are outside the separated-support conclusion.

## 6. Macroscopic loops: an explicit boundary,not a forbidden escape by fiat

For a normalized SU2 trace of a closed word C_h,|w_(C_h)|<=1 and

Osc(w_(C_h))<=2*|distinct link support|<=2*word_length(C_h).

Thus unrenormalized loops of polynomial word length also satisfy the criterion when their physical supports remain separated. For a proposed multiplicative perimeter normalization Z_h=exp(mu*P/h),however,the oscillation budget can be exponential. The theorem may then be inconclusive. Such an ansatz neither changes the source state nor by itself proves finite correlations,positivity,locality or a continuum observable.

A positive finite analogue shows why the assumption cannot simply be dropped. Take a stationary binary Markov chain with mean0 and correlation rho^d,rho=1/64. For spacing h=1/(2N),endpoints distance2N have physical separation1. Renormalize EACH endpoint spin by Z_N=rho^-N. Their covariance is exactly1. At separation1/2 it is rho^-N and diverges; at separation2 it is rho^(2N) and vanishes. The endpoint joint law (1+rho^d*s*t)/4 is normalized and positive. This is not SU2 and not a continuum witness: it demonstrates the logical limitation of the upper bound and unconstrained normalization.

NEXT executable source issue: determine what the ACTUAL retained SU2 expansion says about macroscopic Wilson-loop expectations and connected readers under a stated perimeter-normalization task. Supply a source-derived estimate or locate the precise additional area/perimeter/normalization bound needed. Do not import an area law from an isotropic Wilson regulator,claim N2 support control automatically supplies minimal-surface order,or declare the loophole closed from the current upper bound alone.

## 7. What a successor must change,and what is not proved

Clock rescaling alone cannot affect any equal-time conclusion above. To obtain nonzero separated correlations for these declared readers,a successor must invalidate at least one used premise: uniform source spatial decay,subexponential observer budget,positive physical support separation,or this multiplication-observable specification. Leaving the window may allow changed estimates,but no new trajectory is constructed here. Crossing a sufficient-bound endpoint is not evidence of an actual critical point.

The theorem does not cover arbitrary electric/noncommuting operators,all Wilson-loop renormalizations,all distributional limits or higher correlations. It does not establish four-dimensional covariance,reconstruction,interacting nontriviality or Yang-Mills triviality. Such promotion requires a faithful observable/state bridge and separate analytic work.

## 8. Verification and continuation

The checker freshly replays source clustering controls and the R4/predecessor controls,then checks48 actual midpoint geometry packets,12 actual finite-box plaquette incidence/budget packets,48 exact polynomial-tail planners,48 exponential-envelope classifications and12 positive-chain renormalization controls. These finite controls do not certify the upstream SU2 cluster theorem or the continuum argument.

The scoped spatial-budget issue is resolved at written conditional scope. The macroscopic-loop/perimeter boundary is a nonredundant executable successor,so this iteration does not stop the new plan. Independent source review and parent physical/continuum/root gates remain open.

Contract: `contracts/yang-mills-spatial-scaling-budget.v1.json`.
Checker: `checkers/check_yang_mills_spatial_scaling_budget.py`.
Receipt: `results/yang-mills-spatial-scaling-budget-v1.json`.
