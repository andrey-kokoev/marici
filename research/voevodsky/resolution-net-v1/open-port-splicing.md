# Genuine arrival/rewrite interleaving, with no waiting agents

`OpenNet` is a separate extension of the closed tree-port prototype. Each missing level0 history is represented by a uniquely named typed external port (negative node ID), not by an Admission value or a new agent. The same layered-seed constructors surround these interfaces. Existing F/seed and F/step rewrites run unchanged, including before any evidence arrives.

`arrive(slot,ticket,evidence)` checks a pure level0 history with the required package, compiles it into a candidate subnet, and splices its principal port into the missing interface. The external input port disappears. Candidate admission must succeed before stores and receipts are published. Ticket/slot reuse and package mismatch are rejected. This is one new BOUNDARY operation, not an internal interaction rule; compiling incoming history costs its size.

Counts: zero new internal agent signatures, zero new local rewrite schemas, one new typed arrival operation. The admitted open tree has one result boundary plus its remaining input boundaries. Closed admission uses an empty boundary map and continues to pass unchanged tests.

Critical distinction: structural normality does NOT imply release. The entire skeleton can normalize with all input ports still open. Readback/released require BOTH no pending F and no missing inputs. A completed late pure-history insertion adds no F work. This is an observer condition, not yet an emitted consumable release token.

Fresh tests:40 exhaustive mixed-event paths over a two-slot fixture (112 states),200 randomized four-slot schedules, a normalize-before-any-arrival case, late insertion of nontrivial pure histories, and three atomic invalid-arrival controls. Four-slot runs have exactly7 structural rewrites and4 arrivals independent of schedule. Closed-net schedule/admission regressions were rerun and pass.

Reproduce: python research/voevodsky/resolution-net-v1/check_open_net.py. Result: results/open-net.json.

No claim yet of a universal open-net confluence theorem, a linear externally consumable release protocol, ticket authentication, or global single-use ownership across forks. Next derive arrival/rewrite critical diamonds (especially arrival next to F/seed), an open-context substitution simulation and availability invariant. Then compare online observations with the legacy join rather than inferring bisimulation from eventual equality.
