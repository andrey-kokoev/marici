# Quarter-source generator size boundary

## Question

Can the retained exact source-term backend test the finite-accident rival at a larger source size than `k=8`?

## Claim boundary

The backend exposes only fixed `8×8` matrices `A`, `B`, and `C` and declares `k=8`. A call carrying endpoint label `8` returns terms, but every generated source index remains in `0,...,7`; it therefore reuses the fixed size-eight object rather than constructing a size-nine census. No parameterized source matrix constructor is exposed. This establishes an authority boundary, not a failure of Hall feasibility at larger size.

## Disposition

Block the larger-size branch at the first missing typed object: source-derived constructors `A_k,B_k,C_k` with verified terminal-minor identities. Reopen when those constructors produce validated size-nine matrices; then rerun the Hall census without recycling size-eight terms. Do not infer larger-size feasibility or failure from the permissive endpoint-label call. Reallocate work to another executable rival.
