# The source-side Mackey norm is a degree-idempotent

Epistemic-graph event: 1357.

## Quasi-idempotence theorem

Let integral maps `S:C_G->C_H` and `T:C_H->C_G` satisfy

`S T=d I_H`.

Define the source-side norm operator `N=T S`.  Then

`N^2=d N`.

After inverting `d`, the normalized operator

`e=(1/d)N`

is an idempotent.  It projects onto `im(T)` along `ker(S)`: the norm identity
makes `T` injective and `S` surjective after localization, and the two
submodules split.

Integrally, `N` is only a degree-idempotent.  If the target is `d`-torsion
free, then `ker(N)=ker(S)`, but `im(N)=T(im(S))` may be a proper finite-index
submodule of `im(T)`.

## Bad-prime degeneration

Modulo a prime `p|d`, the relation becomes

`N^2=0`.

The norm can remain nonzero, producing a canonical square-zero operator
rather than a projector.  For the one-bit deck quotient,

`S=[1 1]`, `T=[1;1]`, `d=2`,

so

`N=[[1,1],[1,1]]`.

Over `F_2`, this matrix is nonzero and square-zero.  Its image equals its
one-dimensional kernel, the invariant trace line.

## Physical consequence

An integral physical Mackey object need not split its source chains even when
the norm equation holds.  Splitting is a localized conclusion; at degree
primes it is replaced by nilpotent structure.  For five-site branch degrees
`2^k`, every mod-two source-side norm is square-zero, although higher
filtration information may survive.

This theorem remains conditional on physical maps `S,T`; the formal deck
matrices do not construct their relative-chain analogues.
