# Double-slit complementarity from a source QND instrument

## Source reuse

The double-slit attack does not need an invented measurement operation.  The
source-motivated controlled-pointer interaction already admitted in
`same-effect-different-physical-capability.md` supplies it.

Use the path alternatives as the control and prepare the pointer in \(|0\rangle\):

\[
|L\rangle|0\rangle\mapsto|L\rangle e_L,
\qquad
|R\rangle|0\rangle\mapsto|R\rangle e_R,
\]

with

\[
e_L=\binom10,
\qquad
e_R=\binom cs,
\qquad
c^2+s^2=1.
\]

At the existing exact source point,

\[
c=\frac35,
\qquad
s=\frac45.
\]

## Two possibility structures from one coupling

If the pointer outcome is forgotten, the path coherence is multiplied by

\[
\langle e_L,e_R\rangle=c.
\]

The screen therefore has visibility

\[
V=|c|=\frac35.
\]

If the pointer is used to distinguish the paths, the optimal positive binary
separator is the difference of its two record projectors.  Its eigenvalues are
\(\pm s\), so

\[
D=|s|=\frac45.
\]

The source unitary itself forces

\[
\boxed{V^2+D^2=c^2+s^2=1.}
\]

Thus the “measure” and “do not measure” pictures are not separate dynamical
laws.  They are two authorized readouts of one path--pointer interaction:

\[
\text{forget pointer}\longrightarrow\text{interference},
\qquad
\text{separate pointer records}\longrightarrow\text{which path}.
\]

## Eraser square

The pointer basis obtained from the normalized sum and difference

\[
e_+\propto e_L+e_R,
\qquad
e_-\propto e_L-e_R
\]

produces two conditioned path ensembles with full visibility and opposite
phase.  Their normalized coherences are \(+1/2\) and \(-1/2\).  Forgetting the
eraser outcome recombines them to the original unconditioned coherence
\(c/2\).

This gives the typed quantum-eraser explanation:

- conditioning changes the accessible readout fiber;
- it does not rewrite the earlier path history;
- the unconditioned record remains unchanged;
- complementary fringes cancel or partially cancel when their label is
  forgotten.

## Result and boundary

The bounded source model derives the complete visibility--distinguishability
and eraser packet from one interaction.  It therefore improves Entry 2026:
the optimal separator is no longer merely declared abstractly.

It remains a one-mode/two-level controlled-pointer specialization.  The
shared Carrier has not yet been shown to generate this QND interaction, and
the continuum double-slit propagation and Born frequency law remain outside
the theorem.

## Verification

```text
uv run --with sympy python research/nima/checkers/check_double_slit_qnd_source_instrument.py
```

