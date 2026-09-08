# v68: conductor costalk regulator continuation

Independent replay passed 554,284 counted exact checks.

`rzk/94-conductor-costalk-regulator-continuation.rzk.md` records the complete
occurrence-degree-zero costalk as a free `Lambda = Z[beta]` module:
`Lambda(-1) + Lambda(-2)^15 + Lambda(-3)^18`. Hence all 34 stable classes and
the rank-31 counit kernel survive after inverting `beta`.

The target primary and counit image have a different feature: three lower-grade
counit-image directions are killed by `beta`, although their supported source
classes are not. Three explicit chain-level transfers convert these into
nonzero zero-unit comparison classes. Stable invariant ranks are 11 for the
costalk, 10 for the zero-primary kernel, and one for the counit image.

The Rzk module passes a fresh check. Nonzero-regulator continuation therefore
preserves rather than selects the ambiguity: fixing the invariant primary still
leaves ten invariant zero-primary directions, including the relation-only
classes. A geometric source selector remains necessary.
