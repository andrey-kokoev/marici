# v37: D03 Rees filling resonance compatibility

**Naturality update:** [`rzk-coefficient-interface-v38.md`](rzk-coefficient-interface-v38.md)
separates individual graded lift existence from the nonsplitting obstruction
to a family linear over the full alternating coefficient ring.

`rzk/47-d03-resonance-compatibility.rzk.md` records the chain-level consequence
of the exact two-generator annihilator reported for the primitive filling
variation `Omega03`.

The eight normal coordinates are ordered

    (t02,t04,t13,t15,t24,u03,u14,u25),

and `mu=t15*t24*u14*u25`. The formal primitives satisfy

    d Wu   = u03 Omega03,
    d Wmu  = mu Omega03.

Rzk constructs

    Theta03 = u03 Wmu - mu Wu,

checks `d Theta03=0`, and supplies an integral detector that vanishes on every
boundary but evaluates `Theta03` to one. Thus an asserted filler for this
secondary compatibility would imply `0_Z=1_Z` in the packet.

A fresh 71-file headless closure passed in 29.95 seconds. Evidence:
`results/47-d03-resonance-compatibility.typecheck.json`.

Scope: the module checks the universal chain algebra and keeps the two
annihilating primitives separate. The exact annihilator theorem, the explicit
21/15/30/45-term chains, endpoint-zero property of `Omega03`, and the complete
512-weight census remain supported by the incoming checker and certificate.
No physical admissibility or identification with the conductor comparison is
encoded.
