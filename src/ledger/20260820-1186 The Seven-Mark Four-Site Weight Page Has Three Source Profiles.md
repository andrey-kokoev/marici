---
title: "The Seven-Mark Four-Site Weight Page Has Three Source Profiles"
date: 2026-08-20
entry: 1186
status: partially-superseded-by-entry-1188
sector: cosmology
---

# 1186 — The Seven-Mark Four-Site Weight Page Has Three Source Profiles

Sequence claim: `seqclaim-489c2cde145dc0b22277eb58`.

> **Correction (Entry 1188).** The surface counts and (W_4) ranks below
> remain valid, but the displayed (W_5) and (W_6) budgets assumed every
> distinct pair line avoided the branch nodes. In the source packet,
> boundary-sum pairs share two nodes and their double covers split into
> rational deck pairs. Treat the (W_5,W_6) columns below only as the
> branch-avoiding benchmark.

## Typed logarithmic page

For the total-energy quartic double solid \(X\) with marked divisor \(D\),
the generic logarithmic weight page contributing to degree-three complement
cohomology has layers

\[
H^3(X),
\qquad
H^2(D_i)(-1),
\qquad
H^1(D_{ij})(-2),
\qquad
H^0(D_{ijk})(-3).
\]

After identifying equal geometric hyperplanes, occurrence duplicates remain
as contractible labelled simplices. For distinct geometric marks, use the
source-derived coefficient types:

- rank \(20\) for the quartic-double-solid middle system;
- rank \(7\) for a smooth-mark \(E_7\) primitive kernel;
- rank \(3\) for a four-node-mark \(A_1^3\) primitive kernel;
- rank \(2\) elliptic \(H^1\) for each generic pair intersection;
- two deck-resolved Tate points for each generic triple intersection.

## Exact source profiles

The 28 terms reduce to three geometric profiles:

\[
\begin{array}{c|c|c|c|c|c|c}
\#D_i&\text{smooth}&\text{four-node}&W_4&W_5&W_6&\text{terms}\\
\hline
5&0&5&15&20&20&4\\
5&1&4&19&20&20&4\\
6&1&5&22&30&40&20.
\end{array}
\]

All profiles also have

\[
W_3=20.
\]

Here \(W_k\) denotes the rank budget on the indicated generic associated-
graded layer, not the final rank of \(H^3(X\setminus D)\).

## Meaning

The seven-mark coefficient system is finite and rigidly typed:

\[
\boxed{
\text{threefold middle variation}
+
\text{Tate }E_7/A_1^3\text{ surface lattices}
+
\text{elliptic pair systems}
+
\text{deck-Tate triple points}.
}
\]

No additional Hodge type is available at the generic \(E_1\) page. This is
strong support for H2 at four sites, but it is not yet a cohomology theorem:
incidence differentials, branch collisions, and nontrivial extensions can
reduce or glue these ranks.

## Next falsifier

Compute the first weight-page differential using the actual labelled
restriction/Gysin maps. Start with one representative of each of the three
profiles. Preserve the elliptic pair systems rather than replacing them by
their ranks. A residual object outside the displayed four coefficient types
would falsify the current finite architecture.

## Evidence

- `research/benincasa/checkers/four_site_qg_seven_mark_weight_page.py`
- `research/benincasa/results/four-site-qg-seven-mark-weight-page.json`
- Entries 1159--1161 and 1182--1185.
