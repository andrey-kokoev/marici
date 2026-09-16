# Strict successor naturality and unique H234 recovery fill the signed mixed horns through tetrahedral degree

## Setting

Work in the observer-generated signed asymptotic category. Let

\[
\mathsf S_k:\mathcal N_k\to\mathcal N_{k+1}
\]

be an admitted cutoff/refinement successor preserving composition and
whiskering. Assume the three independently constructed faces satisfy

\[
\mathsf S_k(H_{123,k})=H_{123,k+1},
\]

\[
\mathsf S_k(H_{124,k})=H_{124,k+1},
\]

\[
\mathsf S_k(H_{134,k})=H_{134,k+1}.
\]

At every stage, recover \(H_{234,k}\) uniquely by right whiskering along the
faithful integrated observer representation.

## Naturality of the recovered face

The tetrahedral equation at stage \(k\) is

\[
H_{124,k}\circ(H_{234,k}*C_{12,k})
=
H_{134,k}\circ(C_{34,k}*H_{123,k}).
\]

Apply \(\mathsf S_k\). Preservation of composition and whiskering, together
with naturality of the other three faces, gives

\[
H_{124,k+1}\circ
(\mathsf S_k(H_{234,k})*C_{12,k+1})
=
H_{134,k+1}\circ
(C_{34,k+1}*H_{123,k+1}).
\]

But \(H_{234,k+1}\) is the unique preimage under faithful right whiskering that
satisfies this equation. Therefore

\[
\boxed{
\mathsf S_k(H_{234,k})=H_{234,k+1}.}
\]

No independent mixed cell for face \(234\) must be selected.

## Mixed horn consequences

The preceding equality fills the bidegree \((1,2)\) horn consisting of one
successor edge and the triangular face \(234\). The assumed strict naturality
fills the corresponding horns for faces \(123,124,134\).

Together, the four mixed triangular prisms form the side boundary between the
tetrahedron at \(k\) and the tetrahedron at \(k+1\). Since both tetrahedral
pasting equations hold and every side prism commutes, the bidegree \((1,3)\)
mixed horn has a unique signed filler.

For a successor chain \(k\to k+1\to k+2\), strict composition

\[
\mathsf S_{k+1}\mathsf S_k=
\mathsf S_{k,k+2}
\]

makes the two pasted mixed cells equal. This supplies the corresponding
bidegree \((2,2)\) compatibility through the same uniqueness argument.

## Truncated result

Hence the signed observer-generated system has mixed horn fillers in the
following range:

\[
(1,1),\quad(1,2),\quad(1,3),\quad(2,1),\quad(2,2),
\]

provided the successor acts on an immutable realization of each named face.
The result is a bisimplicial coherence theorem through tetrahedral process
degree and two-step successor degree.

## What this does not prove

It does not establish:

- Kan filling in arbitrary degree;
- invertibility of physical projections or traces;
- positive mixed horn fillers;
- naturality across a successor that changes regulator normalization without a
  supplied comparison cell;
- contractibility of all filler spaces outside the faithfully whiskered
  observer-generated subsystem.

## Significance

The first missing signed mixed horn is therefore not among the four semilocal
faces under the admitted strict successor. It occurs when either:

1. successor provenance changes and strict naturality is unavailable; or
2. one passes from signed asymptotic cells to positive metric lifts.

This localizes the active conjecture to the positive/certificate-changing
bisimplicial direction rather than the established signed refinement tower.
