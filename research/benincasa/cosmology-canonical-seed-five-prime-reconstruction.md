# Five primes reconstruct the complete canonical seed coefficient vector

The degree-14 seed was extracted at verified prime 32051 with unchanged typed
support. Five-prime CRT followed by standard unique-height rational
reconstruction recovers all 18 coefficients and every candidate replays all
five residues.

The two coefficients unresolved after four primes are

- q-pole-0 exponent `(0,2)`: `275/1111065984`;
- q-pole-0 exponent `(2,0)`: `125/1111065984`.

The complete vector now has a five-prime rational candidate. This does not yet
prove a characteristic-zero seed identity: the rational coefficients must be
inserted into the exact symbolic `T+S_K+S_q` relation and replayed over the
integer/rational source module. Deterministic pivot selection also remains a
presentation choice until that replay succeeds.
