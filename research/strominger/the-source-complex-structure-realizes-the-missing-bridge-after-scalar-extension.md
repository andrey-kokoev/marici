# The Source Complex Structure Realizes the Missing Bridge after Scalar Extension

## Exact candidate

The folded sheet outputs are

\[
A=\partial_{\bar z}f,
\qquad
B=\partial_z\bar f.
\]

Under a source phase \(f\mapsto e^{i\theta}f\), conjugation forces

\[
A\mapsto e^{i\theta}A,
\qquad
B\mapsto e^{-i\theta}B.
\]

At \(\theta=\pi/2\), the sheet operation is

\[
J_{\mathrm{sheet}}=\operatorname{diag}(i,-i)=iZ_{\mathrm{sheet}}.
\]

It is projectively the selective gate. In the electric/magnetic parity basis,

\[
H J_{\mathrm{sheet}}H^{-1}=iX_{E/M}.
\]

Thus the ordinary source complex structure realizes exactly the mixed bridge
identified in Entry 3775. It is unitary, squares to \(-I\), and is odd under
sheet reflection.

## Coefficient and authority boundary

The established finite combinatorial source is integral or rational over a
real Laurent lattice. Multiplication by \(i\) leaves that source category. It
becomes an internal operation only after complexifying the coefficient module.

Scalar extension proves representability, not constructibility. A physical
implementation requires an authorized complex or electric-magnetic duality
structure on the source states themselves. Merely observing complex-valued
outputs does not supply that operation.

The result therefore has two exact scopes:

```text
complexified magnetic source
  bridge exists canonically as multiplication by i

original integral/rational physical source
  bridge is absent unless a duality rotation is independently derived
```

## Refined frontier

The missing interaction is no longer algebraically mysterious. It is the
physical realization of the source complex structure. The next source test is
whether the magnetic construction has a genuine duality rotation—preserving
its equations, domains, boundary conditions, and admissible state lattice—or
only a formal complexification used for calculation.

If the duality rotation is authorized, the selective-gate path and its forced
reflection-unlocked midpoint follow. If not, the bridge remains a virtual
operation of the complexified carrier.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/source_complex_structure_realizes_parity_bridge_checks.py
```
