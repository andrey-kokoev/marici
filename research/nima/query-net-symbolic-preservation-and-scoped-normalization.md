# Symbolic preservation and scoped normalization of the query net

## Domain

Finite disjoint unions of the constructor components in `four_cell_query_net.py`: an EB--FB principal pair, each auxiliary attached to one READ principal port and each READ auxiliary attached to a distinct named OUT. Source identities are disjoint; within each pair the family tags agree and normalized residues are opposite. Each source carries an arbitrary finite component vector over an exact additive scalar domain. The constructor currently uses two components and globally unique family/channel labels. Fresh allocation is monotone above all live node identifiers. No other graph composition or additional rule is admitted here.

## Written proof (not proof-assistant checked)

1. **Closure and linearity.** EB--FB replaces the principal pair by two separate VALUE agents at its two unchanged external boundary peers. Each inherits one, and only one, consumed source record. VALUE--READ replaces that pair by one ANSWER at the READ auxiliary's former peer. Every new port is wired once, every outside endpoint is preserved, and fresh nodes cannot alias live nodes. Reachable components are therefore a waiting pair, two independent waiting values, a mixture of one answer and one value, or two answers.
2. **Semantic preservation.** The denotation at each named OUT is its source record, found through its pending READ or its completed ANSWER. The first rule transfers the two records to their respective VALUEs without summing or exchanging them. The second transfers its one record to ANSWER. Thus each rule preserves every named component, source identity and pole record. Every fixed linear combination of these channel observations is also preserved; no choice of weights follows from that fact.
3. **Termination.** The nonnegative integer `2*(#EB+#FB)+#VALUE+#READ` decreases by exactly two in either rule. Initial rank for m constructor components is 6m, hence every reduction sequence has at most 3m steps.
4. **Commutation.** Distinct enabled pairs in these reachable components have disjoint agents and distinct external OUT/READ endpoints. Rules preserve the other pair's principal wire and payload. Executing both in either order gives the same graph under the bijection matching fresh nodes to rule-local output slots. This is a constructor-domain local diamond argument, not a theorem about arbitrary port graphs.
5. **Normal form.** Every incomplete constructor component has an enabled pair: its EB--FB, or a VALUE--READ. Therefore a terminal state has exactly two ANSWER--OUT pairs per original component. Termination and the local diamonds give uniqueness modulo fresh names, with the original channel records as answers. All maximal runs have exactly 3m steps.

The argument extends to arbitrary finite disjoint unions satisfying these premises; it does not cover connected contexts, added erasers/copiers, or arbitrary malformed graphs.

## Executable symbolic check

`check_four_cell_query_net_symbolic.py` assigns eight independent component symbols and two arbitrary residue symbols to the two-family constructor. It verifies 25 states modulo fresh names, 50 edges and 35 local diamonds, with one terminal signature. Each step preserves all channel records and decreases rank by two. This symbolic check is stronger than a single numerical payload witness but is not a machine-checked proof of the written general theorem.

## Remaining physical gap

The net transports supplied values faithfully; it does not derive them, establish nine-point history authority, compile rational arithmetic into a finite alphabet, prove full-superform sufficiency, or select physical contour weights. The next meaningful bridge is to define target-function-valued observations and specify which geometric operations correspond to admitted net rules, rather than merely increasing test counts.

Result: `research/nima/results/four-cell-query-net-symbolic.json`.
