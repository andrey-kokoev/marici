# The trivial-sector arithmetic form is a Tate compression with explicit leakage

## Strength and result

For the trivial angular character and a FIXED FINITE prime set, the constructed half-line arithmetic form is exactly the pullback of the negative semilocal Tate connection together with the prescribed endpoint swap. The map is zero extension followed by the unitary Fourier transform, with the two source endpoint functionals retained on its graph.

This is a genuine common-domain form comparison with the independently specified Tate multiplier. It is not an invariant-subspace intertwining: the complementary leakage is retained explicitly, and a prime-place increment has an infinite-rank nonzero leakage channel.

Inputs:
- `the-semilocal-tate-logarithmic-connection-commutes-with-fourier-sewing-and-adds-under-cutoffs.md`
- `euler-reflection-verifies-the-tate-gamma-matrix-unitarity-and-square-law.md`
- `a-subtracted-gamma-shift-operator-completes-the-one-slot-euler-green-form.md`

## 1. Freeze the independent Tate convention

Write xi for the real Mellin/Fourier frequency, and set s=1/2+i xi in the scattering formulas. With the supplied even archimedean branch,

    gamma_infty(xi)=pi^(i xi) Gamma(1/4-i xi/2)/Gamma(1/4+i xi/2),
    a_infty(xi)=-i partial_xi log gamma_infty
               =log(pi)-Re psi(1/4+i xi/2).

For an unramified finite prime p,

    gamma_p(xi)=(1-p^(-1/2-i xi))/(1-p^(-1/2+i xi)),
    a_p(xi)=2 log(p) sum_(k>=1) p^(-k/2) cos(k xi log p).

For a finite prime set P, let a_P=a_infty+sum_(p in P)a_p. The independently prescribed self-adjoint operator is multiplication by a_P on

    Dom A_P={h in L2(R):a_P h in L2(R)}.

The finite-place terms are bounded; the archimedean term grows at most logarithmically. These signs follow from the fixed convention -i partial log gamma. They must not be changed to force agreement with the arithmetic form.

## 2. Source map and common domain

Use D_gamma=H^1(R_+,exp(2 gamma u)du), gamma>1/2, with unrestricted endpoint trace, as in the one-slot arithmetic construction. Let E_+ be zero extension to the full real line and let F be the unitary Fourier transform with phase exp(-i xi u). Set

    U=F E_+.

