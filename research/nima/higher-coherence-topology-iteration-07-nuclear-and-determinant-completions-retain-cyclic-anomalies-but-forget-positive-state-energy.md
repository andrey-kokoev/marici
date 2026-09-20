# Higher-coherence topology iteration 07: nuclear and determinant completions retain cyclic anomalies but forget positive state energy

## Candidate topology

Place finite coherence operators in Schatten ideals and complete the scalar
character through an order-three regularized determinant:

\[
L(z)\in\mathcal S_3,
\qquad
\det_3(I-L(z)).
\]

Primitive and square traces become explicit anomaly counterterms, while the
higher bulk is controlled in the native trace ideal. This topology is designed
to totalize infinitely many prime increments through cyclic traces rather than
state norms.

## What it absorbs

For the composition law `a star b=a+b+ab`, the removed low-order term

\[
r(x)=-x+\frac{x^2}{2}
\]

produces an exact two-cocycle

\[
\alpha(a,b)=r(a\star b)-r(a)-r(b).
\]

Its higher associativity coherence telescopes automatically. Thus
nuclear/determinant topology genuinely absorbs an infinite family of
primitive/square composition residuals into one normal-form object.

This is a successful example of the repeated-cone idea.

## State-level obstruction

Scalar determinant convergence does not give trace-norm convergence of the
corresponding Fock state. For one prime eigenvalue

\[
\lambda=p^{-s},
\qquad r=|\lambda|,
\]

the normalized factor has

\[
\log N_3(\lambda)
=r(1-\cos\arg\lambda)+O(r^2).
\]

Away from the real axis this positive absolute mass is not cancelled by the
holomorphic primitive/square counterterm. Therefore the determinant line may
converge while the positive state norm diverges.

## Haar residual in trace ideals

The local Haar mismatch is a positive rank-one scalar multiple

\[
R_p(z)
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)
|b_z\rangle\langle b_z|
\]

up to its orientation convention. Whenever the scalar coefficient is
nonnegative,

\[
\|R_p(z)\|_1
=
\bigl|1-p^{-2\operatorname{Re}z}\bigr|E_p(b_z).
\]

Thus trace-norm completion does not hide it. Quotienting by commutators can
kill cyclically invisible skew terms, but a nonzero positive rank-one operator
has nonzero trace and cannot be a trace-class commutator with vanishing trace.

## Divisor blindness

Regularized determinant coherence depends on the bulk and its anomaly packet,
not on an independently chosen endpoint section. Multiplying the endpoint by
a reflection-symmetric factor such as `1-z^2` changes its zeros while leaving
the determinant anomaly unchanged. Therefore determinant topology alone cannot
orient the Xi divisor.

The missing natural map from the determinant line to the Evans boundary line
cannot be defined by dividing their scalar sections; that would simply assume
divisor agreement.

## Verdict for topology 7

Nuclear/trace-ideal topology is effective for:

- summing cyclic prime data;
- generating higher anomaly coherences automatically;
- defining determinant lines without a trace-class Fock state.

It fails as a confinement topology because it separates scalar cyclic
coherence from positive state energy. The Haar residual either remains
trace-norm visible or is forgotten together with the positive state needed for
noncollapse.

The next nonredundant topology to test is a local-convex holomorphic topology
of compact convergence/Montel type, where all spectral jets are retained and
higher fillers might converge normally as analytic sections.