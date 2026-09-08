# v31: exact replay of the Q contraction identities

**Plan completed:** [`rzk-coefficient-interface-v32.md`](rzk-coefficient-interface-v32.md)
extracts the seven selected triangles and checks their exact three-term
corrected-roof boundary in Rzk.

Task 5 is regenerated from the exported sparse matrices by
`checkers/verify_full_q_contraction_certificate.py` rather than accepted from
certificate summary flags.

The verifier reads all of:

- 393 base-Q states;
- 872 base differential entries;
- 50 projection entries;
- 144 inclusion entries;
- 1,813 homotopy entries;
- the seven-state cellular differential.

It performs exact sparse polynomial matrix composition over the declared
18-variable coefficient ring. Products involving both positive- and
negative-sheet short occurrences are reduced to zero before comparison. No
numeric specialization or parameter sampling is used.

The replay checks

    p_Q i_Q = 1,
    d h_Q + h_Q d = 1 - i_Q p_Q,
    p_Q d = d p_Q,
    d i_Q = i_Q d.

The independent replay passed. Evidence:
`results/full-q-contraction-replay.json`.

This checkpoint differs from the preceding Rzk modules: the 2,879 sparse map
entries and their polynomial compositions are replayed by the exact Python
checker, not re-emitted as a multi-megabyte Rzk term. The reduced seven- and
fourteen-state target differentials remain independently Rzk-checked in
modules 40 and 41. Consequently the contraction is admitted as externally
replayed evidence, not as a native Rzk identity proof.

The remaining task is to formalize the selected seven-triangle Morse primitive
inside the checked reduced target/interface.
