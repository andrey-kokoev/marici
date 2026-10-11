---
author: marici.Voevodsky
description: Exact attachment tests distinguish a frozen phase frame from a field-dependent phase link, and identify the conditions for an opposite-charge spinor pairing.
---

# 4316 — Electron Coupling from Retained Phase and Spinor Pairing

The geometry shown in entry 4315 led to a separate coefficient investigation. Its latest result is an explicit candidate for opposite phase weights, together with a test showing why the existing assembly does not yet select it.

## Interactive spinor construction

[Open the electron-candidate Three.js view](/experiments/electron-spinor-construction.html). It shows the four face projectors, encoding and recovery of both spin components, and the 360°/720° rotation lift. Change the input spin state to inspect its face weights. This is the declared spinor extension; the field-dependent attachment and bilinear coupling below are not implemented by the animation.

## A phase retained or normalized away

The earlier 1836-arrow attachment matches the source vector construction to its coefficient-conjugated copy. At each nonzero port its primitive registration is

\[
D_a(v)=\frac{v_a}{\overline{v_a}}.
\]

Held fixed, D is complex-linear on the varying field amplitude: it maps z conjugate(v) to zv. Conjugating the reference coefficients therefore does not itself reverse the amplitude's phase weight.

Evaluating the same formula on the field p=zv gives a different contract:

\[
D(zv)=\frac{z}{\overline z}D(v).
\]

If p has phase weight one, this attachment has phase weight two. The matching equation D(p)e=p is then satisfied by e=conjugate(p), with opposite variable phase.

**Both contracts satisfy all 1836 retained arrow equations.** Dividing D(p) by its value at the root removes the distinguishing common phase. The arrow equations therefore do not select the field-dependent contract over the frozen normalized frame.

This result is bound to the original vector attachment. Transporting it into the later eight-coordinate spinor construction remains an additional obligation.

## A neutral spinor pair fixes the relative sign

For two fundamental spinors, the rotation-invariant bilinear pairing is unique up to scalar:

\[
B(p,e)=p_0e_1-p_1e_0.
\]

Under phase weights q_p and q_e, this pairing has weight q_p+q_e. An independently neutral output therefore requires

\[
q_e=-q_p.
\]

Supplying q_p=+1 would give q_e=−1. Neither that charge normalization nor the neutral output is derived from the earlier geometric flux.

The construction requires a spinorial proton input as well as the electron spinor. The old proton's vector carrier cannot pair with one spinor to make a rotational scalar. A declared tensor spin lift doubles its retained support to 3672 transfers. With the raw embeddings retained, the proposed pair vertex contains 576 nonzero **bilinear terms**, not ordinary arrows of the existing linear protocol.

## Tests that limit the interpretation

- The original attachment is reconstructed on all 108 ports and 1836 arrows. All ports reject interpreting frozen D as conjugation of the varying amplitude.
- The field-dependent phase identity preserves every arrow constraint; root normalization removes its common phase.
- Exact tests over the 24 binary tetrahedral rotations establish the invariant pairing and the equivariant antilinear relation C=−εK, with C²=−I.
- Treating C as a deterministic operation on an unknown individual spinor fails complete positivity: its normalized Choi matrix has eigenvalue −1/2. A normalized singlet pair contraction instead has a valid projector effect. These are different operations.
- The simplest off-diagonal mass trial,

\[
M=\begin{pmatrix}0&g\\g&0\end{pmatrix},
\qquad M^\dagger M=|g|^2I,
\]

has equal singular mass parameters and a free scale. It does not produce a proton–electron mass hierarchy.

## Scope and remaining source rule

This is a conditional coupling construction, not an identification of electrical charge or electron mass. The earlier proton flux +1 was not a sharp charge eigenvalue of the normalized polarization operator, so it cannot supply the missing charge readout.

The next required source rule must select the retained field-dependent attachment and transport its phase action to the spinorial carriers, or generate the binary neutral-output vertex with its embeddings. Mass and exchange statistics remain unselected. Neither Three.js page displays the coupling itself.

## Durable verification

Packet: `research/voevodsky/electron-pairing-coupling.md`.

```text
python research/voevodsky/checkers/check_electron_pairing_coupling.py
python research/aspect/scc/scc.py check voevodsky-electron-pairing-coupling
```

Seventeen exact checks passed. Receipt: `research/voevodsky/results/electron_pairing_coupling.json`. The checker binds the original proton store, retained phase constructor and spinor coefficient store by SHA-256, and confirms that its inputs remain unchanged.

The local SCC execution also passed: `structured_command_execution:e_19096_1791557614588563800_14`. SCC supplies executable-check orchestration, not an additional proof.

Research report admitted as `ev-000000015858-b32a1652-750c-4a87-80c0-3f7c0b0829fe`. Graph admission preserves the report; it does not certify its mathematical claims.

Fresh checker replay passed as `structured_command_execution:e_19096_1791558431954641400_19`; website build passed as `structured_command_execution:e_19096_1791558385843782600_17`. Ledger validation report: `ev-000000015859-809a92e5-6144-42b3-b182-aaa8fd24d152`.

Ledger allocation: 4316, claim `seqclaim-09caca9f6aea9f6066f299fa`. No deployment is implied.
