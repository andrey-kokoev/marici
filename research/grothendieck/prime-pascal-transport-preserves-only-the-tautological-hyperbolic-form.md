# Prime Pascal Transport Preserves Only the Tautological Hyperbolic Form

## Finite moment quotient

Fix a prime \(p\), put \(L=\log p\), and let \(r=p^{-1/2-z}\). After the
moving-seam window is retained as an independent boundary summand, translation
of the first \(N+1\) endpoint moments is represented on the transported tail
by the lower-triangular Pascal matrix

\[
(A_{p,N})_{kj}
=r\binom{k}{j}(-L)^{k-j},
\qquad 0\le j\le k\le N.
\]

Its diagonal is \(r\), so it is invertible wherever \(r\ne0\). The inverse is
the oppositely translated Pascal matrix with reciprocal scalar:

\[
A_{p,N}^{-1}=r^{-1}P_N(L).
\]

The seam is essential to this statement. Without the finite interval
\([0,L]\), restriction to the transported tail is not a lossless source map.
The matrix above describes the moment action after that missing part has been
retained separately, not reconstructed from the tail.

## Hyperbolic preservation

On the doubled carrier \(V_N\oplus V_N^*\), let prime transport act by

\[
H(A_{p,N})=A_{p,N}\oplus A_{p,N}^{-T}.
\]

The canonical evaluation form is

\[
Q_N=
\begin{pmatrix}
0&I\\
I&0
\end{pmatrix}.
\]

Direct multiplication gives

\[
H(A_{p,N})^TQ_NH(A_{p,N})=Q_N.
\]

Thus exact prime transport, its contragredient observer action, and the
retained seam are compatible with the doubled cross-form at every finite
moment order.

## Why this is not yet RH-bearing

The preservation theorem is tautological at the level of the hyperbolic
functor: every invertible \(A\) makes \(A\oplus A^{-T}\) preserve the same
evaluation form. It distinguishes a correct contragredient lift from a
same-sheet duplication, but it does not distinguish the theta source from a
hostile invertible transport.

Moreover, both polarizations remain totally isotropic:

\[
Q_N((x,0),(x,0))=0,
\qquad
Q_N((0,\alpha),(0,\alpha))=0.
\]

Hence a nonzero pure-sector state can carry zero quadratic value, and two
nonzero perspectives can still have zero cross evaluation. Preserving \(Q_N\)
does not prevent an endpoint section from vanishing.

## Same-sheet falsifier

If one incorrectly applies the same prime transport to both sectors, the
doubled map is \(A_{p,N}\oplus A_{p,N}\). It preserves \(Q_N\) only if

\[
A_{p,N}^TA_{p,N}=I,
\]

which the nontrivial Pascal shear does not satisfy. Thus the smallest Gram
minor detects the typing error immediately: the reciprocal sector must carry
the contragredient, not a second copy of the source action.

## Infinite tower

The identities hold at every finite quotient and are compatible under moment
truncation algebraically. But spectral differentiation raises degree, so no
finite quotient is invariant under the vertical generator. The completed
object remains the pro-system

\[
\{V_N\oplus V_N^*,Q_N\}_{N\ge0}.
\]

To gain zero-confinement force, the theta source must select additional
structure inside this hyperbolic pro-object, such as a positive Lagrangian
relation, cone, real polarization, or smoothing graph. That structure must
exclude endpoint-orthogonal states off the seam and survive prime transport,
moving seams, spectral raising, and completion.

## Falsifier for the next structure

At the first moment cutoff, reject a proposed oriented subobject if:

- it is not transported by \(A_{p,N}\oplus A_{p,N}^{-T}\);
- its transition requires reconstructing the seam from the tail;
- it contains a nonzero admissible state with zero endpoint evaluation;
- its positivity follows from choosing a metric after observing the endpoint
  section;
- it fails compatibility with the inclusion into the next moment quotient.

## Scope

This proves exact hyperbolic preservation for prime Pascal transport and its
contragredient. It also proves that this preservation alone has no endpoint
orientation force. It does not construct the required positive Lagrangian
relation, analytic completion, Schur–Evans bridge, zero confinement, or RH.
