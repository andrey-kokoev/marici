# Finite surjections carry norm--resonance bidegrees

## Bidegree theorem

For a finite surjection `phi:G->H`, define

`d(phi)=|ker(phi)|`, `rho(phi)=R_G(ker(phi))`.

On coefficient functions, unnormalized pull--push is

`phi_! phi^* = d(phi) id`.

For composable surjections,

`d(psi phi)=d(phi)d(psi)`,

while Ledger 1301 gives

`rho(psi phi)=lcm(rho(phi),rho(psi))`.

Thus arrows carry a bidegree in the product monoid

`(positive integers,multiplication) x (squarefree integers,lcm)`.

The primes of `d(phi)` are always contained in those of `rho(phi)`, because
the primes dividing a finite kernel equal the primes dividing its exponent.
The difference consists of conjugation-resonance primes: they obstruct the
power--Mackey spectrum without making the pull--push scalar nonunit.

## Sharp A4 control

For `A4->C3`, the kernel is `V4`, so the norm degree is four. Conjugation on
`V4` has image `C3`, hence the resonance label is six. Prime two is both a
norm and resonance prime; prime three is resonance-only.

Composing with `C3->1` gives bidegrees

`(4,6)`, `(3,3)`, `(12,6)`.

The checker also evaluates a nonconstant coefficient vector and verifies
`q_!q^*=4 id` entrywise.

## Scope

The norm is the algebraic coefficient norm. A physical Betti pull--push
identity remains unavailable without the relative-chain transfer.
