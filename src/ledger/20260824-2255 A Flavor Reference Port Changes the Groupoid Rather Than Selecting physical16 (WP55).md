---
author: marici.Figueiredo
sequence_claim: seqclaim-70b1c55bf8e6d78e3179dae9
---

# 2255 - A Flavor Reference Port Changes the Groupoid Rather Than Selecting physical16 (WP55)

For a left-handed generation-space reference ray (r), the relative readout
(O_r(H)=r^\dagger Hr) does not descend on the original full weak-basis
quotient if (r) is held fixed. An exact (3/5,4/5) rotation gives the values
(1) and (73/25) on two representatives of the same orbit.

Descent is restored only after enlarging states to pairs ((H,r)) and acting
simultaneously: ((H,r)\mapsto(QHQ^\dagger,Qr)). Fixing the reference then
reduces the allowed arrows to `Stab(r)`. This is a new relational experiment,
not recovery of an absolute phase or coordinate of the original flavor state.

The port therefore does not select a proper `physical16` subfamily and is not
a sparse presentation rigidifier. No declared flavor instrument independently
prepares or measures such a generation-space reference ray.

Artifacts:

- `research/flavor/flavor-relational-reference-port.md`
- `research/flavor/checkers/wp55_relational_reference_port.py`
- `research/flavor/results/wp55_relational_reference_port.json`
- updated `research/flavor/flavor-programme-index.md`

Verification: exact SymPy checker, 5/5 gates, exit 0. Epistemic admission
`ev-000000003125-685a09f7-d325-4cae-8635-c9ed3b309f47`.
