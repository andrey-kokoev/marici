# Quarter Hurwitz Bernstein positivity is termwise

## Question

Are positive Bernstein coefficients produced by cancellation, or by positive endpoint mixed-column determinants?

## Claim boundary

The result covers principal Hurwitz minor orders one through eight in the order-six pencil. It does not prove positivity for every mixed choice or arbitrary source order.

## Disposition

Multilinearity gives the exact identity

\[
b_{k,j}=\binom{k}{j}^{-1}
\sum_{|S|=j}\det M_{k,S},
\]

where \(M_{k,S}\) uses endpoint columns in positions \(S\) and product columns elsewhere. All 510 individual mixed determinants are strictly positive, and every identity with the interpolated Bernstein coefficient holds exactly. Thus bounded Bernstein positivity is termwise and cancellation-free. Writing \(M_{k,S}=A_k\) with columns replaced by \(B_k\) shows these determinants equal \(\det(A_k)\) times principal minors of \(A_k^{-1}B_k\). The next leaf is `quarter-hurwitz-transfer-p-matrix-versus-total-positivity`, testing whether this transfer matrix has the stronger total-positivity structure needed for a network proof.
