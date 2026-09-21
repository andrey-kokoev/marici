# The rigged Tate response lifts the residual-labelled nonzero attachment

## Result and exact strength

The independently defined all-prime weighted-dual Tate response admits a continuous labelled GRAPH lift of Nima's residual-port coefficient attachment. The lift preserves its paired form, actual relation and balancing kernels, cut refinement, and the explicit observer detecting a nonzero first attachment class.

The source port is retained in this graph. Projection back to it is an explicit inverse on graph letters. This is NOT reconstruction from arithmetic outputs, an output-only semilocal equivalence, or an ordinary L2 realization. Endpoint data, positive response, negative leakage, and the window residual remain distinct labels.

Inputs:
- `../grothendieck/the-all-prime-tate-response-converges-in-a-two-sided-weighted-dual.md`
- `../nima/the-residual-port-restores-the-labelled-two-seam-comparison.md`
- `../nima/an-explicit-residual-observer-detects-the-nonzero-attachment-class.md`

## 1. A graph carrier on the actual common domain

Fix gamma>1/2 and a compact Euler interior K with gamma<eta<=Im z<=Y<beta, |z|<=Z. Use the existing half-line port

    P_K=C(K;D_gamma) direct_sum C(K;H_gamma),

where D_gamma is the unrestricted-trace weighted H1 domain. Write an element as (u,v). The second coordinate v is the WINDOW residual.

Let Atilde_rig:D_br->H_- be Grothendieck's full all-prime response, with H_-=L2(R,exp(-2 gamma|x|)dx). Define bounded maps on D_gamma by

    t_+(u)=restriction_(x>0) Atilde_rig E_+u,
    t_-(u)=restriction_(x<0) Atilde_rig E_+u,
    b(u)=(ell_+(u),ell_-(u)).

The two traces of D_br are independent, so E_+ requires no artificial zero boundary condition. All these maps are applied pointwise to the continuous spectral families.

The graph lift is

    G(u,v)=(u,v; t_+(u),t_-(u),b(u)).

Let G_K be its range, with the sum norm of the retained P_K coordinates, the two C(K;H_- on each half-line) response coordinates, and C(K;C^2) endpoint coordinate with l1 norm. This is a closed Banach graph. The projection

    R(u,v;t_+,t_-,b)=(u,v)

is contractive and inverse to G on G_K. There are no independent choices of t_+, t_- or b on this graph.

For an explicit bound, take

    C_A=C_infty+2 sum_(n>=2) Lambda(n)n^(-gamma-1/2),
    C_b=(2 gamma+1)^(-1/2)+(2 gamma-1)^(-1/2),
    C_G=1+2 C_A+C_b.

The previous rigged theorem supplies C_infty for Atilde_infty E_+:D_gamma->H_-. Then

    ||G(u,v)|| <= C_G ||(u,v)||,   ||R||<=1.

Separate spectral suprema are allowed in this bound. No weighted control norm is inserted into the physical pairing.

## 2. The paired graph form is prescribed by the Tate comparison

