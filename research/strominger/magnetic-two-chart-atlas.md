# Two maximal-minor charts cover every tested injective component

Companion to checkers/magnetic_atlas_complexity_checks.py (6/6, exit 0) and
results/magnetic_atlas_complexity.json.

Across

\[
2\le g\le8,\qquad1\le q\le30,\qquad0\le k\le20,
\]

4,371 injective component blocks were compared in two coordinates:

1. the preferred Hall-selected maximal minor;
2. the canonical nonzero maximal minor selected from row pivots.

The alternate chart differs from the preferred chart by at most one target
row. No component requires two simultaneous exchanges, and every alternate
row set remains nested as the cutoff grows.

Only six \((g,q)\) pairs require a nontrivial chart:

\[
(2,12),\ (4,16),\ (5,4),\ (5,12),\ (6,20),\ (8,24).
\]

Their transitions use only three row swaps:

\[
1\mapsto3,\qquad -4\mapsto-6,\qquad4\mapsto2.
\]

All other injective blocks remain in the preferred chart. The only
simultaneous vanishing of every maximal-minor coordinate occurs at the known
rank-defect loci

\[
(g,q)=(2,1),\qquad(2,7).
\]

This supplies a finite-range two-chart Plucker theorem:

\[
\boxed{
\text{injective component}
\Longrightarrow
\text{preferred chart or one-row neighbor is nonzero}.
}
\]

The atlas size is independent of cutoff throughout the scan. The result is
not yet unbounded in \(g,q\); a symbolic classification of the three
row-exchange mechanisms remains open.

