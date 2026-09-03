# The recovery kernel is the canonical no-dark quotient but not the physical Schur auxiliary by default

## Question

Given a faithful incidence-recovery pair \(I:E\to H\), \(R:H\to E\) with \(RI=I_E\), can one construct a completed quotient without waiting for an independently declared auxiliary subspace?

## Canonical splitting

The operator

\[
P=IR:H\longrightarrow H
\]

is a bounded projection because

\[
P^2=IRIR=IR=P.
\]

Its range is \(I(E)\), and

\[
H=I(E)\oplus\ker R.
\]

Indeed, every \(h\in H\) has the unique decomposition

\[
h=I(Rh)+\bigl(h-I(Rh)\bigr),
\]

with the second term in \(\ker R\).

## Canonical quotient

Let \(q_R:H\to H/\ker R\). Since \(R\) annihilates \(\ker R\), it descends to

\[
\overline R:H/\ker R\longrightarrow E.
\]

The maps \(q_RI\) and \(\overline R\) are mutual inverses. Thus the recovery kernel supplies a canonical completed quotient on which every retained source coordinate, including the two-endpoint plane, is faithful.

The quotient norm obeys

\[
\lVert q_R I x\rVert\le \lVert I\rVert\lVert x\rVert,
\qquad
\lVert q_R I x\rVert\ge \frac{1}{\lVert R\rVert}\lVert x\rVert.
\]

Hence prime-uniform bounds on \(I_p\) and \(R_p\) give a uniform no-dark angle on this recovery quotient.

## Why this does not close the Schur theorem

The physical Schur short eliminates a source-derived auxiliary history subspace \(N_{\rm phys}\). Nothing in \(RI=I_E\) proves

\[
N_{\rm phys}=\ker R
\]

or even \(N_{\rm phys}\subseteq\ker R\). Replacing \(N_{\rm phys}\) by \(\ker R\) changes the eliminated directions and can change the effective Green form and determinant.

The exact comparison gate is therefore

\[
N_{\rm phys}\subseteq\ker R.
\]

This inclusion is sufficient for recovery to descend through \(H/N_{\rm phys}\). Equality is stronger than necessary. If the inclusion fails, one physical auxiliary vector carries a nonzero recovered source coordinate, and this recovery route is rejected.

## Hostile finite model

Let \(H=\mathbb C^2\), \(E=\mathbb C\), \(I(x)=(x,0)\), and \(R(a,b)=a\). Then \(\ker R=\operatorname{span}\{(0,1)\}\). Choosing the physical auxiliary line \(N_{\rm phys}=\operatorname{span}\{(1,1)\}\) preserves the abstract incidence-recovery identity but violates \(N_{\rm phys}\subseteq\ker R\); quotienting by the physical line identifies the retained endpoint with an auxiliary direction.

## Disposition

The available incidence-recovery pair canonically constructs a faithful recovery quotient. Promotion to the physical Schur quotient requires only the typed inclusion \(N_{\rm phys}\subseteq\ker R\), not a full Gram-table evaluation. This is the narrowest next source test; choosing \(\ker R\) as the auxiliary space without that comparison is unauthorized.
