# Infinite Euler cancellation gives a full-line kernel with zero endpoints

## Result

The positive-side response of Grothendieck's infinite Euler construction cancels too. More generally, within the declared norm-summable vertical Euler class, an endpoint-subtracted full-line residual belongs to ordinary L2 if and only if that residual is identically zero.

Multiplying the supplied source Cauchy function by q(q-1), with additional decay, also kills BOTH endpoint outputs. This gives an infinite-dimensional kernel of the reduced map

    f -> (Atilde_rig E_+f, beta_end(f))

on every D_gamma, gamma>1/2. It settles noninjectivity of that unrestricted reduced map, in addition to its previously proved compactness and nonclosed range.

The sources are nonzero but their responses are zero. This is not a nonzero-output self-adjoint L2 realization, or a claim that finite-place responses converge in ordinary L2.

Inputs:
- `../grothendieck/infinite-euler-superpositions-have-a-hardy-residual-domain-and-a-nonzero-kernel.md`
- `endpoint-subtracted-tate-leakage-is-not-L2-on-any-nonzero-finite-euler-packet.md`
- `the-reduced-rigged-arithmetic-response-is-compact-with-nonclosed-range.md`

## 1. Source class and notation

Fix sigma>1, 1/2<gamma<sigma-1/2, and a complex measure mu on s=sigma+i t with integral (1+|t|)d|mu|(t)<infinity. The actual source

    f_mu(u)=integral exp(-(s-1/2)u)dmu(s)

converges in D_gamma. Keep the prescribed relative response

    R f=Atilde_rig E_+f-E_end f,
    E_end f(u)=exp(u/2)ell_+(f)+exp(-u/2)ell_-(f).

Let r_mu^+(v)=R f_mu(v) and r_mu^-(v)=R f_mu(-v), v>0. Write L=xi'/xi and

    C(q)=integral dmu(s)/(s-q),
    D(q)=integral L(s)dmu(s)/(s-q),   Re q<sigma.

The supplied negative transform is

    F_-(q)=D(q)-L(q)C(q),  1<Re q<sigma.

All statements concern the existing weighted-dual response, with its existing subtraction. No output counterterm is added.

## 2. Calculate the positive transform from the actual shifts

For one Euler state e_s, Re s>1, the positive prime response at u>0 is

    P(s)exp(-(s-1/2)u)
      +exp(-(s-1/2)u) sum_(n<=exp(u)) Lambda(n)n^(s-1),
    P=-zeta'/zeta.

Against exp(-(q-1/2)u), Re q>1, its integral is

    [P(s)+P(q)]/(s+q-1).

The regulated gamma shifts give

    [log(pi)-psi(s/2)/2-psi(q/2)/2]/(s+q-1).

Indeed their shift numerator integrates to exp(-s a)+exp(-q a)-2exp(-2a), with denominator 1-exp(-2a); the fixed gamma_E+log(pi) term removes the digamma constants. Here psi is digamma.

The two prescribed endpoint modes contribute

    -1/[s(q-1)]-1/[(s-1)q].

Combining these source terms yields the exact positive residual transform

    F_s^+(q)=-[L(s)+L(q)]/(s+q-1),  Re q>1.

Absolute prime estimates and the gamma graph bound permit integration against the first-moment measure mu. Consequently

    F_+(q)=-D(1-q)-L(q)C(1-q),  Re q>1.

The functional equation xi(1-q)=xi(q) gives L(1-q)=-L(q). Thus, with F(q)=D(q)-L(q)C(q) defined meromorphically for Re q<sigma,

    F_+(q)=-F(1-q).

This is a reflection of the MEROMORPHIC expression. It is not an illicit reflection of an unevaluated Laplace integral outside its convergence half-plane.

## 3. Positive-side domain criterion and the full-line consequence

The positive residual belongs to ordinary L2 exactly when its calculated transform extends to a Hardy H2 function on Re q>1/2, with the same Laplace normalization as the supplied negative criterion:

    sup_(epsilon>0) (1/(2pi)) integral
      |F_+(1/2+epsilon+i t)|^2 dt <infinity.

This follows from Laplace Plancherel and uniqueness on a common damped half-plane. It is not merely a pole-cancellation condition.

Suppose BOTH residual sides are L2. Their Hardy boundary values are Fourier transforms of their zero extensions to v>=0. The meromorphic reflection relation gives

    hat(r_+)(t)=-hat(r_-)(-t)

almost everywhere on the boundary line. There is no uncancelled pole on that line: such a pole would violate the Hardy point-evaluation bound. The expression D-LC is meromorphic in a neighborhood of the line, so the remaining boundary values agree with those from both sides.

By Fourier uniqueness, the zero extension of r_+ equals minus the reflection of the zero extension of r_-. The first is supported in [0,infinity), the second in (-infinity,0]. An ordinary L2 function supported only at zero vanishes. Therefore

    R f_mu in L2(R)  iff  R f_mu=0.

