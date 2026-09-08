# v27: two conductor states of the endpoint-relative source

**Next checkpoint:** [`rzk-coefficient-interface-v28.md`](rzk-coefficient-interface-v28.md)
encodes the endpoint pullback homotopy and checks its two conductor
cancellations with endpoint lines retained.

`rzk/38-endpoint-relative-source-fibre.rzk.md` completes task 1 of the full-Q
support plan without enumerating the 2,338 old source states again.

For an arbitrary old source basis `A`, source differential, and two endpoint
augmentations, it defines the enlarged basis

    old(A) + c_plus + c_minus

and the fibre differential. An old column retains its old differential and
acquires the two scaled conductor outputs; both new conductor columns have zero
differential.

A concrete endpoint test packet checks the required columns

    v_plus  -> c_plus,
    v_minus -> c_minus,

with every other old test state mapping to zero, proves square-zero on every
basis state, and extends this to arbitrary finite integral chains.

A fresh 71-file headless closure passed in 27.33 seconds. Evidence:
`results/38-endpoint-relative-source-fibre.typecheck.json`.

Scope: the complete old basis is represented parametrically. This establishes
the fibre construction and the two genuinely new states, but does not claim to
have replayed the complete 2,338-state differential. The explicit endpoint-map
homotopy after pullback is the next task.
