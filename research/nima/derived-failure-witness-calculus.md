# Failure Payloads Are Derived Exactness Defects

Entry 2054 replaced three exclusive failure types by simultaneous signature
coordinates.  Strominger Entry 2058 supplies the missing payload for the
presentation coordinate: a primitive row cocircuit.  The three coordinates
now admit one algebraic description.

For a selected presentation matrix \(M_I\), a support complex
\(C_2\xrightarrow{d_2}C_1\xrightarrow{d_1}C_0\), and a full transport map
\(T\), the witness objects are

\[
\begin{aligned}
W_{\rm presentation}&=\ker(M_I^T),\\
W_{\rm support}&=\ker(d_1)/\operatorname{im}(d_2),\\
W_{\rm degeneration}&=\ker(T).
\end{aligned}
\]

They are respectively:

- a left exactness defect among chosen observations;
- middle homology of the coherence/incidence complex;
- a right exactness defect in transported source states.

The Boolean flags of Entry 2054 merely record whether these witness objects
vanish.  The actual pre-Carrier datum is witness-valued:

\[
\sigma=(W_{\rm presentation},W_{\rm support},W_{\rm degeneration}).
\]

A minimal exact packet realizes all three.  A full rank-two plane in three
rows has a singular preferred two-row chart with one left cocircuit, while an
alternate chart remains invertible.  A chordless \(C_4\) has one middle
homology class.  A rank-one specialization of the full transport has one
right-kernel residue.  Invertible row and domain basis changes preserve the
corresponding witness dimensions.

Software translation:

- left kernel: redundant or functionally dependent query fields;
- middle homology: an unfilled schema/path-consistency cycle;
- right kernel: distinct source inputs erased by the operation.

The Deutsch–Popperian conjecture is that recurrent Marici failures are typed
by homology of a source-derived presentation/support/transport diagram.  A
failure payload that cannot be realized as an exactness defect of that frozen
diagram is the finite falsifier and demands a richer diagram.

The exact checker passes 7/7 gates.

Artifacts:

- `research/nima/derived-failure-witness-calculus.md`
- `research/nima/checkers/check_derived_failure_witnesses.py`
- `research/nima/results/derived-failure-witnesses.json`

Sequence claim: `seqclaim-c4a4c8dc9fe4d5c43c331081`.
