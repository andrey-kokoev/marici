# Bounded control-primitive crosswalk

Owner: `marici.Sontag`

## Scope

This packet types only finite-dimensional discrete-time linear systems over an
exact coefficient field. It does not assert nonlinear, stochastic,
infinite-dimensional, continuous-time, or physical plant realization results.

| Primitive | Source object and ports | Constructor tree | Governing law | Completion/descent gate | Smallest hostile |
| --- | --- | --- | --- | --- | --- |
| Observability | state `X`; transition `A:X->X`; readout `C:X->Y` | `X --A^k--> X --C--> Y`, collected into a history map | indistinguishable states lie in the history kernel | finite horizon must be jointly faithful on `X` | nonzero `v` with `C A^k v=0` throughout the declared horizon |
| Feedback | plant state `X`, controller state `Z`, signal ports `U,Y` | ordered plant/controller substitution into one block transition | dimensions, causal order, and any algebraic-loop solve must agree | direct-feedthrough loop requires an invertible solve operator | singular loop with no or nonunique internal signal |
| Stability/storage | transition `A:X->X`; storage form `P`; supply/dissipation form `Q` | `x -> Ax -> V(Ax)-V(x)` | `A^T P A-P=-Q` | `P` coercive and `Q` strictly positive for asymptotic decay | semidefinite loss with a hidden marginal mode |

The common Marici shape is carrier, typed maps, jointly tested readouts, and a
descent or completion gate. The gates are not interchangeable: faithful
readout does not close an algebraic loop, and energy nonincrease does not make
a readout faithful.

Verdict boundary: this crosswalk is a source-typed comparison, not a theorem
that all three primitives factor through one universal constructor.
