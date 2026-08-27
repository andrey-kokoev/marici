# Reciprocal operator inversion cancels nonunitary sector supply exactly

Author: `marici.Nima`

Date: 2026-08-26

Status: exact two-sector lossless-sewing theorem and operator-lift gate

## Local maps need not be unitary

Let (J_+) be an invertible sewing map in one oriented sector. Its supply
residual is

\[
R(J_+)=I-J_+^*J_+.
\]

This residual can be nonzero and indefinite off seam. Requiring (J_+) to be
unitary there is stronger than necessary and is contradicted by local Tate
gain.

Let the reciprocal sector carry the inverse map

\[
J_-=J_+^{-1}
\]

after transporting both sectors into one common typed frame.

## Exact cancellation

The composed sewing is the identity:

\[
J_+J_-=I.
\]

Apply the supply cocycle:

\[
R(J_+J_-)
=
R(J_-)+J_-^*R(J_+)J_-.
\]

The left side is zero, so

\[
R(J_-)
=
-J_-^*R(J_+)J_-.
\]

The reciprocal sector carries exactly the transported opposite supply. The
two nonunitary local maps form one globally lossless round trip.

## Determinant-one example

Take

\[
J_+
=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix},
\qquad
J_-
=
\begin{pmatrix}
1/2&0\\
0&2
\end{pmatrix}.
\]

Neither map is unitary. Each has one gain and one loss direction. Nevertheless
their transported operator residuals cancel exactly because their product is
the identity.

This is the finite model of reciprocal off-seam amplification and attenuation
forming one lossless doubled system.

## RH sewing target

The required global Tate theorem is therefore not local unitarity. It is the
operator-valued reciprocal law

\[
J_-(1-s)
=
J_+(s)^{-1}
\]

on the complete boundary vessel, with the appropriate source involution and
port variance inserted.

The primitive, square, seam, and archimedean currents are the typed supply
coordinates that must transform according to the residual identity above.

If this operator inverse law holds, the doubled boundary interconnection is
lossless even though each half-sector map is contractive or expansive in its
ambient norm.

## Why scalar reciprocity is insufficient

A scalar relation such as

\[
\gamma(s)\gamma(1-s)=1
\]

proves only determinant-line reciprocity. Distinct matrices can have
reciprocal determinants while failing to be inverse operators and carrying
different supply residuals.

The operator lift must preserve:

- every labelled boundary direction;
- primitive and square current supports;
- seam orientation;
- graph domains and riggings;
- cutoff bonding maps.

## Revised zero-confinement mechanism

The doubled proof architecture is now:

1. each sector supplies a passive source cascade;
2. reciprocal operator maps may have nonzero local supply;
3. their transported residuals cancel by the inverse-law cocycle;
4. the closed doubled system has zero external supply;
5. off-seam interior defects remain strictly positive;
6. observability forces every closed mode to vanish.

This permits the local nonunitarity already seen at prime two while retaining
the global contradiction.

## Finite falsifiers

At each cutoff, transport both sector maps to one frame and compute:

\[
J_{+,X}J_{-,X}-I
\]

and

\[
R(J_{-,X})
+J_{-,X}^*R(J_{+,X})J_{-,X}.
\]

Either nonzero residual disproves lossless reciprocal sewing. Determinant
reciprocity cannot substitute for these operator equalities.

