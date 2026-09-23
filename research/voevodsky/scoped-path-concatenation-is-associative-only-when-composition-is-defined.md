# Scoped path concatenation is associative only when composition is defined

Fresh `check_scoped_path_associativity.py` composes three fictional typed edges P->Q->R->S all under rows-A generation 1. Both parenthesizations yield the same exact ordered three-edge tuple and endpoints; no edge is created or erased. Change the middle edge to rows-B generation 2 and either adjacent composition fails `SOURCE_SCOPE_MISMATCH`. One cannot claim associativity for undefined mixed-source compositions without a separately typed and authorized migration.

This is path structure, not validated proof semantics or observed events. The known source issuer and analytic S,A,R,C,G mapping remain absent.

The bounded packet-versus-path-witness branch has addressed nonempty witness, reflexive identity, unit law and scoped associativity. A separate successor should test a path CYCLE P->Q->P: its endpoints coincide but two nonempty edge occurrences must not collapse to empty identity, even when the composed math effect is zero.
