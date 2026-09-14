# v116: soft D1 coefficient-localization decision

`rzk/144-soft-d1-coefficient-localization-decision.rzk.md` turns the cutoff-12
Smith profile into an explicit coefficient decision table.

Because the completed saturation index has prime support `{2,3,7}`, localization
at 42 (or rational coefficients) saturates the completed image at this cutoff.
Inverting only 2, 6, 14, or 21 is insufficient because each omits at least one
surviving torsion prime.

This does not authorize a coefficient change and is not an all-degree result.
For an integral amplitude, an actual saturation/derived torsion extension is
still preferred. The table only states the exact consequence of the verified
D12 Smith factors.

The Rzk module passes all nine declarations with no assumptions.
