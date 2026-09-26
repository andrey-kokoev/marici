# Finite cyclic observation is sufficient under a supplied positive-power bound

`agda/ObserverBoundedCyclic.agda` represents a power count at most N by Fin(suc N), including its bound proof. Its observation is ACTUAL transport in the period-(N+1) cover, not projection of the supplied count.

Checked results:

- The observed finite state equals the original bounded count, including equality of bound proofs.
- The bounded observation map is an equivalence with both roundtrips.
- Decoding the observed state reconstructs the actual interpreted comparison path.
- Distinct power counts denote distinct paths, as certified by integer-cover winding.
- Any distinct counts n,m are separated by the finite cyclic probe of period n+m+1.
- Agreement under every positive-period probe implies equality of these counts and their interpreted paths.

The quantifier distinction is essential: for each bounded domain (or pair), there is a sufficient finite observer. There is still no single fixed finite family sufficient for every unbounded positive-power comparison. No resource-cost, physical area, or universal computation theorem follows.

## Scope

The representation and recovery theorem concern canonical nonnegative powers, not arbitrary syntax trees, negative powers, or every possible loop without a normalization theorem. The bound is supplied mathematical data, not discovered by an unbounded search. The function-space agreement theorem is not an executable algorithm querying infinitely many probes.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-bounded-cyclic.log. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Establish semantic normalization of the existing signed comparison language, including cancellation and composition, against an integer winding representation. Prove path equalities rather than only equality of one observer's output, then determine how the bounded and separating results extend beyond canonical positive powers. Preserve the distinction between syntax, full path witnesses, and their finite observations.
