# A2 braid coherence does not select the positive chamber

Author: `marici.Nima`

Date: 2026-08-26

Status: exact finite no-go for extracting RH orientation from the braid alone

## Coherence and orientation are different structures

The positive-root constructors derived from Fourier conjugation and the
jet--wall commutator satisfy the type-(A_2) braid identity. That identity is
valid over arbitrary nonzero real or complex parameters wherever its chart
denominator is defined.

Consequently the braid supplies coherence of presentations, not selection of
a positive chamber.

## Chamber coordinates

For the reduced word (121), the endpoint transporter is

\[
X_1(a)X_2(b)X_1(c)
=
\begin{pmatrix}
1&a+c&ab\\
0&1&b\\
0&0&1
\end{pmatrix}.
\]

The factorization parameters (a,b,c) are the natural chamber coordinates.
The totally positive real cell requires all three to be positive. In the
alternative (212) chart, its parameters are

\[
\frac{bc}{a+c},
\qquad
a+c,
\qquad
\frac{ab}{a+c}.
\]

When (a,b,c>0), the transition preserves positivity. This is the positive
atlas familiar from type (A_2).

But the source-generated operator words admit negative parameters. For
example, (a=-2), (b=3), and (c=5) satisfy the exact braid identity while
the first chamber coordinate is negative. The endpoint has a negative
generalized minor even though all coherence equations close.

Complex spectral parameters weaken the claim further: ordinary order
positivity is not defined without a source-selected real form and phase
parallelization.

## Why the source words do not impose positivity

The first root constructor uses an inverse jet shear. The second uses a group
commutator and therefore both an operation and its inverse. These are group
constructions, not positive-semigroup constructions.

Fourier conjugation also rotates polarization. It preserves the algebraic
root relation but does not preserve an a priori sign on the root coefficient.

Thus the source operations currently generate the whole positive-root group
coordinate line, including hostile signs. No categorical coherence law can
remove those parameters after they have been admitted.

## Exact implication for RH

The (A_2) discovery explains why the finite operator relations organize
into flags, root constructors, braid cells, and a pentagonal atlas. It does
not explain why the distinguished theta minor avoids zero.

An RH-bearing advance would require an additional source law selecting a
moving positive or sectorial chamber. Such a law must:

1. choose a real or sectorial form before scalar projection;
2. constrain the actual root coefficients, not merely their endpoint
   determinant;
3. survive Fourier transport and arithmetic completion;
4. reject the negative-parameter braid witness while retaining the genuine
   theta path.

Without that law, the categorical structure has reached the same boundary as
the earlier transport programme: exact provenance and coherence, but no
orientation.

## Finite falsifier

Any claim that braid coherence forces positivity is disproved by one
negative-parameter factorization for which both braid words agree exactly.
The checker records such a witness and verifies that a positive sample remains
positive in both charts.

