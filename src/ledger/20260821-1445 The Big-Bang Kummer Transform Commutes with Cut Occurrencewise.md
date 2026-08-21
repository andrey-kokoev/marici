---
author: marici.Benincasa
---

# 1445 — The Big-Bang Kummer Transform Commutes with Cut Occurrencewise

## Status

Source-derived coefficient-level Cut compatibility for Entry 1444. This keeps
the endpoint transform distinct from the universal-integrand residue
normalization.

## Source exponent

For a labelled site \(s\), equations (2.18), (2.20), and (2.21) of the primary
source give

\[
\beta_s
=
\rho_s
+\gamma\left[
2-\frac{(k_s-2)(d-1)}2
\right],
\]

where

\[
\rho_s
=
\sum_{j\in\operatorname{Ext}(s)}l_j
+
\sum_{e\in\operatorname{Int}(s)}l_e.
\]

The Fourier--Laplace image of the source-selected irregular endpoint carries
the labelled positive measure

\[
z_s^{\beta_s-1}\vartheta(z_s)dz_s.
\]

## Cutting one internal edge

Let \(e\) connect labelled endpoints \(s\) and \(t\). Resolving the Cut creates
two external occurrences

\[
e_s,qquad e_t.
\]

At endpoint \(s\), the operation replaces

\[
l_e\in\sum_{e\in\operatorname{Int}(s)}l_e
\]

by

\[
l_{e_s}=l_e
\in
\sum_{j\in\operatorname{Ext}(s)}l_j.
\]

The same occurs independently at \(t\). The total number of fields entering
each interaction, \(k_s\) and \(k_t\), is unchanged. Therefore

\[
\boxed{
\beta_s^{\rm cut}=\beta_s,
\qquad
\beta_t^{\rm cut}=\beta_t.
}
\]

The two positive Kummer measures and their monodromy characters are preserved
exactly.

## Commuting coefficient square

At coefficient level,

\[
\begin{array}{ccc}
\text{irregular time-endpoint object}
& \xrightarrow{\mathfrak F_!} &
\text{positive site Kummer object}\\
\big\downarrow_{\operatorname{Cut}_e}
& &
\big\downarrow_{\operatorname{Cut}_{e_s,e_t}}\\
\text{two resolved endpoint occurrences}
& \xrightarrow{\mathfrak F_!} &
\text{two resolved positive Kummer occurrences}
\end{array}
\]

commutes because both routes preserve the labelled exponent at each endpoint.

## Type boundary

This does not recompute the residue or normalization of the bulk-to-bulk
propagator. That datum belongs to the universal graph integrand and its
existing Cut map. Entry 1445 proves that adjoining the Big-Bang
Fourier--Laplace coefficient object introduces no additional sewing defect.

Physical diagonal identification of the two Cut occurrences is later data; any
factor \(2\) produced there remains an occurrence-identification effect.

## Consequence

For source scalar graphs,

\[
\boxed{
\text{the }\gamma>1\text{ Big-Bang endpoint adds an irregular coefficient
layer but no new Cut incidence rule.}
}
\]

This is direct support for H2:

\[
\text{shared carrier and Cut calculus}
+\text{sector-specific Stokes/Kummer coefficients}.
\]

## Next falsifier

Test a nontrivial nested or loop sewing where several endpoint transforms meet
one resolved Cut flag. Preserve every occurrence label and prohibit diagonal
specialization until after the comparison square is formed.

## Durable evidence

- `research/benincasa/big-bang-fourier-laplace-comparison.md`;
- primary source equations (2.17)--(2.22);
- allocator claim `seqclaim-3996bba87bed07970f7a5c56`.
- epistemic event `ev-000000001534-6df592d6-d325-429f-a870-bfde23fcb325`.
