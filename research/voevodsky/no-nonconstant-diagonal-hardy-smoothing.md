# No nonconstant diagonal Hardy smoothing

## Question

Can the missing moment-to-Hardy comparison be repaired by damping polynomial coefficients with a fixed diagonal multiplier?

## Claim boundary

No. Every coefficient-diagonal map retaining any nonconstant coefficient is unbounded from a finite interval-moment norm to Hardy coefficient space. This does not exclude non-diagonal source-derived intertwiners.

## Candidate map

Let

\[
S\left(\sum_{k\geq0}a_kz^k\right)
=
\sum_{k\geq0}s_ka_kz^k
\]

for a fixed sequence \((s_k)\). This includes radial smoothing

\[
p(z)\mapsto p(rz)
\]

with \(s_k=r^k\), as well as faster coefficient damping.

Suppose there is some fixed \(k\geq1\) with

\[
s_k\neq0.
\]

## Hostile family

Take

\[
p_m(z)=(1-z)^m.
\]

For every finite positive measure \(\mu\) on \([0,1]\),

\[
\lVert p_m\rVert_{L^2(\mu)}^2
=
\int_0^1(1-z)^{2m}\,d\mu(z)
\leq
\mu([0,1]).
\]

The coefficient of \(z^k\) is

\[
(-1)^k\binom mk.
\]

Therefore

\[
\lVert Sp_m\rVert_{H^2}^2
\geq
|s_k|^2\binom mk^2.
\]

For fixed \(k\),

\[
\binom mk
\sim
\frac{m^k}{k!}.
\]

Hence

\[
\lVert Sp_m\rVert_{H^2}
\longrightarrow
\infty
\]

while the reference moment norm remains bounded. Thus \(S\) is unbounded.

## Consequences

The only bounded coefficient-diagonal map of this type can retain the constant coefficient alone:

\[
s_k=0
\qquad
(k\geq1).
\]

Such a rank-one projection cannot carry the Gaussian-jet family or reconstruct the zero-side form.

In particular, none of the following repairs the missing arrow:

- fixed radial dilation \(p(z)\mapsto p(rz)\) with \(r>0\);
- exponential coefficient damping;
- superexponential damping with every coefficient multiplier nonzero.

The reason is that the hostile sequence tests each fixed retained coefficient separately; decay as \(k\to\infty\) is irrelevant.

## Coherence interpretation

A diagonal smoother tries to compare the two observer families degree by degree. The lower observer family detects the failure: one fixed Hardy coordinate grows polynomially in \(m\) while the entire interval-moment observation stays bounded.

Therefore any viable comparison must mix coefficients non-diagonally, depend on the source geometry, or use a domain stronger than the finite moment norm. Merely damping high degree cannot supply the missing coherencer.

## Disposition

The simplest nontrivial Hardy intertwiner class is eliminated. The remaining candidate must be a genuinely non-diagonal source-derived transform, not a coefficient multiplier. This result does not provide such a transform and does not advance the RH implication directly.

## Verification

- `research/voevodsky/checkers/check_no_diagonal_hardy_smoothing.py`
- `research/voevodsky/results/no_diagonal_hardy_smoothing.json`
