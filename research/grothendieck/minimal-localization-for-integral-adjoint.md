# Smith divisibility gives the minimal localization for a Betti adjoint

Epistemic-graph event: 1354.

## Denominator theorem

Assume the target pairing matrix `P_H` is square and nondegenerate over `Q`.
Choose Smith data

`U P_H V=diag(d_1,...,d_r)=D`

with positive nonzero invariant factors, and set

`B=Q^T P_G`, `B'=U B`.

The adjunction equation `P_H S=B` becomes

`d_i X_ij=B'_ij`, where `X=V^(-1)S`.

Define the reduced denominator

`e_ij=d_i/gcd(d_i,B'_ij)`

and

`L=lcm_(i,j) e_ij`.

Then `L` is the least positive integer that clears every denominator of the
unique rational adjoint.  An integral adjoint exists exactly when `L=1`.
Over `Z[1/N]`, an adjoint exists exactly when every prime dividing `L` also
divides `N`.  Hence the prime support of `L` is the minimal localization
locus.

## Hostile controls

- `P_H=[6]`, `B=[4]` gives `L=3`: inverting two does nothing, while inverting
  three produces `S=2/3`.
- `P_H=[6]`, `B=[6]` gives `L=1`: the nonunimodular pairing nevertheless
  admits the integral adjoint `S=1`.

Thus the determinant or pairing index alone overestimates the obstruction;
the pullback image can already contain the needed divisibility.

## Arithmetic separation

The adjoint-localization primes depend jointly on `P_H` and `Q^T P_G`.  They
need not equal the deck-degree primes or the monodromy resonance primes.
Accordingly the paired system has three independent arithmetic supports:
norm degree, resonance, and pairing-lattice denominator.  Coincidence in the
formal delta basis is not a theorem for the physical relative pairing.

## Five-site consequence

A future physical pairing packet should publish Smith data and the transformed
adjunction right-hand side in each degree.  This decides integral existence
and its minimal localization before any boundary or norm calculation.