For graph elements g=(u,v;t_+,t_-,b) and g'=(u',v';t'_+,t'_-,b'), let t and t' denote their two-sided joined responses. Set

    Q_G(g,g')
      =-1/2 [<E_+u,t'>_0+<t,E_+u'>_0]
       +b^* J_end b'
       +<u,v'>_0+<v,u'>_0.

A bracket with the response in the first slot denotes the conjugate of the reversed test/dual bracket. It is well defined without putting the response in ordinary L2.

The fixed full Tate response is Hermitian on its test domain in the unweighted dual pairing. The supplied limiting compression identity therefore gives

    Q_G(G(u,v),G(u',v'))
      =q_ar(u,u')+<u,v'>_0+<v,u'>_0
      =Q_res((u,v),(u',v')).

Thus G is a paired isomorphism onto its GRAPH image. If B=max(1,2 C_ar) is the existing residual-port form bound, Q_G has the same bound B in the graph norm because R is contractive.

Negative-side leakage does not enter this positive-test pairing, but is retained, not set to zero. Any additional negative test h_- in the corresponding positive-weight space observes it by the bounded functional <h_-,t_->_0. This explains exactly what the scalar paired identity does and does not observe.

## 3. The actual source letter map and its radius bound

Keep the supplied source-defined ports

    U_f(z)=sqrt(2) X_f(z) exp(i z x),
    V_f(z)=W_f(z)-L_ar U_f(z).

Define the lifted letter by

    Psi_rig(f)=G(U_f,V_f).

It retains the original ordered spectral arguments. It is linear and bounded, with

    ||Psi_rig(f)|| <= C_G C_Psi ||f||_beta.

Here C_Psi is the explicit compact-spectral constant in the supplied residual-port theorem. No division by a window amplitude or reconstruction from a response is used.

On a record with m retained slots, apply G to EVERY retained feature, including features in coefficient buffers as well as seams. Keep vacua, endpoints, physical multipliers, edge labels and external root factors unchanged. Projective tensoring gives

    ||G_records x||_(s,b) <= ||x||_(s,C_G b),
    ||R_records y||_(s,b) <= ||y||_(s,b).

These are inverse maps on the declared all-feature-radius completion scales. At a single fixed radius the forward bound may require a larger INPUT radius; no isometry of fixed-radius Hilbert completions is claimed.

The forcing-to-graph substitution similarly costs at most max(1,C_G C_Psi)^m. It therefore has the same factorial and inherited actual-letter source domains as the supplied attachment, at the displayed enlarged radii. No new factorization lift for a different source completion is inferred.

## 4. Actual source kernels and the attachment chain map

The maps G_records and R_records commute with ordered concatenation, tensor reassociation, and moving a feature between seam and memory. The differential's physical multiplier tau/sqrt(w_seam) is unchanged.

Consequently they are inverse coefficient-complex chain maps on the specified completed scales. The graph differential and normalization are the same labelled operations on graph letters, not operations defined by a scalar Gram fit.

More explicitly, linearity preserves every original zero formal terminal record, including the diamond

    a+(b+c)-(a+b)-c=0.

Associativity preserves the existing action-balancing relations. Thus D_rig and D_(2,rig) are the actual derivatives after substitution and satisfy

    D_rig(I^2)=0,
    D_(2,rig)(ab)=D_rig(a) tensor_balanced D_rig(b),  a,b in I,
    D_(2,rig)(I^3)=0.

They annihilate the OLD source kernels; no new ideal is defined from the response form.

For the common first attachment roof, with source model K_src=[I^2/I^3 -> I/I^3], define

    F_rig^(-1)(p)=(0,D_(2,rig)(p)),
    F_rig^0(e)=(D_rig(e),0).

Then F_rig=G_records F_Psi and R_records F_rig=F_Psi, with the original shifts and connecting projection unchanged. Density and the radius estimates extend these equations to the specified source completions.

## 5. Cut refinement and place exhaustion

Artificial-cut normalization obeys

    N_rig G_external=G_balanced N_Psi.

This follows slotwise from ordered concatenation, including coefficient buffers. The original cut-l1 estimates are unchanged after the feature-radius enlargement. Source-generated pairings and the total collision-current identities transport because their individual slot forms agree.

For a window refinement, U is additive and V retains the existing transported-tail boundary difference. Applying the bounded linear graph maps transports these identities without resetting any tail. The response coordinates are additive images of U; the window residual remains its own coordinate. No claim identifies separate bulk/forcing current labels with arithmetic summands.

For finite prime sets, use the same ambient coordinate carrier but replace Atilde_rig by Atilde_P in G. If P contains all primes <=N, the sharper supplied positive/negative response bounds give

    ||G_P-G||_(P_K -> ambient) <= 3 T_N,

where T_N is the cutoff majorant from the rigged theorem. The u, v and endpoint coordinates do not change. For a fixed m-slot record, telescoping its tensor product gives an error at most m C_G^(m-1) 3 T_N times the old record norm. Enlarging the input feature radius beyond C_G b absorbs m and proves convergence on the declared scales.

For clarity: with v held at its ALL-PRIME value, the finite-P graph form uses q_ar,P and need not equal the full Clark form exactly. It converges to it by the stated bounds. No cutoff-dependent refitting of the window residual is needed for the limiting theorem.

## 6. Transport the actual nonzero observer

Use exactly Nima's four-event witness: a singly retained diamond on 2,3 followed by the forgotten diamond on 5,7, with v_src=ac. Keep its selected feature sectors from the windows [log 2,log 4] and [log 4,log 12] and its selected forgotten edge 12->60.

At z_0=i y, let e_0(x)=exp(-y x), L_0=L(1/2+y), and use the existing observer

    o_0=(e_0,-2 L_0 e_0).

Its graph lift is G(o_0), including the ACTUAL full rigged response Atilde_rig E_+e_0 and both endpoint coordinates. These are legitimate weighted-dual vectors even though the ordinary L2 obstructions apply.

Lift the two-sector observer eta by applying G to its feature coordinate and keeping all spectator vacua unchanged. Its graph control bound is at most C_G times the supplied one-feature bound. By the proved paired identity,

    Q_joint,rig(j_rig(v_src),eta_rig)
      =Q_joint,Psi(j_Psi(v_src),eta)
      =w_seam sqrt(2)(mu_2-mu_1)/(2y) >0.

The arithmetic multiplier still cancels; the same positive difference of window moment means remains. The observer is a bounded bottom-degree scalar functional. No general Green inverse on the graph carrier is needed.

The coefficient-complex graph isomorphism transports the old attachment roof to the new one and back. Hence a zero new roof in the declared strict localization would imply a zero old roof. Equivalently, on the finite projective source packet the old source-equivariant nullhomotopy obstruction remains: I acts trivially on the outer target, so H(ac)=aH(c)=0, contradicting the displayed observation.

The completed rigged graph attachment is therefore genuinely nonzero, not merely a paired scalar realization.

## 7. Boundary of the result

Established: a continuous paired graph lift to the independent all-prime rigged response, actual kernel/balancing descent, normalization and refinement compatibility, and preservation of the explicit nonzero attachment class.

Not established: reconstruction from response coordinates alone, equality with an output-only analytical completion, perfect duality, positivity, or an ordinary L2 all-prime realization. The preceding endpoint-subtracted leakage theorem excludes that last strengthening on every nonzero finite Euler packet.

This graph lift deliberately retains the source port. Its inverse is projection to RETAINED data, not an inverse of the Tate operator. Negative-side Tate leakage and the window moment residual remain different source-labelled objects throughout.

## Verification

Fresh checks pass:
- `uv run --with sympy python research/voevodsky/checkers/check_rigged_residual_attachment_lift.py`
- `uv run --with sympy python research/nima/checkers/check_residual_port_attachment.py`
- `uv run --with sympy python research/nima/checkers/check_residual_attachment_nonzero.py`
- `uv run --with sympy python research/grothendieck/checkers/check_rigged_all_prime_tate_comparison.py`

The new finite checker verifies a non-real Hermitian graph pullback, its retained-input inverse, the two-slot tensor identity, nonzero retained leakage, linear source/refinement identities, and observer transport. Actual balanced packets and their nonzero detection are checked by the owning source checkers; their completed graph transport is proved above.
