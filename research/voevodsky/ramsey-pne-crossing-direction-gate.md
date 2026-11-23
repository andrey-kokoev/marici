# When to reopen the Ramsey–P/N/E crossing comparison

**Result.** On the aligned eight-state readings, fixing stay `R = A` and the double crossing `X² = AB` fixes a half-turn. Its only square roots within the square symmetry group are the two quarter-turns `AC` and `CA` (words in execution order). Both preserve the verified computation; the direction of one crossing is not identified. P/N/E can distinguish return through the arrival face from travel through the other internal face. No independent identification of either with a directed Ramsey event has been established.

**Admission test for new evidence.** Give a source rule on a Ramsey process that identifies a particular ordered event as one crossing *without using its endpoint probe bits to choose the event or its direction*. Supply the pre-event wiring and the map from the process states to the named wirings. From pre-event triple `000` (slot order 0, 4, 6), the predictions are:

- `001`: selects `X = AC`, hence `C = RX`.
- `100`: selects `X = CA`, hence `C = XR`.
- Otherwise: rejects both as interpretations of this event.

One event distinguishes the two existing global assignments; it does not by itself prove a common update mechanism. The presence of both endpoints in the census, a solver's discovery order, or a route labelled after seeing its endpoint is not evidence of this kind.

**Follow-up: direct center changes and excursions.** The [parent catalogue replay](../chatgpt/ramsey/ramsey38_transfer_frame_gate.json) counted 477,142 parent records, 594 eligible roots, and one root supporting the original frame. No novel eligible root supported both `A` and `B`. Thus there are not two distinct qualifying roots to serve as the ends of a direct transfer under this test. That count is about roots, not labelled wirings: it does not exclude leaving the frame and returning to the same root with a different labelling. For that, one needs a transport rule on the intervening states. The [seven-label test](../chatgpt/ramsey/ramsey_seventh_label_transport.py) is stationary, whereas the [graph-changing loop search](../chatgpt/ramsey/ramsey_frame_loop_search.py) transports a six-label comparison. Neither supplies the missing seven-label path. Even realizing both inverse traversals would establish possible moves, not select the traversal corresponding to a neutron crossing.

[Frame contract](../chatgpt/ramsey/ramsey38_frame_interface_freeze.md) · [Probe predictions](results/ramsey_cycle_probe_direction.json) · [Native crossing-face check](checkers/pne_cross_face_partition.mjs) · [Previous context ledger](../../src/ledger/20261122-4337%20One%20Eight-State%20Action%20and%20Two%20Witness%20Rules.md)
