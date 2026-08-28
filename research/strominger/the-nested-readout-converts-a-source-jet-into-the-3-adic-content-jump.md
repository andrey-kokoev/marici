# The nested readout converts a source jet into the three-adic content jump

## Question

Where does the modulus-three content law first enter the composable chain?

## Three typed stages

The relevant objects are:

\[
U_n=C^n,
\qquad
A_n=\text{nested magnetic response}(U_n),
\qquad
d_1(A_n-I).
\]

The two generating arrows are the nested commutator constructor and the
determinantal-content readout.

## Source congruence jet

The neutral commutator response satisfies

\[
C=I+3J\pmod 9,
\qquad
J\not\equiv0\pmod3.
\]

Therefore

\[
C^n=I+3nJ\pmod9.
\]

The source already carries three distinct first-jet classes indexed by
\(n\bmod3\). No Smith operation is needed to create that distinction.

## Nested-readout conversion law

Define the normalized response jet

\[
B_n=\frac{A_n-I}{3}\pmod3.
\]

The exact bounded calculation on the three residue classes gives an affine
law

\[
B_n=B_0+nK\pmod3.
\]

It has a unique zero:

\[
B_n=0
\quad\Longleftrightarrow\quad
n\equiv2\pmod3.
\]

Thus the nested commutator readout does not create the three source classes.
It selects one of them by sending it to the zero response jet.

## Content exposes the selected class

The first determinantal divisor obeys

\[
v_3(d_1(A_n-I))\ge2
\quad\Longleftrightarrow\quad
B_n=0.
\]

Consequently the content rule

\[
d_1=
\begin{cases}
2304,&n\equiv2\pmod3,\\
768,&n\not\equiv2\pmod3
\end{cases}
\]

is not created by the gcd. The gcd exposes the extra divisibility already
present when the affine nested-response jet vanishes.

## Location of the mechanism

The composable explanation is:

\[
\text{source first jet}
\longrightarrow
\text{affine nested-readout selection}
\longrightarrow
\text{content valuation}.
\]

- The source arrow supplies the three congruence classes.
- The nested constructor selects class two as a zero.
- The content readout reports that zero as an additional factor of 3.

The rank defect is present in all three classes, so it is logically independent
of this selection.

## Final Smith cancellation

For the two ordinary classes,

\[
(v_3(d_1),v_3(d_2),v_3(d_3))=(1,2,3).
\]

For the selected class,

\[
(v_3(d_1),v_3(d_2),v_3(d_3))=(2,5,7).
\]

The nested readout therefore amplifies the selected first jet across every
determinantal layer. Nevertheless the snake-index ratio satisfies

\[
v_3\left(\frac{d_3}{d_2d_1}\right)=0
\]

in all three classes.

The final quotient does not preserve the three-adic distinction. The content
port sees it; the snake-index valuation does not. This is an exact
detector-relative loss of residual information.

## Relation to spectral gluing

The spectral-plane quotient is 2-primary. It plays no role in this
three-adic conversion. The prime 3 enters through the first congruence subgroup
of the source response and is exposed by the nonlinear nested constructor.

## Theorem status

The source jet law follows for all integral \(n\) from the binomial identity
modulo 9. The affine response law and unique zero are exhaustively checked on
the three residue classes, which is sufficient for this first-jet quotient.

Seven of seven gates pass.

## Claim boundary

This identifies the origin of the first content jump. It does not claim that
the first jet determines higher Smith invariants or snake square classes; prior
hostile tests already falsified that stronger claim.
