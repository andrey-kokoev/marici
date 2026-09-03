# Full cross-Gram coordinates versus Hall coupling

## Question

Is a full cross-Gram matrix equivalent to Hall coupling data, and does Gram positivity enforce interlacing support?

## Claim boundary

A full cross block is informationally equivalent to the coupling only when each cross entry is declared to be the corresponding edge capacity; with fixed margins, `(m-1)(n-1)` entries are independent. Positive definiteness does not enforce Hall support. For the diagonal two-edge graph, take cross block `X=[[0,1/2],[1/2,0]]` and identity endpoint blocks. The block Gram matrix is positive definite because its Schur complement is `(3/4)I`; `X` is entrywise nonnegative and has row and column margins `(1/2,1/2)`, yet all its mass lies on forbidden off-diagonal edges. This counterexample does not address a source-derived identification already carrying support constraints.

## Disposition

Separate information completeness from admissibility. Full cross coordinates recover a coupling, but Hall certification additionally requires entrywise nonnegativity, prescribed margins, zero capacities on forbidden edges, and a source-derived identification. Gram positivity supplies none of the support condition. Next test whether flexible endpoint blocks make positive-semidefinite Gram embeddability automatic for every finite coupling, which would show that Gram positivity contributes no Hall restriction at all.
