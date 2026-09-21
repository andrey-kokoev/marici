# All-prime Tate leakage diverges on the common Euler source domain

## Result and attribution

Voevodsky's supplied `the-trivial-sector-arithmetic-form-is-a-tate-compression-with-explicit-leakage.md` already closes the requested finite-place comparison: the half-line arithmetic form is a compression of the NEGATIVE trivial-sector Tate connection, with the actual endpoint swap kept on a correlated response graph.

The remaining unregularized all-prime operator limit has a genuine obstruction. On a nonnegative compactly supported common-core vector, the negative-side prime leakage has divergent L2 norm. The same obstruction occurs on positive Euler exponential states, including the prescribed completed-theta even-port states at real s>1 in the admitted domain.

Thus the finite-place form comparison cannot be promoted to strong or weak full-line operator convergence on this source domain. The weighted half-line arithmetic forms still converge. This is a distinction between those two types of convergence, not a contradiction between the constructions.

## 1. Freeze the finite-place comparison

Use the source domain D_gamma^1=H^1(R_+,exp(2 gamma u)du), gamma>1/2, with unrestricted trace at zero. Let E_+ be zero extension and F the unitary full-line Fourier transform. Put U=F E_+.

For a finite prime set P, the independently specified trivial-sector Tate symbol is

    a_P(xi)=a_infty(xi)+sum_(p in P) a_p(xi),

    a_infty(xi)=log(pi)-Re psi(1/4+i xi/2),

    a_p(xi)=2 log(p) sum_(k>=1) p^(-k/2) cos(k xi log p).

Write A_P for its maximal self-adjoint multiplication operator, and Atilde_P=F^(-1)A_P F. Voevodsky proves U(D_gamma^1) is contained in Dom A_P. This allows nonzero endpoint traces; zero extension need not belong to full-line H^1 to belong to the logarithmic multiplier domain.

With the source-defined endpoint vector beta_end(f), the exact common-domain form is

    q_ar,P(f,g)=-<U f,A_P U g>+beta_end(f)^* J_end beta_end(g).

The regular operator decomposition is

    A_P U f=-U B_P f+F leak_P f,

    B_P f=-E_+^* Atilde_P E_+ f,
    leak_P f=1_(u<0) Atilde_P E_+ f.

The leakage is part of the comparison, not an omitted endpoint scalar. These formulas and their signs are inputs here, not newly inferred from a scalar Clark identity.

## 2. Positive prime leakage on a short-support source

Choose 0<L<log 2 and a nonzero real nonnegative f in C_c^infinity(0,L). It belongs to every common weighted Sobolev source domain under discussion.

Let S_a h(u)=h(u+a) on the full line. The prime increment is

    Atilde_p=log(p) sum_(k>=1) p^(-k/2) [S_(k log p)+S_(-k log p)].

Its series is operator-norm convergent for each fixed p. Applied to E_+f, the first translations are supported on the negative intervals

    (-k log p, L-k log p).

The opposite translations are supported on the positive half-line and contribute no leakage. Within one prime tower the negative intervals are disjoint because L<log p. Consequently

    ||leak_p f||_2^2
      =(log p)^2 sum_(k>=1) p^(-k) ||f||_2^2
      =(log p)^2/(p-1) ||f||_2^2.

For different primes the translated supports can overlap. They must NOT be treated as orthogonal. Instead every prime leakage function is nonnegative, so all cross inner products are nonnegative. For a finite set P,

    ||sum_(p in P) leak_p f||_2^2
      >= ||f||_2^2 sum_(p in P) (log p)^2/(p-1).

The right side diverges along increasing sets exhausting the primes. Indeed it dominates (log 2)^2 sum_(p in P)1/p, and Euler's reciprocal-prime sum diverges. No prime-number asymptotic is required: convergence of that reciprocal sum would bound the finite Euler products, contradicting their domination of growing harmonic sums.

## 3. The gamma and endpoint terms do not remove the obstruction

The fixed archimedean leakage leak_infty f is an L2 vector by the finite-place graph-domain theorem. Hence

    ||leak_P f||_2
      >= ||sum_(p in P) leak_p f||_2-||leak_infty f||_2
      -> infinity.

Orthogonal projection onto the negative half-line gives

    ||A_P U f||_2 >= ||leak_P f||_2 -> infinity.

There is therefore neither strong nor weak L2 convergence of A_P U f: a weakly convergent Hilbert-space family would be norm bounded.

