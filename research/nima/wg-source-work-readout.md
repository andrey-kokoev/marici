# Conserved witness flow selects the positive response cost

## Question

Can a declared interpretation of retained arrows distinguish the two energy signs found in the shared-reservoir comparison, rather than choosing the sign to obtain binding?

## Fixed-boundary interpretation

Use the same 1836 internal arrows, 108 equal reservoir links and uniform signed layer sources as `wg-reservoir-completion.md`. Interpret a real arrow coefficient f_e as conserved flow. Its boundary is Bf=J. Give the arrows positive conductances c_e, with unit internal conductances and reservoir conductance k in the tested fixtures.

The primal cost is

    min_f (1/2) sum_e f_e^2/c_e, subject to Bf=J.

Its Lagrangian is E(f)-x^T(Bf-J). Stationarity yields f=C B^T x and hence D x=J, where D=B C B^T. Substitution into the dual gives

    max_x J^T x - x^T D x/2,

with value J^T D^+ J/2 on neutral full-graph sources. This is the positive stored-field cost. The reservoir potentials are gauge-fixed to zero only after retaining their source-balance equations.

The earlier scalar-force model instead minimized x^T D x/2-J^T x and has the negative value. It is a different variational problem, not a second convention for the same fixed-boundary transport cost.

## Verification of the variational meaning

For an optimal flow f and any circulation z with Bz=0, the cross term is

    sum_e f_e z_e/c_e = x^T Bz = 0.

Consequently E(f+z)-E(f)=E(z), establishing minimality. The checker finds an actual three-arrow cycle in the source graph and verifies an excess 3/2 for unit circulation. All source equations, primal-dual equality and orientation reversal are checked exactly.

A quasistatic source ramp J(t)=tJ has x(t)=tx. Its supplied work integral is J^T x/2, agreeing with the positive cost. This parameter is a specified preparation path, not a derived physical time.

## Pair comparison

Using the same reservoir for both isolated sources and their opposite-sign pair, the transport-cost cross-term is negative. At k=1 it is -17/1831 in the declared units. This sign follows from the fixed-boundary variational principle, not from selecting the attractive answer after solving the response equation. No distance-dependent force is computed.

## Surviving scope and stopping condition

The bare WG record has no real conductance or current-conservation interpretation. Thus the calculation selects the readout conditional on a conserved-flow interpretation; it does not show that WG itself selects that interpretation.

Even preserving every arrow and every optimal flow leaves a scaling freedom: C -> 2C, x -> x/2, E -> E/2. Incidence, boundary, orientations and optimal witnesses are unchanged. A physical energy scale cannot be recovered from those invariants alone.

The first missing input is an owner-selected WG interpretation assigning conserved currents and their conductance/energy metric. Do not create further reservoir variants to infer that missing datum from a desired mass. This branch stops at that input unless a source-derived rule is supplied.

## Reproduction

```text
python research/nima/checkers/check_wg_source_work_readout.py
```

Execution: `structured_command_execution:e_32876_1791217163616642600_11`. Results: `results/wg-source-work-readout.json`. All arithmetic is exact rational arithmetic conditional on the explicit metric and source fixtures. No publication, commit or physical mass prediction is claimed.
