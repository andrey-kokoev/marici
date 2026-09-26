# Online legacy comparison: equal saturated availability, unequal immediate timing

The checker uses actual BarrierNet JOIN/HOLD reductions, with existing NEXT agents serving solely as external waiting interfaces that the harness replaces by READY when an input arrives. This does not model the upstream cleanup/GATE process and does not modify legacy source files.

Exhaustively explored the four-input fixtures modulo fresh identifiers and receipt ordering:

* legacy:57 reachable states,128 transitions;
* resolution:416 reachable states,1648 transitions.

For every reachable state, exhaust internal reductions to quiescence. Every resulting terminal internal state releases iff all four inputs arrived. Every missing input label remains admissible. Both systems induce the SAME32 arrival-labelled edges on the16 received-input subsets, with the same saturated release observation. The result covers states reached by interleaving arrivals and internal work, not just a single preferred schedule.

This proves a finite quiescent/tau-saturated availability correspondence. It is NOT automatically general weak bisimulation: the checker does not establish a branching-bisimulation relation on all intermediate states or compare consuming environments. Receipt histories are explicitly projected out for this comparison, not declared equal.

An explicit strong-timing counterexample is retained: normalize the new net before inputs arrive, accept three inputs, saturate the legacy prefix, then deliver the last input. The new observer is immediately released; the legacy still needs an internal READY/HOLD step. Thus strict immediate-readiness equality is false. This is expected from moving structural work before evidence arrival.

The experiment therefore supports an actual but bounded simplification: runtime JOIN/HOLD waiting states can be replaced by uniform resolution structure plus typed external evidence interfaces if clients observe quiescent availability, not exact release latency or linear READY-token consumption. It does NOT support fewer total states or a speed advantage; the new fixture admits more partial structural states.

Fresh command: python research/voevodsky/resolution-net-v1/check_online_legacy_observation.py. Result: results/online-legacy-observation.json.

Next connect the finite Python calculus more precisely to the Agda witness-bearing closure (including what open contexts add). Keep global ticket ownership/linear consumption as a separate open branch: the successful saturated observer comparison does not resolve it.
