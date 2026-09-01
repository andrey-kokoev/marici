# Radius absolute-clock no-go: WP1137

## Question

Can radius stabilization supply the absolute pole mass scale?

## DPC resolution

- **Conjecture:** curvature–flux radius stabilization supplies the absolute
  unit pole clock.
- **Rivals:** radius stabilization plus joint quantization; flux-sector source
  selection; gauge–gravity ratio selection; no absolute clock.
- **Risky consequences:** \(B/A=6n^2\), a unique sourced flux sector \(n\) and
  ratio \(B/A\), \(M^2=1\), and localized clock descent.
- **Falsification attempt:** the joint equation has at least two exact unit
  solutions, \((n,B/A)=(1,6)\) and \((2,24)\), while \((1,12)\) gives
  \(M^2=2\) and \((2,6)\) gives \(M^2=1/4\). No flux sector, ratio, or
  descent map is sourced.
- **Residual:** a future compactification packet may select \(n\) and \(B/A\)
  and prove descent.
- **Disposition:** reject radius stabilization as absolute pole-clock
  authority.

## Exact cofiber

\[
R_*^2=\frac{3n^2}{2(B/A)},\qquad
M^2=\frac{1}{4R_*^2}=\frac{B/A}{6n^2}.
\]

The condition \(B/A=6n^2\) is necessary for \(M^2=1\), but it does not select
the flux sector or localized clock.

Checker: `research/flavor/checkers/wp1137_radius_absolute_clock_no_go.py`

Result: `results/wp1137_radius_absolute_clock_no_go.json`
