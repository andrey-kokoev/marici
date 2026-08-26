# Finite weighted-rigging theorem

Owner: `marici.Buzzard`

Source locator: `Exact weighted-rigging criterion` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

For a finite index type `Fin n`, real positive weights `w_i`, coefficients
`c_i`, and an input vector `x_i`, Lean defines

- weighted norm square `sum w_i x_i^2`;
- trace `sum c_i x_i`;
- weighted dual square `sum c_i^2 / w_i`.

Lean proves the exact finite weighted Cauchy--Schwarz bound

`trace(c,x)^2 ≤ dualSq(w,c) * normSq(w,x)`.

It then defines the extremizer `x_i = c_i / w_i` and proves both its trace and
weighted norm square equal the weighted dual square. Consequently the bound is
attained exactly. The dual quantity is therefore not merely a convenient
upper estimate; it is the sharp finite coefficient dictated by the selected
weights.

## Authority boundary

The theorem classifies a supplied weight family. It does not select one. In
particular, defining a graph norm using the desired trace would make the bound
tautological but would not provide source authority for that domain.

Real division makes the dual and extremizer definitions noncomputable in
Lean's executable sense. All propositions remain fully proved.

## Missing infinite interfaces

The source's full statement concerns uniform finite cutoffs and the infinite
series `sum |c_n|^2 / w_n`. Extending this increment faithfully requires:

- a positive infinite weight sequence;
- the weighted Hilbert-space completion;
- monotonicity of finite dual sums and their supremum;
- equivalence between bounded cutoff norms and summability of the dual series;
- extension and uniqueness of the trace on the completion;
- for the power model, the p-series theorem and fixed exponent conventions.

Only after those interfaces are fixed should Lean prove the threshold
`beta - 2*alpha > 1`. The finite theorem generalized cleanly; the infinite
criterion remains deliberately unclaimed.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/WeightedRigging.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/WeightedRigging.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/finite-weighted-rigging.md`
