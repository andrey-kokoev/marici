# Explicit history encoding, decoding and retained-syndrome recovery

## Constructed interface

The history-code adapter now has an exact Clifford encoder/decoder and an
explicit syndrome-conditioned correction table, not just an abstract code
subspace. The code remains Kitaev's existing five-qubit component code.

The checker synthesizes a Clifford reduction from its four stabilizers and
derived logical-Z operator, tracks Pauli phases, and inverts the reduction.
A logical phase adjustment matches the owning derived logical-X convention.
Each component takes one history bit and four ready-zero data ancillas.
Five components encode the 22 history labels into 25 physical data qubits.

The stored circuit uses H, S, X, CNOT and SWAP. The emitted, unoptimized gate
lists have 31 encoder gates per component, 155 for all five components, and
255 decoder gates in the explicit inverse lists. These are circuit-description
counts, not measured work or a fault-tolerant resource estimate. Controlled
recovery operations are additional to those counts.

All amplitudes are calculated exactly in Q(sqrt(2),i). The checker verifies
stabilization, logical basis conventions, orthonormality, and encoder/decoder
inversion on all 32 component basis vectors.

## Physical-error interface and recovery controls

During encoded storage, assume at most one physical data-qubit error in the
linear span of I,X,Y,Z. This is an explicit noise interface, not a source-derived
microscopic bath or a calibrated error rate.

For each of the 16 component Pauli cases, decode the noisy logical zero and one.
The first four output bits contain a unique syndrome. The fifth carries the
logical state with a calculable Pauli byproduct. A complete table specifies
which logical X/Z correction to apply, coherently controlled by the retained
syndrome. The correction has the same residual scalar phase on both logical
basis states; that phase is retained in the syndrome amplitude.

Thus arbitrary logical superpositions are recovered without erasing the noise
record. Linearity extends the result to arbitrary channels in the declared
single-qubit error span. Five-block tensoring preserves every one of the 22
history amplitudes. The table and gate lists are saved in the result receipt.

There are now twenty physical syndrome bits after decoding the full history.
They cannot silently be treated as ready-zero ancillas for another encoding.
Fresh ancillas or a separately accounted reset/transfer operation are required.

## Boundaries retained

- This **bare decoding circuit** is tested with ideal encoding, decoding and
  correction controls. Faults during the decoder can propagate. It is not a
  replacement proof for the earlier verified-Shor fault-tolerant recovery gadget.
- The source-level phase flip on a logical history label still has zero syndrome.
  No gate compilation converts it into a single physical-qubit error.
- A generic finite-time coupling sum sigma_l tensor B_l can generate products
  of errors at multiple locations. Its whole evolution is not automatically in
  the single-event error class. Physical bath, correlation and timing assumptions
  remain to be supplied and tested.
- The modular-address controls used during seam filling are not yet compiled
  into protected encoded operations. Decode/control/re-encode would expose an
  unprotected interval unless separately qualified.
- Bond/battery energy stays unchanged by the abstract history isometry, but no
  physical work cost for these gates, ancillas or syndrome disposal is derived.

## Verification and next requirement

    python research/voevodsky/checkers/check_history_code_circuit.py

Fresh execution passed. Receipt: `results/history_code_circuit.json`, including
complete gate lists, all correction entries and source/preceding-receipt hashes.

The encoding/recovery interface is now executable in the declared gate model.
The remaining physical step is an actual admitted noise/control coupling with
which to test it, not another proof that this code corrects one idealized fault.
No particle mass, lifetime, isotope stability or autonomous storage claim follows.
