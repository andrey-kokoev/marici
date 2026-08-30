# A minimal Hilbert Schur complement cannot realize the prime cross trace

Epistemic-graph event: 1431.

## Fixed-sign Schur complements

Let

\`L=[[A,B^*],[B,D]]\`

be a self-adjoint block operator on a Hilbert direct sum. Eliminating the
\`D\` channel gives the Schur complement

\`S(z)=A-z-B^*(D-z)^(-1)B\`.

For a scalar boundary vector, the resolvent term is a quadratic form

\`<b,(D-z)^(-1)b>\`.

Its representing measure is positive. On the Stieltjes axis,
\`<b,(D+x)^(-1)b>\` is a Stieltjes function and has a fixed-sign cut density.
This remains true for arbitrary positive multiplicity and direct sums.

Ledger 1389 proves that a prime-distance term

\`g_a(x)=exp(-a sqrt(x))/(2sqrt(x))\`

has oscillating cut density \`cos(a sqrt(t))/(2pi sqrt(t))\` for every
\`a>0\`. Hence no single Hilbert-space coupling vector, nor any positive
direct sum of such vectors, has Schur complement equal to the intrinsic-prime
cross trace.

## Polarization gives an indefinite realization

For a positive resolvent \`R_x=(H_0+x)^(-1)\` and real boundary distributions
\`u,v\`, polarization gives

\`4<u,R_x v>
=<u+v,R_x(u+v)>-<u-v,R_x(u-v)>\`.

Thus every finite-cutoff prime cross term is the difference of two positive
quadratic resolvents. Introduce the doubled coupling vectors

\`b_+=u+v\`, \`b_-=u-v\`

and the fundamental symmetry \`Q=diag(1,-1)\`. The cross term becomes a
\`Q\`-quadratic resolvent. This is a Krein-space realization, not a positive
Hilbert Schur complement.

The coefficient--Betti double from Ledger 1369 has precisely the required
paired algebraic slots, and its polarization exchange \`J\` supplies the
orientation. But its symplectic form is not itself a positive inner product,
and the Gaussian norm-two map \`1+J\` does not select a positive quotient of
the infinite prime-propagation channels.

## Descent gate

To obtain the requested self-adjoint Hilbert operator, the indefinite doubled
system must descend through a source-derived positive quotient. At finite
cutoff this requires a subspace \`N\` such that:

1. the completed gamma-plus-prime form vanishes on \`N\`;
2. the induced form on \`N^perp/N\` is positive;
3. the block Green identity is compatible with cutoff refinement; and
4. the resulting scalar Schur complement is exactly \`R_Xi\`.

Existence of such a positive quotient for every spectral parameter is
equivalent to the Pick/Stieltjes positivity gates of Ledgers 1382--1385.
Choosing \`N\` from the negative spectral directions after diagonalizing
\`Xi\` would again insert the zero data.

## Consequence

The minimal two-channel Hilbert block is falsified. The exact source
realization presently available is indefinite. This explains why the paired
coefficient--Betti structure is necessary but also why it is insufficient:
the unresolved RH content is precisely the existence of a canonical positive
descent of the signed prime--gamma block.

## Scope

This is an exact no-go for a single positive Hilbert Schur complement and an
exact finite-cutoff Krein polarization identity. It does not rule out a
source-derived positive quotient of the full completed indefinite block.
