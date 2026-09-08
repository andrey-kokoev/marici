# v28: endpoint pullback homotopy

**Next checkpoint:** [`rzk-coefficient-interface-v29.md`](rzk-coefficient-interface-v29.md)
constructs and checks the reduced seven-state cellular Q complex over the six
independent long variables.

`rzk/39-endpoint-pullback-homotopy.rzk.md` encodes the explicit homotopy used
after pulling the endpoint maps to the relative source.

On the endpoint/conductor packet it defines

    P(v_plus)  = -z tensor ell_plus,
    P(c_plus)  = conductor-unit tensor ell_plus,
    P(v_minus) = -z tensor ell_minus,
    P(c_minus) = conductor-unit tensor ell_minus,

and zero on the other test source state. The line-valued target differential
is induced from the checked relative fibre differential.

Rzk first strengthens the previous scalar observation to the setoid equation
`d_F z = conductor-unit`. It then checks both endpoint sign equations: the
conductor component of `d(-z)` cancels the new value `P(c_sigma)`, while the
opposite endpoint contributes coefficient zero. The two formal endpoint lines
remain separate throughout.

A fresh 74-file headless closure passed in 30.80 seconds. Evidence:

- `results/39-endpoint-pullback-homotopy.typecheck.json`
- `results/endpoint-pullback-homotopy-generation.json`

Scope: the explicit P data and endpoint/conductor cancellation are internal.
The remaining incoming-flag columns of `dP+Pd=m_partial p` still rely on the
certificate-backed sparse comparison; the complete 2,340-column replay is not
claimed. The reduced seven-state Q complex is the next task.