This map is source-defined and isometric in the underlying unweighted L2 norm. For f in D_gamma, both f and f' are in L1 by the exponential weight. Integration by parts gives, for xi!=0,

    (F E_+ f)(xi)=(f(0)+integral_0^infinity exp(-i xi u) f'(u)du)
                  /(sqrt(2pi) i xi).

Together with the L1 low-frequency bound, this gives O(1/|xi|) decay with constants bounded by ||f||_D. Since a_P has logarithmic growth, a_P U f is square-integrable. Thus U maps D_gamma continuously into the maximal multiplier graph domain of A_P.

Zero extension need not belong to H^1(R) when f(0)!=0. That jump does NOT exclude it from the much weaker logarithmic multiplier domain. Imposing a zero trace here would incorrectly remove the prepared exponential states.

A common dense source core is the restrictions of compactly supported smooth real-line functions. The same core used in the preceding arithmetic construction therefore maps into Dom A_P without changing its boundary convention.

## 3. Compute the regular compression from source translations

Let V_P=sum_(p in P,k>=1) log(p)p^(-k/2) T_(k log p). This is bounded even on unweighted half-line L2 for finite P. Keep the subtracted gamma operator G from the preceding note. Define the regular form

    q_reg,P(f,g)=<f,(G-V_P)g>_0+<(G-V_P)f,g>_0.

A full-line left translation has Fourier multiplier exp(i a xi). Zero extension compresses it to the half-line left translation; its adjoint supplies the opposite translation in the symmetrized form. Therefore the prime multiplier of q_reg,P is -sum a_p.

For the gamma term, symmetrizing the REGULATED subtracted shift integral gives the full-line multiplier

    -log(pi)-gamma_E
      +integral_0^infinity
        [exp(-t)-exp(-t/4) cos(xi t/2)]/[1-exp(-t)] dt
      =-log(pi)+Re psi(1/4+i xi/2)
      =-a_infty(xi).

The subtraction is retained throughout. On the common core Fourier transformation of finite regulators is legitimate. The earlier graph estimates remove the half-line regulators. On the full line, zero extension satisfies the translation bound

    ||S_a E_+f-E_+f||_2 <= sqrt(a)|f(0)|+2a||f'||_2,

so the small-t full-line integral also converges in L2. The large-t integral is exponentially convergent. Closedness of the maximal multiplier identifies its limit with the displayed symbol.

Consequently on D_gamma,

    q_reg,P(f,g) = -<U f,A_P U g>_L2(R).

The sign is negative with the frozen scattering convention. This is not merely agreement of exponential scalar kernels; it holds for arbitrary vectors on the common graph domain.

## 4. Retain the endpoint graph

Use the source functionals

    ell_+(f)=integral exp(-u/2)f(u)du,
    ell_-(f)=integral exp(u/2)f(u)du.

They are continuous on H_gamma. Write beta_end(f)=(ell_+(f),ell_-(f)) and J_end=[[0,1],[1,0]]. The full finite-place arithmetic form is

    q_ar,P(f,g)=-<U f,A_P U g>
                +beta_end(f)^* J_end beta_end(g).

Thus f maps to the correlated response graph (U f,beta_end(f)) in Dom A_P plus the two-dimensional endpoint fiber. The endpoint data come from the SAME source f; no independent endpoint states are fitted.

The ambient operator -A_P direct_sum J_end is self-adjoint on its indicated product domain, but the source response occupies its graph image. No assertion that this graph is the whole product, reducing, or closed in every candidate norm follows.

The endpoint form need not be represented by an H_0-valued operator: exp(u/2) is not in unweighted L2. Retaining the endpoint fiber avoids that incorrect promotion.

## 5. Exact operator decomposition and leakage

Let Atilde_P=F^(-1) A_P F. For f in D_gamma define

    B_P f=-E_+^* Atilde_P E_+ f,
    leak_P f=1_(u<0) Atilde_P E_+ f.

Both are well-defined by section 2. The regular operator identity is

    A_P U f = -U B_P f + F leak_P f.

The negative-side term is the precise obstruction to replacing the compression theorem by the false intertwining A_P U=-U B_P. It is not automatically encoded by the rank-two endpoint swap.

For one prime p, take f supported in (0,log p). In the increment Atilde_p, the shifts S_(k log p) give disjoint negative-side translates, and the opposite shifts have no negative-side contribution. Hence

    ||leak_p f||_2^2
       =(log p)^2 sum_(k>=1) p^(-k) ||f||_2^2
       =(log p)^2/(p-1) ||f||_2^2.

This exhibits an infinite-rank leakage map on that interval. A finite-rank endpoint adjustment cannot cancel this prime increment for all such f. It does not assert that the full gamma-plus-prime leakage equals the prime leakage, or exclude cancellation on particular states.

## 6. Place naturality and remaining strength

Adding a prime changes A_P, B_P and leak_P by their independently defined prime increments. Thus the compression and leakage comparison is place-additive at each finite set. It respects the source operation rather than fitting a scalar correction after evaluation.

On the weighted Euler domain, V_P converges as P grows to the already constructed all-prime operator, so the HALF-LINE arithmetic forms converge there. This does not prove convergence of the full critical-line Tate multipliers or their negative-side leakage on the same states. Those limits must not be identified without an additional estimate.

For prepared completed-theta states, the form reduces to the finite-place arithmetic kernel; using the full prime operator recovers the earlier Euler-chart Clark identity. For finite P, the missing primes remain missing—the kernel is not silently called the full xi kernel.

Closed here: a source-defined graph-domain comparison with the independent trivial-sector finite-place Tate connection, the exact sign, endpoint realization, and explicit failure of invariant-subspace intertwining.

Still separate: arbitrary angular characters, an all-prime full-line operator limit, additional Sonin/Green boundary restrictions, and positivity. The source B/R tail split remains distinct from the arithmetic gamma/prime split.

## Verification

`uv run --with sympy --with mpmath python research/voevodsky/checkers/check_trivial_sector_tate_compression.py`

Exact prime-symbol and leakage-sum identities pass. High-precision archimedean fixtures match the independently recorded even scattering branch with its logarithmic derivative. The common-domain compression and extension are the proofs above, not a numerical claim of operator equivalence.
