# Single-current phase no-go

## Bounded question

Within the WP638 low-energy theory, can any source-authorized experiment using
only the single charged current reconstruct its overall phase or uniquely
recover the ultraviolet path ratio?

## Single-current groupoid

After messenger matching, write the charged portal as

\[
\chi J+\chi^\dagger J^\dagger,
\qquad
J=g\mathcal O_6,
\qquad
g=L_A+L_B.
\]

The admitted charged-field rephasing acts by

\[
\chi\mapsto e^{i\alpha}\chi,
\qquad
g\mapsto e^{-i\alpha}g.
\]

A \(\chi\)-free source record must have zero net charged-field number. Every
polynomial monomial \(g^m(g^*)^n\) that descends therefore satisfies \(m=n\)
and is a power of \(q=|g|^2\). Thus

\[
\mathbb C[g,g^*]^{U(1)}=\mathbb C[q].
\]

The overall phase of \(g\) is not missing physical information in this
groupoid; it is gauge-equivalent presentation data. Adding a second charged
current \(r\) would create the relative invariant \(gr^*\), but that is a new
relational experiment over the stabilizer of the reference current. It does
not reveal an absolute phase of the original one-current theory.

## Ultraviolet decomposition kernel

The map from two messenger paths to the low-energy current is addition:

\[
(L_A,L_B)\longmapsto g=L_A+L_B.
\]

It is not faithful to the ultraviolet cycle coordinate. The exact pair

\[
(L_A,L_B)=(1,1),
\qquad
(L_A,L_B)=(1+i,1-i)
\]

has the same matched current \(g=2\). Its path ratios are respectively \(1\)
and \(-i\), so the points are inequivalent under the cycle invariant while
every probe factoring only through the single low-energy current identifies
them.

This does not contradict WP636: a heavy transition that resolves the two paths
can detect their relative phase. It proves that integrating out the path
resolution is itself a nonfaithful arrow.

## Classification

The one-current invariant ring rigidifies the charged portal only up to its
norm. It does not select a value of the UV cycle, does not select `physical16`,
and cannot identify the UV constructor. Two distinct repairs exist:

1. retain a source-authorized path-resolving heavy experiment;
2. add a second charged reference current and state the new stabilizer
   groupoid explicitly.

Neither repair is presently a detector-calibrated flavor instrument. The
smallest exact UV falsifier is the two-point pair above.

## Reproduction

Run:

    python research/flavor/checkers/wp642_single_current_phase_no_go.py

The generated result is
`research/flavor/results/wp642_single_current_phase_no_go.json`.
