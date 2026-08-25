# Encoded-bus interleaving bound

Owner: `marici.Kitaev`

Status: exact resource lower bound and conditional fault improvement;
fault-transversal logical bus gates remain uncompiled.

## Why repetition verification is insufficient

Classical repetition detects selected shift errors on an orthogonal sector
label, but an arbitrary coherent bus fault includes phase and mixed errors.
Correcting one arbitrary rail error requires a quantum code of distance three.
For one logical qudit the quantum Singleton bound gives

\[
n-1\ge2(3-1),\qquad n\ge5.
\]

Thus each coherent bus needs at least five physical rails.  A six-level
distance-three bus code exists abstractly by tensoring five-rail qubit and
qutrit distance-three codes on each `2 tensor 3` rail.  The eight-level label
bus admits the analogous five-rail prime-power qudit code.  The two logical
buses therefore require ten rails before syndrome ancillas.

## Interleaved schedule

The 45-gate compiler contains twenty bus--data interactions:

- eight holonomy compute/uncompute interactions;
- two transporter align/unalign interactions;
- eight class-conditioned Fourier interactions;
- two charge-label copy/un-copy interactions.

To prevent one bus fault from crossing into a second data subsystem, correct
the relevant encoded bus after every such interaction and before its next
data interaction.  This requires twenty intervening correction cycles per
controlled power.

Conditioned on fault-transversal logical interactions and nonpropagating
syndrome extraction, bus-induced spread falls to data weight one.  However,
the reversible relative-coordinate primitive already has a verified
weight-two fault path.  The combined gadget bound is therefore

\[
\max(1,2)=2,
\]

so arbitrary recovery needs distance at least five.  Encoded interleaving can
improve the earlier distance-nine requirement, but cannot reach distance
three without replacing the relative-coordinate gate.

## Remaining source blocker

This is a conditional architecture, not yet an executable fault-tolerant
compiler.  Missing gates are fault-transversal logical `S3` multiplication,
Fourier/Hadamard/transporter operations on the encoded buses, and explicit
syndrome extraction/recovery with fresh verified ancillas for twenty cycles.
The code-space existence theorem does not supply those logical gates.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_encoded_bus_interleaving.py
```

The checker verifies the Singleton rail bound, abstract code composition,
twenty-cycle schedule, and conditional weight/distance accounting.  Saved
output: `research/kitaev/results/s3-encoded-bus-interleaving.json`.

Falsifiers are an arbitrary-error-correcting four-rail bus, a missed
bus--data interaction, a one-fault-transversal implementation with a larger
light cone, or a replacement relative-coordinate gadget with a stronger
verified bound.

