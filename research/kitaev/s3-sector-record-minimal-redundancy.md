# Minimal single-bit protection for the eight-sector record

Owner: `marici.Kitaev`

Status: exact finite coding theorem for the final classical record; phase
acquisition and encoder faults remain outside the guarantee.

## Bounded question

How much record redundancy is minimally required to correct one arbitrary bit
flip after the three-bit `D(S3)` sector label has been acquired?

The raw residues `(0,1,2,3,6,7,4,5)` occupy every word of `F2^3`, so every
single-bit flip is another valid sector label.  Zero errors are detectable.

For a binary code of length `n`, size eight, and minimum distance at least
three, the radius-one Hamming balls are disjoint.  Hence

\[
8(1+n)\le 2^n.
\]

This fails for every `n <= 5`, while `n=6` is possible.  Take as generator
columns six of the seven nonzero vectors in `F2^3`, for example

\[
G=\begin{pmatrix}
1&0&0&1&1&0\\
0&1&0&1&0&1\\
0&0&1&0&1&1
\end{pmatrix}.
\]

Every nonzero message has codeword weight three or four, so the resulting
`[6,3,3]` punctured-simplex code contains eight words and corrects one
arbitrary record-bit flip.  Thus six final record bits are necessary and
sufficient.

## Instrument placement

After inverse `F8`, the ideal three-qubit register is a computational-basis
sector label.  A reversible linear encoder with three clean target bits can
map `|r>|000>` to `|r>|rG>`, after which the six encoded bits may be measured
or stored and decoded by nearest neighbor.  Equivalently, trusted classical
electronics may encode an already trustworthy three-bit measurement record.

This protects only faults occurring **after** the label supplied to the
encoder is correct.  A fault in controlled phase acquisition, inverse `F8`,
or the encoder itself may create a wrong codeword and is not repaired by the
distance-three claim.  Protecting acquisition needs repeated syndrome/phase
information or a fault-tolerant encoded instrument and remains open.

The result adds three final record bits and requires six message-to-record
XOR couplings for the displayed systematic implementation after retaining the
three input bits.  It does not add controlled powers of the `D(S3)` unitary.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_sector_record_redundancy.py
```

The checker enumerates all eight codewords, all 48 single-bit corruptions,
and every Hamming-bound length through six.  It verifies unique decoding and
deliberately confirms that all 24 raw three-bit flips mislabel.  Saved output:
`research/kitaev/results/s3-sector-record-redundancy.json`.

Falsifiers are a collision of radius-one balls, minimum distance below three,
a length-five size-eight distance-three code, or any claim that this final
record code repairs a fault before the correct label exists.

