---
id: 570
date: 2026-08-18
title: The Lower Conductor Graph Cycle Lies in Top-Weight H2
authors:
  - marici.Nima
---

# The Lower Conductor Graph Cycle Lies in Top-Weight \(H^2\)

Entry 569 computes one surviving deck-odd cycle in the \(K_{2,2}\) boundary
dual graph. This entry fixes its global cohomological degree.

Let \(U\) be the physical open tangential surface and let
\((X,D)\) be its resolved smooth compactification with SNC infinity divisor.
For a complex surface, reduced degree-one cohomology of the boundary dual
complex contributes to the top-weight part of middle cohomology:

\[
\boxed{
\widetilde H^1(\Delta(D))
\longrightarrow
\operatorname{Gr}^W_4H^2(U).
}
\]

Since

\[
\widetilde H^1(K_{2,2})\simeq\mathbb Q\langle\gamma\rangle,
\]

the conductor graph cycle belongs to the boundary/top-weight grade of
\(H^2(U)\), not automatically to \(H^1(U)\).

## Correction

The local classes of Entry 567 are degree-one classes of the local link
complement. After Čech and Gysin shifts in the surface weight spectral
sequence, their surviving graph combination occupies global degree two.
Therefore neither

\[
b_1=2
\]

nor

\[
b_1=1
\]

follows from Entries 567--569.

This removes an apparent conflict with the physical critical rank five. The
five-dimensional middle critical quotient can already contain:

- the top-weight graph cycle \(\gamma\);
- the adjacent sheet-difference boundary grade;
- three remaining interior/extension directions.

That pattern has exactly the deck-odd count \(2+3\) forced by Entry 565. It is
a compatible architecture, not yet a theorem that the physical
hypercohomology is concentrated in \(H^2\).

## Remaining gate

The full logarithmic weight differential must determine whether \(H^1(U)\)
vanishes and whether all five critical directions survive in \(H^2(U)\).
The relevant comparison is now within middle cohomology:

\[
3\text{ interior odd directions}
\quad+\quad
2\text{ boundary odd directions}.
\]

No enlargement to seven or nine physical classes is justified by the local
resonance census alone.

The executable degree audit is
\`research/benincasa/check_generic_lower_boundary_weight_degree.py\`.
