# Invariant transmission-zero factorization

Owner: `marici.Sontag`

## Bounded question

After reachable/observable quotienting, which source-derived conditions can
exclude an invariant zero of one distinguished scalar port?  The scope is
finite-dimensional rational discrete-time SISO input with a multi-output
passive realization.  No analytic-completion or theta realization is claimed.

Source correction: `research/nima/theta-scalar-zero-is-a-transmission-zero-not-an-observability-defect.md`.
The impedance/scattering distinction is corrected by
`research/nima/theta-positive-real-impedance-can-have-an-off-seam-dark-scattering-zero.md`.
The analytic-type obstruction is supplied by
`research/nima/theta-even-entire-completion-cannot-be-a-positive-real-impedance.md`.

## Typed compiler

For

\[
x^+=Ax+Bu,\qquad y=Cx+Du,
\]

first replace the presented state by its reachable/observable quotient and
retain the quotient map.  For a selected output row \((C_s,D_s)\), compile

\[
P_s(\lambda)=
\begin{pmatrix}\lambda I-A&-B\\ C_s&D_s\end{pmatrix}.
\]

A selected-port invariant zero is a value where this matrix loses rank.  The
full output family and each selected row are different typed ports; neither
may silently replace the other.

## Smallest passive multiport hostile

Take one state, one input, and two output ports:

\[
A=\frac35,\quad B=-\frac{12}{25},\quad
C=\begin{pmatrix}\frac45\\0\end{pmatrix},\quad
D=\begin{pmatrix}\frac9{25}\\\frac45\end{pmatrix}.
\]

The full colligation has columns

\[
V=\begin{pmatrix}A&B\\C&D\end{pmatrix}
=\begin{pmatrix}
3/5&-12/25\\4/5&9/25\\0&4/5
\end{pmatrix},
\qquad V^T V=I_2.
\]

Thus it obeys the exact storage law

\[
|x^+|^2+\|y\|^2=|x|^2+|u|^2.
\]

It is controllable because \(B\ne0\) and observable from the complete output
because \(C\ne0\).  Nevertheless its selected first-port Rosenbrock matrix is

\[
P_1(\lambda)=
\begin{pmatrix}\lambda-3/5&12/25\\4/5&9/25\end{pmatrix},
\]

whose determinant is \((9/25)\lambda-3/5\).  It loses rank at
\(\lambda=5/3\), outside the Schur stability disk.  A witness is
\((x,u)=(-9/20,1)\).  The selected port is dark, while the complementary port
equals \(4/5\), so full-output energy remains visible.  Passivity,
losslessness, controllability, and observability therefore do not imply that
the selected transfer is minimum phase.

## Gate classification

- **Bare collocation is insufficient.**  Algebraic equality \(C_s=B^T\)
  alone does not impose a zero-free domain.  The scalar realization
  \(A=0,B=C_s=1,D_s=1/2\) is controllable, observable, and collocated, but its
  Rosenbrock determinant is \(\lambda/2+1\), with zero \(-2\).  It is not
  passive; this isolates why collocation needs an independently established
  dissipativity strictness condition.
- **Strict positive-realness is sufficient only for the same distinguished
  scalar to which positivity applies.**  If a source theorem establishes
  \(\operatorname{Re}G_s(\lambda)>0\) throughout the declared region, then
  that \(G_s\) is nonzero there.  Positivity cannot be transported through an
  untyped port conversion.  In particular, the strictly positive-real
  impedance \(Z_a(s)=s/a\) produces the scattering coefficient
  \(h_a(s)=(Z_a-1)/(Z_a+1)=(s-a)/(s+a)\), which vanishes at \(s=a\).
- **Scalar outerness is sufficient in its declared Hardy domain.**  A
  source-derived outer factor has no nonconstant inner zero factor there.
  Merely dividing out observed zeros or assuming an outer inverse is circular.
- **Minimum phase is sufficient by definition relative to the declared
  stability domain.**  It is a classification, not an explanation; the
  certificate must precede inspection of the completed scalar divisor.

Before these tests, an **analytic-type gate** separates a sector-local
impedance or Weyl response, its Cayley-transformed scattering or overlap
readout, and an even entire completed section.  A nonconstant even entire
function cannot be positive-real on one open half-plane: evenness reflects
positivity across the seam, and its negative exponential would be bounded
entire, forcing constancy.  A completed xi-type section therefore cannot
itself be the positive-real impedance.  Positivity must live before
completion, with a separate source-derived zero-preserving comparison to the
completed readout.

Collocation plus a source-derived strict positive-real lemma can exclude zeros
of the collocated impedance quantity itself.  It cannot exclude zeros of a
different scattering or overlap readout without a separate theorem for that
actual port.  Collocation by itself cannot.

## Constructor verdict

The exact constructor tree is

`source realization -> reachable/observable quotient -> selected source port -> Rosenbrock matrix -> rank test`.

Full-output storage is a parallel conservation cell, not a zero-exclusion
cell.  The verdict is an exact finite-dimensional factorization of the zero
test and an obstruction to promoting passivity, losslessness, observability,
or bare collocation into minimum phase.

## Frozen optionality disposition

Post-activation: excitement 9/10, confidence 10/10, realized information gain
8/10.  The rational one-state isometry made the distinction unusually sharp;
the hand-selected finite witness is the main confound.

Raw delta: passivity/losslessness and bare-collocation sufficiency branches
were eliminated.  Strict positive-realness survives only for the identical
distinguished scalar on its certified domain; it does not cross the Cayley
impedance-to-scattering adapter.  Source-derived scalar outerness and minimum
phase remain sufficient only in their explicitly declared domains.  The
quotient-first compiler, Rosenbrock witness, storage coherence cell, and bright
complementary port were constructed.  The checker declares and passes 13 exact
tests.  Analytic completion, MIMO outerness, and a source-derived theta
strictness theorem remain unresolved.
