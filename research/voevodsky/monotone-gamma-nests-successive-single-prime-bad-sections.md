# Monotone gamma nests successive single-prime bad sections

## Question

Does monotonicity of the gamma multiplier control the total endpoint variation across the one-prime cosine lobes?

## Claim boundary

After translating every cosine period to one reference cell, successive bad sections are nested. If each section is connected, its two endpoints move inward monotonically, so their total variation telescopes and is bounded independently of the number of lobes. Connectedness of every source section remains the first missing analytic premise.

## Reference-cell sections

Let

\[
a(u)=m_\Gamma(u)-c\cos(\omega u),
\qquad
p=\frac{2\pi}{\omega},
\]

and fix \(\delta\). In the reference cell \([-p/2,p/2]\), define

\[
S_j
=
\{x:m_\Gamma(jp+x)-c\cos(\omega x)<\delta\}.
\]

Since \(m_\Gamma\) is strictly increasing on the positive axis,

\[
m_\Gamma((j+1)p+x)
>
m_\Gamma(jp+x).
\]

The cosine term is identical in both cells. Therefore

\[
S_{j+1}\subseteq S_j.
\]

This nesting is exact and uses no approximation that gamma varies slowly.

## Endpoint variation

Assume each nonempty section is one interval,

\[
S_j=[\alpha_j,\beta_j].
\]

Nesting gives

\[
\alpha_j\leq\alpha_{j+1},
\qquad
\beta_{j+1}\leq\beta_j.
\]

Hence

\[
\operatorname{TV}(\alpha)
=
\alpha_{N-1}-\alpha_0,
\]

\[
\operatorname{TV}(\beta)
=
\beta_0-\beta_{N-1}.
\]

Consequently,

\[
\operatorname{TV}(\alpha)+
\operatorname{TV}(\beta)
\leq
\beta_0-\alpha_0
\leq p.
\]

The Abel modulation budget is therefore independent of \(N\).

## Connectivity gate

Nesting alone does not prove that \(S_j\) is connected. The right half-cell is straightforward because

\[
\frac{d}{du}
[m_\Gamma(u)-c\cos(\omega u)]
=
m_\Gamma'(u)+c\omega\sin(\omega u)>0
\]

where \(\sin(\omega u)\geq0\). The left half-cell needs a derivative or convexity comparison excluding more than one turning point. Numerical root isolation observed one interval per occupied lobe, but that is not a theorem.

## Disposition

The endpoint-variation problem is reduced to connectivity of each one-prime bad section. Once connectivity is proved, the total variation bound entering Abel summation is at most one cosine period, rather than growing with the component count. No transition-trace or RH conclusion follows yet.

## Verification

- `research/voevodsky/checkers/check_nested_bad_section_variation.py`
- `research/voevodsky/results/nested_bad_section_variation.json`
