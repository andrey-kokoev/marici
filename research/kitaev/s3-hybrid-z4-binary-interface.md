# Native hybrid Z4 magic reduces to CS only across a charged digit interface

Owner: `marici.Kitaev`

## Exact algebraic reduction

Under the digit map \(r=2a+d\),

\[
i^{br}=(-1)^{ab}i^{bd},
\]

so

\[
c=1:\ CZ(b,a)CS(b,d),\qquad
c=2:\ CZ(b,d),\qquad
c=3:\ CZ(b,a)CS^\dagger(b,d).
\]

The checker verifies all three matrices exactly. Thus the odd native hybrid
phase is the already identified CS species after exposing binary digits; it
does not create a new abstract magic species.

## Conditional resource comparison

Native CDFG uses 26 odd hybrid invocations and four shared conjunction
episodes. Applying the three-T CS reduction and seven-T Toffoli decomposition
gives

\[
26\cdot3+4\cdot14=134T
\]

before lens-switch cost. The complete binary route is \(217T\). Therefore the
hybrid route improves strictly exactly when the total interface cost is below
\(83T\)-equivalent units.

## Interface boundary

The digit identification is not a free stabilizer relabelling: native
ququart and binary two-qubit Pauli label groups are nonisomorphic. Combining
native Clifford \(F_4\) with binary-digit interactions requires a charged
code switch, a persistent hybrid interface, or direct native injection. A
naive full cycle uses four directional transitions per pointer, sixteen total.
No such interface or native factory is admitted.

## Falsifiers

- Failure of any exact digit decomposition.
- A Pauli-preserving free digit relabelling.
- A different admitted interface census.
- A verified direct native factory with independently derived cost.

## Artifacts

- Checker: `checkers/check_s3_hybrid_z4_binary_interface.py`
- Result: `results/s3-hybrid-z4-binary-interface.json`
- Result SHA256:
  `E099E93BD63F5C29822AFC73BED5FAC343FE4BB18749FB08E42CC055AB798FF9`
- Graph admission: `ev-000000003474-5399fa72-d0f6-43a2-81d7-b6694a317168`
- Ledger: entry 2512, `seqclaim-4d9690d93c8b4cca4fac2f4c`
