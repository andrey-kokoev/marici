# A subtracted gamma-shift operator completes the one-slot Euler Green form

## Strength

One-slot arithmetic operator/form realization on an explicit Euler-chart graph domain. The gamma operator is constructed from a convergent SUBTRACTED translation integral; the endpoint swap is derived from a second translation integral. Together with the existing prime-power operator, these give the endpoint--gamma--prime form on one common dense core and its continuous graph-domain extension.

On the prescribed completed-theta exponential states, its polarization equals the full Clark kernel. This does not establish unitary equivalence with the independent full-line semilocal Tate operator, a closed form on unweighted L2, or positivity.

Inputs:
- `the-euler-prime-channel-has-a-source-defined-shift-operator-comparison.md`
- `../grothendieck/clark-sewing-to-the-endpoint-gamma-prime-green-kernel.md`

## 1. Domain and boundary convention

Fix gamma>1/2. Let

    H_gamma=L2(R_+,exp(2 gamma u)du),
    D_gamma={f in H_gamma : f' in H_gamma},
    ||f||_D^2=||f||_gamma^2+||f'||_gamma^2.

The derivative is weak and there is NO boundary condition f(0)=0. The core consists of restrictions to [0,infinity) of smooth compactly supported functions on the real line. Cutoff and mollification give density in D_gamma. This core permits nonzero endpoint trace.

By contrast C_c^infinity(0,infinity) is dense in H_gamma but not in this full graph domain: its graph closure has zero trace. It must not be used to exclude the required exponential states, whose trace is one.

The left translations T_a f(u)=f(u+a) satisfy ||T_a||<=exp(-gamma a). Their strongly continuous generator is the derivative with domain D_gamma and unrestricted initial trace. For f in D_gamma,

    ||f-T_a f||_gamma <= a ||f'||_gamma.

The coordinate u is the feature half-line, not the source forcing variable x.

## 2. Independently construct the gamma operator

Let gamma_E denote Euler's constant. Define

    G f=-(log(pi)+gamma_E)f/2
        +(1/2) integral_0^infinity
          [exp(-t)f-exp(-t/4)T_(t/2)f]/[1-exp(-t)] dt.

The two numerator terms MUST remain subtracted before integration. Separately they have a nonintegrable t=0 singularity. The formula is the translation-semigroup version of the independently fixed digamma integral, not an operator reconstructed from a desired scalar Gram.

For 0<t<=1 split its numerator as

    [exp(-t)-exp(-t/4)]f + exp(-t/4)[f-T_(t/2)f].

Using |exp(-t)-exp(-t/4)|<=3t/4 and 1-exp(-t)>=t/e gives an integrand norm at most

    (3e/4)||f||_gamma+(e/2)||f'||_gamma.

For t>=1 put c_gamma=1/4+gamma/2. The integrand norm is at most

    [exp(-t)+exp(-c_gamma t)] ||f||_gamma/[1-exp(-1)].

Thus G:D_gamma->H_gamma is a well-defined bounded graph-domain operator. For example

    ||Gf||_gamma <= C0 ||f||_gamma+C1 ||f'||_gamma,
    C1=e/4,
    C0=|log(pi)+gamma_E|/2+3e/8
       +[exp(-1)+exp(-c_gamma)/c_gamma]/[2(1-exp(-1))].

This is a Bochner integral in H_gamma. The bound proves convergence without assuming a formal functional calculus for an unbounded completed generator.

## 3. Quantitative regulator removal

If the integral is restricted to epsilon<=t<=L, with 0<epsilon<=1<=L, the omitted small-t piece is bounded by

    epsilon [(3e/8)||f||_gamma+(e/4)||f'||_gamma],

and the omitted large-t piece by

    [exp(-L)+exp(-c_gamma L)/c_gamma]
       ||f||_gamma/[2(1-exp(-1))].

Hence the regulated operators converge in operator norm D_gamma->H_gamma. The small-t subtraction is essential; it is not a removable bookkeeping convention.

## 4. Endpoint operator and its swap form

Independently define the bounded translation operator

    U f=integral_0^infinity [exp(-a/2)+exp(a/2)] T_a f da.

It has norm at most 1/(gamma+1/2)+1/(gamma-1/2). Define continuous endpoint functionals

    ell_+(f)=integral_0^infinity exp(-u/2) f(u) du,
    ell_-(f)=integral_0^infinity exp(u/2) f(u) du.

Their norms on H_gamma are respectively at most (2gamma+1)^(-1/2) and (2gamma-1)^(-1/2). Fubini is justified by these weighted estimates. Symmetrizing U in the ORIGINAL unweighted pairing yields

    <f,Ug>_0+<Uf,g>_0
      =conjugate(ell_+(f))ell_-(g)
       +conjugate(ell_-(f))ell_+(g).

Indeed the two triangular translation kernels join to

    exp((v-u)/2)+exp((u-v)/2),

which is exactly the rank-two endpoint swap kernel. The negative odd endpoint direction is retained; no positive endpoint metric is substituted.

## 5. Common arithmetic form

Let V=sum Lambda(n)n^(-1/2)T_(log n) be the independently convergent prime operator on H_gamma from the preceding note. Put

    L_ar=U+G-V : D_gamma -> H_gamma,
    q_ar(f,g)=<f,L_ar g>_0+<L_ar f,g>_0.

The core in section 1 is common to all these operations. The estimates extend q_ar continuously and Hermitianly to D_gamma. Equivalently it has a bounded self-adjoint Riesz representative in the positive graph norm of D_gamma. That Riesz representative changes the carrier norm, not the signed form.

This is not a claim that L_ar itself is self-adjoint, that q_ar is closed as an unbounded form on H_0, or that its graph completion is the already independent semilocal operator domain. Those require additional operator-domain arguments.

## 6. Exponential-state intertwining and polarization

For s=1/2-i z with Re s>gamma+1/2, let e_s(u)=exp(-(s-1/2)u). It belongs to D_gamma. Translation gives

    exp(-t/4)T_(t/2)e_s=exp(-s t/2)e_s,

so the convergent digamma integral proves

    G e_s=[-log(pi)+psi(s/2)]e_s/2.

The other two operators satisfy

    U e_s=[1/s+1/(s-1)]e_s,
    V e_s=[sum Lambda(n)n^(-s)]e_s.

Consequently L_ar e_s=L(s)e_s, with the independently prescribed Euler-chart logarithmic derivative L(s)=xi'(s)/xi(s). All three contributions were constructed before evaluating these eigenstates.

For t=conjugate(s_w), the ORIGINAL unweighted pairing gives

    q_ar(e_(s_w),e_(s_z))=[L(s_z)+conjugate(L(s_w))]/[s_z+conjugate(s_w)-1].

Its endpoint, gamma, and prime terms are exactly the existing arithmetic crosswalk, separately normalized. Using the weighted inner product in this formula would give a different denominator and is not allowed.

The fixed even-sheet projection of the normalized theta feature gives

    U_Phi(z)=sqrt(2) X(z)e_(s_z).

It follows that

    q_ar(U_Phi(w),U_Phi(z))
      =2 conjugate(X(w))X(z)
        [L(s_z)+conjugate(L(s_w))]/[s_z+conjugate(s_w)-1]
      =K_Clark(w,z).

This is the explicit one-slot form comparison on the prepared completed-theta states and their sesquilinear packets. It does not assert that an arbitrary forcing has the xi amplitude.

## 7. Continuity of the source packet map

On a compact spectral set gamma<eta<=Im z<=Y<beta, |z|<=Z, the fixed even-sheet projection maps weighted source forcing to D_gamma with bound

    ||U_f(z)||_D <= sqrt(1+Z^2)
                   ||f||_beta/sqrt(2(beta-Y)(eta-gamma)).

Here U_f is the same even-transform projection for f. The derivative in u simply multiplies the exponential by iz. Finite spectral packets, and their coefficient-L1 completions on this compact set, therefore map continuously into the common graph domain. Pairwise form identities extend by continuity with the spectral indices retained.

For different gamma the operators agree on common domains: their source translation formulas and regulated limits do. Their allowed spectral states cover the Euler chart by choosing gamma between 1/2 and the compact spectral lower imaginary bound.

## 8. Boundaries and next operator-level question

The one-slot endpoint--gamma--prime form now has an independent source-translation realization and a common domain, with a prescribed map from the theta Clark states. The B/R tail-current split is still NOT identified termwise with gamma/prime arithmetic channels.

The unresolved stronger question is comparison with the independently specified full semilocal Tate/endpoint operator, including its domain, angular/prime refinement, and boundary conventions. Equality on this prepared family does not imply equivalence of the full operator domains or positivity. In particular no critical-line extension of the raw prime series follows.

## Verification

- `uv run --with sympy python research/voevodsky/checkers/check_gamma_endpoint_operator_assembly.py`: passes 12 exact subtracted digamma integrals, translation eigenvalues, endpoint symmetrization, and three-channel polarization identities.
- Fresh `uv run --with sympy --with mpmath python research/grothendieck/checkers/check_clark_arithmetic_green_crosswalk.py`: passes the existing completed-xi kernel and Euler-tail regressions.

The graph-domain and regulator estimates are the proofs above, not numerical quadrature certificates or positivity tests.
