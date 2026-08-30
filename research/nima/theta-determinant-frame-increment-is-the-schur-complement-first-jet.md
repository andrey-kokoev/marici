# Determinant-frame increment is the Schur-complement first jet

## Exact cutoff law

Let the sector denominator at cutoff (X) be

\[
D_X(z)=\det A_X(z),
\qquad
A_X(z)=I+M_X(z).
\]

After adjoining a new labelled source block, write the enlarged matrix as

\[
A_Y(z)=
\begin{pmatrix}
A_X(z)&B(z)\\
C(z)&E(z)
\end{pmatrix}.
\]

Where (A_X) is invertible, define the Schur complement

\[
S_{Y/X}(z)
=
E(z)-C(z)A_X(z)^{-1}B(z).
\]

Block determinant factorization gives

\[
D_Y(z)=D_X(z)\det S_{Y/X}(z).
\]

Therefore the logarithmic first-jet increment is exactly

\[
\left.
\left(
\frac{D_Y'}{D_Y}-\frac{D_X'}{D_X}
\right)
\right|_{z=0}
=
\operatorname{Tr}
\left(
S_{Y/X}(0)^{-1}S_{Y/X}'(0)
\right).
\]

This is the natural cutoff bonding law for the residual linear determinant
frame.

## Mixed terms are unavoidable

Differentiating the Schur complement gives

\[
\begin{aligned}
S_{Y/X}'={}&E'
-C'A_X^{-1}B
+CA_X^{-1}A_X'A_X^{-1}B\\
&-CA_X^{-1}B'.
\end{aligned}
\]

The increment is therefore not generally the first jet of the newly added
diagonal block (E). It includes:

- incoming coupling variation;
- outgoing coupling variation;
- propagation through the retained block;
- variation of the retained block itself.

A scalar primitive-current term can equal the determinant-frame increment only
after these mixed terms are included or cancelled by a source-derived
coherence identity.

## Exact arithmetic target

For a prime or prime-power extension (X\subset Y), let (j_{Y/X}) denote the
typed primitive boundary-current increment. The proposed frame law is

\[
j_{Y/X}
=
\operatorname{Tr}
\left(
S_{Y/X}(0)^{-1}S_{Y/X}'(0)
\right).
\]

This equality must be proved before reciprocal sewing and before summing over
cutoffs. It is not enough for both sides to reproduce the same completed
logarithmic derivative after scalar projection.

The endpoint, seam, prime-square, and archimedean channels may enter through
the mixed Schur terms. They remain coupled and cannot be assigned independent
positivity.

## Reality reduces the residual gauge

The finite-type ambiguity has the form

\[
D_X(z)\longmapsto e^{a_Xz}D_X(z).
\]

If the sector determinant obeys Schwarz reality, preservation of that law
forces (a_X) to be real. The same condition makes the multiplier unimodular
on the imaginary seam:

\[
|e^{a_Xit}|=1.
\]

Thus the remaining determinant-frame anomaly is one real current per cutoff,
not an arbitrary complex frame.

Under the hostile refactoring, the cutoff increment changes by

\[
a_Y-a_X.
\]

The Schur-complement identity fixes this difference if and only if the
enlarged source block and its incidence maps are already typed.

## Finite falsifiers

The route fails at the first cutoff where any of the following occurs:

- (A_X(0)) is singular;
- (S_{Y/X}(0)) is singular;
- the primitive current differs from the Schur first jet;
- deleting mixed terms changes the trace;
- two source-compatible block presentations give different increments;
- the increments do not telescope under two successive label additions.

For two additions (X\subset Y\subset Z), the coherence test is

\[
j_{Z/X}=j_{Z/Y}+j_{Y/X}.
\]

The determinant identity guarantees this only when all three Schur complements
are formed from one compatible block system. Equal final scalar products do
not supply that compatibility.

## Preregistered acceptance protocol

The primewise test is admissible only with four safeguards.

### Source independence

Construct \(A_X,B,C,E\) from labelled theta/Tate operations before evaluating
or comparing the primitive current. A matrix fitted to the desired current is
not evidence for the identity.

### Frame authority

Freeze the admitted basis transformations and determinant normalization before
the jet calculation. Independently changing the input and output determinant
frames can shift the logarithmic jet and conceal the residual linear
exponential gauge. A genuine similarity transformation does not shift the
determinant jet because its two frame contributions cancel.

### Pathwise equality

For every individual extension, record the typed residual

\[
\mathcal R_{Y/X}
=
j_{Y/X}
-
\operatorname{Tr}
\left(
S_{Y/X}(0)^{-1}S_{Y/X}'(0)
\right).
\]

Require

\[
\mathcal R_{Y/X}=0
\]

at each addition. Vanishing only after summing several additions is
insufficient because equal-and-opposite local defects can telescope away.

### Presentation coherence

Repeat the calculation in at least one independently source-authorized block
presentation. The jet must transform under the declared determinant-line
comparison. Equality caused by arbitrary elimination coordinates is rejected.

## Optical independent reproduction

A finite reciprocal accretive three-mode network independently reproduces the
structural theorem:

- the complete Schur first jet equals the logarithmic determinant increment;
- the retained-state mixed derivative is nonzero;
- deleting that term gives the wrong jet;
- the two mode-addition orders have different local increments;
- both orders telescope to the same total when formed inside one compatible
  block system.

This is an exact finite coherence witness. It supplies no theta matrix,
primitive-current authority, or completion theorem.

## Decisive next computation

Construct one actual finite theta/Tate sector matrix with its retained tail,
seam, endpoint, primitive, and square channels. Add one prime-labelled block.
Compute (S_{Y/X}) and its first logarithmic jet exactly.

If it equals the source primitive-current increment and composes under a second
prime addition, the determinant line has its first authorized frame law. If it
does not, finite exponential type does not repair the determinant-sewing route.
