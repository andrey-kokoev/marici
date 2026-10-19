# Arbitrary clocks: finite-energy survival versus physical propagation

Owner: `marici.Kitaev`. Spatial-scaling iteration2/10. Selected issue: `issue-tree:87b983be841a61be1b85d24a:arbitrary-clock-locality:v1`.

## DPC and disposition

**Problem.** Can a whole-Hamiltonian clock rescaling retain nonzero finite-energy correlations in the source window while also retaining propagation across positive physical distances?

**Conjecture.** A nonzero finite positive-time spectral channel bounds the rescaled electric coefficient. Bounded eta then bounds the actual finite-range interaction strength. An explicit interaction-picture locality estimate forces all covered separated commutators to vanish at every fixed finite time. The estimate covers finite exponential,not just polynomial,norm/support budgets.

**Rivals.** Bound the unbounded electric Casimir as an interaction; count both orientations of a geometric plaquette; omit scalar subtraction and confuse its volume cost with propagation; use a physical-sector tensor factorization; claim a nonzero Euclidean channel automatically supplies a nonzero timelike commutator; promote vanishing commutators of a selected family to universal Yang-Mills triviality.

**Risky consequence.** A conditional arbitrary-clock obstruction with explicit4/16/32 incidence/path constants,a physically separated bounded-operator class including finite perimeter exponentials,and a precise additional limiting-commutator witness. No continuum existence or observable comparison is created by this theorem.

**Falsifiers.** A free SU2 plaquette channel has nonzero finite positive-time correlations while disjoint supports commute at all times: the dynamical witness is genuinely additional. A finite reducing-sector counterexample has compression-commutator defect1 if observables do not preserve the physical subspace. Positive-time ratio fixtures reject unbounded clock rates. Exact checks do not certify the analytic gap or infinite-cutoff theorem.

**Disposition.** The conditional gap/locality theorem is established below at written-proof scope. Actual source constants and gauge restriction are verified without importing an unverified literature theorem. The next executable issue is the relativistic spectral/nontriviality and observer-limit bridge: when does a proposed faithful continuum channel have the missing nonzero commutator witness? The deferred loop-static expectation task is not declared refuted.

## 1. One regulator,one clock,and the gap premise

For each spacing h choose an actual finite open cubic source box Lambda_h and its physical gauge-invariant Hilbert subspace. All statements concern the SAME source for the spectral and dynamical readers. Assume its physical vacuum-energy-subtracted Hamiltonian has the previously claimed full form-domain gap

H_h-E0_h >= c0*kappa_h*(I-Pvac_h), c0=5/64.

This is an upstream unreviewed analytic premise,not a gap inferred from one observable. The underlying source is

H_h=kappa_h*sum_e(-Delta_e)+lambda_h*sum_p(1-w_p),
w_p=(1/2)Tr W_p, eta_h=lambda_h/kappa_h<=eta_star,
eta_star=27/262144.

The source sufficient window is strict at eta_star; the non-strict constant eta_star is only a uniform upper envelope here. The argument actually applies to any bounded eta interval with the same kind of positive gap-to-electric coefficient.

For any positive clock factor s_h put

Htilde_h=s_h*(H_h-E0_h), sigma_h=s_h*kappa_h, J_h=s_h*lambda_h=sigma_h*eta_h.

The Euclidean spectral and real unitary parameters below are both those of Htilde_h. No equality between stochastic-quantization time and physical time is assumed.

## 2. A finite positive-time channel bounds the clock

Let v_h be a physical Hilbert vector orthogonal to the whole declared vacuum sector; its norm may depend on h without a uniform bound. Put

C_h(t)=<v_h,exp(-t Htilde_h)v_h>.

Suppose for some FIXED t*>0 and constants C>=c>0,

C_h(t*/2)<=C, C_h(t*)>=c

eventually. Finite positive-time limits with a nonzero later limit imply such bounds (one may choose C>c). The spectral theorem and the full gap give

c<=C*exp[-(5/128)*sigma_h*t*],
sigma_h<=S*:=[128/(5t*)]*log(C/c).

Therefore J_h<=J*:=eta_star*S*. If C=c then positive sigma is incompatible with those exact bounds; no division by a missing positive margin is hidden. These are bounds in the chosen clock,independent of the earlier disputed bare physical matching.

## 3. Actual interaction norm and unbounded-on-site removal

Work FIRST on the full finite kinematic tensor product of link L2(SU2) spaces. Remove the scalar J_h*number_of_plaquettes from the rescaled potential; scalar shifts change neither commutators nor energy gaps. The remaining interaction is

Phi_p=-J_h*w_p, ||Phi_p||=J_h.

Indeed the normalized SU2 trace ranges over[-1,1],and both endpoints occur by varying one link with the others identity. The original unshifted plaquette potential has norm2J_h; its scalar part does not propagate information.

