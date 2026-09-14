# v175: divided transition removes an integral order-six class

The primitive divided transition `a^3+a^3b` is itself an integral target vector,
even though only its triple appears as the labelled s11 transition. Its effect
was computed in the true D16 relation-derived Smith presentation.

Before adjoining it, the full Bockstein lattice has nonunit factors
`2^21,6^9,12^4`. After adjoining the divided transition they are
`2^21,6^8,12^4`: the saturation index drops by six. By comparison, adjoining
the labelled triple drops the index only by two.

Thus the labelled transition represents the threefold multiple of a complete
order-six torsion direction: it removes the 2-primary part, while the primitive
divided cell removes both its 2- and 3-primary parts and pairs with the local log
generator by a unit.

This supplies a concrete integral alternative to inverting 3. The remaining
geometric question is whether the primitive logarithmic nearby-cycle cell
authorizes adjoining `a^3+a^3b` rather than only its labelled triple.

Evidence is the refreshed `results/L2-bockstein-relation-smith-D16.json`.
`rzk/203-l2-divided-transition-integral-effect-d16.rzk.md` passes all eight
declarations without assumptions.
