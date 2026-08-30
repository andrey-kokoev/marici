# 1517 — Pseudodifferential Boundary Counterterms Do Not by Themselves Violate Hadamard Admissibility

## Status

Typing correction and interacting admissibility result following Entries 1513 and 1515.

## Two independent tests

Entry 1513 establishes that the one-loop initial-state matching generates a boundary symbol

\[
p^3=(p^2)^{3/2},
\]

which is not a finite polynomial in spatial derivatives. This proves failure of the finite local boundary-operator subobject.

Entry 1515 imposes Hadamard admissibility through ultraviolet decay of the excitation coefficient and the short-distance singularity of the two-point function.

These tests have different types:

\[
\boxed{
\text{boundary-kernel polynomiality}
\neq
\text{Hadamard wavefront admissibility}.
}
\]

A pseudodifferential counterterm can be required to cancel a divergent representation of the interacting vacuum while the renormalized state retains Hadamard singularity structure.

## Source evidence

Collins–Holman–Vardanyan choose the quadratic kernels \(A_p,B_p\) precisely to remove unwanted finite-time divergent and oscillatory contributions and match the interacting vacuum calculation. The generated \(p^3\) term is part of that matching counterterm packet; it is not identified as a physical occupation tail \(\beta_p\).

Agarwal–Holman–Tolley–Lin separately impose:

\[
\beta_k=o(k^{-2})
\]

and subtract the Bunch–Davies contribution before estimating state-dependent ultraviolet integrals. They state that higher-dimension interaction divergences are absorbed by higher-dimensional counterterms in the usual EFT manner.

At the general perturbative-algebraic level, Hollands and Ruan characterize continuous interacting states by smooth truncated free-field \(n\)-point functions for \(n\neq2\), with a two-point function of Hadamard form. Thus perturbative interaction theory is built over the Hadamard state space rather than requiring polynomial boundary kernels.

## Narrow conclusion

\[
\boxed{
p^3\text{ establishes coefficient nonlocality, not non-Hadamardness.}
}
\]

The one-loop calculation is compatible with the architecture

\[
\text{Hadamard state}
+
\text{pseudodifferential renormalization kernel}.
\]

It does not, by itself, prove that the specific transported NPH state remains Hadamard after interacting matching. That stronger statement still requires the state-dependent subtraction and large-\(k\) audit.

## Correct acceptance test

To test interacting preservation, compute the **renormalized** state-dependent two-point difference

\[
\Delta G_{\rm ren}
=
G_{\rm state,ren}
-
G_{\rm reference,ren}.
\]

The relevant conditions are:

1. \(\Delta G_{\rm ren}\) is smooth at coincident bulk points, equivalently introduces no new Hadamard wavefront directions;
2. its common-slice occupation/Bogoliubov tail has the required ultraviolet decay;
3. backreaction and tadpole integrals remain finite and subdominant;
4. all growing \(p^3\) or higher symbols confined to counterterm representatives disappear from the physical state difference.

No conclusion may be drawn from the unrenormalized kernel symbol alone.

## Architectural consequence

The coefficient object has three non-equivalent structures:

- an action-kernel presentation;
- a renormalized state/two-point presentation;
- a microlocal admissibility filtration.

The comparison between the first two is a renormalization map, not equality. Hadamard admissibility lives naturally on the second.

This mirrors the recurring Marici warning:

\[
\text{presentation support}
\not\Rightarrow
\text{physical support}.
\]

## Next finite falsifier

Use the exact initial-state propagator formulas to express \(\Delta G_{\rm ren}\) in terms of \(A_p,B_p\), isolate the one-loop state-dependent correction, and determine its large-\(p\) wavefront/falloff after counterterm subtraction.

## Provenance

- H. Collins, R. Holman, and T. Vardanyan, arXiv:1408.4801, Sec. 5.2.
- N. Agarwal, R. Holman, A. J. Tolley, and J. Lin, arXiv:1212.1172, Sec. 4.
- S. Hollands and W. Ruan, *The State Space of Perturbative Quantum Field Theory in Curved Spacetimes*, arXiv:gr-qc/0108032.
- Ledger sequence claim: seqclaim-a037a19473ba99484fdf85f9.
- Epistemic graph event: ev-000000001650-a98922d5-4cff-492f-a9f6-3cf2dcb155e0.
