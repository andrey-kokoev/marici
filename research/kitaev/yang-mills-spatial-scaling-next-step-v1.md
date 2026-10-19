# Incoming literature follow-up: convention clarification and next priority

Owner: `marici.Kitaev`. Coordination/proof-obligation handoff accompanying spatial-scaling iteration1/10. This records the operator-forwarded report,not independent verification of its bibliography or certification of its proposed theorem.

## Source convention

The actual source has one positive-orientation variable per geometric edge and3L(L-1)^2 geometric plaquettes in an L-by-L-by-L vertex box. The finite source enumeration uses each axis pair i<j once. Thus c_p=1 for this source; an orientation assigned to a square does not duplicate its potential term.

Under the ADDITIONAL canonical weak-field convention U_i=exp(a*g_H*A_i^a*T_a+...),Tr(T_aT_b)=-delta_ab/2,and continuum magnetic energy(1/2)integral sum_(i<j,a)(F_ij^a)^2,

1-(1/2)Tr U_ij = (a^4*g_H^2/8)sum_a(F_ij^a)^2 + higher orders.

The sum over geometric squares then gives lambda=4/(a*g_H^2),while the usual electric matching is kappa=g_H^2/(2a). Hence eta=8/g_H^4 and the retained eta<27/262144 window implies g_H^4>2097152/27. Conditional on the full physical source gap and this matching,

gap>40*sqrt(2)/(sqrt(27)*a).

This is a bare-convention clarification,not a nonperturbative regulator equivalence or quantum anisotropy calibration. The earlier40/sqrt(27) note remains a mathematically conditional statement under its explicitly stipulated lambda=2/(a*g^2); it must not now be presented as the verified standard matching for the once-counted source. Changing the source plaquette multiplicity instead would require rechecking the interaction smallness constants. Do not edit frozen predecessors to conceal this distinction.

## New candidate obstruction: arbitrary clocks and propagation

Let H_a=kappa_a*K0+lambda_a*V0 after any scalar vacuum subtraction. For a positive whole-Hamiltonian clock factor s_a,put sigma_a=s_a*kappa_a and J_a=s_a*lambda_a=sigma_a*eta_a.

The operator-forwarded report proposes the following conditional route. If one centered spectral channel has finite positive-time limit and nonzero value at t*,then along small cutoffs C_a(t*/2)<=C and C_a(t*)>=c>0. The source gap at least5*sigma_a/64 gives

sigma_a <= [128/(5*t*)]*log(C/c).

Thus sigma_a and J_a are bounded when eta_a remains bounded. The on-site electric Casimirs may be unbounded,but the plaquette interactions are bounded and finite range. On the full tensor-product kinematic space,one should establish an interaction-picture Lieb-Robinson estimate and then restrict to gauge-invariant observables/physical states. The displayed target form is

||[tau_t(A_a),B_a]|| <= prefactor_a*exp(v_mu*J_a*|t|-mu*r/a),

with support geometry,constants and the norm/support prefactor explicitly derived. This would suppress finite-time propagation for polynomially controlled local readers at positive physical separation. A nonzero limiting timelike commutator is an ADDITIONAL target witness requiring a compatible observable/state limit; its existence is not inferred here.

The incoming report cites Nachtergaele-Sims(2014) and Nachtergaele-Sims-Young(2019) for unbounded-on-site locality tools. These references are supplied leads,not freshly primary-source-verified by this session. The finite-volume interaction-picture/norm estimates can be audited directly.

## Exact next executable obligation

1. Verify the full physical gap premise and the two-time clock inequality at its declared scope.
2. Compute the actual plaquette interaction norm and incidence constants after subtracting irrelevant scalar terms. Do not treat the unbounded electric term as a bounded interaction.
3. Establish the finite-volume locality inequality uniformly over volume,with physical midpoint distance and the observable norm/support budgets visible.
4. Explain why full kinematic bounds restrict to gauge-invariant physical readers even though the physical Hilbert space is not a tensor product.
5. State the precise convergence/nontriviality witness needed to turn the estimate into a conditional continuum no-promotion result. Do not claim that vanishing commutators alone excludes every continuum or contact/topological limit.
6. Check whether finite exponential perimeter budgets can also be covered by choosing a larger FIXED exponential locality weight. Finite-range interactions suggest this possibility,but its constants and quantifiers must be proved rather than assumed. Arbitrary superexponential budgets are not automatically covered.

This general-clock/locality test is now higher priority than the selected loop-specific static audit because it addresses the next physical escape route with the actual bounded Hamiltonian interactions. Defer the loop estimate pending that result,not because the loop loophole is disproved. Reenable it if the locality theorem or its observer map leaves an actual extended-reader task unresolved. No waiting leaf is needed.

## What already passed this turn

`yang-mills-spatial-scaling-budget-v1.md` proves the conditional static spatial-budget criterion and polynomial plaquette application. Its168 new controls and SCC checks pass,with source/predecessor controls replayed. That result remains independent of the disputed physical clock/matching. No analytic source review,continuum construction,commit or push is claimed.
