# Same-frame KK momentum-ratio cofiber: WP1062

## Question

What same-frame momentum ratios does the common-twist/KK source supply?

## Source-derived vector ports

WP1060 gives the half-twist pole/soft clock

\[
M^2=\frac{1}{4R^2}.
\]

WP771 gives vector KK masses

\[
p_N^2=M_{V,N}^2=\frac{N^2}{R^2}.
\]

In the same radius frame,

\[
\frac{p_N^2}{M^2}=4N^2.
\]

The radius cancels, so this ratio is independent of WP1061's unresolved
absolute clock.

The first two source-derived vector ports are therefore

\[
\frac{p_1^2}{M^2}=4,
\qquad
\frac{R(p_1^2)}{R(0)}=\frac{1}{1+4}=\frac15,
\]

\[
\frac{p_2^2}{M^2}=16,
\qquad
\frac{R(p_2^2)}{R(0)}=\frac{1}{1+16}=\frac1{17}.
\]

## Unit-ratio hostile

WP1042's conditional readout grants

\[
\frac{p^2}{M^2}=1,
\qquad
\frac{R(p^2)}{R(0)}=\frac12.
\]

That requires a distinct soft/pole-scale momentum channel. The vector KK law
alone does not supply it. Misidentifying the first vector KK port as the
unit-ratio port changes the normalized response by

\[
\frac12-\frac15=\frac3{10}.
\]

## Boundary

The next source must either:

1. derive an actual `physical16` production/decay channel at the soft/pole
   momentum scale; or
2. revise the integer-pole readout to a source-derived vector-KK ratio and
   carry that response through the WP1044--WP1052 gain chain.

The absolute radius, flux sector, and gauge--gravity ratio remain separate
WP1061 gates.

## Classification

Conditional same-frame momentum cofiber. It sharpens the calibrated-momentum
blocker into a missing soft-scale channel and an exact \(N=1\) vector-port
hostile.

Checker: `research/flavor/checkers/wp1062_same_frame_kk_momentum_ratio_cofiber.py`

Result: `results/wp1062_same_frame_kk_momentum_ratio_cofiber.json`
