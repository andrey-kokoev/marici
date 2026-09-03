# Loewner certificate for the torsor route width

## Question

Can the generalized-eigenvalue route-width target be certified directly by a source form inequality?

## Equivalent inequality

Let \(H\ge0\) be the source admissibility form on the torsor subspace and let \(R\) be the omitted physical route. The bound

\[
R^*R\le\gamma^2H
\]

is equivalent to

\[
\|Rw\|^2\le\gamma^2 w^*Hw
\]

for every torsor displacement \(w\). Hence on the admissible ellipsoid \(w^*Hw\le1\),

\[
\omega_R\le\gamma.
\]

The smallest admissible \(\gamma^2\) is the largest generalized eigenvalue of \((R^*R,H)\). Thus a Loewner inequality is an exact certificate, not merely a sufficient relaxation.

## Semidefinite support

The inequality automatically enforces the nullspace gate. If \(Hw=0\), positivity gives

\[
0\le\|Rw\|^2\le0,
\]

so \(Rw=0\). No separate pseudoinverse convention is needed before restricting to the support.

## Mixed-direction hostile

Take \(H=I\) and scalar route

\[
R=\begin{pmatrix}3/5&4/5\end{pmatrix}.
\]

Each coordinate image has squared norm below one, but

\[
RR^*=1.
\]

The mixed direction is terminal. Separate torsor-column bounds therefore do not imply a strict route width. The complete inequality \(R^*R\le\gamma^2H\) detects the unit generalized eigenvalue.

For

\[
R=\begin{pmatrix}1/2&1/2\end{pmatrix},
\]

the sharp value is \(\gamma^2=1/2\), and the Loewner slack is positive semidefinite of rank one.

## Source proof formats

The owner may prove the inequality by exact factorization of

\[
\gamma^2H-R^*R,
\]

an exact LDL decomposition on the reduced support, a sum-of-squares identity, or a source monotonicity theorem. Numerical eigenvalues without a certified residual do not establish the inequality.

For prime-uniform confinement, the same \(\gamma\) must work for all primes and combine with the base route bound through

\[
q_0+\gamma<1.
\]

## Verification

`research/aspect/checkers/check_loewner_route_width.py` verifies strict and terminal Loewner slacks and the failure of separate column tests using exact rationals.

## Disposition

The generalized-eigenvalue handoff is reduced to one matrix/form inequality on the rank-seven torsor. Without source-derived \(H_p\) and \(R_p\), the inequality remains undefined; once they exist, no coordinate radius or vertex enumeration is needed.
