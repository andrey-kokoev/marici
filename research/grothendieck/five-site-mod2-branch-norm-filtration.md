# Five-site mod-two branch-norm filtration

## Exact special-fiber structure

Over \(\mathbf F_2\), write the five-site deck group algebra as

\[
\mathbf F_2[(C_2)^5]
\cong
\mathbf F_2[\epsilon_1,\ldots,\epsilon_5]/(\epsilon_1^2,\ldots,\epsilon_5^2),
\qquad \epsilon_i=1+g_i.
\]

For a nonempty branch subset \(B\), the kernel of the sheet-label quotient
is \((C_2)^B\).  Its norm is

\[
N_B=\sum_{k\in(C_2)^B}k
=\prod_{i\in B}(1+g_i)
=\prod_{i\in B}\epsilon_i.
\]

Therefore \(N_B\) is nonzero in augmentation degree exactly \(|B|\), while

\[
N_B^2=0,
\qquad
\epsilon_iN_B=0\quad(i\in B).
\]

The 31 nonempty labelled deck subsets consequently reproduce the formal
Boolean deck-branch degree profile

\[
(5,10,10,5,1)
\]

in augmentation degrees one through five. This is a statement about the
formal deck lattice and its Loewy filtration, not a claim that all 31
simultaneous geometric branch loci are nonempty or have codimension equal to
their subset size.

## Meaning and boundary

This refines the bad-prime result: at the unique bad prime of the five-site
\(2\)-group tower, the failed normalized projectors do not merely disappear.
They become canonical nonzero socle-type classes whose augmentation degree
records how many branch signs coalesced.

The statement is conditional on the independently integral deck lattice.
It neither constructs the missing physical relative-chain specialization
nor supplies geometric Frobenius.  Calling the squaring map “Frobenius” here
would add arithmetic interpretation beyond the admitted finite group
algebra calculation.

The separate source-locus census gives the geometric restriction. Generic
complex loop geometry realizes degrees one through three; degree four needs
the zero-circumradius Gram discriminant, and degree five additionally needs
fifth-point cosphericity. On the real positive-definite chamber, distinct
branches do not intersect unless external points collide. The rank-two chart
requires affine consistency and then carries the conditional Kummer line
\(w^2+R=0\), with fifth selector \(Nw=C_p\). None of these supported
realizations changes the formal algebraic profile above.

## Verification

`checkers/five_site_mod2_branch_norm_filtration.py` computes in the exact
square-zero monomial presentation, checks all 31 norms, their squares and
kernel-generator annihilators, and verifies the complete formal Boolean
degree profile. Geometric support is audited separately in Nima events 1187,
1194, 1197, 1201, 1211, and 1216.
