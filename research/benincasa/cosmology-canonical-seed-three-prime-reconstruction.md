# Three primes reconstruct seventeen of eighteen canonical seed coefficients

The canonical degree-14 seeds were extracted at prime 32027 and paired by
typed descriptor with primes 32003 and 32009. All supports agree.

CRT over the three primes gives modulus `32824466901229`. Standard unique-height
rational reconstruction with bound `4050181` recovers:

- pole 0: `7/7` coefficients;
- pole 1: `10/11` coefficients.

Every recovered candidate replays all three residues. The remaining descriptor
is the `g1`, q-pole-1 row at levels `(1,1,2,1,1)` and exponent `(0,6)`, with
residues `20914,22919,18955`.

Because one coefficient remains unresolved and no characteristic-zero source
relation has been replayed, none of the reconstructed list is promoted to a
rational seed theorem. A fourth prime or an independent coefficient-height
bound is required.
