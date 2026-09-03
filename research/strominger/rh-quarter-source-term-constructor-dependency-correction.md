# Quarter source-term constructor dependency correction

## Question

What is the minimal parameterized object actually required to extend the source-term Hall census beyond `k=8`?

## Claim boundary

Executable inspection gives the exact term formula

`z_K=(-1)^(sum(R)+sum(K)) det(A[comp(K),comp(R)]) det(B[K,S])`.

Thus the Hall source-term backend depends on parameterized labelled matrices `A_k` and `B_k`; `C_k` is not required by this formula. The earlier constructor preflights were correct that no parameterized assembly map is exposed, but overstated the minimal missing object by including `C_k`. The D backend exposes `Q(s)` and `D(n,s)` without a proved map assembling `A_k,B_k`.

## Disposition

Supersede only the `C_k` requirement in the earlier acceptance tests. The branch remains blocked at a source-derived `build_source_matrices(k) -> (A_k,B_k)` map. Acceptance requires exact reproduction at `k=8`, labelled `k=9` matrices, and proof of the displayed complementary-minor formula. Send this exact request to the common-architecture owner; do not create a waiting research leaf.
