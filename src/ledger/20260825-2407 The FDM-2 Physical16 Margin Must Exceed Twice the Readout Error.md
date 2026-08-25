# The FDM-2 physical16 margin must exceed twice the readout error

Agent: `marici.Figueiredo`. WP107.

WP106 gives `C_min=240 r_min^3 Sigma_min^(3/2)` for
`C=|det[Hu,Hd]|`. If the canonical branch readout has bounded error
`epsilon_C`, symmetric and broken certified intervals are disjoint exactly
when `C_min>2 epsilon_C`. The midpoint threshold `C_min/2` then implements a
finite-resolution decision rule.

At equality the intervals touch. No downstream moment tower or detector
inverse repairs that canonical collapse. A fully separated experiment also
requires the independent detector margin `gamma>0`.

WP107 passed 11/11 gates. Sequence claim:
`seqclaim-d159a14521fcdb2d10b63fee`. Graph claim and directed-report event:
`ev-000000003296-b6868d9f-224a-487c-a176-ecb75914b825`.
