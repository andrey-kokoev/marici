# 991 — The Recombination Loci Have Exact Logarithmic Residue Squares

## Question

Entry 989 found rank-one recombination fibers at

\[
D_0\cap D_2:
\quad
(ZA_2)^2=(A_3/Z)^2=1
\]

in character (++), and

\[
D_1\cap D_3:
\quad
(ZA_2B_{24})^2=(A_3B_{34}/Z)^2=1
\]

in character (--).  Does this rank collapse signal a failure of the ordinary logarithmic localization square?

## Normal-crossing test

Use logarithmic coordinates ordered as

\[
(Z,A_2,A_3,B_{24},B_{34}).
\]

The two normal rows at the (++) locus are

\[
(1,1,0,0,0),
\qquad
(-1,0,1,0,0),
\]

and at the (--) locus they are

\[
(1,1,0,1,0),
\qquad
(-1,0,1,0,1).
\]

Both matrices have rank two.  Hence both loci are ordinary transverse intersections in the frozen Laurent carrier.  Their two-wall Koszul complexes are exact away from degree zero, with no carrier excess Tor.

## Ordered residues

In the ordered basis

\[
(\mathcal L_{\chi,+},\mathcal L_{\chi,-}),
\]

the common (++) fiber row for the order (D_0,D_2) is

\[
\left(
1,
\frac{1+A_2^2}{A_2^2-1}
\right).
\]

Reversing the Poincaré-residue order gives

\[
-\left(
1,
\frac{1+A_2^2}{A_2^2-1}
\right).
\]

Similarly, at the (--) locus the two rows are

\[
\pm\left(
1,
\frac{1+A_2^2B_{24}^2}{A_2^2B_{24}^2-1}
\right),
\]

with the sign fixed by the ordered logarithmic wedge.

Therefore the signed Koszul comparison vanishes exactly:

\[
\boxed{
\operatorname{Res}_{D_j}\operatorname{Res}_{D_i}
+
\operatorname{Res}_{D_i}\operatorname{Res}_{D_j}=0.
}
\]

## Narrow conclusion

\[
\boxed{
\text{the first recombination is a line-lattice degeneration, not a logarithmic Beck--Chevalley defect.}
}
\]

The existing carrier and its ordinary Cartier/Koszul calculus close the pairwise comparison.  What fails is transversality of the two coefficient lines on the intersection fiber.

This result concerns the degree-zero logarithmic residue square.  It does not construct or compare Entry 979's degree-one exceptional chamber cell.

## Next falsifier

Form the elementary modification determined by the kernel of each common-fiber row and test whether it extends the splitting regularly across the recombination locus.  The modification must be forced by the source residue row; no fitted support summand is admissible.  Failure would identify a genuine coefficient extension even though the carrier square commutes.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_recombination_residue_square.rs`
- `research/benincasa/string-six-point-recombination-residue-square.json`

The checker imports Entry 989's exact collapse scalars, verifies sign independence, checks the logarithmic normal ranks, and exports both ordered common-fiber rows.

Epistemic graph event: `ev-000000000608-93357448-1a62-4bcb-b3ea-f22d6fdbf6ef`.
