# The complementary observer owns the essential margin while the compact channel repairs only finite defects

## Question

Can the division of labor between a compact analytic channel and its complement be stated invariantly, without choosing a finite-dimensional defect subspace in advance?

## Claim boundary

Yes in Hilbert-space operator theory. Modulo compact operators, the joint Gramian equals the complementary Gramian. Therefore the complement alone owns the essential lower margin. The compact analytic channel can only remove finite-dimensional kernel defects left by an upper semi-Fredholm complement. This is an operator-theoretic theorem; it does not identify a physical complement.

## Problem

Let

\[
A:X\to Y,
\qquad
D:X\to Z
\]

be bounded, with \(A\) compact, and define

\[
T=\binom AD.
\]

The joint Gramian is

\[
T^*T=A^*A+D^*D.
\]

We seek an invariant statement of which channel controls completed-source stability.

## Bold conjecture

A compact positive correction \(A^*A\) can create an essential lower margin absent from \(D^*D\).

## Named rivals

1. Compact corrections vanish in the Calkin algebra and cannot alter the essential margin.
2. They may remove a finite-dimensional zero eigenspace and thereby make the full Gramian invertible.
3. Compact corrections can repair an infinite sequence of eigenvalues converging to zero.
4. The decomposition depends on a chosen basis and has no invariant meaning.

## Calkin formulation

Let

\[
\mathcal Q(X)=\mathcal B(X)/\mathcal K(X)
\]

be the Calkin algebra, with quotient map \(q\). Since \(A\) is compact,

\[
A^*A\in\mathcal K(X).
\]

Therefore

\[
q(T^*T)
=q(A^*A+D^*D)
=q(D^*D).
\]

This equality is basis-independent.

## Essential-margin theorem

The following are equivalent:

1. \(D\) is bounded below on a finite-codimensional closed subspace;
2. \(D\) has closed range and finite-dimensional kernel;
3. \(D\) is upper semi-Fredholm;
4. \(q(D^*D)\) is positive and invertible in \(\mathcal Q(X)\);
5. there are \(\gamma>0\) and compact self-adjoint \(K\) such that

   \[
   D^*D+K\ge\gamma^2I.
   \]

Thus a stable joint observer can exist only if the complementary channel already has a positive essential lower margin.

## Finite-defect repair theorem

Assume \(D\) is upper semi-Fredholm. Then

\[
T=\binom AD
\]

is bounded below exactly when

\[
\ker A\cap\ker D=0.
\]

### Proof

Because \(D\) is bounded below on \((\ker D)^\perp\), \(D^*D\) has a positive spectral gap away from its finite-dimensional kernel. The compact positive operator \(A^*A\) cannot close that essential gap. The sum

\[
A^*A+D^*D
\]

is strictly positive exactly when it is strictly positive on \(\ker D\). On that finite-dimensional space,

\[
\langle A^*Ak,k\rangle=\|Ak\|^2,
\]

so strict positivity is equivalent to injectivity of \(A|_{\ker D}\), namely

\[
\ker A\cap\ker D=0.
\]

Strict positivity of \(T^*T\) is equivalent to \(T\) being bounded below.

## What compact repair can and cannot do

The compact analytic channel may:

- detect the finite-dimensional kernel of \(D\);
- change discrete eigenvalues of the Gramian;
- remove isolated zero modes of finite multiplicity;
- improve finite-cutoff conditioning.

It cannot:

- make \(q(D^*D)\) invertible when it was not;
- remove zero from the essential spectrum;
- repair an orthonormal sequence with \(Dx_n\to0\);
- supply a uniform margin on infinitely many asymptotically invisible directions.

Rival 3 therefore fails.

## Approximate-sequence form

If \(D\) lacks an essential lower margin, there exists an orthonormal sequence \((x_n)\) with

\[
Dx_n\to0.
\]

Compactness gives

\[
Ax_n\to0.
\]

Hence

\[
Tx_n\to0.
\]

This is the operational witness of the Calkin obstruction.

## Symmetry descent

Suppose a group acts unitarily on \(X\), and both Gramians are equivariant. Then their Calkin classes lie in the corresponding equivariant commutant. A compact analytic channel may alter finite-dimensional isotypic defects but cannot change the essential representation sectors on which \(D\) must be coercive.

For a genuine quotient descent with kernel-variation subspace \(X_K\), any infinite-dimensional part of \(X_K\) must be controlled essentially by \(D\). It cannot be delegated to compact analytic repair.

## Green/Real worked example

For the Euler-to-radial analytic channel \(A_{\rm rad}\), the canonical fold and Real comparison preserve compactness:

\[
C_uF^2=W_uC_u,
\qquad
U^\top=U^*.
\]

These identities constrain the representative \(A_{\rm rad}\), but in the Calkin algebra

\[
q(A_{\rm rad}^*A_{\rm rad})=0.
\]

Therefore any stable arithmetic/analytic joint observer must obtain its essential margin from the complementary arithmetic Gramian. The radial channel may repair only finite-dimensional arithmetic defects.

## Constructor-role law

A `compact_analytic_observer` contributes only a compact Gramian class. A `complementary_observer` must declare an invertible positive Calkin Gramian class. A `finite_defect_repair` must declare injectivity on the finite kernel left by the complement.

These roles form the factorization:

\[
\text{essential margin from }D
\quad+\quad
\text{finite-defect repair from }A
\quad\Longrightarrow\quad
\text{stable joint observation}.
\]

No coefficient substitution can exchange the two roles unless it changes the Calkin class and separately repairs the finite kernel.

## Strongest falsification attempt

A finite-rank positive operator can make a noninvertible Gramian invertible when the only obstruction is a finite-dimensional kernel. This confirms rival 2 and prevents the overstatement that compact corrections never create invertibility. The exact invariant is essential invertibility: compact repair may remove discrete zero modes but not essential zero.

## Disposition

The bold conjecture is rejected. The complementary observer owns the essential margin, while the compact analytic channel repairs at most finite-dimensional defects. This gives the programme an invariant operational decomposition and a sharper constructor-role boundary than compactness alone.
