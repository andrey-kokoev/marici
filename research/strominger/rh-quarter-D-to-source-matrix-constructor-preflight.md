# Quarter D-to-source-matrix constructor preflight

## Question

Does the D-family backend supply the missing parameterized source matrices needed for a size-nine Hall test?

## Claim boundary

The backend generates `Q(s)` and `D(n,s)` at size nine; the tested objects have degrees 4 and 108. It exposes no parameterized assembly map producing labelled `A_k,B_k,C_k` matrices or proving their terminal-minor source formula. Polynomial availability therefore does not authorize construction of the missing source matrices. This is an interface absence, not evidence against size-nine Hall feasibility.

## Disposition

Block this branch at `build_source_matrices(k)`. Reopen only when the map reproduces retained `A,B,C` exactly at `k=8`, produces dimensionally valid matrices at `k=9`, and verifies every source-term determinant identity before flow analysis. Do not derive further acceptance abstractions from the same missing map; reallocate to a distinct executable programme rival.
