# Quarter transfer principal minors are log-supermodular

## Question

Do the transfer principal minors satisfy generalized Hadamard–Fischer inequalities?

## Claim boundary

The exhaustive result covers one order-eight endpoint transfer matrix. It does not prove the same lattice inequality at arbitrary Hurwitz size or source order.

## Disposition

The GKK orientation fails immediately. Instead, every one of the 32,896 unordered subset pairs satisfies the reverse inequality

\[
p(A)p(B)\leq p(A\cup B)p(A\cap B).
\]

Exactly 26,335 inequalities are strict and 6,561 are equal. The equality count is \(3^8\), matching comparable subset pairs; all incomparable pairs are strict. Thus the principal-minor map is strictly log-supermodular off comparable pairs, not GKK log-submodular. The next leaf is `quarter-hurwitz-transfer-almost-principal-signs`: use Desnanot–Jacobi identities to test whether paired almost-principal minors always have opposite signs, which would locally generate the reverse lattice inequalities.
