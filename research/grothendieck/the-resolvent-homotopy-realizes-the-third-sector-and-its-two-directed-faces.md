# The Resolvent Homotopy Realizes the Third Sector and Its Two Directed Faces

## Three analytic sectors

Let

\[
R_z=(D-z)^{-1},
\qquad
x_+=R_zf,
\qquad
x_-=R_{-z}f.
\]

The seam-cocycle filler is

\[
K_z=R_{-z}R_zf.
\]

It should not be treated as a correction attached to either unilateral tail.
It is a third, relational sector situated between them.

The two source-derived face maps are exact:

\[
(D+z)K_z=x_+,
\qquad
(D-z)K_z=x_-.
\]

Their difference is the resolvent coherence law

\[
x_--x_+=-2zK_z.
\]

Endpoint evaluation supplies the remaining common cell:

\[
\operatorname{ev}_0(x_--x_+)
=
-2z\operatorname{ev}_0K_z.
\]

Thus the minimal analytic skeleton is exactly:

```text
direct tail sector   x+
          ^
          | D+z
relational sector    K
          | D-z
          v
reciprocal sector    x-

shared endpoint/control evaluation
```

This realizes `3+2+1`: three state sectors, two directed faces, and one common
endpoint mate.

## Why the third sector is forced

A direct scalar comparator between `x+` and `x-` depends on the source.  For
the exponential family `f_alpha(q)=exp(-alpha q)`,

\[
\frac{x_-(q)}{x_+(q)}
=
\frac{\alpha-z}{\alpha+z}.
\]

Changing `alpha` changes the comparator.  Hence no source-independent scalar
transition closes the two tails.

After adjoining `K`, both transitions are given by the universal differential
faces `D+z` and `D-z`.  The enlargement replaces a fitted comparison by a
source-local incidence.

## Relation to `3(3+2+1)+2+1`

The calculation proves the outer `3+2+1` skeleton.  The operator's stronger
proposal says that each of the three sectors should itself carry the already
derived internal packet:

- three content towers;
- two directed witness towers;
- one mate cell.

That gives `3(3+2+1)+2+1`, where the outer two arrows are the resolvent faces
and the final outer cell is augmentation/endpoint evaluation.

This full nesting is not yet proved.  Direct and reciprocal tails already
carry the finite primitive, square, connected, seam, and archimedean packet.
The new obligation is to lift that whole packet to `K` and prove both face maps
preserve its grades and graph domains.

## Theta-specific acceptance gates

For every finite Euler cutoff, construct boundary packets

\[
P_+,
\qquad
P_K,
\qquad
P_-
\]

and lifts

\[
d_+:P_K\longrightarrow P_+,
\qquad
d_-:P_K\longrightarrow P_-.
\]

Acceptance requires:

1. the underlying state maps are `D+z` and `D-z`;
2. primitive and square grades are transported without scalar mixing;
3. connected tails remain in their declared completion class;
4. seam and archimedean traces commute with the two faces;
5. augmentation of `d_- - d_+` equals the known cocycle;
6. the construction is compatible with cutoff inclusions.

The first nonzero grade-specific braid residual is the falsifier.  Universal
resolvent closure at state level is insufficient if one boundary grade fails
to lift.

## Result

The third-sector proposal is correct at the analytic level.  The universal
resolvent homotopy is the missing relational sector, its two differentials are
the directed comparison faces, and endpoint augmentation is their common mate
cell.  The full `3(3+2+1)+2+1` architecture is now a sharply testable lift
problem rather than numerology.

