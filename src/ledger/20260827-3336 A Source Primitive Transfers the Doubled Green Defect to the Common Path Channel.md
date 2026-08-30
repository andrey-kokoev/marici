# A Source Primitive Transfers the Doubled Green Defect to the Common Path Channel

Provenance correction: the full complex primitive-current calculation already
appears in
`research/grothendieck/theta-primitive-seam-current-leaves-an-explicit-mixed-bulk-residual.md`.
This entry supplies its real specialization and the new interpretation that
the residual is exactly the endpoint-to-path lifting obstruction; it is not an
independent discovery of the mixed residual.

For the reciprocal doubled real flow

\[
u'=-zu-cf,
\qquad
v'=+zv-cf,
\]

direct differentiation gives

\[
2z(u^2+v^2)=-(u^2-v^2)'-2cf(u-v).
\]

Adjoining the canonical source primitive `h'=f` and the current
`J_p=2hc(u-v)` absorbs the forcing, but exactly leaves

\[
2z(u^2+v^2)
=-\bigl(u^2-v^2+J_p\bigr)'
-2zhc(u+v).
\]

Thus the primitive does not eliminate the defect; it transfers it from the
relative forcing channel to one common-path residual. If `u+v=0` pointwise,
the current closes and positive integrated bulk forces `z=0` under vanishing
endpoint flux. But scalar Evans nullity gives only a terminal common-mode
condition, not pathwise cancellation.

The Green-current programme and the earlier endpoint-to-path lifting problem
are therefore the same obstruction in two coordinate systems. The next gate
is an actual Fourier--Tate law that either forces pointwise common-mode
cancellation or supplies a further source current for `2zhc(u+v)`.

Research packet:
`research/grothendieck/a-source-primitive-transfers-the-doubled-green-defect-to-the-common-path-channel.md`

Exact checker:
`research/grothendieck/checkers/check_primitive_lift_common_path_residual.py`

The checker passes 7/7 exact tests.