Let K_h=sigma_h*sum_e(-Delta_e). It is an unbounded self-adjoint ON-SITE operator. At fixed finite box the full Hamiltonian is its bounded self-adjoint perturbation,so unitary evolution exists on its self-adjoint domain. Factoring its product on-site unitary gives an interaction-picture evolution generated by

Phi_p(t)=exp(itK_h)*Phi_p*exp(-itK_h).

These operators are self-adjoint,bounded by J_h,strongly continuous and still supported on the same four links. Their operator-norm continuity is NOT required. Bounded strongly continuous interaction-picture generators have the strong Dyson/Duhamel identities on each finite-volume Hilbert space. All subsequent estimates use their norm bounds,not ||K_h|| and not a norm derivative of its on-site action.

For fixed final t,the original Heisenberg operator is the interaction-picture evolution of exp(itK_h)A exp(-itK_h),which has the same support and norm as A. Thus any interaction-picture bound uniform over bounded operators on a support applies to the full dynamics. This avoids differentiating an arbitrary bounded A against the unbounded electric Hamiltonian.

## 4. Finite-volume commutator recursion with explicit constants

Let X,Y be disjoint finite link supports and B supported on Y. In the interaction picture define

C_B(X,t)=sup_(A supported X,||A||<=1)||[alpha_(t,0)(A),B]||.

Jacobi's identity and unitary variation of constants give,for t>=0,

C_B(X,t)<=C_B(X,0)+2J_h*sum_(p intersecting X) integral_0^t C_B(p,u)du.

To justify the inequality,for fixed A only interactions meeting X contribute to [Phi(u),A]. The derivative of its evolved commutator is a homogeneous commutator with the bounded sum of those evolved interactions,plus the inhomogeneous terms [alpha(A),[alpha(Phi_p(u)),B]]. The homogeneous part is unitary conjugation and costs no exponential norm factor; each inhomogeneous term is bounded by2||A||*||[alpha(Phi_p(u)),B]||. Taking the supremum gives the displayed recursion. One can first test on vectors and a countable strong-star dense subset of each bounded local unit ball (finite-volume Hilbert spaces are separable); norm lower semicontinuity makes the sup measurable. No unbounded-generator commutator domain is invoked.

Each source link lies in at most4 geometric plaquettes. Each plaquette meets at most16 plaquettes by counting4 links times4 incidences; repeated counting is an upper bound. In the plaquette-sharing LINK graph every plaquette has diameter1. A chain of n intersecting plaquettes from X to Y therefore requires n>=d(X,Y).

Iterating the recursion and using C_B(Z,0)<=2||B||*1_(Z intersects Y),the weighted chain count a_n satisfies

a_n(X,Y)<=4|X|*16^(n-1)*J_h^n, n>=1,
a_n=0 for n<d(X,Y).

The remainder after N iterations is at most (|X|/2)||B||*(32J_h*t)^N/N!,hence tends to zero. Uniformly over the finite box,

||[tau_t(A),B]||
<= (|X|/2)*||A||*||B||*sum_(n>=d(X,Y))(32J_h*|t|)^n/n!.

Negative times use the reversed strongly continuous interaction with the same supports and norms. The scalar vacuum subtraction changes no unitary commutator.

For ANY fixed mu>0 and d>=1,the tail is bounded by

sum_(n>=d)x^n/n! <= exp(-mu*d)*(exp(x*exp(mu))-1).

Consequently

||[tau_t(A),B]||
<= (|X|/2)*||A||*||B||*exp(-mu*d(X,Y))
   *(exp(32*exp(mu)*J_h*|t|)-1).

The constants4,16,32 are deliberately conservative. There is no dependence on box volume or sigma_h outside J_h. This is the required finite-range locality proof; external locality references remain useful cross-checks but are not silently substituted for this derivation.

## 5. Gauss restriction is a reducing-subspace operation

Let P_G be normalized vertex gauge averaging on the finite full tensor product. The electric Casimirs and plaquette traces commute with it. If A,B are bounded gauge-invariant local operators,they and their adjoints preserve the physical subspace,so P_G reduces both.

Thus the physical commutator is the restriction of P_G[tau_t(A),B]P_G and its norm cannot exceed the full kinematic bound. The physical Hilbert space need NOT factorize over links. We do not insert P_G into each interaction and then pretend those compressed interactions retain tensor supports.

The spectral hypothesis in section2 is needed only on the physical subspace. No unproved full-kinematic gap is imported to apply the locality argument. Non-gauge-invariant operators need not obey this compression identity; a finite matrix counterexample is included in the controls.

## 6. Physical separation and finite-exponential observer budgets

Use actual link midpoints at spacing h. A graph step within one plaquette moves a midpoint by at most h,so d(X_h,Y_h)>=r_h/h,where r_h is the actual physical support separation. Assume liminf r_h>=r>0. Define the norm/support budget

