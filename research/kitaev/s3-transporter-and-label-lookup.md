# Explicit transporter and sector-label lookup

Owner: `marici.Kitaev`

Status: exact logical actions derived; transporter and coherent lookup remain
nonstabilizer, while label-to-label copy is executable Clifford.

## Transporter

Write `S3` elements as `c^k s^e`.  Freeze representatives `e`, `s`, and `c`
for the identity, transposition, and three-cycle classes.  The checker derives
the unique chosen table

\[
t(e)=e,quad t(c)=e,quad t(c^2)=s,quad t(c^k s)=c^k,
\]

and verifies `t(h) h t(h)^-1` equals the representative for all six
holonomies.

The coherent alignment is the 36-state permutation

\[
|h,x\rangle\mapsto|h,t(h)x\rangle,
\]

with the explicit inverse using `t(h)^-1`.  It is unitary, but conjugation of
the eight product-Pauli generators does not remain in the hybrid product
Pauli group.  Thus it is not an executable Clifford operation on the frozen
qubit--qutrit encoding.

## Sector lookup and copy

The frozen residues are

```text
A 000   B 001   C 010   D 011
E 110   F 111   G 100   H 101
```

Once a residue exists in three logical qubits, copy to another label block by
three logical XOR/SUM gates.  The checker verifies copy and inverse cleanup on
all 64 source/target words.  Those SUM gates are supplied by verified
Clifford Choi teleportation.

The unavailable step is earlier: coherently computing the three displayed
predicates from flux class and centralizer-charge mode is controlled by the
eight central projectors.  The exact truth table does not make that
projector-controlled lookup a product-Clifford gate.

## Verification

Run:

```text
uv run --with numpy python research/kitaev/checkers/check_s3_transporter_and_label_lookup.py
```

Saved output:
`research/kitaev/results/s3-transporter-and-label-lookup.json`.
