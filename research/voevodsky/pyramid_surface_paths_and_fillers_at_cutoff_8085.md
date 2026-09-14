# Pyramid surface paths and fillers at cutoff 8085

## Question

Does the cutoff-8085 four-cube transition repeat the cutoff-525 pattern: coherent growth of surface paths and fillers, vanishing positive-degree cubical homology, and an independently arising probe-null direction?

## Claim boundary

The census compares the complete finite effective-divisor cubical complexes at cutoffs 8084 and 8085. Cells are generated directly from jointly admissible distinct shell moves. Boundary ranks are checked over two large prime fields; agreement is finite modular evidence for the reported integer ranks. Probe ranks come from the independently generated four-cube result.

## Bold conjecture

The grade-8085 edges complete a unique canonical four-cell

\[
[210;\{1,2,3,4\}],
\]

whose 24 direction orderings give typed surface paths from 210 to 1155. Every new lower-dimensional boundary relation is filled by an admitted higher cell, so positive-degree homology remains zero. Nevertheless, the existing two-modulated-setting probe acquires a one-dimensional radical, detected by a third setting.

## Rivals

- the truncation leaves an unfilled surface or higher cycle;
- more than one four-cell enters at the same grade;
- the canonical cube is present but some of its faces are absent from the admitted complex;
- the probe defect coincides with genuine homology rather than filled coherence;
- modular ranks disagree.

## Typed census

For each cutoff, enumerate all cells \([N;I]\) and their maximal directed path count \(|I|!\). Build every cubical boundary

\[
C_k\xrightarrow{d_k}C_{k-1}
\]

and verify \(d_{k-1}d_k=0\). Compute

\[
\beta_k=
\dim C_k-
\operatorname{rank}d_k-
\operatorname{rank}d_{k+1}.
\]

For the canonical four-cell, enumerate all 24 permutations of its shell directions and retain their complete vertex sequences.

## Risky consequences

The conjecture predicts:

- exactly one admitted four-cell at 8085 and none at 8084;
- all 24 square faces and all eight three-dimensional faces of the canonical four-cell are admitted;
- the 24 canonical surface paths have common endpoints 210 and 1155;
- every positive-degree Betti number is zero at both cutoffs;
- the independently measured two-setting deficiency changes from zero to one at 8085, while three settings restore zero.

## Computed census

At cutoff 8084, cell counts are

\[
(2547,2407,495,43),
\]

boundary ranks are

\[
(1955,452,43),
\]

and there are 3655 typed maximal cell paths. Every positive-degree Betti number vanishes.

At cutoff 8085, cell counts are

\[
(2548,2410,499,46,1),
\]

boundary ranks are

\[
(1956,454,45,1),
\]

and there are 3708 typed maximal paths. Again every positive-degree Betti number vanishes.

The grade adds one vertex, three edges, four squares, three cubes, and one four-cell. Their maximal-path contribution is

\[
3+4\cdot2+3\cdot6+1\cdot24=53,
\]

exactly the increase from 3655 to 3708. The unique four-cell has all 24 square faces, all eight three-faces, and 24 distinct directed paths from 210 to 1155.

## Disposition

The conjecture survives. Cutoff 8085 adds a completely filled four-dimensional coherence package with no positive-degree homology, while the independently computed probe deficiency follows zero, one, zero under two settings below, two settings at, and three settings at the cutoff. The probe-null direction therefore lies inside filled coherence rather than representing a missing filler. Any future nonzero positive-degree class will be retained as a genuine pyramid residual.
