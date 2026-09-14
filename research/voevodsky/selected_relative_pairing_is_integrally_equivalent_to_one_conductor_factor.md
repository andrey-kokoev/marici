# The selected relative pairing is integrally equivalent to one conductor factor

## Question

Can the unique connection-stable active relative pairing be carried to an elementary conductor matrix by explicit integral basis changes, rather than only by equality of Smith invariants?

## Claim boundary

This constructs an integral lattice isomorphism. It does not identify the basis changes with source-labelled cycles or forms, and it does not provide the required parameter map between connections.

## Matrices

Let

\[
C_{\rm act}=
\begin{pmatrix}
-1&1&0\\
1&0&1\\
0&1&-1
\end{pmatrix}
\]

be the selected relative pairing and

\[
J_1=
\begin{pmatrix}
2&0&1\\
0&1&0\\
0&0&1
\end{pmatrix}
\]

be the first elementary conductor factor.

Define

\[
U=
\begin{pmatrix}
0&0&-1\\
0&-1&0\\
-1&-1&0
\end{pmatrix},
\qquad
V=
\begin{pmatrix}
-1&-1&0\\
-1&0&-1\\
1&0&0
\end{pmatrix}.
\]

Both are unimodular:

\[
\det U=\det V=1.
\]

Direct multiplication gives

\[
U C_{\rm act} V=J_1.
\]

Thus the selected relative pairing and the elementary conductor factor are isomorphic as integral pairings.

## Parity-character transport

The unique mod-two left cokernel character of \(C_{\rm act}\) is

\[
\ell_{\rm rel}=(1,1,1).
\]

The corresponding character of \(J_1\) is

\[
\ell_1=(1,0,1).
\]

The row-basis transformation carries them exactly:

\[
\ell_1U=\ell_{\rm rel}\pmod2,
\qquad
\ell_{\rm rel}U^{-1}=\ell_1\pmod2.
\]

Therefore the relative active-boundary-plus-endpoints parity becomes the conductor wall-one parity under this integral equivalence.

## Site exchange

The second conductor factor \(J_2\) is obtained from \(J_1\) by exchanging the two conductor sites. Consequently the same abstract relative pairing is integrally equivalent to \(J_2\) after composing with that permutation. A geometric realization still has to show that this permutation is induced by the source wall exchange.

## Remaining geometric gate

The arithmetic comparison is now explicit. The first missing arrow is no longer an integral basis matrix but a source-derived identification assigning:

- the relative active boundary and endpoints to the conductor wall-one support data;
- the canonical forms \((\vartheta_2,\vartheta_3,\vartheta_4)\) to the conductor primitive basis;
- the relative kinematic parameters \((X_1,X_2,Y)\) to a conductor discriminant chart so that the transported Gauss–Manin connection equals the wallwise intermediate connection.

Without these labels and parameter map, \(U\) and \(V\) are lattice equivalences rather than geometric comparison morphisms.

## Disposition

The selected relative pairing realizes the full integral arithmetic and parity character of one elementary conductor factor. Only source-labelled support and parameter compatibility remain before it can be promoted to a relative geometric realization.
