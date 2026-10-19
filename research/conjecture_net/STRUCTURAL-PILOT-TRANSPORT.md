# Same-witness transport: unitary return and Hamiltonian pilot

Contract: `contracts/structural-pilot-transport.v1.json`.

## Scope and source

Fix the actual Bool-factor source and label order `00,01,10,11`. Let P_L and P_R flip the first and second factors and put Q_j=(I-P_j)/2. Use **one** complex carrier C[Bool×Bool], one delta encoding, one pair of generators H_j=pi Q_j and the existing positive reversed-schedule return.

This is a concrete common witness for the two finite structural pilots, not a common physical carrier for every sector. The broader interface's implementation and physical interpretation remain open. Applicable coherence obligations are forward realization, attachment transport, route/coherencer compatibility, and retained readout descent.

The accepted operational export supplies the native operators, local dynamics, interval return, reconstruction/swap and fixed-source faithfulness. Its written `standard-spectral-correspondence.md` identifies the operational witness with this **same** standard-complex witness. That interpretation is not a kernel theorem about classical reals.

## Diagram

```text
Native Bool source + retained schedules
            |
            | delta encoding and source-linearized flips
            v
Operational completion spectral witness
            |
            | rho_C, rho on parameters [accepted written interpretation]
            v
C4 spectral witness, H_j=pi Q_j, U_j(t)
            |
            | r(q+i p)=(q,p); R(A+i B)=[[A,-B],[B,A]]
            v
R8 canonical Hamiltonian witness, E_H=(q^T H q+p^T H p)/2
```

The last square commutes on every state: `r(Mz)=R(M)r(z)`. No independently chosen Hamiltonian or endpoint-matching adapter appears at its bottom.

## General realification identities

Write M=A+iB and z=q+ip. Multiplying components gives

`r(Mz)=(Aq-Bp,Bq+Ap)=R(M)r(z)`.

The same block multiplication proves `R(MN)=R(M)R(N)` and `R(I)=I`. Conjugate transpose gives `R(M*)=R(M)^T`. Realification is injective and preserves the usual real squared norm.

Let J=[[0,I],[-I,0]]. Every R(M) commutes with J. If U is unitary, `R(U)^T R(U)=I`; hence `R(U)^T J R(U)=J`. Thus its action is both orthogonal and symplectic, without identifying a phase-space point with a probability distribution.

For the native real symmetric H, define

`E_H(q,p)=(q^T H q+p^T H p)/2`.

Its gradient is `(Hq,Hp)`, so Hamilton's convention `q'=partial E/partial p`, `p'=-partial E/partial q` gives

`x'=J grad E_H=(Hp,-Hq)=R(-iH)x`.

This is precisely the realification of `i z'=Hz`. The matrix A_H=R(-iH) obeys `A_H^T J+J A_H=0`. These coordinate identities are written general algebra; the checker tests the bilinear action/composition identities on a complete real matrix-unit basis and the native generators exactly. It does not call a finite sample a proof of all-time analysis.

## Scale and orientation

The older normalized-angle construction uses Q_L, Q_R and H0=Q_L+Q_R with dimensionless angle theta. The accepted spectral witness uses H_j=pi Q_j and parameter t. They agree only after **theta=pi t**. By the chain rule, `d/dt=pi d/dtheta`. On the diagonal, the t-generator is pi H0, not H0. Generator normalization must not be inferred from matching corner matrices alone.

For forward schedule r, let (a,b) be its reversed operations and v=P_R P_L e_s. The return is

- `gamma(t)=U_a(t)v` on [0,1];
- `gamma(t)=U_b(t-1)P_a v` on [1,2].

Realify these formulas without changing their sign or order. The resulting real path is driven by pi Q_a on (0,1) and pi Q_b on (1,2), with the corresponding quadratic Hamiltonians. The seam and endpoints agree by linear transport. This is **positive continuation in reversed operation order**, not literal inverse-phase time reversal. Neither presentation claims differentiability at the seam or one fixed autonomous generator for the full switched traversal.

Injectivity of r preserves distinct seam basis states and equality/inequality of the entire ordered path pair. Consequently reconstruction, schedule swap and fixed-source faithfulness survive this coordinate change. The broader programme's physical observer family is not thereby selected.

## Evidence and admission boundary

```sh
python research/conjecture_net/check_structural_pilot_transport.py
python research/conjecture_net/test_structural_pilot_transport.py
```

The checker validates the live operational export (including external/compiler pins), retained source hashes, contract scope, and exact coordinate algebra. Its newly produced result is a **transport audit**, not a new Agda closure, a kernel realification proof, a physical test, or an automatic ++ for either programme target. Existing fresh operational closure evidence is reused at its accepted mixed level.

Mathematical same-witness transport is specified here at written/exact-algebra level. A consumer requiring kernel transport must formalize these identities. Programme-level admission, the universal carrier embedding, physical time/energy, Born measurement and empirical calibration are not discharged by this document.
