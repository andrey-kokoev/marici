# A finite-agent unary counter moves n-growth into net size

Use fixed agent names ACC, BIT0, BIT1, UNIT, NIL, QUERY. In a schematic local counter, ACC meeting BIT0 reconnects; meeting BIT1 appends one UNIT to a unary accumulator wire, so n consumed bits produce one UNIT per one-bit. A threshold k probe walks up to k UNITs. Fresh `check_finite_signature_unary_net.py` tests 106,496 word/threshold cases through n=12: exact count, n consume steps, at most n UNITs, and min(count,k) query traversals. Distinguishable count values 0..n are now represented by different NETWORK SIZES under a fixed finite agent-name vocabulary.

Important limit: the checker is an abstract port-chain skeleton. It has not implemented the insertion, query, and garbage reconnection as a complete linear principal-port interaction-net rewrite system. It therefore establishes a possible complexity allocation, not a finished interaction net or a Nima E/E_B model.

Next produce an exact linear port-incidence rule for ACC--BIT1 insertion, including the UNIT principal/auxiliary connections and consumed-agent cleanup. Check that each wire has exactly two endpoints, that no fan-out occurs, and that threshold queries can traverse UNITs without destroying a reusable state unless their destructive semantics are declared.
