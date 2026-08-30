# Eight-site cosmology inventory conventions

## Frozen source object

The source graph is the labelled cycle (C_8), with sites and edges ordered

\[
(X_1,\ldots,X_8;y_1,\ldots,y_8).
\]

For each edge (i\to i+1), the cosmological-polytope source contributes the three labelled vertices

\[
(X_i,X_{i+1},y_i)=(1,1,-1),(1,-1,1),(-1,1,1),
\]

with all other coordinates zero.  Connected cyclic regions of lengths (1,\ldots,7), the eight fused facets (G\setminus e_i), and the total-energy facet (G) are generated before any orbit selection.

The common block consists of the eight singleton regions and (G).  Its exact rank is (9).  A maximal source denominator has rank (16); consequently it contains exactly seven noncommon facets, and every selected noncommon row must raise the quotient rank by one.  This is a derived source constraint, not an extrapolation from seven sites.

## Occurrence equivalence and orientation

Only labelled cyclic rotation by (C_8) is quotiented.  Reflections and unlabelled graph isomorphisms are not imposed.  Every orbit packet retains:

- its canonical labelled key;
- stabilizer order and orbit size;
- enumerated source multiplicity;
- the ordered source representative.

Residue orientations are transported in source order.  Returning to canonical lexical order contributes the parity of that sorting permutation.

## Predeclared partition and ranking

Before any Cayley--Menger equation is evaluated, the inventory is partitioned by:

1. compatibility-poset isomorphism type, colored by region/fused-facet type and region cardinality;
2. signed-energy wall rank;
3. number of free signed energies, hence free loop-square variables;
4. homogeneous-diagonal behavior from augmented rank.

The attack order is fixed independently of discriminants:

1. visit every new compatibility-poset type once before additional members;
2. maximize free loop-square rank;
3. prioritize nontrivial cyclic stabilizer;
4. use the frozen combinatorial nesting/separation score;
5. resolve remaining ties by the lexicographically least labelled key.

## Universal routing geometry

The cyclic pairing is retained with independent labelled parameters at cyclic distances three and four:

\[
\langle q_i,q_j\rangle=
\begin{cases}
2,&d=0,\\
3/2,&d=1,\\
1/2,&d=2,\\
k,&d=3,\\
l,&d=4.
\end{cases}
\]

The four cumulative routes (q_1,q_1+q_2,q_1+q_2+q_3,q_1+q_2+q_3+q_4) give

\[
\det G=-\frac14 k(6+7k).
\]

Thus the two frozen Gram boundaries remain (k=0) and (k=-6/7).  The parameter (l) enters the three extension equations but not this Gram determinant.  An (l)-dependent Jacobian factor is therefore coefficient geometry, not a disguised third Gram boundary.

The ordered cover rows are

\[
(F_1,F_6,F_7,F_8).
\]

For each orbit the checker solves the seven labelled wall equations, constructs these four cover equations, differentiates with respect to every free signed energy, and takes every maximal minor.  Saturation removes only the frozen Gram, soft, and lower-incidence factors.

## Physical and Cartier gates

Strict positivity of all (X_i) is tested exactly by the Gordan alternative.  Base-relation rank is at most three; the checker uses projective coefficient normalization and exact rational Fourier--Motzkin elimination, returning explicit row coefficients for every obstruction.

Each Gram specialization is audited as a divisorial hull.  Global polynomial principality and generic Cartier behavior are kept distinct.  The generic Cartier length is computed from squarefreeness of the exact divisorial-hull generator.

No fitted carrier facet, support summand, or post hoc normalization is admitted.
