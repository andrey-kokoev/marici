# Unary counter insertion has a linear local port rewrite

Specify an active pair ACC.p--BIT.p with external wires ACC.a--HEAD.p and BIT.a--NEXT.p. BIT0 replaces the pair by ACC2, reconnecting ACC2.a--HEAD.p and ACC2.p--NEXT.p. BIT1 replaces it by ACC2 plus fresh UNIT, reconnecting ACC2.a--UNIT.p, UNIT.a--HEAD.p, and ACC2.p--NEXT.p. Fresh `check_linear_unary_insertion_ports.py` checks both rules against NIL and UNIT heads: every pre/post port appears in exactly one wire, and each external HEAD/NEXT endpoint is used once. This supplies an explicit locally linear insertion rule with finite agent names.

The checker is a port-boundary rewrite test, not an end-to-end interaction-net evaluator. It lacks termination at END, query interaction with UNIT/NIL, disposal of consumed agents, and confluence analysis. In particular, reading the unary chain from outside the net is NOT a legitimate implementation of reusable threshold queries.

Next design a destructive threshold QUERY(k) with unary k representation, explicit UNIT/NIL principal interactions and a declared consumed-state contract; verify linearity. Reusability would require copying or persistent sharing, a separate construction.
