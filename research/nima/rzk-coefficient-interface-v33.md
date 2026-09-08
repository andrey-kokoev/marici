# v33: Morse filling torsor and attachment rigidity

**Endpoint-normal update:** [`rzk-coefficient-interface-v34.md`](rzk-coefficient-interface-v34.md)
constructs the six branch-normal witnesses and proves that their full product
makes both primitive endpoint classes boundaries.

`rzk/43-morse-filling-attachment.rzk.md` internalizes the most immediately
useful finite consequence of the new research.

A Q-filling variation is represented by

    (c03,c14,c25) in Z^3.

Rzk defines its two torsor coordinates

    (c03-c25, c14-c25)

and the complete five-row short-boundary attachment matrix

    (-c03+c14,
      c03-c25,
      c03-c25,
     -c03+c14,
     -c14+c25).

It proves that diagonal variations have zero torsor coordinates, that zero
coordinates force `c03=c14=c25`, and that the kernel conditions of the
attachment matrix force the same diagonal relation. Therefore fixing the full
lower attachment leaves only the already-null diagonal Q variation: the
filling homotopy class is unique in this ordinary model.

A fresh 73-file headless closure passed in 30.13 seconds. Evidence:
`results/43-morse-filling-attachment.typecheck.json`.

This gives an actionable test for any future conductor filling: its two
integer coordinates must vanish if it preserves the Morse lower attachment.
It does not assert that a physical conductor filling has been transported into
this torsor. The marked-normal Z/2 ambiguity belongs to a different fine degree
and is not collapsed into these two integers.
