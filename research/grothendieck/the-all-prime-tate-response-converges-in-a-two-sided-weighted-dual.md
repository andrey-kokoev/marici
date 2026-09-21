# The all-prime Tate response converges in a two-sided weighted dual

## Result

**A rigged all-prime comparison retaining the full leakage.** For gamma>1/2, the prime part of the full-line Tate response converges in operator norm from L2(exp(2 gamma|u|)) to its unweighted-pairing dual L2(exp(-2 gamma|u|)). Adding the fixed archimedean operator on a common piecewise Sobolev domain gives a limiting response compatible with every finite-place multiplier.

Its positive-side compression, negative-side leakage, and prescribed endpoint swap satisfy the exact limiting comparison. Nothing is subtracted from the prime response. The weaker RESPONSE topology admits what the previous full-line L2 no-go excludes.

This is the trivial angular sector and a specified weighted dual realization, not a self-adjoint all-prime multiplication operator on unweighted L2 or a critical-line continuation of a Dirichlet operator series.

## 1. Declare both sides of the dual pair

Fix gamma>1/2 and put

H_+=L2(R,exp(2 gamma|u|)du),

H_-=L2(R,exp(-2 gamma|u|)du).

The duality is the ORIGINAL pairing

    <h,v>_0=integral conjugate(h(u)) v(u) du.

Cauchy--Schwarz identifies H_- with the continuous conjugate-linear scalar dual of H_+. The control weights are reciprocal; they do not replace this pairing with a weighted arithmetic form.

For the archimedean input domain use

