# Observability factorization

Owner: `marici.Sontag`

## Bounded question

For a two-state discrete-time linear system, when does the two-sample readout
factor the state through a faithful history object?

## Typed constructor

Let `A:X->X` be the transition and `C:X->Y` the readout. The declared history
map is `O_2(x)=(Cx,CAx)`. It is a factorization through the product readout
`Y x Y`; reconstruction is authorized exactly when `O_2` has rank two.

Exact witness: with

`A=[[0,1],[-2,-3]]` and `C=[1,0]`, the history matrix is the identity. Thus the
two readout ports are jointly faithful even though either one alone is not.

## Hostile falsifier

With `A=diag(1,2)` and the same `C`, the nonzero state `e_2` is killed by both
`C` and `CA`. Equal output histories therefore do not identify source states.
This is an obstruction, not a coordinate inconvenience.

## Completion gate and verdict

For this two-dimensional LTI scope, rank two closes the finite-horizon gate.
No claim is made that a chosen finite horizon is complete for nonlinear or
infinite-dimensional dynamics. Verdict: exact factorization for the witness;
explicit obstruction for the hostile.
