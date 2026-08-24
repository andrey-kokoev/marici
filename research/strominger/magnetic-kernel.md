# The magnetic kernel is closed, but not always rational-exact

Companion to `checkers/magnetic_kernel_checks.py` (24/24, exit 0) and
`results/magnetic_kernel.json`. This is a finite-cutoff theorem about the
fold engine. It does not identify a source class or physical gauge mode.

## Question and type boundary

For the folded output pair \((f,\bar f)\), the magnetic readout is

\[
M=\partial_{\bar z}f-\partial_z\bar f.
\]

Thus \(M=0\) is exactly the closedness condition for the one-form
\(\omega=f\,dz+\bar f\,d\bar z\). The handoff hypothesis proposed that
magnetic-zero data are pure gauge, meaning \(\omega=d\Phi\). The computation
separates two meanings that must not be conflated:

- local elementary exactness, allowing logarithms;
- rational exactness, requiring \(\Phi\in\mathbb Q(z,\bar z)\).

The declared datum space is the 27-dimensional Laurent-monomial grid

\[
V=\operatorname{span}_{\mathbb Q}\{z^{-a}\bar z^m:
a\in\{0,2,4\},\ -4\le m\le4\},
\]

at grades \(g=2,3\). All ranks and kernels are exact over \(\mathbb Q\).

## Kernel theorem on the finite grid

The magnetic maps have

\[
\operatorname{rank}M_2=24,\quad \dim\ker M_2=3,
\qquad
\operatorname{rank}M_3=25,\quad \dim\ker M_3=2.
\]

Explicit bases are

\[
\ker M_2=\operatorname{span}\left\{
\bar z^{-1},\ 1-\bar z^{-2},\ z^{-2}\bar z^{-3}\right\},
\]

\[
\ker M_3=\operatorname{span}\left\{
\bar z^{-2},\ z^{-2}\bar z^{-4}\right\}.
\]

Every listed line has a symbolically verified local elementary potential.
The familiar sporadic datum \(\bar z^{-2}\) is magnetic-zero only at
\(g=3\) among \(g=1,2,3,4\), while its electric readout remains nonzero at
all four grades. The accident is therefore a one-grade kernel crossing, not
a dead fold output.

## Rational exactness and the residue obstruction

Three kernel generators have rational potentials:

\[
\Phi_{2,\bar z^{-1}}=-\frac{20}{1+u},\qquad
\Phi_{2,1-\bar z^{-2}}=-\frac{20(z+\bar z)}{1+u},\qquad
\Phi_{3,\bar z^{-2}}=-\frac{60}{(1+u)^2}.
\]

The remaining line at each grade is closed but not rational-exact. For
\(z^{-2}\bar z^{-3}\) at \(g=2\), the \(z\)-component has residues
\((-60,+60)\) at \(z=0,-1/\bar z\). For
\(z^{-2}\bar z^{-4}\) at \(g=3\), they are
\((-1008,+1008)\). Nonzero residues forbid a rational primitive; the
verified elementary potentials contain logarithms.

Therefore

\[
\boxed{M=0\iff\omega\text{ is closed}\Longrightarrow
\omega\text{ is locally elementary-exact},}
\]

but rational pure gauge is a proper subspace:

\[
\dim\ker_{\mathrm{rat}}M_2=2<3,\qquad
\dim\ker_{\mathrm{rat}}M_3=1<2.
\]

The original rational-pure-gauge formulation is falsified on the declared
grid. Its local-exact version survives, and the residual classes are measured
by logarithmic residues.

## Scope and next discriminators

This is a finite-cutoff, engine-side result. It does not assert an all-grade
kernel law, identify de Rham cohomology on a specified global domain, choose a
preferred kernel representative, or establish source/physical gauge
equivalence. In Nima's terms, a source-to-engine descent map must be frozen
before asking which quotient line is populated. The repeating logarithmic
line \(z^{-2}\bar z^{-(g+1)}\) at \(g=2,3\) suggests an all-grade residue
class, but that pattern remains an unresolved observation.

Falsifiers and extensions:

- a missed kernel vector in the declared grid;
- failure of any displayed potential derivative;
- vanishing of a claimed nonzero residue;
- a grade \(g\ge4\) that breaks or enlarges the guessed logarithmic family;
- a source-derived descent map that retypes or removes these engine lines.

## Verification

`uv run --with sympy python -u research/strominger/checkers/magnetic_kernel_checks.py`
passes 24/24. Groups: SPOR (8), KER (4), EX (5), RAT (5), FAIL (2).
The result JSON records the finite-cutoff scope and exact verdict.

