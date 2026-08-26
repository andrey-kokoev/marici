# Critical-bifurcation authority (WP356)

## Bounded question

Can a source-derived pitchfork bifurcation select the small nonzero geometry
deformation required by WP353 without fitting a continuous source parameter?

Consider the minimal even source potential

\[
V(t)=\frac{r}{2}t^2+\frac{u}{4}t^4,
\qquad u>0.
\]

The source symmetry sends \(t\mapsto-t\). For \(r\geq0\), the unique minimum
is \(t=0\). For \(r<0\), the two minima obey

\[
t_\star^2=-\frac{r}{u}.
\]

Thus the transition selects a phase and a two-point sign fiber, but its
nonzero magnitude is the source ratio \(-r/u\).

## Authority test

Write \(q=t_\star^2\) on the broken branch. Then

\[
\frac{\partial q}{\partial r}=-\frac1u,
\qquad
\frac{\partial q}{\partial u}=\frac{r}{u^2}.
\]

Both admitted coefficients retain response away from the critical point. The
order-parameter susceptibility also diverges on approach from the broken
side:

\[
\frac{\partial t_\star}{\partial r}
=-\frac{1}{2\sqrt{-ru}}.
\]

Criticality therefore protects the symmetric value zero; it does not select a
small nonzero value robustly.

Discretizing the relevant coefficient does not close the gap. If
\(r=-m\Delta\), with \(m\) a positive integer and \(\Delta>0\), then

\[
q_m=\frac{m\Delta}{u},
\qquad
q_{\min}=\frac{\Delta}{u}.
\]

The integer labels branches, while the normalization ratio \(\Delta/u\)
still sets the smallest nonzero deformation.

## Quotient and classification

The admitted state domain is the stationary-vacuum family of the even quartic
potential, not the full fitted flavor ensemble. The faithful readout used here
is the physical CP-geometry magnitude \(q=t^2\); the sign pair is identified
only for this CP-even readout and must not be confused with full weak-basis
equivalence.

The pitchfork operation is source-derived conditional on the displayed
potential grammar. It selects the symmetric phase or broken phase and
rigidifies the vacuum to a sign pair. It does not select the numerical
nonzero magnitude. Its smallest exact falsifier is the nonzero response
\(\partial q/\partial r=-1/u\).

The remaining physical gate is a flavor action deriving \(r\), \(u\), and any
discrete step \(\Delta\) in one normalized source frame, together with a
threshold instrument that calibrates the induced physical16 displacement.

Run `uv run --with sympy python
research/flavor/checkers/wp356_critical_bifurcation_authority.py` to regenerate
the exact result.
