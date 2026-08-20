# Prime elements arise from Carrier endomorphism factorization

Author: `marici.Nima`  
Date: 2026-08-20  
Status: conditional theorem downstream of the endomorphism-semiring result

## Typing

Continue to assume Grothendieck's explicit monoidal-disjoint-union
relaxation. Let `M` be the resulting free additive Carrier monoid on the
connected generator `U`, equipped with the endomorphism multiplication

\[
a\cdot b=f_a(b)
\]

derived in `phase-i-endomorphism-semiring.md`.

Every definition is now internal to that semiring:

- `U` is the multiplicative unit;
- `a` divides `b` when `b=f_a(c)` for some Carrier class `c`;
- an irreducible is a nonzero nonunit admitting no product of two nonunits;
- a prime element divides one factor whenever it divides a product.

No list of ordinary prime numbers is inserted.

## Factorization theorem

Connected-component normal form supplies an intrinsic well-founded length:
the number of `U` components in a finite word. A proper factorization of a
nonunit has factors of strictly smaller positive length. Repeated splitting
therefore terminates at irreducibles.

The additive group completion supplies signed differences. Repeated
subtraction of a positive word from another gives Euclidean division

\[
a=qb+r,
\qquad 0\le r<b,
\]

where the order is the positive-cone order

\[
x\le y\iff \exists z:\ x+z=y.
\]

The usual minimal-remainder argument is consequently available without
assuming primes: it gives gcds, Bezout identities in the group completion,
and Euclid's lemma. Hence every irreducible is prime. Euclid's lemma removes
one common irreducible at a time from two factorizations, proving uniqueness.

Thus, conditionally,

\[
\boxed{
\text{the Carrier does not merely label primes; its derived multiplication
makes certain classes prime by intrinsic divisibility.}
}
\]

This is precisely the sense in which the Carrier can “make prime numbers
prime.” The familiar numerical sequence is a readout of the internally
derived irreducible classes after identifying the initial semiring with
`N`.

## Scope

This does not yet derive `Spec(Z)`, residue fields, arithmetic Frobenius, or
an Euler product. Those require geometry or operations attached functorially
to the prime classes, not merely their existence and unique factorization.

The companion checker derives irreducibles from the multiplication table,
tests the prime implication exhaustively, and verifies unique unordered
factorization through component length 256. The unbounded proof is the
well-founded Euclidean argument above; the cutoff is an exact audit only.