This equivalence is only for the specified vertical-superposition class. It neither classifies arbitrary D_gamma sources nor excludes nonzero L2 responses in another source class.

## 4. The supplied negative kernel is already a full residual kernel

For Grothendieck's Blaschke sources, C and LC are left-analytic and have sufficient decay for Cauchy's formula to give D=LC on Re q<sigma. Hence

    F_-=0,
    F_+(q)=-[L(1-q)+L(q)]C(1-q)=0.

Laplace uniqueness gives r_-=r_+=0. Thus the original construction satisfies

    Atilde_rig E_+ f_mu=E_end f_mu

on the FULL real line as weighted-dual vectors, not only on its negative half.

For the originally supplied choice, ell_+(f_mu)=C(0) is nonzero. Its unsubtracted full response therefore still has a growing endpoint mode. Zero relative response must not be confused with zero unsubtracted response.

## 5. Kill the endpoints by changing the source, not the operator

For any fixed gamma>1/2 choose sigma>gamma+1/2. Let b=sigma+1. Take the half-plane Blaschke product B in Re q<b with all xi zeros, counted with multiplicity, and reflected poles at 2b-conjugate(rho). Existence and boundedness follow from the same supplied Blaschke argument.

For each integer M>=8 put

    C_M(q)=q(q-1) B(q)/(sigma+2-q)^M,
    dmu_M(t)=C_M(sigma+i t)dt/(2pi).

The supplied Hadamard/Blaschke estimate, with this shifted half-plane, gives

    C_M(q)=O((1+|q|)^(2-M)),
    L(q)C_M(q)=O((1+|q|)^(4-M)),   Re q<=sigma.

The second product is analytic across every xi zero. These estimates ensure finite measure first moment and justify closing both Cauchy integrals to the left. Hence these are admitted Bochner sources in D_gamma and their Cauchy data satisfy D_M=L C_M.

Their endpoints are now exactly

    ell_+(f_M)=C_M(0)=0,
    ell_-(f_M)=C_M(1)=0.

But the source is nonzero: its exponentially damped integral is

    integral_0^infinity exp(-3u/2)f_M(u)du
      =C_M(-1)=2 B(-1)/(sigma+3)^M !=0.

There is no xi zero at -1. Therefore section 4 gives

    Atilde_rig E_+f_M=0,   beta_end(f_M)=0,   f_M!=0.

Varying M gives linearly independent C_M, and thus linearly independent source vectors. This constructs an infinite-dimensional kernel of T_red for EVERY gamma>1/2.

Only the source has changed. The Tate coefficients, endpoints, weights and subtraction are unchanged. The sources are complex superpositions, so positive-input leakage lower bounds do not apply to them.

## 6. Even unsubtracted L2 outputs in this class must vanish

For a general vertical packet the unsubtracted negative transform adds

    C(1)/(q-1)+C(0)/q

to F_-, while the positive transform adds

    C(0)/(q-1)+C(1)/q

to F_+. The relative transforms are analytic near q=1: xi has no zero there, and C,D are analytic there since sigma>1.

If both unsubtracted responses were L2, their Laplace transforms would be holomorphic at q=1. Therefore C(1)=C(0)=0. The endpoints vanish, and section 3 forces the entire response to vanish.

Accordingly, within this class,

    Atilde_rig E_+f_mu in ordinary L2(R)
      iff Atilde_rig E_+f_mu=0 and beta_end(f_mu)=0.

The reverse implication is immediate. For the forward implication the endpoint conclusion and vanishing were just proved. The constructed f_M provide nonzero inputs in this domain, but not nonzero L2 output vectors.

## 7. Implications and limits

This closes the positive-side question for the supplied construction and resolves the previously open injectivity gate for the unrestricted REDUCED response: it is not injective, with an infinite-dimensional kernel. Its compactness, infinite rank and nonclosed range remain consistent with that fact.

This does not contradict prepared-sector recovery from holomorphic endpoint families. The new vectors are aggregated superpositions with genuinely unbounded spectral support, not pointwise exponential profiles on a fixed labelled compact spectral family.

It also does not give a kernel of the five-label port response that retains a weak even copy: that coordinate still sees the nonzero f_M. Window residuals remain different objects from Tate leakage.

Finally, weighted-dual equality to an L2 vector, here zero, does not establish ordinary L2 convergence of the finite-place responses. No dense self-adjoint all-prime operator domain, positivity statement, or generic ordinary L2 realization is claimed.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_full_line_infinite_euler_kernel.py`

Passes the exact positive transform, functional-equation reflection, endpoint-killing factors and proper left-analytic Cauchy-data fixtures. The fixture zeros are not claimed xi zeros. Infinite existence and nonzero source certificates use the supplied Blaschke construction and the proofs above.