The prescribed endpoint response beta_end(f) is fixed as P grows. Appending that finite-dimensional fiber does not change the divergent full-line component. This argument concerns the fixed supplied endpoint graph, not an arbitrary cutoff-dependent renormalization chosen to cancel a desired output.

## 4. Why the half-line construction still converges

For this same compactly supported f,

    T_(k log p) f=0

for every p>=2 and k>=1, because u>=0 and log p>L. Thus the one-sided prime operator satisfies V_P f=0 for every P.

More generally, V_P converges in operator norm on H_gamma to V. Its associated unweighted-pairing form obeys

    |q_prime,P(f,g)-q_prime(f,g)|
      <=2||V_P-V||_(H_gamma->H_gamma) ||f||_gamma ||g||_gamma.

Thus the pulled-back arithmetic forms converge on the common weighted source domain. The full-line Tate operator images do not. In particular, convergence of these compressed forms cannot supply the missing uniform graph bound for U into the growing-place Tate multiplier domains.

On two test functions supported in (0,L), every prime form term is zero, even while the full operator leakage diverges on either positive input. This is a direct hostile against inferring full operator convergence from convergence of observed forms.

## 5. The obstruction also reaches the prepared Euler states

It is not restricted to auxiliary compact bumps. Take

    f=e_s,  e_s(u)=exp(-alpha u),
    alpha=s-1/2>gamma,  s real.

All prime leakage terms remain nonnegative. Keeping just the k=1 contribution of each prime gives

    ||leak_p e_s||_2^2
      >= (log p)^2/p * integral_0^(log p) exp(-2 alpha v) dv
      = (log p)^2/p * [1-p^(-2 alpha)]/(2 alpha).

For p>=2 the last bracket is bounded below by

    c_alpha=[1-2^(-2 alpha)]/(2 alpha)>0.

Nonnegative cross terms therefore give

    ||sum_(p in P) leak_p e_s||_2^2
      >= c_alpha sum_(p in P) (log p)^2/p -> infinity.

The fixed gamma term again cannot remove this norm divergence. Meanwhile

    V_P e_s=P_P(s)e_s -> P(s)e_s

on the weighted Euler domain by absolute convergence at s>gamma+1/2>1.

For the completed theta source, U_Phi(z)=sqrt(2)xi(s)e_s with z=i(s-1/2). At real s>1, xi(s) is positive and nonzero. Multiplying by this fixed scalar preserves the divergence. Thus even these source-derived states do not admit the proposed unregularized all-prime full-line L2 operator limit, although their half-line arithmetic action and Clark polarization are well defined.

## 6. Exact strength and next boundary

Closed:

- the finite-place compression comparison, by Voevodsky's theorem;
- an explicit failure of its all-prime strong/weak operator limit on the common source domain;
- compatibility of that failure with convergent half-line Euler operators and forms.

Not excluded:

- a distributional or appropriate dual-space realization;
- another explicitly specified regularization or smaller domain;
- additional angular sectors or independently proved Sonin restrictions.

Such alternatives require their own source maps and domain statements. They are not the unregularized limit of A_P U on the already declared Euler source states. No positivity assertion or identification of bulk/forcing with gamma/prime channels follows.

In unweighted L2 the surviving statement is the weighted half-line FORM comparison, not an invariant-subspace or full-line operator equivalence. The subsequent `the-all-prime-tate-response-converges-in-a-two-sided-weighted-dual.md` constructs an operator-norm limit into an explicitly weaker two-sided weighted dual, retaining both leakage and endpoint data. That response-space completion changes no prime coefficients and does not contradict the present L2 obstruction.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_all_prime_tate_leakage_obstruction.py`

Passed 21 exact nonnegative-translate correlation checks, 88 prime-tower geometric norm checks, and 33 positive Euler-state lower bounds. The compact polynomial fixture belongs to the Sobolev domain; the proof applies also to smooth nonnegative bumps. Infinite divergence follows from the displayed lower bound and Euler's theorem, not a finite numerical trend.

References:

- `research/voevodsky/the-trivial-sector-arithmetic-form-is-a-tate-compression-with-explicit-leakage.md`;
- `research/voevodsky/the-semilocal-tate-logarithmic-connection-commutes-with-fourier-sewing-and-adds-under-cutoffs.md`;
- `research/voevodsky/the-euler-prime-channel-has-a-source-defined-shift-operator-comparison.md`;
- `research/grothendieck/the-euler-gamma-endpoint-operator-reconstructs-the-two-clark-sheets.md`.
