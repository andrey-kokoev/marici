# Quarter almost-principal signs follow interval parity

## Question

Is there one combinatorial law for the base-set-dependent signs of paired almost-principal minors?

## Claim boundary

The exact result covers all 1,792 pairs in the order-eight endpoint transfer. It does not prove the law at arbitrary Hurwitz size or source order.

## Disposition

For \(i<j\) and a base set \(S\) disjoint from \(\{i,j\}\), the first almost-principal minor has sign

\[
(-1)^{j-i+1+|S\cap(i,j)|},
\]

and its paired minor has the opposite sign. Every tested pair obeys this formula. Their product is therefore strictly negative without a casewise orientation choice. This repairs the failed fixed-orientation proposal: the sign variation is not irregular but exactly controlled by interval parity. Combined with the Desnanot–Jacobi induction, the formula explains all bounded principal-minor signs. The next leaf is `quarter-almost-principal-parity-all-order`, seeking a determinant-permutation or Hurwitz sparsity proof of this sign law at arbitrary size.
