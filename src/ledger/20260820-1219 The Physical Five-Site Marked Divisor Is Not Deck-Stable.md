---
title: "The Physical Five-Site Marked Divisor Is Not Deck-Stable"
date: 2026-08-20
entry: 1219
status: active-supported-equivariant
sector: cosmology
---

# 1219 — The Physical Five-Site Marked Divisor Is Not Deck-Stable

Sequence claim: `seqclaim-322eb92a3c664b4468ffa842`.

## Physical arrangement versus coefficient deck group

Entry 1217 constructs the physical \(C_2^5\) edge-sheet cover. The frozen
source divisor contains 26 positive-energy sections. It is not invariant under
the deck group: flipping \(y_e\) transports a positive partial-energy section
to a signed-energy section absent from the physical divisor.

Therefore

\[
\boxed{
\text{the physical marked-relative object is not itself a }C_2^5
\text{ representation}.
}
\]

Only its full deck-orbit completion carries that action.

## Exact orbit completion

The 26 sections have three profiles:

\[
\begin{array}{c|c|c|c}
\text{type}&\text{count}&\text{active sheet flips}&\text{orbit size}\\
\hline
q_G&1&0&1\\
q_{G\setminus e}&5&1&2\\
q_A&20&2&4.
\end{array}
\]

Hence the completed signed arrangement has

\[
\boxed{1+5\cdot2+20\cdot4=91}
\]

sections.

## Character decomposition

Let \(\chi_i\) be the sign character of the \(i\)-th edge sheet. The
91-dimensional section permutation module decomposes as

\[
\boxed{
26\,\mathbf1
\oplus
9\sum_{i=1}^5\chi_i
\oplus
2\sum_{1\le i<j\le5}\chi_i\chi_j.
}
\]

No character involving three or more sheet flips occurs. The dimension check
is

\[
26+5\cdot9+10\cdot2=91.
\]

## Physical selection

The Euclidean condition \(y_i\ge0\) chooses one positive section in each deck
orbit. That choice is source-defined by the real chamber but is not an
invariant vector of the orbit representation.

Averaging each orbit is canonical only after adjoining all signed sections.
It changes the marked divisor and therefore cannot be silently interpreted as
physical descent.

## Comparison with the occurrence kernel

Entry 1218 remains valid: complementary occurrence differences are deck
trivial because \(A\) and \(A^c\) have identical boundary-edge vectors. Thus

\[
\text{deck-trivial occurrence kernel}
\not\Rightarrow
\text{deck-stable full marked divisor}.
\]

This is another local-symbol versus global-object distinction.

## Classification

The 91-section completion is sector-specific signed-energy coefficient data
over the unchanged carrier. It does not justify adding carrier walls to the
physical positive arrangement.

## Next falsifier

Construct the relative cohomology first for the physical 26-section pair and
separately for the 91-section orbit completion. Derive the comparison induced
by inclusion. Test whether the physical Bunch--Davies chamber maps to a
canonical summand or extension; do not replace it by the invariant average.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_marked_deck_orbit_completion.rs`
- `research/benincasa/results/five-site-marked-deck-orbit-completion.json`
