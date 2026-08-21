# Radical resonance unit sieve

## Corollary

For a finite surjection `q:G->H`, let `K=ker(q)`, let `A_q` be the
conjugation image in `Aut(K)`, and define

`R_q = rad(exp(K)*exp(A_q))`.

Ledger 1281 implies that the compatible power indices are exactly

`{n>=1 : gcd(n,R_q)=1}`.

Thus compatibility is periodic modulo the square-free resonance modulus and
its residue classes form the unit group `(Z/R_q Z)^x`.  The compatible
indices are closed under multiplication, as required by

`P_m P_n = P_(mn)`.

In each complete period, the number of survivors is `phi(R_q)`, so their
natural density is

`phi(R_q)/R_q = product_{p|R_q}(1-1/p)`.

## Examples

- the abelian five-site deck quotients have `R_q=2`: exactly odd indices;
- `A4->C3` and `Q8 semidirect C3->C3` have `R_q=6`: units modulo six;
- `C5 semidirect C4->C4` has `R_q=10`: indices prime to ten;
- central `Heisenberg27->C3^2` has `R_q=3`: indices prime to three.

## Typing boundary

This is a finite congruence sieve on algebraic correspondence operations.
It is not an Euler product, a distribution of Carrier-derived primes, a
geometric Frobenius spectrum, or a physical selection theorem.  The actual
basis power maps can depend on exponents larger than `R_q`; only their
compatibility indicator factors through the radical modulus.

