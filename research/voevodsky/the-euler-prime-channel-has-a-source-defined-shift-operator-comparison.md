# The Euler prime channel has a source-defined shift-operator comparison

## Strength and scope

A one-slot operator/form comparison for the PRIME channel on the Euler chart. A source-defined sum of half-line prime-power translations converges in operator norm on an explicit weighted domain. The fixed sum of the normalized Clark sheets maps the completed-theta feature to exponential states on which its polarized form equals the prime term of the existing arithmetic crosswalk.

This is not a full equivalence with the semilocal Tate/endpoint Green operator, not an identification of the forcing reservoir with primes, and not continuation of a Dirichlet operator series to the critical line.

Inputs:
- `../grothendieck/clark-sewing-to-the-endpoint-gamma-prime-green-kernel.md`
- `the-completed-clark-pair-is-a-fixed-codiagonal-sewing-of-four-oriented-resolvent-cross-entries.md`
- `clark-source-interface-domain-and-positivity-audit.md`

## 1. Independent prime operator and domain

Let u>=0 be the Clark half-line FEATURE coordinate, distinct from the forcing integration variable x. Fix gamma>1/2 and

    H_gamma=L2(R_+, exp(2 gamma u)du).

For a>=0 let T_a f(u)=f(u+a). Direct change of variables gives ||T_a||<=exp(-gamma a). Define the prime-power operator from its arithmetic coefficients,

    V_N=sum_(2<=n<=N) Lambda(n) n^(-1/2) T_(log n).

With sigma0=gamma+1/2>1, the series converges absolutely in operator norm:

    ||V||<=sum_(n>=2) Lambda(n)n^(-sigma0).

For sufficiently large N the tail is bounded by

    ||V-V_N|| <= N^(1-sigma0)
                 [log N/(sigma0-1)+1/(sigma0-1)^2].

This uses Lambda(n)<=log n and the integral majorant for the eventually decreasing function log(x)x^(-sigma0). The construction precedes evaluating any Clark kernel.

The functions C_c^infinity(0,infinity) form a dense source core in H_gamma. The operator is bounded on all H_gamma, so no self-adjoint boundary condition for an unbounded derivative is being silently imposed. On compactly supported inputs only finitely many prime shifts act nontrivially. The norm limit is their unique continuous extension on this weighted domain.

## 2. Preserve the prescribed unweighted pairing

Use the original half-line L2 pairing, not the weighted inner product, to define

    q_prime(f,g)=-<f,Vg>_0-<Vf,g>_0.

The inclusion H_gamma->H_0 is contractive, hence |q_prime(f,g)|<=2||V|| ||f||_gamma ||g||_gamma. This form has a bounded self-adjoint Riesz representative on H_gamma:

    A_prime=-(W V+V^* W),   W=M_(exp(-2 gamma u)),

where V^* is the H_gamma adjoint. The weight changes the controlling domain and Riesz representation, not the underlying arithmetic form.

For clarity, T_a^* in H_gamma is exp(-2 gamma a) times the right shift with zero extension. It is not the unweighted right-shift formula. The original unweighted pairing is essential to the divided denominator below.

## 3. Exponential states and exact prime polarization

For s=1/2-i z put

    e_s(u)=exp(-(s-1/2)u)=exp(i z u).

If Re s>gamma+1/2, equivalently Im z>gamma, then e_s belongs to H_gamma. The source shifts satisfy

    n^(-1/2) T_(log n)e_s=n^(-s)e_s.

Therefore V e_s=P(s)e_s, with the absolutely convergent prime-power current P(s)=sum Lambda(n)n^(-s). For t=conjugate(s_w),

    q_prime(e_(s_w),e_(s_z))
       =-[P(s_z)+conjugate(P(s_w))]/[s_z+conjugate(s_w)-1].

This is exactly K_prime in the fixed arithmetic crosswalk. Using the weighted Hilbert pairing directly would replace its denominator by s_z+conjugate(s_w)-1-2 gamma and give the wrong kernel.

The states need not be compactly supported: cutoff approximation converges in H_gamma and extends both the operator and its form identity from the dense core. For different gamma, the operators and forms agree on domain intersections because their finite shift sums do and their limits agree in H_0. These domains cover the Euler chart by choosing 1/2<gamma<min(Im w,Im z).

## 4. The source map is the fixed even-sheet projection

The normalized Clark amplitude is (E(z),E_star(z)), with E=X+iX' and E_star=X-iX'. The fixed linear sheet functional

    ell(v1,v2)=(v1+v2)/sqrt(2)

gives ell(E,E_star)=sqrt(2)X. Thus the projected completed-theta feature is

    U_Phi(z)=sqrt(2)X(z)e_(s_z).

This is the even-transform port already present in the source sewing, not a feature chosen by fitting the prime Gram. On a compact spectral set with gamma<eta<=Im z<=Y<beta, the source trace bound gives a bounded forcing-to-H_gamma map for this projection, with constant at most 1/sqrt(2(beta-Y)(eta-gamma)) in the weighted forcing norm.

Applying the independently constructed q_prime yields

    q_prime(U_Phi(w),U_Phi(z))
       =2 conjugate(X(w))X(z) K_prime(s_z,conjugate(s_w)).

The operator action on this projected source state is the exact identity V U_Phi(z)=P(s_z)U_Phi(z). Finite spectral packets follow by sesquilinearity with every spectral pair retained.

For arbitrary shell forcing the same projection and shift action exist, but the special amplitude X is then its own even transform, not automatically completed xi. The xi arithmetic identification is asserted only for the prescribed completed theta forcing and normalization.

## 5. What this does not identify

The source B/R split is NOT the arithmetic gamma/prime split. This construction realizes the independently specified prime-power term on a source-derived even-port state; it does not prove R equals that term.

Nor is this half-line weighted operator the full-line unitary prime translation sum. The latter's absolute channel completion has its own known obstruction. Here translations have the displayed decay in H_gamma, and that decay is confined to the Euler-chart domain. No conclusion on critical-line domain equivalence follows.

The gamma operator, endpoint attachment, their common form domain, and a joint comparison with the independently prescribed semilocal Green operator remain to be constructed. The prime result is a concrete component-level operator comparison, not promotion of the scalar crosswalk to a full operator equivalence.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_euler_prime_shift_operator.py`

Exact checks verify shift eigenvalues, the unweighted denominator, the fixed even-sheet projection, prime-power coefficients, and the analytic tail-integral formula. They explicitly reject substituting the weighted denominator. Operator convergence and domain assertions are proved above.
