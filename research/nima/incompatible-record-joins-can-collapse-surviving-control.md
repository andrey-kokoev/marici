# Incompatible record joins can collapse surviving control

## Result

Formal-concept composition is not merely additive. Combining two independently
admitted record algebras generates a new algebra, and closure of that join may
sharply reduce the compatible control algebra.

For record algebras \(R_1\) and \(R_2\), the closed combined record is

\[
R_{12}=(R_1\vee R_2)'',
\]

and its surviving control algebra is

\[
M_{12}=R_{12}'=R_1'\cap R_2'.
\]

Thus record join is dual to control meet.

## Exact incompatible-frame witness

Inside \(M_2(\mathbb R)\), let

\[
R_X=\operatorname{span}(I,X),
\qquad
R_Z=\operatorname{span}(I,Z).
\]

Each is a two-dimensional maximal commutative record algebra and is its own
commutant. But together they generate \(I,X,Z,XZ\), a basis of the full matrix
algebra. Therefore

\[
(R_X\vee R_Z)''=M_2(\mathbb R),
\qquad
R_X'\cap R_Z'=\mathbb R I.
\]

Each record frame alone preserves two-dimensional control. Recording both
incompatible frames leaves only scalar control.

## Interpretation

More records do not simply add information to a passive store. They alter the
closed interface object and may remove future capabilities. This makes precise
one form of incoherence reduction with operational cost:

- the record algebra becomes richer;
- the compatible control algebra becomes poorer;
- closure exposes the tradeoff rather than hiding it.

The effect is structural even before noise or repetition. Kitaev's pointer
calculus supplies the dynamical version: repeated noncentral records contract
complementary control by powers of the pointer overlap.

## Authority boundary

The generated algebra and its commutant determine compatibility, not authority.
Both input record constructors and the composite closure require source-rooted
support. A cross-axis cell cannot substitute for a final constructor
certificate.

## Falsifier

Any compiler claiming that the joint \(X\)- and \(Z\)-record object retains a
non-scalar sharp control is refuted by a nonzero commutator with one of the two
record generators.