D_br={h in H_+ : h' on each open half-line belongs to H_+},

with the sum-of-squares Sobolev norm. The two traces at zero are independent. The domain is a complete direct sum of the two half-line Sobolev spaces. Piecewise smooth functions compactly supported up to zero are a dense core.

In particular zero extension E_+ maps the previously declared unrestricted-trace half-line D_gamma^1 continuously into D_br. There is no false requirement that E_+f be globally H^1 when f(0)!=0.

## 2. The decisive translation estimate

For S_a h(u)=h(u+a), change variables v=u+a. The ratio between target and source squared weights is

    exp(-2 gamma[|v-a|+|v|]) <= exp(-2 gamma|a|).

Hence

    ||S_a||_(H_+ -> H_-) <= exp(-gamma|a|).

For a>0 equality is attained on inputs supported in (0,a); the analogous statement holds for a<0. This estimate applies to BOTH translation directions. It does not assert that either translation decays as an operator on the unchanged unweighted full-line Hilbert space.

## 3. Full prime response and quantitative place cutoff

Define from the actual prime-power coefficients

    T_prime=sum_(n>=2) Lambda(n)n^(-1/2)
                         [S_(log n)+S_(-log n)].

With sigma=gamma+1/2>1, its series converges absolutely in B(H_+,H_-), and

    ||T_prime|| <= 2 sum_(n>=2) Lambda(n)n^(-sigma).

For a finite prime set P use all powers of each included prime, exactly as in the finite-place Tate multiplier. If P contains every prime <=N, with N>=3, then

    ||T_prime-T_prime,P||
      <= 2 T_N,

    T_N=N^(1-sigma)[log N/(sigma-1)+1/(sigma-1)^2].

Indeed every omitted prime power exceeds N, and Lambda(n)<=log n gives the decreasing-function integral majorant. This proves convergence independently of the ordering of the cofinal finite prime sets.

The series is Hermitian in the unweighted dual pairing: the two shifts are adjoints of one another on L2, and absolute convergence passes their identity to the dual limit. This is a bounded map between a test space and its dual, not an endomorphism claimed self-adjoint on L2.

## 4. The fixed gamma response admits the same input domain

Let Atilde_infty be the Fourier conjugate of the independently prescribed multiplier

    a_infty(xi)=log(pi)-Re psi(1/4+i xi/2).

Its subtracted translation representation has numerator

    exp(-a/2)(S_a+S_-a)-2 exp(-2a)I,

denominator 1-exp(-2a), and constant gamma_E+log(pi). This is the NEGATIVE of the symmetrized half-line gamma term, consistently with the frozen Tate sign.

For h in D_br let j=h(0+)-h(0-). The piecewise fundamental theorem gives

    ||S_(+/-a)h-h||_0 <= a||h'_br||_0+sqrt(a)|j|.

Thus, writing d0=1-exp(-2), the omitted small-shift integral (0,epsilon), epsilon<=1, has norm at most

    [epsilon(3||h||_0+2||h'_br||_0)+4 sqrt(epsilon)|j|]/d0.

For the tail (L,infinity), L>=1, the norm bound is

    [4 exp(-L/2)+exp(-2L)]||h||_0/d0.

The trace is bounded by the piecewise Sobolev norm. These estimates prove operator-norm convergence of the regulated gamma response D_br->H_0, hence also D_br->H_-. Fourier transformation of the finite regulators and identification of their pointwise symbol limit recover Atilde_infty on its maximal multiplier domain. In particular every input in D_br lies in that domain after Fourier transformation.

No zero trace or new gamma subtraction is selected. The jump contributes the explicitly integrable square-root regulator term.

## 5. The limiting full response

Set

    Atilde_rig=Atilde_infty+T_prime : D_br -> H_-.

At finite P this is the existing Atilde_P on the common source domain, viewed in the weaker response space. The convergence satisfies

    ||(Atilde_rig-Atilde_P)h||_(H_-) <= 2 T_N ||h||_(H_+).

Gamma regulator removal and prime-place exhaustion can be performed independently: their operator-norm errors add. This supplies an actual response limit with explicit cutoff control, not only a weak identity on selected exponential states.

For different gamma, these constructions agree under the natural domain inclusions and dual restrictions. Finite sums agree, and their absolutely convergent limits agree. No optimality claim for the chosen weighted test scale is made.

## 6. Compression and leakage remain separate

Both support projections are contractions on H_+ and H_-. For f in the original half-line D_gamma^1 define

    B_rig f=-restriction_(u>0) Atilde_rig E_+ f,

    leak_rig f=restriction_(u<0) Atilde_rig E_+ f.

Their values are in the corresponding weighted NEGATIVE-norm half-line spaces. They retain all gamma and prime components. The exact identity is

    Atilde_rig E_+ f=-E_+ B_rig f+E_- leak_rig f

in H_-. Both terms are limits of the supplied finite-place terms; neither is discarded.

For the prime leakage alone, only S_(log n) contributes on the negative side. Therefore its place-cutoff error has the sharper bound

    ||leak_prime-leak_prime,P||_(H_gamma^+ -> H_- on R_-)
       <= T_N.

The full positive-side response has the bound 2T_N. In particular the previously divergent leakage is now an actual convergent vector in a DECLARED weighted dual space. It has not been encoded as an endpoint scalar or cancelled by a fitted correction.

## 7. Fourier transport must also be rigged

Define the spectral test space Hhat_+=F(H_+) with its transported norm. For v in H_- define F_-v as the functional

    (F_-v)(F h)=<h,v>_0,  h in H_+.

On H_0 responses this agrees with ordinary unitary Fourier transformation and L2 pairing. In general an H_- vector may grow exponentially; its ordinary tempered Fourier transform is NOT presumed to exist.

Thus F_- is the correct dual Fourier transport into Hhat_+^h. The finite responses A_P Fh converge there to

    A_rig(Fh)=F_- Atilde_rig h,  h in D_br.

The compression/leakage identity in section 6 transfers literally through F_-. It must not be written using an L2 Fourier operator on a response known only to lie in H_-.

This identifies the exact topology in which the finite-place spectral maps have a limit, rather than declaring a pointwise infinite Tate multiplier on the critical frequency line.

## 8. Endpoint graph and limiting arithmetic form

Keep the original half-line endpoint functionals

    ell_+(f)=integral exp(-u/2)f(u)du,
    ell_-(f)=integral exp(u/2)f(u)du,

and beta_end=(ell_+,ell_-), with J_end the swap matrix. They are bounded on H_gamma^+ because gamma>1/2.

For f,g in D_gamma^1 the exact limiting identity is

    q_ar(f,g)
      =-<E_+f,Atilde_rig E_+g>_0
         +beta_end(f)^* J_end beta_end(g).

The first bracket is test/dual pairing. Equivalently it is the corresponding spectral dual pairing under F and F_-. It follows either by operator-norm convergence of the finite-place comparison or by the already convergent half-line prime form.

The correlated source graph is still (E_+f,beta_end(f)), and its response is (-Atilde_rig E_+f,J_end beta_end(f)). Negative-side test functions observe leak_rig directly, even though the positive-side arithmetic form does not. The endpoint data come from the same f and stay independent of the place cutoff.

On the prescribed completed-theta states this recovers the existing full Euler-chart Clark polarization. It does not assert that the arithmetic-only even port reproduces arbitrary forcing-window pairings.

## 9. Compatibility with the no-go and with residual ports

For a short-support positive source, the unweighted one-prime leakage norm is proportional to

    (log p)^2/(p-1).

In the present negative-side weighted norm the exact same disjoint-tower computation gives

    ||leak_p f||_(H_-)^2
      =(log p)^2/[p^(1+2 gamma)-1] ||f||_(H_gamma^+)^2.

The source values and translation coefficients are unchanged; only the response topology differs. Consequently the earlier failure of strong or weak UNWEIGHTED L2 convergence remains valid, including on prepared positive Euler states.

Nima's `the-residual-port-restores-the-labelled-two-seam-comparison.md` retains the independent window-moment residual in a triangular even/moment coordinate change. The present rigged identity may be used on its arithmetic summand. That residual is NOT negative-half-line Tate leakage, does not cancel it, and is not eliminated by this dual-space completion. No new multi-seam arithmetic equivalence follows merely from the one-slot response limit.

Still separate are angular-sector assembly, positivity, an unweighted self-adjoint all-prime operator, and completed perfect-module duality. The construction preserves the existing scalar pairing and all response labels while weakening only the specified response topology.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_rigged_all_prime_tate_comparison.py`

Passed 2210 two-sided translation-weight checks, 24 weighted prime-tower identities, the cutoff integral and gamma jump/tail integrals, and a non-real signed compression/leakage fixture. Infinite convergence follows from the explicit summable operator majorant above.

References:

- `research/voevodsky/the-trivial-sector-arithmetic-form-is-a-tate-compression-with-explicit-leakage.md`;
- `research/grothendieck/all-prime-tate-leakage-diverges-on-the-common-euler-source-domain.md`;
- `research/grothendieck/the-euler-gamma-endpoint-operator-reconstructs-the-two-clark-sheets.md`;
- `research/nima/the-residual-port-restores-the-labelled-two-seam-comparison.md`.
