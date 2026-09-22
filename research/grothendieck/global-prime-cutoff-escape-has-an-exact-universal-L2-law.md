# Global prime-cutoff escape has an exact universal L2 law

## Result

Let h belong to ordinary L2(R) and to the domain of the fixed archimedean operator Atilde_infty. For the unchanged finite-place response T_P h, include every prime p<=P and all its powers. Define

    J_- h(t)=integral_0^infinity exp(-a/2)h(t-a)da,
    J_+ h(t)=integral_0^infinity exp(-a/2)h(t+a)da.

Then the GLOBAL ordinary-L2 asymptotic is

    P^(-1/2)T_P h(u)
      =J_- h(u+log P)+J_+ h(u-log P)+o_L2(1).

In particular, with the unitary Fourier convention having phase exp(-i xi u),

    lim_(P->infinity) ||T_P h||_2^2/P
      =||J_- h||_2^2+||J_+ h||_2^2
      =2 integral_R |hat h(xi)|^2/(1/4+xi^2) dxi.

The coefficient is strictly positive for every nonzero h. This applies far beyond the exact arithmetic kernel, and needs no all-prime limit on h. For half-line sources in D_gamma, take h=E_+f; the existing archimedean domain theorem supplies the hypothesis even when the zero-extension trace jumps.

This is a moving-profile asymptotic of the original response, not an operator renormalization or an added endpoint subtraction.

## 1. A finite positive measure encoding the first prime powers

Put L=log P and

    m_P=P^(-1/2) sum_(p<=P) log(p)p^(-1/2) delta_(log(P/p)).

These are measures on [0,infinity). The prime number theorem and partial summation give

    W(X)=sum_(p<=X) log(p)/sqrt(p) ~ 2sqrt(X),
    W(X)<=C sqrt(X), X>=2.

For each fixed A>=0, their tail masses tend to

    m_P([A,infinity)) -> 2exp(-A/2).

Possible endpoint atoms have mass at most log(P)/sqrt(2P), tending to zero. Also, uniformly in P,

    m_P([A,infinity)) <= C exp(-A/2),

where the tail is zero when P exp(-A)<2. Their total masses tend to two. Thus m_P converges narrowly, with uniform tightness, to

    dm(a)=exp(-a/2) da, a>=0.

Only the PNT, not a zero-location assumption or a quantitative PNT remainder, enters here.

## 2. Convergence after convolving with any fixed L2 vector

Translations are strongly continuous on L2. Consequently, for any fixed h in L2,

    integral h(t-a) dm_P(a) -> J_- h(t),
    integral h(t+a) dm_P(a) -> J_+ h(t)

in L2(t).

Here is the needed vector-valued justification. On [0,A], the translation orbit is norm-continuous and has compact image. Approximate it uniformly by a finite linear combination of fixed vectors with continuous scalar coefficients. Narrow measure convergence proves convergence for that approximation. The uniformly bounded masses control its error. Outside [0,A], uniform tightness bounds the norm by ||h||_2 times the tail mass. Let A tend to infinity after the compact approximation. No total-variation convergence of atomic measures to a density is asserted.

The normalized first-power positive shifts, evaluated at u=t-L, are exactly the first integral above. The negative shifts, evaluated at u=t+L, are exactly the second. Translation invariance of the L2 norm therefore gives the claimed global two-profile expansion for the first powers.

## 3. Every remaining term is negligible at this scale

The included higher powers have ordinary-L2 operator norm at most

    2 sum_(p<=P) log(p) sum_(k>=2) p^(-k/2)
      <=C sum_(p<=P) log(p)/p
      =O(log P).

The last estimate follows by partial summation from theta(X)<=C X. Dividing by sqrt(P) makes their operator norm tend to zero. All powers remain present in the finite response; this estimate proves their lower asymptotic order.

The archimedean term is fixed and Atilde_infty h is in L2 by hypothesis. Its normalized norm is ||Atilde_infty h||_2/sqrt(P), also tending to zero. Combining this with section 2 proves the global expansion.

## 4. The two separated profiles account for all leading mass

For any fixed a,b in L2, their translated correlation tends to zero at infinite separation. One proof approximates both by compactly supported functions and then uses Cauchy--Schwarz for the approximation errors.

Apply this to J_-h and J_+h, whose centers separate by 2log P. Their cross term tends to zero. The o_L2(1) remainder likewise contributes nothing to the limiting squared norm, since both profile norms are fixed. Thus

    lim ||T_P h||_2^2/P=||J_-h||_2^2+||J_+h||_2^2.

The convolution kernels exp(-t/2)1_(t>=0) and exp(t/2)1_(t<=0) have multipliers

    1/(1/2+i xi),  1/(1/2-i xi),

respectively. Plancherel yields the exact coefficient stated at the start. In particular the two profile norms are equal and their sum is nonzero unless h=0.

This identifies ALL leading ordinary-L2 mass, rather than inferring a global coefficient from a few moving windows.

## 5. Relation to the kernel-source profiles

For h=E_+f the profiles can be written

    J_-h(t)=0 for t<0,
    J_-h(t)=exp(-t/2) integral_0^t exp(x/2)f(x)dx for t>=0,

    J_+h(t)=exp(t/2) integral_(max(t,0))^infinity exp(-x/2)f(x)dx.

For the exponentially decaying zero-endpoint kernel sources, these are precisely H_- and H_+ from the earlier cutoff-escape theorem. The endpoint ell_+(f)=0 makes J_+h vanish for t<0; ell_-(f)=0 converts J_-h into its rapidly decaying tail-integral expression for t>=0.

Hence those sources have the exact nonzero ordinary-L2 coefficient above despite their all-prime weighted-dual response being zero. Their already proved weighted norm order P^(1/2-gamma) remains valid. A global unweighted remainder estimate alone is not used to infer a weighted remainder estimate on moving windows.

For general h this theorem does not presume that either endpoint functional exists, that h is in a weighted test space, or that an all-prime response has been defined. Only the finite-place operators and the stated archimedean domain are needed.

## 6. Scope

The convergence of the convolved measures is strong on each FIXED L2 source. The subsequent `fractional-source-priors-make-global-escape-uniform-and-quantitative.md` proves uniform quantitative convergence on every positive fractional Sobolev prior ball, using an explicit prime-measure tail discrepancy. It also proves that ordinary L2 operator-norm convergence fails already for the bounded first-prime part, by simultaneous high-frequency recurrence. The fixed archimedean operator is unbounded, so its negligible contribution likewise requires the fixed-domain-vector hypothesis.

No nonzero source in this domain can have an ordinary weak-L2 convergent sequence of canonical finite-place responses: the exact coefficient forces unbounded norms. This says nothing about positivity of an arithmetic form, a self-adjoint all-prime realization, or actual-letter factorization.

The operators, included prime powers, endpoint conventions, and original attachment source remain unchanged. In particular the raw-kernel preparation barrier and the actual theta-weighted relation-factor lifts are separate statements.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_global_prime_cutoff_escape.py`

The checker verifies exact exponential profiles, their equal energies, separated-profile correlation decay, and normalized first-prime measure masses. The infinite theorem is the PNT, tightness, strong translation continuity, and Plancherel proof above; the numerical fixtures do not establish it.

Inputs:

- `research/grothendieck/exact-kernel-sources-have-growing-cutoff-responses-escaping-to-both-ends.md`;
- `research/grothendieck/the-all-prime-tate-response-converges-in-a-two-sided-weighted-dual.md`.