N_h=max(1,(|X_h|/2)*||A_h||*||B_h||).

Fix amplitude units independently of h and assume

gamma:=limsup_(h->0) h*log N_h < infinity.

This includes polynomial budgets and finite exponential perimeter budgets; e.g.norms bounded by powers of h times exp(gamma_A/h),exp(gamma_B/h),with polynomial support cardinality. Choose one FIXED mu>gamma/r. With J_h<=J* and |t|<=T,the time factor exp(32 exp(mu)J*T)-1 is finite and independent of h. Therefore

sup_(|t|<=T)||[tau_t(A_h),B_h]|| ->0.

Unlike the static Dobrushin bound,the finite-range locality weight mu can be arbitrarily large. Its large constant must be retained,but for fixed r,gamma,T it does not affect the cutoff limit. Thus finite exponential perimeter normalization does NOT by itself evade this dynamical bound. No uniformity over arbitrary r->0,T->infinity or gamma->infinity is asserted. Arbitrary superexponential observer budgets are not covered by the stated criterion.

## 7. Exact conditional continuum obstruction and missing witness

Suppose the SAME cutoff family has the positive-time channel of section2 and bounded gauge-invariant local reader families with the supports/budgets of section6. For arbitrary normalized physical vectors u_h,v_h,

|<u_h,[tau_t(A_h),B_h]v_h>|<=||[tau_t(A_h),B_h]|| ->0,

uniformly on compact time intervals. Time-smearing with fixed integrable compactly supported weights also tends to zero. If an actual state/observable comparison identifies these matrix elements with a continuum commutator distribution,that continuum witness is zero. A proposed target with a nonzero such timelike witness is therefore incompatible with these premises.

This is a TWO-witness conditional theorem: one finite nonzero Euclidean spectral channel bounds the clock; a second state/observable comparison with nonzero continuum commutator would contradict locality. The latter is not automatically supplied by the former. No spatial-refinement maps,Wightman distributions,continuum field domains or Lorentz covariance are constructed here. Nor is a thermodynamic/local limit order exchanged: the estimates apply to any finite-box net; a claimed thermodynamic interpretation must use its actually identified local matrix elements.

An actual free-source guard makes the distinction concrete. At eta=0,for w=(1/2)Tr W_p,Peter-Weyl orthogonality gives mean0 and norm square1/4; the four-link electric excitation energy is3sigma. Therefore its Euclidean vacuum correlation is (1/4)exp(-3sigma*t),finite and nonzero at all positive times for fixed sigma. Yet the on-site product dynamics leaves supports fixed,and disjoint supports commute at EVERY time. This is not relativistic propagation. It refutes treating a nonzero temporal channel as the missing dynamical witness.

## 8. Convention correction is separate from the arbitrary-clock proof

The actual source counts geometric squares once. Under the stated canonical bare matching kappa=g_H^2/(2h),lambda=4/(h*g_H^2),eta=8/g_H^4,the source window implies g_H^4>2097152/27 and the conditional gap floor is40*sqrt(2)/(sqrt(27)*h). The earlier lambda=2 conditional note remains unchanged under its own declared premise. None of this proves nonperturbative anisotropy calibration or identifies Hamiltonian g_H with an isotropic Wilson parameter.

The arbitrary-clock theorem does not need either matching: it uses only the physical gap-to-electric floor,bounded eta,a positive-time channel and the actual finite-range interaction.

## 9. Next necessary bridge,not a manufactured waiting leaf

The clock/locality issue is resolved at written conditional scope. The next executable question is to connect the vanishing separated commutators to a precise relativistic nontriviality criterion,including the observable-limit topology. A useful bounded test is one Hermitian scalar channel: under Lorentz covariance,a relativistic positive-energy spectrum and centered clustering/unique-vacuum hypotheses,does a commutator supported on spatial coincidence force that channel to be trivial? Prove the distribution/spectral implication or locate its missing assumption. State exactly what cutoff-to-continuum reader convergence would license it; do not assume that comparison already exists.

This bridge can decide whether the additional timelike witness follows from a stated target rather than being inserted by hand. It is nonredundant after the present two-witness theorem. The loop-specific static task remains deferred,not disproved; reenable it only if an actual extended-reader normalization problem survives the relevant target test. Independent analytic review and the general physical/continuum/root goals stay open.

Checker controls actual plaquette norms/incidence/path counts,exact series envelopes,clock ratios,finite-exponential budget planners,reducing-sector guards and actual free-source temporal channels. They do not mechanically certify the spectral theorem,strong Duhamel identities or continuum reconstruction.

Contract: `contracts/yang-mills-arbitrary-clock-locality.v1.json`.
Checker: `checkers/check_yang_mills_arbitrary_clock_locality.py`.
Receipt: `results/yang-mills-arbitrary-clock-locality-v1.json`.
