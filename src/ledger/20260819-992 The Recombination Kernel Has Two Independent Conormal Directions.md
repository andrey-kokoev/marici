# 992 — The Recombination Kernel Has Two Independent Conormal Directions

> **Retracted by Entry 995.** The finite-difference helper substituted its auxiliary increment before taking the rational limit and produced a spurious second direction. Native exact differentiation gives conormal rank one on every signed sheet. The claims and next falsifier below are retained only as provenance of the failed audit.

## Elementary-modification test

Entry 991 showed that the carrier residue square is exact, while the two coefficient eigendirections coincide on the intersection fiber.  Let

\[
q_{++}=\frac{1+A_2^2}{A_2^2-1},
\qquad
q_{--}=\frac{1+A_2^2B_{24}^2}{A_2^2B_{24}^2-1}.
\]

The source-forced kernel sections are

\[
K_{++}=\mathcal L_{++,-}-q_{++}\mathcal L_{++,+},
\]

\[
K_{--}=\mathcal L_{--,-}-q_{--}\mathcal L_{--,+}.
\]

Both vanish on their recombination loci.  If the first conormal image had rank one, a single elementary line modification could repair the splitting.

## Normal coordinates

For (++), use

\[
U=ZA_2,
\qquad
V=A_3/Z.
\]

For (--), use

\[
U=ZA_2B_{24},
\qquad
V=A_3B_{34}/Z.
\]

At every signed point

\[
(U,V)=(\pm1,\pm1),
\]

compute the two exact conormal symbols

\[
\partial_UK_\chi,
\qquad
\partial_VK_\chi.
\]

## Result

For both characters and all four signed sheets,

\[
\boxed{
\operatorname{rank}
\langle
\partial_UK_\chi,
\partial_VK_\chi
\rangle=2.
}
\]

Thus the vanishing kernel section approaches the common fiber through two independent coefficient directions.

## Consequence

\[
\boxed{
\text{no rank-one elementary modification can extend the eigensplitting across recombination.}
}
\]

The minimal supported correction, if it is to be retained, must preserve the full two-normal Koszul/conormal object.  Choosing one normal direction would be noncanonical and would violate the source symmetry.

This is coefficient complexity over an existing codimension-two carrier intersection.  It neither requires nor supports a new carrier stratum.

## Updated architecture

The tested six-point string sector now has:

\[
\text{global split degree-zero coefficient lines in the generic and single-wall loci},
\]

but

\[
\text{a rank-two conormal coefficient extension at two character-selective intersections}.
\]

This is structurally parallel to the cosmological lesson that an associated-grade line can fail to control the next supported normal layer.

## Next falsifier

Construct the two-normal Koszul specialization of (K_\chi) and compute its cohomology.  If the two conormal symbols form an exact Koszul image, the splitting failure is resolved by the existing derived calculus.  If a supported class survives, it is a genuine sector-specific coefficient extension.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_character_plane_reflection.rs`
- `research/benincasa/string-six-point-character-plane-reflection.json`

The checker introduces independent exact normal coordinates, forms the source-derived kernel section, computes both first difference quotients symbolically, and evaluates their six-word projective rank on every signed sheet.

Epistemic graph event: `ev-000000000609-9f11fa4a-5f52-4f01-9970-da5864f3e55d`.
