# Native alternating normalization versus the one-coordinate stalk kernel

Date: 2026-09-07

## Result

The normalization/conductor construction used by the global mixed-variance audit and the native alternating normalization geometry have different first-order and punctured geometry unless an additional comparison is supplied.

The native alternating normalization branch is

\[
B_+=C[X_{13},X_{15},X_{35}]
\]

and its polarity conjugate is

\[
B_-=C[X_{02},X_{04},X_{24}].
\]

In words: each normalization sheet has three independent short-occurrence directions.

Entry 434 instead instantiates each loaded stalk with

\[
A_{+,L}=B_L[z_+],\qquad A_{-,L}=B_L[z_-].
\]

In words: the universal stalk node has one additional branch coordinate on each sheet.

These are valid coefficient models for different geometric questions. They are not canonically interchangeable.

## 1. First-order obstruction

At the conductor, the native positive conormal module is

\[
\mathfrak m_+/\mathfrak m_+^2
=
C\,dX_{13}\oplus C\,dX_{15}\oplus C\,dX_{35}.
\]

In words: it has rank three.

The one-coordinate stalk branch has

\[
(z_+)/(z_+^2)\cong C\,dz_+.
\]

In words: it has rank one.

A cyclically equivariant linear comparison can only send

\[
dz_+\longmapsto
a(dX_{13}+dX_{15}+dX_{35}).
\]

In words: one scalar branch direction reaches only the cyclic diagonal in the native three-dimensional conormal space.

Therefore two native conormal directions per sheet are absent from the one-coordinate branch model.

## 2. The alternating first symbol cannot factor through the scalar branch tangent

The native alternating conductor symbol has six separately labelled occurrence components. On one sheet its three coefficients are independently attached to the three short directions.

A factorization through one \(z_+\) tangent would force the three positive-sheet coefficients to be equal after coefficient transport. The source symbol does not have that property generically.

Thus

\[
\operatorname{gr}^1_{\mathfrak c}
\]

of the native alternating sheet geometry cannot be reconstructed from the one-dimensional \(z_\pm\) tangent data alone.

In words: matching the sheet difference on constants does not determine the labelled first-normal information.

## 3. Punctured overlap obstruction

The native positive punctured sheet is covered by

\[
D(X_{13}),\quad D(X_{15}),\quad D(X_{35}).
\]

Its triple overlap supports the top occurrence residue

\[
\frac{\omega_+}{X_{13}X_{15}X_{35}}.
\]

In words: this is the residue degree constructed in the previous punctured-reverse calculation.

A one-coordinate branch \(C[z_+]\) has only the single punctured chart \(D(z_+)\). Its punctured Čech complex has no pairwise or triple-overlap degree capable of representing the native top residue.

This is not a numerical rank mismatch at one truncation. It is a difference in the codimension of the conductor and therefore in the derived punctured geometry.

## 4. Consequence for Entries 434–435

Entry 434 proves that its conductor-difference kernel commutes with all loaded \(u\)-localizations. It does not specify a map

\[
C[X_{13},X_{15},X_{35}]
\longrightarrow B_L[z_+]
\]

or the reverse map that preserves the three native conormal directions.

Entry 435 then assembles the stalkwise kernel and verifies the frozen connector signature. That establishes the stated signature comparison, but it does not construct the missing native-to-\(z\) punctured overlap map.

Therefore the present coefficient-level test says:

- the one-coordinate kernel is valid in its one-normal scope;
- it cannot by itself reproduce the native three-occurrence conductor tower;
- it cannot by itself reproduce the native triple-occurrence punctured residue;
- an additional comparison object or derived correspondence must carry the two missing conormal directions per sheet.

This does not falsify the mixed-variance transform. It narrows the missing construction.

## 5. Next gate

Construct a derived map from the native alternating normalization object into the universal conductor kernel that preserves

1. all three first conormal directions per sheet;
2. the alternating first symbol;
3. the triple-occurrence punctured residue;
4. the generic \(Q\) class;
5. both endpoint connector constants.

A map using only the scalar \(z_\pm\) branch coordinate cannot satisfy the first three conditions.

## Verification

The standalone checker verifies the rank, cyclic-equivariance, labelled-support, and punctured-cover obstructions exactly.
