# The Veronese Symbol Bridge Does Not Intertwine the Two Quantum Towers

> **Superseded at tower level.** This audit correctly computes the Casimir of
> the within-grade Cartan action, but incorrectly compares it with the
> grade-changing metaplectic action. The full even-Veronese algebra carries a
> second `sl2` action with Casimir `-3/4`, as recorded in the correction below.
> The no-intertwiner statement survives only for the mismatched pair of
> actions explicitly described here.

## Representation-level audit

The theta and endpoint constructions share a classical conic, but they do
not carry the same quantization of it.

For theta, the oscillator operators

\[
E=\frac{Q^2}{2},\qquad F=-\frac{P^2}{2},\qquad
H=\frac{QP+PQ}{2}
\]

act on each parity sector of the polynomial oscillator module. With

\[
\Omega=H^2+2H+4FE,
\]

the central character is fixed:

\[
\Omega=-\frac34 I.
\]

For the endpoint tower, the grade-\(l\) piece is

\[
H_l\cong\operatorname{Sym}^{2l}\mathbb C^2.
\]

Using the standard action

\[
E=x\partial_y,\qquad F=y\partial_x,\qquad
H=x\partial_x-y\partial_y,
\]

the same Casimir convention gives

\[
\Omega=4l(l+1)I
\]

on \(H_l\). No endpoint grade therefore has the oscillator central
character.

## Consequence

The classical map is a moment-map or symbol correspondence:

```text
two-dimensional spinor -> null quadratic triple -> Veronese conic.
```

It is not an intertwiner between the theta oscillator module and an endpoint
grade. Equality of the conic relation only identifies their associated
commutative geometry. Quantization remembers additional data, and the
Casimir separates the two towers immediately.

The correct common object is therefore the `sl2` control algebra together
with two inequivalent module families:

- theta: infinite lowest-weight oscillator parity modules;
- endpoint: finite highest-weight modules of weights \(2l\).

Any cross-sector comparison must be a correspondence between these module
categories, a symbol/associated-graded functor, or a kernel carrying both
actions. It cannot be an ordinary nonzero `sl2` intertwiner between one
endpoint grade and the theta oscillator sector.

## What survives from the six-square compiler

The six primitive squares remain a valid test for arrows internal to one
chosen module family. They do not by themselves provide a bridge between the
two quantizations. A cross-family square must expose the Casimir discrepancy
as a boundary, filtration, or bimodule term.

This retypes the seam again. The seam is a plausible location for the missing
comparison datum because it was already omitted by the classical symbol
projection. But the Casimir mismatch does not prove that the existing theta
seam supplies it.

## Falsifier and next target

The obstruction is falsified by a source-derived nonzero map \(T_l\) from an
endpoint grade to an oscillator sector satisfying

\[
T_lE=ET_l,\qquad T_lF=FT_l,\qquad T_lH=HT_l.
\]

Such a map would also intertwine \(\Omega\), contradicting the displayed
central characters unless the declared actions or domains differ from the
ones audited here.

The constructive next target is not another rank comparison. It is an
explicit filtered kernel whose associated graded is the shared Veronese
conic and whose quantum defect equals

\[
4l(l+1)+\frac34.
\]

That defect must be derived from a boundary or relative channel rather than
subtracted by hand.
