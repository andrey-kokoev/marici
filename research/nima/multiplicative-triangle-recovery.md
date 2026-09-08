# Multiplicative triangle recovery without roots

## Question

Can locally factorizing nonzero weights be reconstructed from triangle factors without logarithms or phase branches?

## Claim boundary

Coefficients take values in an abelian group of units. Zeros and noncommutative coefficients are excluded. This is not channel-scale reconstruction or source identification.

Facet cross-products make each ac-to-bd flip ratio independent of its surrounding triangulations. Pentagon telescoping gives a multiplicative simplex cocycle g. Fix root 0 and assign h_ijk=g_0ijk away from the root, with root-containing h equal to one. Multiplicative simplex contraction gives delta h=g using only inversion and multiplication.

The product of h over triangular faces then has the same flip ratios as the input. Flip connectivity leaves one constant factor. Multiply h by this factor on exactly the triangles incident to a fixed boundary edge; every triangulation contains precisely one such triangle. This removes the discrepancy without extracting an (n-2)nd root.

The checker uses the prior local-nullspace vector f and weights b^f with b=2,-2,1+i. All fourteen values reconstruct exactly in each case, while an integer global channel character evaluates to b rather than one. The examples are thus local-pass and channel-fail. A one-entry deformation is rejected by inconsistent contextual ratios.

## Disposition

Triangle-factor recovery needs no root choices, even for signed or complex units. Channel recovery remains distinct: its incidence map has the previously proved common (n-3)rd-root kernel. The recovered triangle factors are a chosen representative, not a uniqueness theorem; their multiplicative gauge remains to be classified.
