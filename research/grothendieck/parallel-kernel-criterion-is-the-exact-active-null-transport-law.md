# The parallel-kernel criterion is the exact active null-transport law

## Setup

Let `V -> I` be a finite-rank vector bundle over an interval inside one open
half-plane. Write a source-derived transport equation as

\[
v'(r)=A(r)v(r),
\]

and let the scalar observation be a nonzero covector field

\[
L(r):V_r\longrightarrow\mathbb C.
\]

The scalar-null hyperplane is `K_r=ker L(r)`.

## Exact criterion

The hyperplane family `K_r` is preserved by the transport if and only if
there is a scalar function `alpha(r)` such that

\[
L'(r)+L(r)A(r)=\alpha(r)L(r).
\]

This is the missing active law in its smallest differential form.

### Proof

If the displayed equation holds and `v` is parallel, then

\[
\frac{d}{dr}L(r)v(r)=\alpha(r)L(r)v(r).
\]

Consequently a scalar null at one point propagates throughout the connected
transport interval.

Conversely, preservation of `ker L` means that the covector
`L'+LA` vanishes on `ker L`. Because `L` has one-dimensional quotient, the
linear factorization theorem from ledger 3808 gives

\[
L'+LA=\alpha L.
\]

Thus active null propagation is exactly static factorization applied to the
covariant derivative rather than to additional observation ports.

## Zero-confinement consequence

Suppose this criterion is derived independently on every horizontal interval
inside each open half-plane, and suppose the transported scalar section has a
known nonzero anchor in each connected sector. Then it has no zero anywhere
in either open sector: a hypothetical zero would propagate to the anchor and
contradict its nonvanishing.

This would confine all zeros to the excluded sewing seam.

The exclusion is essential. The actual completed function has zeros on the
seam. A regular connection preserving the scalar-null hyperplane across the
seam would propagate each such zero into both half-planes, contradicting the
desired geometry. Therefore a successful source connection must be defined
sectorwise and fail to extend as the same null-preserving connection across
the seam. The seam is where the two transport laws meet, change type, or
require an additional interface state.

## Why this is not RH in disguise

For a scalar function alone one could set `alpha=X'/X`; that divides by the
unknown section and is singular precisely at its zeros. Such a construction
is tautological and forbidden.

The accepted derivational order is instead:

```text
labelled theta/Tate source
  -> state bundle V and source connection A
  -> source covector L
  -> identity L' + L A = alpha L
  -> sectorwise zero exclusion
```

The connection and `alpha` must exist before inspecting the divisor. A hostile
symmetric multiplier must fail to lift to the same connection identity.

## Defect covector

For any candidate source connection define

\[
\Omega=L'+LA.
\]

Its class in the quotient

\[
V^*/\langle L\rangle
\]

is the exact active-action defect. The null hyperplane is parallel precisely
when this class vanishes. Unlike another scalar determinant or monitor, this
quotient covector measures transverse leakage of the scalar-null condition
under source transport.

This supplies a finite-cutoff falsifier: construct `A_X` and `L_X` directly
from the labelled cutoff and compute the rank of the two-row matrix

\[
\begin{pmatrix}L_X\\L_X'+L_XA_X\end{pmatrix}.
\]

Rank greater than one is an explicit failure of null transport at that
cutoff. Rank one obtained only after using the scalar zero equation is
circular and also fails.

## Relation to the team transfers

- Aspect's rank-one update is a candidate ingredient of `A`, because it
  changes the source balance upstream and is sheet-covariant.
- Nima's coequalizer theorem says `A` cannot be reconstructed downstream from
  the scalar quotient.
- Strominger's dependent ActionWitness supplies the typing required before
  `A` can be called source-authorized.
- Flavor's co-moving connection shows that presentation parallelism alone is
  insufficient: the identity must act on `L`, not only on the moving frame.

The research frontier is now one explicit source identity rather than an
open-ended search for more ports.
