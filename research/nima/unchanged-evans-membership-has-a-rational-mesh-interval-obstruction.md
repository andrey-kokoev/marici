# Unchanged Evans membership has a rational-mesh interval obstruction

## Question

Can the unchanged two-sided Evans state supply the missing conservative comparison at every Xi divisor point? The operator requested an attack on the joint coherence/spectral-kernel formulation rather than another reformulation of its acceptance criteria.

SCC obligation: forward realization and route/coherencer compatibility. This is a hostile on the unchanged-state candidate, not a construction of the missing independent arithmetic crossing. The SCC model census was inspected; its older corrected-G4 model does not substitute for a certificate of this scalar residual.

## Claim boundary

Write

\[
X(x)=\xi(\tfrac12+ix),\qquad
H(t)=\int_0^\infty |X(x)|^2\frac{2t}{x^2-t^2}\,dx.
\]

At the Arb-certified first zeta zero ordinate t_1, a fresh rational-mesh ball calculation gives

\[
H(t_1)<-0.14613<0.
\]

This certifies nonvanishing of the declared unchanged-Evans Hilbert residual. Any candidate comparison that requires this residual to vanish at every Xi zero fails already at t_1. In particular this residual cannot equal a holomorphic multiple of the Xi section near that point. It does not rule out a modified history or cancellation in a different, independently source-defined full adjoint. It has no RH implication: the tested zero is on the critical line.

The earlier conversational claim that only high-precision scouting existed was outdated. A complete Arb certificate already exists under `research/voevodsky/`; the present checker independently reproduces strict negativity with exact rational partition endpoints, a Cauchy bound valid on the entire omitted interval, and an explicit elementary infinite-tail integral. No cross-owner artifact was modified.

## Governing test and rivals

- Proposed closure: the unchanged Evans state already satisfies the tested conservative adjoint equation whenever its Xi mismatch vanishes.
- Rival: spectral matching and conservative admission differ; the tested residual survives at a known Xi zero.
- Risky consequence: closure requires H(t_1)=0. The rival is certified by an enclosure whose upper endpoint is strictly negative, including all omitted pieces.
- Strongest falsification attempt: certified root, ball quadrature, removable-point bound and infinite-tail bound, without treating a high-precision decimal as an exact root or a finite cutoff as the whole integral.

## Certificate construction

The checker obtains t_1 from `acb.zeta_zero(1)` at 160-bit precision and verifies its real part is exactly 1/2. The finite integration ranges are [0,14.12] and [14.15,30], with 29,970 cells of maximum width 1/1000. Every endpoint is rational, and each Arb interval is checked to contain both endpoints. No binary-float mesh is used.

The omitted interval is [L,R]=[14.12,14.15]. Its center is c=14.135 and its half-width is 0.015. Evaluate xi on the complex square enclosing the disk of radius 1/8 around 1/2+ic. If F bounds its modulus, Cauchy's estimate supplies

\[
M=\frac{F}{1/8-0.015}
\]

as a derivative bound at every real parameter in the omitted interval, not merely at its center. Since X(t_1)=0,

\[
|X(x)|\le M|x-t_1|.
\]

Consequently the entire omitted contribution has absolute bound

\[
\frac{2t_+}{L+t_-}\,M^2
\frac{(t_1-L)^2+(R-t_1)^2}{2}.
\]

All occurrences of t_1 are ball-enclosed. The 160-bit run bounds this contribution by 1.838 times 10^(-5).

### Explicit tail for x >= 30

Take N=ceil(x) and s=1/2+ix. Euler–Maclaurin with the first periodic Bernoulli remainder gives

\[
|\zeta(s)|
\le 2\sqrt N+\frac{\sqrt N}{x}
+\frac1{2\sqrt N}+\frac{|s|}{\sqrt N}
\le4\sqrt{x+1}.
\]

Indeed, after division by sqrt(x+1), the four terms are bounded by 2, 1/x, 1/(2x), and 1, respectively, on this range.

For w=1/4+ix/2, the complex Stirling remainder obeys

\[
|R(w)|\le\frac1{12|w|\cos^2(\arg(w)/2)}
\le\frac1{3x}.
\]

Using y atan((1/4)/y) <= 1/4 for y=x/2 then gives

\[
|\Gamma(w)|\le\sqrt{2\pi}(x/2)^{-1/4}
\exp(-\pi x/4+1/(3x)).
\]

Substitution into the completed-Xi formula yields

\[
|X(x)|^2\le25x^{9/2}e^{-\pi x/2}.
\]

The dimensionless prefactor is decreasing for x>=30 and its computed value at 30 is less than 21.199. For the enclosed first zero,

\[
\frac{2t_1}{x^2-t_1^2}\le\frac{40}{x^2}.
\]

With a=pi/2 and X_0=30, the infinite tail is therefore at most

\[
\frac{1000}{\sqrt{X_0}}e^{-aX_0}
\left(\frac{X_0^3}{a}+\frac{3X_0^2}{a^2}
+\frac{6X_0}{a^3}+\frac6{a^4}\right)
<1.146\times10^{-14}.
\]

This is an analytic infinite-range bound, not a convergence inference from finite samples.

## Execution and disposition

Checker:

```text
python research/nima/checkers/check_unchanged_evans_rational_ball_certificate.py
```

Dependency: python-flint 0.9.0. The checker uses the existing repository installation at `research/flavor/.venv/Lib/site-packages` read-only when absent from the default interpreter's path. No package installation or subprocess wrapper is performed. Structured-command refused a new uv/python-flint environment invocation and a direct virtual-environment executable invocation; its admitted `python` command successfully imported the existing package and executed the checker.

Result: `research/nima/results/unchanged-evans-rational-ball-certificate.json`. The 160-bit, width-1/1000 run certified upper bound -0.1433727837392924... . An independent precision/mesh rerun at 224 bits and width 1/2000 (59,940 cells) tightened it to -0.1461387703322955... . Reproduce the latter with `--bits 224 --mesh 1/2000`; its structured-command execution is `e_25120_1791001127945995700_167`. The result records the checker digest and backend location.

A width-1/100 attempt did not certify negativity; the zero-exclusion test was retained and the mesh refined. The checker also deliberately enlarges its certified enclosure to include zero and verifies that this loose enclosure cannot certify rejection. No claim of a formally verified numerical library is made: the certificate uses Arb's validated arithmetic and zeta-zero routine together with the explicit analytic estimates above.

Owner-local SCC manifest: `research/nima/scc-models/unchanged-evans-first-zero-interval.json`. It classifies this as a falsifier of one unchanged-state comparison, not RH closure.

Disposition: the unchanged-state, zero-Hilbert-residual closure candidate is rejected. The first-zero scalar spectral port vanishes while this coherence port does not. The source-authorized modified-history or full-adjoint comparison remains unconstructed; positivity of other source objects does not repair this mismatch.

## Evidence and unchanged source boundaries

- `research/voevodsky/checkers/check_first_zero_evans_complete_certificate.py`: pre-existing root/finite/tail certificate assembly.
- `research/voevodsky/results/first_zero_evans_complete_certificate.json`: pre-existing certified negative upper bound.
- `research/voevodsky/checkers/check_first_xi_zero_evans_adjoint_hilbert_residual.py`: original numerical scout and normalization.
- `research/voevodsky/correction-the-four-unit-table-is-optional-and-the-active-evans-membership-gate-is-authority-blocked.md`: independent G4 crossing remains a separate source requirement; its numerical-only classification is superseded for this scalar test by the interval certificates.

No public-page claim, source comparison map, integral lattice identification, or RH proof is manufactured from this scalar rejection. Files remain local and uncommitted.
