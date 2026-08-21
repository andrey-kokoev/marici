# 1393 — Pairwise Infinity Torsors Define a Rank-Two Affine Mismatch Plane

## Status

Replicated one-characteristic modular result at \((p,z)=(1019,7)\) and \((1019,13)\). Characteristic-zero and physical interpretations remain open.

## Three pairwise affine torsors

Let

\[
\mathscr T_{12},
\qquad
\mathscr T_{13},
\qquad
\mathscr T_{23}
\]

be the affine spaces of cubic primitive solutions satisfying the corresponding two-orbit boundary-zero conditions.

Choose arbitrary representatives

\[
x_{12}\in\mathscr T_{12},
\qquad
x_{13}\in\mathscr T_{13},
\qquad
x_{23}\in\mathscr T_{23}.
\]

Because all three solve the same affine source equation, their differences lie in

\[
K=\ker A.
\]

Entry 1384 constructed

\[
R_{123}
=
K/(T_{12}\oplus T_{13}\oplus T_{23}),
\qquad
\dim R_{123}=246.
\]

## Section-independent difference classes

Define

\[
d_1=[x_{12}-x_{13}],
\qquad
d_2=[x_{13}-x_{23}]
\]

in \(R_{123}\).

Changing any representative by

\[
x_{ij}\mapsto x_{ij}+t_{ij},
\qquad
t_{ij}\in T_{ij},
\]

changes the differences only by the subspace already quotiented in \(R_{123}\).

Therefore \(d_1,d_2\) are independent of the Gaussian sections used to construct the representatives.

## Exact modular result

At both tested maximal-rank fibers,

\[
d_1\ne0,
\qquad
d_2\ne0,
\]

and

\[
\operatorname{rank}\langle d_1,d_2\rangle=2.
\]

Hence

\[
\boxed{
\Pi_{123}
=
\langle d_1,d_2\rangle
\subset R_{123},
\qquad
\dim\Pi_{123}=2.
}
\]

The third difference satisfies

\[
[x_{23}-x_{12}]
=
-d_1-d_2,
\]

so the three torsor mismatches form the expected two-dimensional affine triangle.

## Meaning

The large rank-246 residual contains a compact, source-induced rank-two object selected by the incompatibility of the three pairwise trivializations.

This is stronger than a rank count:

- the ambient quotient is section-independent;
- each difference class is nonzero;
- the two independent differences span a replicated plane;
- no fitted projector or preferred primitive representative is used.

## Prohibited inference

The plane \(\Pi_{123}\) is not yet:

- a physical rank-two period system;
- a Legendre or Kummer local system;
- an integral lattice;
- a characteristic-zero object;
- evidence for a new carrier stratum.

It is a modular affine-torsor mismatch plane inside the existing occurrence carrier.

## Next finite falsifier

Transport \(\Pi_{123}\) under:

1. cyclic occurrence rotation;
2. deck complement;
3. change of maximal-rank base value;
4. eventually the source Gauss--Manin connection.

The immediate finite test is whether cyclic and deck transport preserve the plane and determine a canonical two-dimensional representation.

If the transported plane depends on the chosen occurrence triple beyond the declared symmetry action, it is presentation data rather than a coefficient object.

## Artifacts

- `research/benincasa/results/five-site-asymmetric-affine-mismatch-plane.json`
- `research/benincasa/results/five-site-asymmetric-kummer-resolved-ibp-pilot.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`

Allocator claim: `seqclaim-b049ee4243c661f1eaac4607`.
