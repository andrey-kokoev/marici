# Audit of the Kimi finite-double-contact literature sweep

## Question

Which claims in `references/kimi-finite-double-contact-literature-sweep-2026-09-05.md` survive the directly verified shifted-Gaussian normalization and the explicit heat-flow falsifier?

## Source condition

The incoming report is 988 lines and 150,640 bytes. It says it synthesizes ten dimension reports, a cross-verification report, and an insight report, but those referenced inputs are not present at the cited repository paths. The synthesis is therefore useful as a bibliography and conjecture index, not as reproducible verification of its individual source audits.

## Governing normalization

The directly verified BRS specialization uses

\[
K_{\mathrm{end}}(t,\xi)=e^{t/4-t\xi^2}\cos(t\xi)
\]

in the Marici convention, together with a translated digamma integral and the prime weight

\[
t^{-1/2}e^{-(\log n)^2/(4t)}\cos(\xi\log n).
\]

The normalized heat parameter is

\[
s=\frac1{4t},
\qquad
U(s,\xi)=\sqrt{\frac{t}{\pi}}\Theta(t,\xi),
\qquad
\partial_sU=\partial_\xi^2U.
\]

The incoming report instead bases its central Q1--Q2 synthesis on an endpoint proportional to `exp(t/8) cosh(xi/2)`, prime weights of `exp[-t(log n)^2/2]` type, and the assertion that increasing its `t` is forward heat flow. These are not a positive rescaling or reciprocal reparameterization of the verified two-variable kernel while retaining the same variable names. The report has combined a different explicit-formula test with the shifted spectral Gaussian.

## Rejected central claim: Widder plus Angenent

The report claims that positivity before a first violation and an exact forward heat equation exclude a multiple zero. In the correct heat coordinate, broad positivity lies at large `s`, while a first loss reached by increasing the inverse-variance parameter `t` is approached by decreasing `s`. The contact is the initial boundary of the forward-positive region, not an interior terminal zero reached from earlier positive heat data.

The exact solution

\[
\nu(s,x)=G_{A+s}(x)-
\sqrt{\frac{B+s_*}{A+s_*}}G_{B+s}(x),
\qquad A>B>0,
\]

has a nonnegative threshold trace with a quadratic zero, is strictly positive for `s>s_*`, and is negative at the origin for `s<s_*`. Its threshold trace is a positive Widder measure, and its double zero undergoes the zero-number drop allowed by Angenent. Backward uniqueness is irrelevant because the threshold profile is not identically zero. Thus the report's T1 does not unlock contact exclusion; the proposed theorem is falsified even after the exact heat equation is verified.

## Rejected escape argument

The report's escape proof uses exponential growth of `2 exp(t/8) cosh(xi/2)` and treats the endpoint and gamma terms as independent of `xi`. Neither statement applies to the verified kernel: its endpoint decays Gaussianly in `xi`, and its gamma term is a translated Gaussian average. Escape is nevertheless excluded by the correct argument

\[
K_\Gamma(t,\xi)
=\frac1{\sqrt{\pi t}}
\log\frac{|\xi|}{2\pi}+o_I(1)
\]

uniformly on compact positive `t`-intervals, while the prime term is bounded and the endpoint decays. The conclusion survives, but the report's derivation and its T4 asymptotic problem do not map to this model.

## Qualified useful results

### Almost-periodic prime comb

The correction from a naive `-sum a_n` infimum to minimization over completely multiplicative unimodular characters is mathematically relevant for prime-power frequencies. The example involving `log 2` and `log 4` correctly exposes dependent frequencies. It cannot reduce the full kernel to a one-variable comparison because the verified endpoint and gamma terms also depend on `xi`.

### Exact finite-type cardinal interpolation obstruction

An entire function of finite exponential type has `O(R)` zeros in a disk, whereas the zeta-zero multiset has `R log R` growth. Therefore exact cardinal interpolation that vanishes at every zeta node except finitely many is impossible in a fixed Paley--Wiener class. This does not exclude the weaker strict-peak condition with no prescribed zeros and no uniform gap below one.

### BRS and Burnol interpolation

BRS cardinal functions and Burnol Sonine evaluator systems remain legitimate non-bandlimited interpolation infrastructure. Their growth, quadratic closure, and approximation in the compact-factor Weil topology remain unproved interfaces.

### de Bruijn--Newman and Jensen routes

The report correctly identifies a direction and invariant mismatch: real-rootedness or polynomial hyperbolicity does not imply pointwise positivity of the shifted-Gaussian Weil kernel. These are negative near-matches, not contact-exclusion tools.

### Localized Weil forms

The references to Suzuki, Connes--Consani, Yoshida, Burnol, Bombieri, and Zhu identify real compact-window machinery. Such quadratic forms do not directly prove the pointwise linear inequality in `xi`. Any truncation route still needs a noncircular blockwise error estimate. The alleged Zhu certificate remains unavailable in its arXiv source package.

## Misstated Gaussian detection issue

The report says that Gaussian tests are not known to be positivity-detecting and proposes a form-domain density problem. For the linear completed source distribution, all-scale and all-translate Gaussian positivity is positivity-determining by the standard approximate-identity argument:

\[
(\mathcal W*G_s)(\xi)\ge0\ \forall s,\xi
\quad\Longrightarrow\quad
\mathcal W\text{ is a positive distribution}.
\]

This does not say that one Gaussian scale or a quadratic autocorrelation family is dense. The report conflates those distinct claims. Direct verification of Wong's criterion closes the linear-distribution-to-Weil promotion used by the current model.

## Corrected classification

| Incoming claim | Audit disposition |
|---|---|
| Widder--Angenent excludes first contact after checking the heat equation | rejected by exact counterexample and reversed parameter direction |
| Backward uniqueness handles the residual threshold | irrelevant unless the full threshold profile vanishes |
| Fixed-parameter escape excluded by exponential endpoint growth | wrong kernel; conclusion recovered by digamma coercivity |
| Prime comb infimum uses completely multiplicative characters | useful for the prime block only |
| Exact Paley--Wiener cardinal interpolation impossible | accepted |
| Weaker strict peak impossible | not established |
| de Bruijn--Newman/Jensen flows solve pointwise positivity | correctly rejected |
| Gaussian-to-Weil promotion needs unknown Gaussian density | rejected for the all-scale linear distributional formulation |
| Compact-window forms may provide partial margins | conditionally useful; full error interface absent |

## Remaining new bibliography to inspect

The report is valuable as a source list for:

- Widder, Angenent, and backward-uniqueness theorem hypotheses, now as documented near-misses;
- Cartwright--Levin and Beurling--Malliavin obstructions to exact finite-type interpolation;
- Suzuki and Connes--Consani form-domain results;
- quantitative Turan and prime exponential-sum barriers;
- PF and total-positivity failures claimed at finite order.

None of these citations currently constructs `FiniteDoubleContactExclusion`.

## Disposition

The sweep does not nearly settle item 3. Its main positive claim is invalid because it uses the wrong kernel and the wrong heat direction. Its surviving contribution is a strong bibliography, two useful obstructions, and several conditional compact-window or interpolation interfaces. The current frontier remains a strict arithmetic separation of the actual value, slope, and curvature contact requirements from the von Mangoldt moment body, especially near `xi=0`.
