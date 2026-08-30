# Paired-selector refinement versus simultaneous coarse compatibility

## Two different constructions

Let `c,d:G->R` be selectors with terminal admissible kernels

`K_c=Core_G(Stab_R(c))`, `K_d=Core_G(Stab_R(d))`.

For the paired selector `(c,d)`,

`Stab_R(c,d)=Stab_R(c) intersection Stab_R(d)`

and normal cores commute with intersections, so

`K_(c,d)=K_c intersection K_d`.

This is the terminal kernel of the common refined coefficient quotient. Its
operation spectrum is `U(K_c intersection K_d)`. Monotonicity gives

`U(K_c) union U(K_d) subset U(K_c intersection K_d)`.

By contrast, requiring one index to preserve both original coarse quotient
systems gives

`U(K_c) intersection U(K_d)`,

the unit system modulo `lcm(R(K_c),R(K_d))`. This can be strictly smaller
than the paired-selector refinement spectrum.

## Exact C6 separator

In `G=C6`, take coset selectors for the unique kernels `K2` and `K3` of
orders two and three. Their paired selector has trivial stabilizer and hence
trivial terminal kernel.

- paired-selector refined quotient: modulus `1`, so every index survives;
- simultaneous preservation of the two coarse quotients: moduli `2` and
  `3`, so exactly indices prime to `6` survive.

The exact checker verifies this distinction for indices 1 through 24.

## Scope

Pairing selectors changes the coefficient observable and refines the quotient.
It must not be presented as preservation of both prior quotient constructions.
Neither construction supplies a Betti relative-chain map or physical pairing.
