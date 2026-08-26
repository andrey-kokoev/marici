# Realization and minimality factorization

Owner: `marici.Sontag`

## Bounded question

For finite-dimensional discrete-time SISO linear systems over the rationals,
what does equality of all external Markov parameters authorize about internal
state?

## Preregistered measurement

Pre-activation: excitement 8/10, confidence 9/10, expected information gain
7/10. The close match to the Marici source-identity gate motivates the test;
the classical finite-dimensional setting is a confound.

Open verdicts are exact minimal realization, factorization only after the
reachable/observable quotient, or obstruction to internal identification.
Required tests are exact Hankel rank, reachability and observability ranks,
Markov-parameter equality, a hidden-state witness, and internal spectral
posture.

## Exact minimal witness

Take `A=[1/2]`, `B=[1]`, `C=[1]`, and zero direct feedthrough. Its Markov
parameters are `h_k=2^-k`. The two-by-two Hankel matrix
`[[1,1/2],[1/2,1/4]]` has rank one. The realization has one reachable and one
observable state, so its dimension equals the Hankel rank. It is minimal.

The constructor tree is input through `B` to the state carrier, repeated
transition by `A`, then output through `C`. The governing coherence law is
`h_k=C A^k B`.

## Nonminimal transfer-equivalent hostile

Augment the state by `z+=2z` but leave that coordinate unactuated and
unobserved:

`A_aug=diag(1/2,2)`, `B_aug=(1,0)^T`, `C_aug=(1,0)`.

Every external Markov parameter remains `2^-k`, yet the nonzero hidden state
`e_2` produces zero output for all time and carries an unstable eigenvalue
two. Thus stable transfer behavior does not imply internal stability,
detectability, minimality, or state identity.

## Descent and coordinate gate

The reachable subspace and the observable quotient both retain only the first
coordinate. Their composite reachable/observable quotient is canonically
isomorphic to the one-state witness and reproduces every Markov parameter.
This quotient is the authorized external realization.

A similarity transformation of the augmented realization changes the
displayed matrices and can mix the hidden direction into both coordinates
while preserving all Markov parameters. Consequently, even a fixed state
dimension plus external behavior does not identify presentation coordinates.
Minimal realizations are unique only up to an admitted similarity, not by
literal matrix equality.

## Completion gate and verdict

For the declared finite-dimensional rational SISO scope, finite Hankel rank
plus reachability and observability closes the minimal-realization gate.
Equality of an arbitrarily long external record does not close the internal
identity gate for a nonminimal realization.

Verdict: exact factorization for the one-state witness; exact quotient
factorization for the augmented hostile; obstruction to promoting transfer
equivalence into internal-state identity or stability.

This packet does not assert nonlinear realization, robustness, stochastic
minimality, infinite-dimensional completion, or physical state selection.

## Immediate post-objective record

Post-activation: excitement 8/10, confidence 10/10, realized information gain
7/10. The clean separation is partly due to the deliberately minimal hostile.

Raw delta: the minimal branch and quotient branch survive; literal internal
identity and transfer-to-internal-stability promotions are eliminated. The
Hankel map, reachable inclusion, observable quotient, and similarity transport
are constructed. All exact checks pass. Nonlinear and infinite-dimensional
realization remain unresolved.
