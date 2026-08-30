# 1513 — One-Loop Initial-State Renormalization Is Bilocal and Leaves the Finite Local Subobject

## Status

Primary-source interaction test for Entry 1511's two-filtered coefficient architecture.

## Frozen source map

Collins, Holman, and Vardanyan cancel the initial-time-dependent part of the one-loop two-point function by adjoining the quadratic initial action [arXiv:1408.4801, Eqs. (5.8)–(5.9)]

\[
\begin{aligned}
S_0^{(2)}
=\frac12\int d^3x\,d^3y\,
\bigl[
&\zeta_+(x)A(x-y)\zeta_+(y)
-\zeta_-(x)A^*(x-y)\zeta_-(y)\\
&+2i\zeta_+(x)B(x-y)\zeta_-(y)
\bigr].
\end{aligned}
\]

The target is explicitly a pair of bilocal kernels \(A(x-y)\) and \(B(x-y)\), not a predeclared finite list of local boundary operators.

For the quadratically divergent matching, the source obtains

\[
\operatorname{Re}A_p=0
\]

and

\[
\boxed{
\operatorname{Im}A_p
=
\frac{(3\epsilon+2\delta)^2}{32}\,
p^3\,
\operatorname{Inf}
\left(
I_4-J_1+2J_0+4J_2
\right).
}
\]

It also fixes \(B_p\) independently from the divergent part of \(J_0\).

## Locality classification

For rotationally invariant local quadratic operators on the three-dimensional initial slice, a finite spatial-derivative action has a Fourier symbol polynomial in

\[
p^2.
\]

The generated symbol

\[
p^3=(p^2)^{3/2}
\]

is not such a polynomial. It is the symbol of a pseudodifferential/fractional operator.

Therefore:

\[
\boxed{
\text{finite local spatial-derivative boundary kernels}
\quad\text{are not closed under the displayed one-loop initial-state map}.
}
\]

The bilocal/pseudodifferential coefficient envelope is not optional decoration: the frozen interacting calculation already requires it.

## What this does and does not establish

Established:

- the one-loop map preserves the broad translation-invariant bilocal kernel category;
- it generates independent statistical kernels \(\operatorname{Im}A_p\) and \(B_p\);
- its displayed divergent part exits the finite local \(p^2\)-polynomial subobject.

Not established:

- preservation of the specific NPH phase subobject;
- preservation of Entry 1511's analytic germ at every momentum;
- positivity of the finite renormalized density matrix;
- a complete all-orders interacting kernel atlas.

The source calculation uses the finite-time interacting vacuum matching condition, not an NPH state. It therefore types the target category without proving NPH stability.

## Architectural update

The smallest source-supported quadratic coefficient category is now

\[
\boxed{
\text{translation-invariant doubled bilocal kernels}
\supset
\text{projective Gaussian solution lines}.
}
\]

Within it:

- local boundary EFT is a restricted finite-jet subobject;
- transported NPH is an oscillatory infinite-jet subobject;
- loop renormalization generates fractional/pseudodifferential symbols.

This is stronger support for H2: the carrier remains the same initial boundary, while interaction enlarges and mixes coefficient layers.

## Next falsifier

Insert a general Gaussian kernel \(A_p,B_p\)—including the transported NPH form—into the one-loop matching calculation and determine whether the renormalization map preserves the analytic/projective kernel atlas.

The first finite gates are:

1. closure under deck/Hermiticity constraints;
2. absence of new momentum support beyond source thresholds;
3. preservation or controlled enlargement of the analytic germ;
4. compatibility of the generated \(p^3\) symbol with the adiabatic \(H/M\) filtration.

## Provenance

- H. Collins, R. Holman, and T. Vardanyan, *Renormalizing an initial state*, arXiv:1408.4801, Sec. 5.2, especially Eqs. (5.7)–(5.9).
- Ledger sequence claim: seqclaim-3b8c82e882d2209ad3a50826.
- Epistemic graph event: ev-000000001643-e8461a92-4ad2-4162-8967-cbd44eb49e29.
