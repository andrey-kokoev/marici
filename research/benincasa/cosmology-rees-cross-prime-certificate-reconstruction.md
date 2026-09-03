# Cross-prime labelled certificate reconstruction

Problem: distinguish one integral candidate from unrelated prime-field vectors.

Bold conjecture: stable labelled support at two good primes, together with a
coefficient bound, reconstructs a unique primitive candidate that an independent
prime validates.

Rivals: support-only matching, unbounded rational reconstruction, and
single-prime promotion.

Risky consequences: bounded CRT reconstruction must be unique; a third good
prime must validate; changing one coefficient must be rejected.

Strongest falsification attempt: certificates at primes 101 and 103 with the
same four source labels and input digest reconstructed the ratios
`1,-3/2,5/2,7/2`, hence primitive vector `2,-3,5,7`, uniquely within numerator
and denominator bound 20. The candidate validated at prime 107. Incrementing
one coefficient made validation fail.

Disposition: retained for the bounded labelled protocol. Two primes alone do
not certify integrality. Stable source labels, an input digest, a preregistered
bound, independent-prime validation, and exact integral replay are required.
No Rees source generator was constructed. The next test performs exact integer
boundary replay and a corrupted-vector falsifier.
