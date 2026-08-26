# Source-mass reference descent (WP257)

## Question

Does WP256's improved coordinate

\[
x=\frac{m_{\mathrm{vis}}}{M_{\mathrm{source}}}
\]

define an operation on the faithful `physical16` quotient, or does it require
an added source-label reference port?

## Typing

`physical16` records the weak-basis flavor orbit. A generator or mediator mass
label is not one of its coordinates. The visible mass is a detector readout;
the denominator is separately supplied source metadata. Their quotient is
therefore undefined on `physical16` alone.

The smallest hostile pair holds both the physical flavor point and detector
record fixed at \(m_{\mathrm{vis}}=65\) GeV, while changing only the external
mass label:

\[
\frac{65}{130}=\frac12,
\qquad
\frac{65}{160}=\frac{13}{32}.
\]

Thus the candidate readout is not constant on the fibers that forget the
source-mass port and does not descend to `physical16`.

## Changed groupoid

After adjoining a mass-reference port, simultaneous rescaling of the visible
record and reference leaves the ratio invariant:

\[
\frac{65}{130}=\frac{130}{260}=\frac12.
\]

The admissible symmetry is consequently the stabilizer of the declared
relative experiment. This does not recover an absolute mass property of the
original flavor experiment; it defines a new source-labelled relational
readout.

## Classification

WP256's reduced residual remains useful evidence about detector-template
geometry, but it grants no selector authority on `physical16`. The operation
is neither selector nor texture rigidifier there. On the enlarged experiment
it is a relational readout whose physical authority still requires a named
source-derived reference preparation and common detector calibration.

Run `uv run --with sympy python
research/flavor/checkers/wp257_source_mass_reference_descent.py` for the exact
hostile pair and relational stabilizer test.
