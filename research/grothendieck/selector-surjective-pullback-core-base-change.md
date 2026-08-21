# Surjective selector pullback obeys exact normal-core base change

## Base-change theorem

Let `phi:G->H` be a surjective homomorphism of finite groups and let
`c:H->X` be a selector. Then

`Stab_G(c compose phi)=phi^-1(Stab_H(c))`.

Surjectivity is essential in replacing the quantifier over `phi(G)` by one
over all of `H`. Taking normal cores commutes with this preimage:

`Core_G(phi^-1(S))=phi^-1(Core_H(S))`.

Therefore the terminal selector kernel satisfies the exact base-change law

`K_(phi^*c)=phi^-1(K_c)`.

For the identity selector `delta_0` on `H`, this specializes to

`phi^*delta_0 = 1_(ker phi)`

and the pullback selector has terminal kernel `ker phi`. Thus quotient
pullback changes the selector and can introduce a nontrivial resonance sieve.

## Smallest strict arithmetic control

For `C4->C2`, the target `delta_0` has trivial terminal kernel and all power
indices. Its pullback is the indicator of `{0,2}`, has terminal kernel `C2`,
and retains exactly the odd indices. The exact checker verifies the spectrum
sizes `24` and `12` through index 24.

## Scope

This is coefficient pullback. It explains the variance obstruction but does
not supply a covariant Betti transfer, Gysin map, or physical chain
normalization.
