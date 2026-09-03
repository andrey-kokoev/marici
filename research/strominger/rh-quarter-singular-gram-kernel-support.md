# Singular Gram kernels impose endpoint ranges, not interlacing support

## Question

Can singular endpoint Gram kernels force Hall support zeros without already encoding the support graph?

## Claim boundary

For a positive-semidefinite block matrix `[[A,X],[X^T,B]]`, positivity requires `ker(A)⊆ker(X^T)` and `ker(B)⊆ker(X)`, equivalently `range(X)⊆range(A)` and `range(X^T)⊆range(B)`, followed by a pseudoinverse-whitened contraction condition. Coordinate-aligned kernels eliminate whole rows or columns, leaving a Cartesian rectangle of possible cross entries. With `A=B=diag(1,1,0)`, an off-diagonal upper-left cross block of magnitude `1/2` remains positive semidefinite, and either sign is allowed. Non-coordinate kernels impose linear combinations, not coordinatewise edge support.

## Disposition

Reject singular endpoint kernels as an intrinsic generator of nonrectangular interlacing support. They can remove endpoint directions but cannot select edges within the surviving product space. Encoding the Hall graph into non-coordinate endpoint subspaces would assume the support structure rather than derive it. Next prove the general support-space characterization: a single pair of endpoint range constraints yields `Hom(U_B,U_A)`, whose coordinate support is a complete bipartite rectangle when it is coordinatewise at all.
