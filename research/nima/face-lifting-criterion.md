# Cone-face criterion for boundary support lifting

## Question

Which supports of an affine toric image lift through its displayed monomial parameterization?

## Claim boundary

Let nonnegative integer vectors a_i define a monomial map, and let C be their rational polyhedral cone. This concerns support over a field. Coefficient lifting over a prescribed field remains a separate problem.

Supports of toric field-valued points are faces of the affine semigroup: a product is nonzero exactly when both factors are nonzero. For a finitely generated affine semigroup these supports correspond to cone faces F, with index set S={i:a_i in F}. Conversely each face has its Boolean point by assigning one on the face and zero elsewhere.

For such S, let U be the union of coordinate supports of its a_i. A parameter lift forces every coordinate in U nonzero. Therefore a Boolean lift exists exactly when

\[
S=\{i:\operatorname{supp}(a_i)\subseteq U\}.
\]

Equivalently, F must be induced by a coordinate face of the nonnegative orthant: it admits an exposing covector with nonnegative coordinates. Sufficiency follows by setting coordinates outside U to zero and those in U to one. Necessity follows because no monomial using only forced nonzero coordinates can vanish.

The map (x,y) -> (x,xy) separates the alternatives. Its exponent cone has a face consisting of the ray (1,1), exposed by (1,-1). Its Boolean point (0,1) is in the scheme-theoretic image A^2 but has no parameter preimage: xy nonzero forces x nonzero. This face cannot be exposed by a nonnegative covector. Thus arbitrary cone faces are not interchangeable with coordinate-induced faces.

## Disposition

The exact checker verifies this separating control and all 35 seven-point faces obtained by setting one triangle factor zero. Each tested face passes closure and all local equations. This is not an exhaustive seven-point face census. A global support-lifting theorem requires proving every cone face coordinate-induced or finding a non-coordinate face; merely repeating sparse-support samples cannot establish it.
