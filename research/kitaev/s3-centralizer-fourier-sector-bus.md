# Centralizer-Fourier compiler for the coherent sector bus

Owner: `marici.Kitaev`

Status: exact conditional one-/two-body compiler; arbitrary bus faults remain
four-edge spreading without verification.

## Sector information derived before phase fitting

For flux representative `g`, charge is an irrep of its centralizer:

\[
Z_e=S_3,\qquad Z_t=\mathbb Z_2,\qquad Z_c=\mathbb Z_3.
\]

Their irreps give exactly

\[
(A,B,C),\qquad(D,E),\qquad(F,G,H).
\]

This label census is derived before assigning the target residues.  It is not
an eight-sector oracle inserted by its desired answer.

Write an `S3` centralizer coordinate as `c^k s^epsilon`.  A three-point
Fourier transform in `k` gives modes `m=0,1,2`.  On `m=0`, a parity Hadamard
in `epsilon` produces the trivial and sign charges `A,B`.  The four nonzero
mode states form the two copies of the standard charge `C`.  For a
transposition flux, one Hadamard gives `D,E`; for a three-cycle flux, one
three-point Fourier transform gives `F,G,H`.

The exact dimension check is

\[
1^2+1^2+2^2=6,\quad1^2+1^2=2,\quad1^2+1^2+1^2=3,
\]

and the resulting anyon dimensions square to `36=|S3|^2`.

## Clean two-body architecture

Use the existing six-state holonomy bus and a new eight-state sector-label
bus.  After holonomy computation, isolate the gauge coordinate, align the
holonomy to its fixed class representative, and apply the appropriate
centralizer Fourier gates.  Copy flux class from the holonomy bus to the label
bus, then refine it by copying the charge mode from the coordinate edge.  Both
copies are two-body updates of the label bus.  Reverse the Fourier, alignment,
coordinate, and holonomy computations; the data are restored while the label
bus retains the sector.

The forward extractor has 22 gates:

\[
4+1+1+4+1+1+4+1+1+4=22.
\]

Apply one record-controlled label phase and reverse the 22-gate extractor.
Thus each of controlled `U,U^2,U^4` has 45 serial gates.  Maximum primitive
arity is two, data support remains four, both workspace buses return exactly
clean, and the record qubit is retained.

The conditional contracts are reversible relative-coordinate and
transporter gates, class-conditioned `F3/H`, and two-body label updates.  They
refine already admitted group multiplication, `C3` Fourier, parity, and record
interfaces; their hardware timing remains conditional.

## Fault boundary

Lowering primitive arity does not by itself lower the arbitrary-fault light
cone.  A shared bus revisits all four edges.  An arbitrary bus fault can
survive into later interactions and reach four data edges unless the fault
alphabet is restricted, the bus is verified between visits, or fresh buses
segment the circuit.  Hence the worst-case arbitrary correction requirement
remains distance nine at this stage.

This deliberately does not reuse the earlier nonspreading result for
group-multiplication faults as though it covered arbitrary coherent bus
faults.

## Verification and falsifiers

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_s3_centralizer_fourier_sector_bus.py
```

The checker derives the centralizer census, constructs the exact `S3` regular
left-action matrices and isotypic projectors, verifies the `F3/H` unitaries,
checks all 72 control--sector basis cases for phase and cleanup, and records
the 45-gate inventory.  Saved output:
`research/kitaev/results/s3-centralizer-fourier-sector-bus.json`.

Falsifiers are an incorrect centralizer/irrep census, failure of the `S3`
mode routing, a dirty workspace, a controlled-power mismatch, or a source
gate decomposition contradicting the inventory.  A verified lower-spread bus
would supersede only the fault disposition.
