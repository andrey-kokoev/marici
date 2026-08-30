# 4095 — A Third Prime Falsifies Blind Rational Reconstruction of the Barcode Row

## Status

Established for the first source-labelled first-death row of the interaction-net barcode.

## Attempted reconstruction

Entry 4089 established a two-prime stable labelled support skeleton at

\[
p=32003,\qquad p=32009.
\]

The twenty nonzero coefficients of the first first-death row were combined by CRT. Standard symmetric rational reconstruction used modulus

\[
M_2=32003\cdot32009=1024384027
\]

and height bound

\[
\left\lfloor\sqrt{M_2/2}\right\rfloor=22631.
\]

Fourteen of twenty coefficients produced apparent rational candidates.

## Hostile third prime

The exact source construction was repeated at the independent prime

\[
p=31991.
\]

It reproduced the quotient ranks

\[
53,\quad1386,\quad3039,\quad4692,
\]

kernel profile

\[
20,\quad26,\quad26,
\]

and emergence rank \(1353\).

The same source-labelled first-death row was then compared with the fourteen two-prime rational candidates.

Only one candidate survived reduction modulo \(31991\): the normalization coefficient \(1\).

Thus

\[
1\text{ of }14
\]

two-prime candidates survived the independent prime.

## Three-prime attempt

Using all three primes raises the modulus to

\[
M_3=31991\cdot32003\cdot32009
\]

and the symmetric height bound to \(4047904\).

Even then, only twelve of twenty coefficients admit bounded rational reconstruction. The row is not completely reconstructed.

## Narrow conclusion

Stable labelled support does not supply coefficient-height bounds.

Blind CRT plus symmetric rational reconstruction is unreliable here: thirteen of fourteen plausible two-prime coefficients were false.

Therefore the characteristic-zero barcode cannot be recovered responsibly by accumulating modular samples without a source-derived denominator or height theorem.

## Surviving architecture

The evidence now separates three layers:

1. the labelled barcode skeleton is stable across good primes;
2. finite-field coefficients are prime-dependent presentations of that skeleton;
3. characteristic-zero coefficients require an independently derived arithmetic lattice or exact source solve.

## Next legitimate computation

Choose one first-death class by its frozen source labels and derive its relation directly over \(\mathbb Q\), using fraction-free elimination or a source-derived determinant/minor formula.

The result must then be reduced modulo all three primes and match the exported rows projectively.

No further prime should be added before that exact arithmetic structure is specified.
