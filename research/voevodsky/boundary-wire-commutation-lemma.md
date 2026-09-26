# Boundary-wire commutation for the restricted net rules

Status: conditional mathematical lemma, grounded in fresh inspection of `Net.replace` in `checkers/check_full_unary_query_port_graph.py`. This is not a machine-checked arbitrary-n confluence theorem.

## Hypotheses

A finite port-linear graph has one principal port per agent. An enabled rule removes precisely two agents joined at principal ports. Each rule is deterministic for its unordered typed principal pair. Its replacement uses fresh agents, and maps every external auxiliary boundary port exactly once to a replacement port; internal replacement edges are fixed. The mapping and new agent types depend only on the rule, not on outside agent names or scheduler history. We restrict this statement to the present templates in which boundary ports attach to fresh replacement ports (no boundary-to-boundary splicing). Two enabled redexes A and B are distinct.

## Residuals and commuting square

A and B have disjoint agents: sharing one would require that agent's single principal port to have two partners, unless the pairs were identical. Replacing A cannot remove either agent of B or change B's principal/principal wire. Thus B remains the same enabled typed pair. The symmetric statement holds after replacing B.

Consider each original wire by its endpoints. Wires wholly outside A and B remain unchanged. A wire internal to one pair is removed in either order. A boundary wire from one pair to untouched context acquires the replacement endpoint prescribed by that pair's interface map. A wire connecting an auxiliary port of A to an auxiliary port of B acquires *both* prescribed replacement endpoints, independently of order. Finally, each replacement's own internal edges are the same in either order. Name fresh agents by (redex identity, local slot); both results then have identical types and incidence. Actual sequential serial names differ, but this naming gives an explicit alpha-isomorphism. No forest or termination premise is needed for this local argument, although executable replacement may have additional domain restrictions.

## Executable mapping and remaining audit

`Net.replace` stores each external wire peer under the removed port name, creates replacement agents, and uses `exposed.get` to attach new connections. If the peer belongs to B, it remains until B executes; B then reads the updated peer. This implements the cross-boundary case above. `link` and final `audit` catch repeated or omitted live ports on successful runs, but the API does not explicitly prevalidate the hypotheses and can leave a partially mutated graph on assertion failure. The algorithm's self-loop and malformed-redex behavior is not covered here.

The remaining bridge is a template-by-template static audit: exactly the auxiliary boundary slots occur once, all new ports occur once, no outside-name-dependent action, and fresh allocation is globally collision-free. Existing fifteen-rule dynamic diamonds support but do not substitute for that audit. Given this bridge, deterministic pair rules yield local confluence modulo names; combining with a separately proved termination/invariant theorem would yield unique normal forms. Boolean semantic correctness remains separate.
