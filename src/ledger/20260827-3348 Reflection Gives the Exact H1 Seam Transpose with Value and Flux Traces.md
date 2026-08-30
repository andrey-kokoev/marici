# Reflection Gives the Exact H1 Seam Transpose with Value and Flux Traces

For every finite seam length `L`, reflection

\[
(R_Lu)(q)=u(-q)
\]

is unitary from `H1(0,L)` to `H1(-L,0)`. It exchanges endpoint values,
reverses coordinate derivatives, and preserves outward-normal flux at the
corresponding endpoints. For the real-even theta forcing, its dual action
intertwines the canonical rigged transpose exactly.

The reflected intervals concatenate contravariantly in reverse order, with
matching interface values and fluxes. This supplies the continuum seam return
incidence that could not be inferred from the nondense arithmetic packet.

Provenance correction: the archimedean endpoint/gamma incidence was already
matched in
`research/grothendieck/archimedean-Poisson-reciprocity-closes-without-RH-force.md`.
Together with that earlier theorem, transpose compatibility is now established
on primitive, square, connected-tail, seam, and archimedean boundary grades.
The remaining gate is bulk dynamical realization, not another boundary grade.

Research packet:
`research/grothendieck/reflection-gives-the-exact-h1-seam-transpose-with-value-and-flux-traces.md`

Exact checker:
`research/grothendieck/checkers/check_reflected_h1_seam_transpose.py`

The checker passes 8/8 exact tests.
