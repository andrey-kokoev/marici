# Static Linear Port Refinement Cannot Both Add Information and Inherit Every Scalar Null

For a nonzero linear scalar readout `L: V -> k` and any linear refinement
port `M: V -> W`, the implication

\[
L(v)=0\Longrightarrow M(v)=0
\]

forces `M` to factor through `L`. Equivalently,

\[
\ker L\subseteq\ker M
\quad\Longrightarrow\quad
M=A\circ L
\]

for a unique linear map `A: k -> W`.

Thus a static linear refinement cannot both recover information erased by the
scalar theta readout and automatically darken at every scalar zero. This is
the general theorem behind the exact two-cell cancellation witness in ledger
3805.

The remaining RH-strength action cannot be another passive monitor or wall.
It must enter through an independently derived source restriction, a
transport-generated orbit of ports, a nonlinear conservation law, or a
higher comparison coherence acting on the source-admissible subobject.

Research packet:
`research/grothendieck/static-linear-port-refinement-cannot-both-add-information-and-inherit-every-scalar-null.md`.

Allocator claim: `seqclaim-b2d9a223df5bdc59a62dc6a4`.

Epistemic-graph event: `ev-000000008228-597f3e9d-a75a-412a-9070-42270248c29d`.
