---
title: "Deck Chamber Induction Is Not Orbit-Union Localization"
date: 2026-08-20
entry: 1220
status: active-supported-typing
sector: cosmology
---

# 1220 — Deck Chamber Induction Is Not Orbit-Union Localization

Sequence claim: `seqclaim-2e3c63dd6fa9fe371ed39243`.

## Two inequivalent completions

Entry 1219 constructs the 91-section union of all signed deck translates of
the physical marked divisor. Before computing relative cohomology, distinguish
that union from the equivariant orbit of the physical pair.

Let \(G=C_2^5\), let \(D_+\) be the 26-section positive physical divisor,
and let

\[
U_g=B\setminus gD_+.
\]

There are two different constructions:

\[
\boxed{
\operatorname{Ind}_{1}^{G}\mathcal M_+
=
\bigoplus_{g\in G}R\Gamma(U_g,\mathcal L_g)
}
\]

and

\[
\boxed{
R\Gamma\left(
B\setminus\bigcup_{g\in G}gD_+,
\mathcal L
\right).
}
\]

The first is the induced package of chamber presentations. The second
localizes away every signed wall simultaneously. They are not the same
object.

## Exact incidence packet

The stabilizer of the positive arrangement is trivial, so there are

\[
\boxed{32}
\]

distinct chamber presentations, each containing 26 sections. Thus the
induced package contains 832 section occurrences.

Their union has only 91 distinct sections because of stabilizers at the
section level:

\[
\begin{array}{c|c|c}
\text{section type}&\text{distinct sections}&\text{presentations per section}\\
\hline
\text{total energy}&1&32\\
\text{signed }G\setminus e&10&16\\
\text{signed partial energy}&80&8.
\end{array}
\]

The incidence check is

\[
1\cdot32+10\cdot16+80\cdot8=832.
\]

## Correct equivariant descent

The deck group permutes the 32 chamber summands transitively. After retaining
the labelled deck transports, a compatible invariant tuple is determined by
its value in the identity chamber. Hence evaluation at that chamber identifies

\[
\left(operatorname{Ind}_{1}^{G}\mathcal M_+\right)^G
\simeq
\mathcal M_+.
\]

This does not average or enlarge the physical divisor. It packages all its
deck presentations and then imposes transport compatibility.

By contrast, the 91-wall complement receives restriction maps from every
\(U_g\), but no inverse is supplied. Passing to it is an additional
localization operation.

## Correction to the frontier

The next physical comparison is not initially

\[
H^\bullet(U_+)\to H^\bullet(U_{91}).
\]

It is first the construction and coherence audit of the 32 transported
relative complexes. Only afterward may the common 91-wall localization be
studied as a supported comparison target.

\[
\boxed{
\text{orbit induction}
\neq
\text{orbit-union localization}.
}
\]

## Carrier verdict

Both constructions use the same frozen energy/Cut carrier and its deck
translates. Their difference is categorical and coefficient-theoretic, not a
new incidence generator.

## Next falsifier

Construct the labelled transition functors between the 32 chamber-relative
complexes and test the \(C_2^5\) cocycle on generators. A failed cocycle would
obstruct equivariant physical descent. If it closes, compare the induced
invariant object with the Bunch--Davies positive chamber before considering
the 91-wall supported cofiber.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_deck_chamber_induction.rs`
- `research/benincasa/results/five-site-deck-chamber-induction.json`
