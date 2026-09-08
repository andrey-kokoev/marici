# Local/global complex torus quotient

## Question

Do the nonlocal coefficient relations define genuine torus characters rather than only rational linear constraints?

## Claim boundary

Use nonzero complex coefficients and labelled triangulations. No source embedding or physical quotient is asserted.

Let V be the torus of triangulation weights, L the image of triangle-factor evaluation, and C the image of channel-scale evaluation. The root-free channel lift proves C is a subtorus of L. Triangle recovery identifies L with the locally factorizing weights. The quotient Q=L/C is a complex algebraic torus of dimension

\[
1+\binom{n-1}{3}-\frac{n(n-3)}2.
\]

Write K_L and K_C for the integer character lattices vanishing on L and C respectively. Then K_L is contained in K_C, and

\[
X^*(Q)=K_C/K_L.
\]

This is torsion-free: K_L is saturated in the ambient triangulation character lattice because L is connected, hence also saturated in K_C. The finite channel parameterization kernel does not create a finite component in Q.

At six points the checker reconstructs all three local facet rows and five primitive global kernel rows in one fixed ordering. Their nonzero Smith factors are all one. Adding two chosen global rows to the local rows again yields five Smith factors equal to one. Thus these two classes are an integral basis of X*(Q), not merely a rational complement or a finite-index sublattice. Q is isomorphic to (C*)^2 with the recorded monomial coordinates.

## Disposition

The six-point nonlocal classes have saturated character coordinates. The generic torus dimension follows from the proved image dimensions; the displayed integral basis is six-point specific. A serialization defect in the first checker run was corrected by converting symbolic integers before JSON output and the checker rerun passed.
