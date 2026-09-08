---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2224 — The Gaussian Score Selects the Contact-Infinity Cartier Grade

## Compactified response

Write

\[
\ell_i=\frac{\widehat\ell_i}{s_i}.
\]

Then

\[
R_{jk}
=-8\frac{s_js_k}{\widehat\ell_j\widehat\ell_k}.
\]

Ordinary restriction to either infinity component is zero. But the source-
fixed asymptotic coefficient is

\[
\boxed{
\lim_{s_j,s_k\to0}
\frac{R_{jk}}{s_js_k}
=-\frac8{\widehat\ell_j\widehat\ell_k}.
}
\]

Equivalently,

\[
\lim_{\ell_j,\ell_k\to\infty}
\ell_j\ell_kR_{jk}=-8.
\]

## Physical status

Unlike an unspecified boundary current, this Cartier grade is selected by
the asymptotic expansion of the already constructed mixed boundary
correlator. Its normalization is fixed by the known reciprocal contact
factors; no fitted rescaling is introduced.

The ordinary boundary value still exhibits route loss. The renormalized
asymptotic coefficient detects the filtered interference class of Entry 2178.

## Evidence

- Entries 2178 and 2217–2219
- `research/benincasa/checkers/contact_infinity_score_cartier.rs`
