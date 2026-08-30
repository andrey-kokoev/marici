# Iterated selector pullback has path-independent resonance

## Tower theorem

Let

`G --phi--> H --psi--> J`

be finite-group surjections and let `c` be a selector on `J`. Put

`N_phi=ker(phi)`, `N_psi=ker(psi)`, and let `K_c` be the selector's terminal
kernel. Repeated application of the preimage resonance theorem gives

`R_G(K_((psi phi)^*c))`

`=lcm(R_G(N_phi),R_H(N_psi),R_J(K_c))`.

Consequently

`U_G(K_((psi phi)^*c))`

`=U_G(N_phi) intersection U_H(N_psi) intersection U_J(K_c)`.

Associativity of lcm and intersection makes the result independent of whether
the selector is pulled back stepwise or along the composite. This is strict
coherence in the coefficient correspondence system.

## Strict cyclic tower

For `C12->C6->C2` and the identity selector on `C2`, the successive terminal
kernels have orders `1,3,6` and labels `1,3,6`. Through index 24 the spectra
have sizes `24,16,8`. Direct and stepwise selector pullback agree pointwise.

## Scope

The coherence is contravariant and coefficient-side. It does not construct
the covariant relative-chain maps needed for a physical Mackey object.
