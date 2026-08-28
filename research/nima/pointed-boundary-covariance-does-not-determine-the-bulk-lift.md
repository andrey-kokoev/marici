# Pointed Boundary Covariance Does Not Determine the Bulk Lift

## Boundary covariance is now pointed

The theta endpoint has trivial translation stabilizer. Grothendieck's affine
cut theorem shows that prime-scale transport is covariant when each chart
retains its global logarithmic origin. His Tate--Poisson theorem shows that
archimedean and polar channels swap naturally under reciprocal reflection.

Together these results close the boundary-level covariance problem without
reintroducing the character twist. The endpoint point, prime origins, and
reciprocal channel permutation are compatible.

This does not yet determine a dynamical operator in the bulk.

## General lift torsor

Let \(H\) be the bulk carrier, \(B\) the pointed boundary carrier, and

\[
\tau:H\longrightarrow B
\]

the boundary trace. Suppose \(r:B\to B\) is the already determined boundary
symmetry. A bulk lift is an operator \(R:H\to H\) satisfying

\[
\tau R=r\tau.
\]

If \(R_1\) and \(R_2\) are two lifts, their difference satisfies

\[
\tau(R_1-R_2)=0.
\]

Thus the ambiguity lives in the boundary-invisible bulk sector
\(\ker\tau\). Pointing \(B\) removes boundary phase translations but does not
remove automorphisms or residual maps internal to \(\ker\tau\).

## Isometry does not remove the ambiguity

Take

\[
H=B\oplus N,
\qquad
\tau(b,n)=b.
\]

Even when the boundary action is the identity and the bulk metric is fixed,
the two orthogonal lifts

\[
R_+(b,n)=(b,n),
\qquad
R_-(b,n)=(b,-n)
\]

have the same pointed boundary trace:

\[
\tau R_+=\tau R_-=\tau.
\]

They differ on the invisible bulk channel \(N\). Hence boundary coherence,
endpoint pointing, and norm preservation do not select a unique bulk lift.

## Source consequence

The remaining theta/Tate constructor cannot be another boundary
normalization. It must identify the lower bulk incidence by source dynamics.
Candidate data include:

1. the doubled Clark--Green differential system;
2. the tail--seam graph relation;
3. the forcing reservoir;
4. a Green identity fixing how the invisible bulk sector meets the boundary.

The required theorem must show that these data select one lift, or that all
admissible lifts induce the same completed zero-state law.

## Finite falsifier

The pair \(R_+,R_-\) is the smallest hostile. Any proposed theorem using only
the pointed boundary action, boundary trace, and bulk norm must give the same
input data for both lifts. If it nevertheless selects one, an undeclared bulk
orientation has entered.

For a source-specific candidate \(R\), the finite falsifier is a nonzero
operator \(A\) satisfying

\[
\tau A=0
\]

such that \(R+A\) preserves every declared boundary law and metric law. Its
existence proves that the bulk constructor remains underdetermined.

## Next gate

Construct the actual finite-cutoff lower bulk incidence. Write
\(\mathcal L_{\mathrm{src}}\) for its declared source laws and compute the
stabilizer

\[
\operatorname{Stab}(R;\tau,\mathcal L_{\mathrm{src}})
=
\{A:\tau A=0,\ R+A\in\mathcal L_{\mathrm{src}}\}.
\]

The desired uniqueness theorem is that this stabilizer contains only zero.
Unlike the earlier scalar orientation question, this is a finite operator
calculation once the source matrices and domains are declared.
