# Compact real-form twist gate

## Question

Does a Cayley transform canonically turn the split source real form into the required compact contour on the fixed torus?

## Claim boundary

No. The transform

`z=(x-i)/(x+i)`

maps the extended real line to the unit circle, but sends the omitted source boundary points `x=0` and `x=infinity` to `z=-1` and `z=1`. It therefore identifies `P1` minus `{0,infinity}` with `P1` minus `{-1,1}`; it changes the marked boundary pair rather than preserving the fixed torus presentation.

Algebraic automorphisms of `G_m` have the form `x -> a x` or `a/x`, and none maps all of `R*` onto `S1`. Moreover, choosing `-i` instead of `i` replaces `z` by `z^-1` and reverses the circle orientation. No DNC, incidence, or physical boundary datum selects between these conjugate choices.

## Disposition

A Cayley transform gives a compact presentation only after changing the punctures and choosing quadratic orientation data. It is not a canonical contour constructor for the fixed exceptional torus. The next leaf states the minimal external boundary-condition contract needed to select a compact contour and period sign legitimately.

## Verification

- `research/voevodsky/check_cosmology_compact_real_form_twist_gate.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
