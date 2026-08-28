# Operator Irreducibility Does Not Select the Spectrum

## Question

Does a basis-invariant irreducibility condition remove WP832's
presentation-connected vectorlike completion and make the current spectrum
unavoidable?

## Exact operator packets

Take the base charge and mixing operators

\[
Q_3=\operatorname{diag}(1,2,3),
\qquad
D_3=
\begin{pmatrix}
0&1&0\\
1&1&1\\
0&1&2
\end{pmatrix}.
\]

Their common commutant consists only of scalar multiples of the identity.
Now add the anomaly-neutral pair \((1,-1)):

\[
Q_5=\operatorname{diag}(1,2,3,1,-1),
\]

and choose

\[
D_5=
\begin{pmatrix}
0&1&0&0&1\\
1&1&1&0&0\\
0&1&2&1&0\\
0&0&1&3&1\\
1&0&0&1&4
\end{pmatrix}.
\]

The added states mix with the base sector, \(D_5\) is nondegenerate with
determinant \(-18\), and the common commutant of \(Q_5,D_5\) again consists
only of scalars. This is an exact basis-invariant irreducibility test, stronger
than WP832's connected-support condition.

## Preserved and changed data

Both packets have linear charge sum 6, cubic anomaly 36, positive primitive
contrast one, and scalar common commutant. Their current indices differ:

\[
\operatorname{Tr}Q_3^2=14,
\qquad
\operatorname{Tr}Q_5^2=16.
\]

Thus irreducibility does not select the Hilbert-space dimension or exclude an
anomaly-neutral completion. Scaling \(D_5\mapsto mD_5\) preserves the scalar
commutant for every \(m>0\), while

\[
\det(mD_5)=-18m^5.
\]

It therefore does not select the spectral scale either.

The WP831 current-response fiber remains:

\[
14\cdot1^2
=16\left(\sqrt{\frac78}\right)^2.
\]

## Consequence

Operator irreducibility is a property internal to one completed packet. It can
reject reducing subspaces inside that packet, but it does not compare and
select among inequivalent irreducible packets. A new physical axiom must order
or otherwise distinguish complete irreducible spectra before irreducibility
can contribute to portal selection.

## Claim boundary

The displayed pair is an exact finite operator model. It does not establish a
full spectral triple or quantum field theory: gauge covariance, real
structure, grading, first-order condition, positivity, and a physical action
remain untested. The result is precisely that scalar-common-commutant
irreducibility alone cannot select the spectrum.

## Smallest exact falsifier

The irreducible three-state and five-state packets share anomaly 36 and portal
contrast one while having current indices 14 and 16. Both retain a continuous
spectral scale. Hence basis-invariant irreducibility does not close the WP831
threshold fiber.

## Disposition

Negative irreducibility result. The remaining source principle must uniquely
select among distinct irreducible physical completions, not merely demand that
the chosen completion have no internal reducing sector.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp833_operator_irreducible_vectorlike_completion_no_go.py
```
