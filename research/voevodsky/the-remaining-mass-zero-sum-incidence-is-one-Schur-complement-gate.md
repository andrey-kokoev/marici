# The remaining mass–zero-sum incidence is one Schur-complement gate

For a finite packet, choose one anchor mass vector \(e_0\) and a basis \(Z\) of coefficient-zero-sum differences. In this basis the Weil Gram matrix has block form

\[
\widetilde G=
\begin{pmatrix}
a&b^*\\
b&C
\end{pmatrix}.
\]

Here:

- \(C=Z^*GZ\) is the primitive-increment or mesh-charge block;
- \(a=G(e_0,e_0)\) is the base mass observation;
- \(b=Z^*Ge_0\) is the mass/zero-sum incidence reading.

The exact positivity criterion is

\[
C\succeq0,
\qquad
b\in\operatorname{Ran}C,
\qquad
\boxed{a-b^*C^\dagger b\geq0.}
\]

Thus, conditional on positive realization of the mesh-charge block, the entire remaining finite-rank gate is one scalar Schur complement.

This is the precise rung-four square between:

1. the endpoint/archimedean mass channel;
2. the primitive-increment coherence plane.

Positivity of the two diagonal objects is insufficient. The cross-incidence vector must satisfy

\[
b^*C^\dagger b\leq a.
\]

An exact rank-three hostile has positive zero-sum block and positive mass scalar but Schur margin \(-1/15\), demonstrating that this final inequality is independent.

## Source interpretation

The arithmetic programme should now avoid treating full Gram ranks as unrelated objects. At every finite packet:

- the discrete mixed derivatives assemble \(C\);
- endpoint and gamma balancing determine \(a\);
- the coupled source formula determines \(b\);
- RH requires the source-prescribed \(b\) to lie in the \(C\)-energy ball of radius \(\sqrt a\).

Equivalently, define

\[
\|b\|_{C^\dagger}^2=b^*C^\dagger b.
\]

The remaining inequality is

\[
\boxed{\|b\|_{C^\dagger}\leq\sqrt a.}
\]

This is the exact finite mass/zero-sum incidence law. Uniform source control under packet enlargement and completion would establish the universal rung-four Schwarz gate.

The zero-sum block is not yet globally proved positive from the arithmetic source; its identification with positive kinematic mesh charges remains a comparison obligation. The present reduction is conditional on that block positivity.

## Verification

```text
python research/voevodsky/checkers/check_mass_zero_sum_Schur_gate.py
```

Artifacts:

- `research/voevodsky/checkers/check_mass_zero_sum_Schur_gate.py`
- `research/voevodsky/results/mass_zero_sum_Schur_gate.json`
