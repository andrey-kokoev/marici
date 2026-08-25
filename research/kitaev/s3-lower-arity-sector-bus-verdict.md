# Lower-arity sector-bus verdict for finite `D(S3)`

Owner: `marici.Kitaev`

Status: consolidated exact conditional compiler and fault hierarchy.

## Verdict

The primitive five-body conditional Hamiltonian can be replaced by an exact
clean compiler using only one- and two-body gate contracts, without assuming
an eight-sector oracle.  Sector information is derived from flux and
centralizer charge:

\[
Z_e=S_3,\qquad Z_t=\mathbb Z_2,\qquad Z_c=\mathbb Z_3.
\]

The centralizer Fourier modes derive `A` through `H` before the target residues
are assigned.  A six-state holonomy bus plus an eight-state sector bus
implements each controlled power in 45 serial gates, with four-edge data
support, maximum primitive arity two, and exact cleanup.  All three powers
therefore cost 135 gates.

## Sharp information and locality bounds

- holonomy-only gauge-invariant phases have three signatures;
- a one-shot eight-phase clean label bus needs dimension at least eight;
- sequential compression needs three binary rounds, all charge-sensitive;
- all 40,320 three-bit labelings satisfy that obstruction;
- every exact labeler must touch all four edges;
- a clean flux-bus architecture starts at nine gates before charge overhead.

## Fault hierarchy

Lower arity alone does not improve arbitrary single-fault spread.  An
unverified shared bus revisits all four edges, so the worst-case data weight
remains four and arbitrary recovery requires distance nine.

A verified four-rail cat reduces the accepted control-fanout component to
weight one but does not protect shared bus faults; the global bound is
unchanged.

For arbitrary coherent bus errors, quantum Singleton requires at least five
rails per distance-three logical bus.  Encoding both buses therefore uses ten
rails.  If every logical bus--data gate is one-fault-transversal and correction
is interleaved after all twenty bus--data interactions per controlled power,
bus-induced spread falls conditionally to one.  The existing relative-
coordinate gate still spreads to weight two, leaving a conditional distance-
five data-code requirement.

## Remaining typing

The exact unencoded compiler uses finite reversible and Fourier gate contracts
but still requires device timing/calibration.  The distance-five improvement
is more conditional: fault-transversal encoded `S3` multiplication,
Fourier/Hadamard/transporter gates, explicit syndrome extraction/recovery, and
fresh verified ancillas for twenty correction cycles are not yet compiled.

Thus the lower-arity ideal compiler is established; a complete executable
fault-tolerant compiler is not.

## Verification

Run:

```text
python research/kitaev/checkers/check_s3_lower_arity_sector_bus_audit.py
```

The checker digest-binds six result packets, verifies 40 component gates, the
45-gate-per-power compiler, exact cleanup, all bounds, and the conditional
distance reduction.  Saved output:
`research/kitaev/results/s3-lower-arity-sector-bus-audit.json`.

Post phase: excitement `9/10`, because the five-body postulate became a
source-structured centralizer-Fourier circuit while the fault boundary grew
sharper rather than disappearing; confidence `8/10` in the finite conditional
compiler and `7/10` in the encoded-bus architecture pending logical-gate
synthesis; realized information gain `10/10`.  Confounds are ideal exact
Fourier/reversible gates and the uncompiled error-correction schedule.  These
process observations are not evidence.

