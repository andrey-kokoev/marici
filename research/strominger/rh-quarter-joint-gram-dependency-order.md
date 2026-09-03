# Joint-Gram request is downstream of the source-matrix constructor

## Question

Can the rank-49 joint-Gram request be tested before the missing parameterized source constructor is supplied?

## Claim boundary

No. The exact source term is `z_K=(-1)^(sum(R)+sum(K)) det(A[comp(K),comp(R)]) det(B[K,S])`. It requires labelled `A_k,B_k` and does not require `C_k`. Joint Gram coordinates and interlacing-edge capacities are downstream outputs of these terms. The retained backend contains only fixed `A_8,B_8`; without `build_source_matrices(k)->(A_k,B_k)`, neither size-nine source terms nor an all-order rank `(k-1)^2` joint map are defined. This establishes dependency order, not impossibility of such a map after construction.

## Disposition

Supersede the direct rank-49 handoff by the first missing typed object already requested in event `ev-000000012271-f459a2b3-e0c6-473e-a08f-03bfe6ded9fc`: reproduce labelled `A_8,B_8`, construct labelled `A_9,B_9`, and prove the complementary-minor formula. Only then test bounded rank 49 and general rank `(k-1)^2`. Further local joint-Gram elaboration before that constructor would be non-executable successor proliferation.
