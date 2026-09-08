# Nontrivial gluing on the punctured determinantal face

## Question

Can regular changes of factors glue the four pivot sections on the punctured face?

## Claim boundary

No. This holds over every field for the scheme U obtained by deleting the vertex from X=Spec k[a,b,c,d]/(ad-bc). It does not prohibit pointwise selections or the previously constructed chart sections.

### Coordinate-ring obstruction

The determinant polynomial is irreducible: as a primitive linear polynomial in d over k[a,b,c], its coefficients a and -bc are coprime. Thus X is integral of dimension three. As a hypersurface it is Cohen-Macaulay, hence satisfies Serre's S2 condition. Its four partial derivatives d,-c,-b,a vanish only at the vertex. Away from that point the nonzero-entry charts solve for one variable and are smooth over k. The vertex has codimension three, so X satisfies R1 and is normal by Serre's criterion, in every characteristic.

For a normal Noetherian integral affine scheme, removing a closed subset of codimension at least two leaves the ring of global regular functions unchanged. Therefore Gamma(U,O)=k[a,b,c,d]/(ad-bc). Every hypothetical section U -> A^35 would extend coordinate by coordinate to X -> A^35. The section identities extend because they are polynomial identities holding on the dense open U. This contradicts the previously proved rank obstruction at the face vertex. This argument allows all triangle coordinates, not merely the minimal-support factors.

### Transition class

The map U -> P^1 x P^1 remembers the two rank-one factor lines. U is the total space of O(-1,-1) with its zero section removed. The column-vector factor r is a nonzero section of the pullback of O(-1,0). Its local pivot representatives differ by the invertible scalars computed in boundary-pivot-charts.md.

Picard homotopy invariance identifies the Picard group of the line-bundle total space with Pic(P^1 x P^1)=Z^2. Divisor localization upon removing its zero section quotients by the class (-1,-1). Consequently Pic(U)=Z^2/Z(1,1). The class (-1,0) maps to -1 under (m,n) -> m-n and is nonzero. Thus the pivot cocycle cannot be trivialized by regular rescalings. A reversed convention changes its sign, not its nontriviality. The checker verifies the derivative and integer-class calculations, including the trivial diagonal control; it does not substitute finite samples for these structural theorems.

## Disposition

The pole of a particular pivot is removable by changing charts, but the entire transition system is not trivial. There is no global regular triangle section even on the punctured face. The two proofs separate a genuine line-bundle obstruction from a bad formula. A constructive next question is whether replacing a chosen vector factor by its projective line supplies a proper incidence resolution on which factor information is retained without demanding a scalar trivialization.
