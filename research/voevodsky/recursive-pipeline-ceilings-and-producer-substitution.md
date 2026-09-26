# Recursive pipeline ceilings and producer substitution

Critical-path reassessment: proving closure of causal stream interfaces still unlocks more than any new operation. Implemented `pipeline_stream_interfaces.py`, which traverses each control's principal and saved input through every data successor to NIL or an allowed producer frontier. All data along the path must respect that consumer's stage ceiling; budget and union literal paths have exact own-stage ownership and cannot wait. COPY input is strictly earlier-stage throughout. Same-stage waits remain restricted to membership Q/E at COPY. This is stronger than checking only the current head.

Fresh `check_pipeline_stream_interfaces.py` passes 858 program/schedule runs and 49,912 state occurrences. These are necessary interface checks, not complete graph coverage or universal closure.

## Head-removal closure lemma

For a stream satisfying a fixed consumer ceiling and permitted endpoint set, removing its first B/K exposes a suffix satisfying the SAME conditions: the validator quantified over the entire path. Rules that simply move the saved stream between phases preserve its ceiling when the new phase has the same stage. Q_B--K and Q_S--B exchange support/budget roles without changing stage; AB/AS do likewise. AR completion emits a same-stage B1 ahead of the saved suffix. This suffix argument discharges the specific gap left by head-only causality.

## Producer replacement, the remaining stronger obligation

A consumer can stop at a producer frontier and cannot check what lies behind it. When that producer fires, its result must satisfy every downstream ceiling previously admitting that frontier. If producer stage t < consumer stage s, newly emitted t-labelled data are allowed and a residual t-stage producer remains earlier. COPY may also have same-stage private Q/E clients, so its same-stage output is allowed; its own input still has a strictly lower ceiling.

UL--N is the important forwarding case: it replaces the producer with its literal right stream, all stage t and with no frontier. This is admitted by every later-stage client that formerly waited at UL.r. U_b--N emits a t-labelled bit and forwards its saved left suffix. A universal proof therefore needs the producer's saved suffix to have ceiling <=t and an endpoint set that remains legal for its downstream client; scalar stage inequalities alone do not express that endpoint compatibility. Insertion nil-extension produces a same-stage NIL, not a new same-stage waiting producer at its own input.

Next state an explicit producer-output contract for COPY.a/b and AB/AS/AR/UL/U0/U1.r, plus global coverage ensuring passive B prefixes also obey those contracts when no control currently traverses them. Then prove simultaneous preservation by constructor and local rules. This should be a single contract-substitution proof, not another indefinite cycle of enlarging bounded examples. Terminal RET and prior OUT components must be included, or the no-live-control case could still hide malformed residue.
