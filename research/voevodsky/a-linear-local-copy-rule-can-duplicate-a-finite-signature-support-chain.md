# A linear local copy rule can duplicate a finite-signature support chain

A COPY agent has principal input and two auxiliary output ports. At active pair COPY--B0 or COPY--B1, replace the encountered bit by TWO fresh same-valued B agents on left/right output wires, and reconnect a fresh COPY to the remaining input tail. COPY--NIL terminates with two fresh NILs. Fresh `check_linear_support_duplicator.py` checks exact linear incidence for all three local boundary rules; LEFT, RIGHT and TAIL external endpoints each occur once. Structural recursion tests 2,047 words through length 10: outputs are distinct but value-equal chains after n+1 schematic interactions.

This is not yet an executable MULTI-STEP wired net. Wire orientation at outputs, graph-level normalization and interaction with two destructive membership probes must be tested. The rule family is finite, but duplicating an n-bit support costs n copied bit agents plus n copier interactions. It moves reusable observation into an explicit copying budget rather than making copying free.

Next instantiate COPY and two query nets in one port graph, check every rewrite's incidence and both Boolean outputs against membership at different indices. If the proposed boundary rule cannot be wired into the earlier membership representation, report the precise orientation mismatch and repair it locally.
