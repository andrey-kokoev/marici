# Citation-backed paired-Hadamard-to-Laplace theorem

## Question

Do inspected classical sources now support the zero-side analytic bridge, including the absence of a residual exponential factor?

## Source statements inspected

E. C. Titchmarsh, *The Zeta-Function of Riemann* (Cambridge Tract 26, 1930), Introduction, equations (10)–(11), applies Hadamard factorization to the completed zeta function and writes its genus-one product over nontrivial zeros. In the same Introduction, equation (17) states

\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T).
\]

The Internet Archive scan inspected was item `in.ernet.dli.2015.203927`, file `2015.203927.The-Zeta_djvu.txt`; the OCR is imperfect, so the numbered equations, rather than its mangled symbols, identify the source locations.

Titchmarsh §3.2, following equations (3)–(6), proves `N(10)<1` and `N(18)>0`; since `N(T)` counts positive-ordinate nontrivial zeros with multiplicity, this already excludes `0<|Im rho|<=10`, hence the weaker required range through `1/2`.

Dave Platt and Tim Trudgian, “The Riemann hypothesis is true up to `3·10^12`,” arXiv `2004.09765`, Theorem 1, states that the lowest `12,363,153,437,138` nontrivial zeros lie on the critical line and verifies this through height `3,000,175,332,800`. The published version is *Bulletin of the London Mathematical Society* 53(3), 2021, 792–797, DOI `10.1112/blms.12460`. This is stronger supporting evidence but is not needed for the low-ordinate exclusion once Titchmarsh §3.2 is used.

D. V. Widder, *The Laplace Transform*, Princeton Mathematical Series 6, Chapter II, §§6.1–6.2, pp. 60–62, proves uniqueness for normalized determining functions, with Theorem 6.2 giving Lerch's uniqueness theorem for Laplace–Stieltjes transforms. The inspected scan was Internet Archive item `dli.ernet.206074`; electronic DOI `10.1515/9781400876457`.

## Theorem

Let

\[
\Xi(y)=\xi\!\left(\frac12+y\right),
\qquad a_\rho=\rho-\frac12,
\qquad \lambda_\rho=-a_\rho^2.
\]

Index one representative of each functional-equation orbit `a~-a`, retaining the original zero multiplicity `m_a`. Then:

1. the product
   \[
   \Xi(y)=\Xi(0)\prod_{[a]}\left(1-\frac{y^2}{a^2}\right)^{m_a}
   \]
   converges normally on compact subsets;
2. away from its zeros and from `y=0`,
   \[
   \frac{\Xi'(y)}{2y\Xi(y)}
   =\sum_{[a]}\frac{m_a}{y^2-a^2};
   \]
3. setting `x=y^2`, and defining
   \[
   H(t)=\sum_{[a]}m_a e^{-\lambda_a t},
   \]
   the series for `H` converges normally on every interval `t>=t0>0`, tends to zero as `t` tends to infinity, and satisfies
   \[
   \int_0^\infty e^{-xt}H(t)\,dt
   =\sum_{[a]}\frac{m_a}{x+\lambda_a}
   =\frac{\Xi'(\sqrt{x})}{2\sqrt{x}\,\Xi(\sqrt{x})}
   \]
   throughout any right half-plane contained in
   \[
   \operatorname{Re}x>-\inf_{[a]}\operatorname{Re}\lambda_a.
   \]

The square-root expression is branch-independent because the logarithmic derivative divided by `2y` is even.

## Derivation

Titchmarsh's zero count implies

\[
\sum_{[a]}\frac{m_a}{|a|^2}<\infty
\]

by dyadic shells: the shell with ordinates of size `2^k` contributes `O(k/2^k)`. Hence the paired genus-zero product converges normally.

Hadamard factorization leaves at most an exponential quotient `exp(A+By)` between `Xi` and the paired product. Both are even, so `B=0`; evaluation at `y=0` fixes `exp(A)=Xi(0)`. Thus no residual zero-free exponential factor survives.

Differentiating the normally convergent paired product gives the stated logarithmic derivative with one term per `a~-a` orbit. A positive critical-line ordinate contributes once. Off-line conjugation sends `a` to `conj(a)`, not generally to `-a`, so conjugate off-line functional-equation orbits remain distinct.

For every nontrivial zero `rho=beta+i gamma`,

\[
\operatorname{Re}\lambda_\rho
=\gamma^2-\left(\beta-\frac12\right)^2.
\]

The critical-strip bound gives `|beta-1/2|<1/2`, while Titchmarsh's `N(10)<1` gives `|gamma|>10`; consequently every `Re lambda_rho` is strictly positive. In particular it gives the uniform estimate `Re lambda_rho>100-1/4`.

For `t>=t0`, the zero count supplies a summable Gaussian shell majorant. On a right half-plane with `Re(x+lambda_a)>0`, Tonelli applied to absolute values reduces interchange to

\[
\sum_{[a]}\frac{m_a}{\operatorname{Re}(x+\lambda_a)}<\infty,
\]

whose tail is bounded by a constant times the inverse-square sum. Direct integration then proves the transform identity. Widder's Lerch theorem supplies uniqueness when this transform is compared with an independently derived continuous endpoint–gamma–prime kernel; equality almost everywhere upgrades to equality everywhere by continuity.

## Claim boundary

This theorem closes the zero-side Hadamard, multiplicity, convergence, low-height, interchange, and uniqueness gates. It does not yet verify that the separately derived endpoint–gamma–prime transform uses the identical completed-zeta normalization, nor does it prove all-rank positivity of the gamma-plus-prime remainder Hankel cones.

## Disposition

The next admissible step is a joint normalization comparison with the source-owned endpoint, gamma, and prime transform. The remainder-cone positivity problem remains independent and unresolved.