# The Celestial Hodge Structure Is the Source-Derived Parity Bridge

## Question

Does the operation represented by multiplication by \(i\) exist only after
complexifying the finite Laurent census, or is it already a real constructor
of the radiative source?

## Real source construction

Let \(C_{AB}\) be a real symmetric trace-free tensor on an oriented
Riemannian celestial two-manifold. Define

\[
(JC)_{AB}=\epsilon_A{}^C C_{CB}.
\]

In two dimensions the right side is again symmetric and trace-free. Moreover,

\[
J^2=-1,
\qquad
\langle JC,JC\rangle=\langle C,C\rangle.
\]

In an oriented orthonormal frame write

\[
C=\begin{pmatrix}a&b\\b&-a\end{pmatrix}.
\]

Then \(J(a+ib)=i(a+ib)\). On the conjugate helicity coordinate it acts by
\(-i\). Hence its sheet matrix is exactly

\[
J_{\rm sheet}=\operatorname{diag}(i,-i),
\]

and in the electric/magnetic parity basis it is \(iX_{E/M}\), the missing
bridge isolated in Entry 3775.

## Why this is not scalar extension

The helicity coordinate is complex, but the underlying tensor and the Hodge
operation are real. The previously used real-coefficient Laurent slice keeps
only one coordinate chart inside this real rank-two fiber; its failure to be
closed under multiplication by \(i\) is a failure of that census slice, not a
failure of the physical radiative source.

The celestial orientation is essential. An orientation-reversing reflection
anticommutes with \(J\), which is exactly why the bridge mixes electric and
magnetic parity. If orientation is deleted, no canonical sign of \(J\) remains.

Because the Levi-Civita tensor is parallel,

\[
\nabla(JC)=J(\nabla C).
\]

Thus \(J\) commutes with the covariant derivative fold and preserves the
corresponding smooth, support, and Sobolev domains. This certifies the bridge
on the radiative tensor bundle without claiming an electric-magnetic duality
of the full nonlinear Einstein system.

## Claim boundary

The source algebra now contains the missing mixed parity generator. What it
still does not contain is an executable instrument that selectively applies
that generator. A bundle automorphism proves source authority and
constructibility of the state transformation; it does not by itself prove
laboratory or asymptotic-control capability.

This supersedes the scalar-extension-only interpretation in Entry 3778 while
retaining its exact sheet-matrix calculation.

## Disposition

The algebraic bridge is closed at the radiative-source level. The active
frontier moves from existence of the generator to authority for selective
execution of the Hodge rotation.

## Verification

```powershell
python research/strominger/checkers/celestial_hodge_bridge_checks.py
```
