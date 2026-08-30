# The naive noncommutative tail adjugate leaves the forcing derivative

## Question

The augmented tail equation supplies the source-derived triangular operator

\[
D_z=
\begin{pmatrix}
P+z&M_f\\
0&P
\end{pmatrix},
\qquad P=\partial_q,
\]

where \(M_f\) is multiplication by the labelled theta forcing.  Can its
ordinary triangular adjugate already provide the reverse arrow required by the
Cartan contraction programme?

## Exact calculation

The direct analogue of the commutative adjugate is

\[
Q_z=
\begin{pmatrix}
P&-M_f\\
0&P+z
\end{pmatrix}.
\]

On a common polynomial core, the commutator is

\[
[P,M_f]=M_{f'}.
\]

Consequently the two ordered composites are

\[
Q_zD_z=
\begin{pmatrix}
P^2+zP&M_{f'}\\
0&P^2+zP
\end{pmatrix},
\]

and

\[
D_zQ_z=
\begin{pmatrix}
P^2+zP&-M_{f'}\\
0&P^2+zP
\end{pmatrix}.
\]

Thus the adjugate does not give a Cartan identity.  It leaves two independently
typed defects:

1. the diagonal is the second-order operator \(P^2+zP\), not multiplication by
   the normal displacement \(a=\operatorname{Re}(z)\);
2. the off-diagonal defect is exactly the derivative current \(M_{f'}\), with
   opposite signs in the two composition orders.

The opposite signs do not authorize cancellation.  The composites act on the
two different objects of the incidence arrow.  Adding them first requires a
source-derived comparison or trace that identifies those objects and preserves
their boundary domains.

## DPC verdict

The calculation supplies a finite source-local falsifier for the naive reverse
arrow.  Any viable reverse construction must enlarge the system so that
\(M_{f'}\) becomes an explicitly typed boundary or reservoir incidence, and it
must separately reduce the diagonal second-order flow to the signed normal
Cartan factor.  Merely observing cancellation after an untyped scalar
projection is insufficient.

This points to a concrete next gate: determine whether the theta source grammar
closes the derivative forcing into the already distinguished primitive,
prime-square, seam, and archimedean currents on a common boundary-bearing
domain.  A residual component outside that source closure disproves this route.

## Verification

`check_rh_noncommutative_tail_adjugate.py` verifies both ordered identities
exactly over rational polynomial test vectors and records the residual signs.

