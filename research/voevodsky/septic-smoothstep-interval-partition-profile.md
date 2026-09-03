# Explicit C3 interval partition profile

## Question

Can prior windowing results be turned into a concrete smooth proper-interval partition with an exact leakage constant?

## Claim boundary

This packet constructs a normalized auxiliary profile and computes its derivative budget. The chart locations and overlap width remain analytic choices, not arithmetic source data.

## Profile

Use the septic smoothstep

\[
s(t)=35t^4-84t^5+70t^6-20t^7,
\qquad 0\le t\le1.
\]

Extend it by zero for \(t\le0\) and one for \(t\ge1\). Its first three derivatives vanish at both endpoints, so the extension is \(C^3\). On an overlap of width \(h\), set

\[
s_h(x)=s(x/h).
\]

Then

\[
\lVert s_h'''\rVert_{L^1}=h^{-2}\lVert s'''\rVert_{L^1}.
\]

A two-window partition uses \(s_h\) and \(1-s_h\) on each overlap, with constant plateaus away from overlaps. Unlike a trigonometric polynomial, this piecewise-polynomial window can be subordinate to proper intervals.

## Exact derivative budget

The checker solves for the extrema of \(s''\) and evaluates

\[
\lVert s'''\rVert_{L^1}
\]

exactly. If the periodic cover has two overlap transitions, each of two complementary windows contributes two copies of this budget. Aspect's Fourier estimate then gives

\[
C_{\rm loc}(h)
\le
\frac{\pi}{6}
\cdot4h^{-2}\lVert s'''\rVert_{L^1}.
\]

This is explicit once \(h\) and the chart-coordinate normalization are fixed.

## Prior-research synthesis

Three earlier observations determine the construction:

1. the commutator needs a finite first absolute Fourier moment;
2. a \(C^3\) window bounds that moment by \((\pi/6)\lVert\chi'''\rVert_1\);
3. finite Fourier windows cannot have proper support, while sharp indicators fail the moment bound.

The septic profile occupies the remaining admissible class: compactly subordinate, finitely differentiable, and quantitatively bounded.

## Disposition

A concrete auxiliary partition profile now exists. The remaining source decisions are the interval cover, overlap width \(h\), and coordinate-transfer normalization. Different choices change only the explicit bounded remainder constant; independence of the final closed-form statement still requires a bounded-change comparison.

## Verification

- `research/voevodsky/checkers/check_septic_smoothstep_partition.py`
- `research/voevodsky/results/septic_smoothstep_partition.json`
- `research/aspect/interval-window-fourier-moment-gate.md`
