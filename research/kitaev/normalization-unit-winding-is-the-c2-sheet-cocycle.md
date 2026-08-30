# Normalization-Unit Winding Is the C2 Sheet Cocycle

Let \(\Omega\) be an annulus and let \(u\in\mathcal O(\Omega)^\times\) be a
holomorphic unit. Its winding around the hole is

\[
\nu(u)=\frac1{2\pi i}\oint\frac{u'(z)}{u(z)}\,dz\in\mathbb Z.
\]

Every unit has the form

\[
u(z)=z^{\nu(u)}e^{h(z)}
\]

after choosing the standard annular coordinate and a holomorphic \(h\).
Consequently:

\[
u\text{ has a global holomorphic logarithm}
\quad\Longleftrightarrow\quad
\nu(u)=0,
\]

and

\[
u\text{ has a global holomorphic square root}
\quad\Longleftrightarrow\quad
\nu(u)\equiv0\pmod2.
\]

The parity

\[
\chi(u)=\nu(u)\bmod2\in C_2
\]

is therefore the obstruction cocycle for splitting a scalar normalization
equally between two sheets.

## Composition law

Winding is additive:

\[
\nu(uv)=\nu(u)+\nu(v),
\qquad
\chi(uv)=\chi(u)+\chi(v)\pmod2.
\]

This is the required displacement cocycle. Reciprocal transport reverses the
integer winding,

\[
\nu(u^{-1})=-\nu(u),
\]

while preserving its parity class.

## Vacuum normalization comes second

All monomials \(u_n(z)=z^n\) satisfy \(u_n(1)=1\). Thus the preferred vacuum
value at \(z=1\) does not determine winding. For odd \(n\), no global
single-valued square root exists at all. For even \(n\), there are two square
roots differing by sign; the condition \(\sqrt{u}(1)=+1\) then selects one.

Hence the correct hierarchy is:

1. prove that the normalization is a holomorphic unit;
2. compute and trivialize its \(C_2\) winding obstruction;
3. use the vacuum value to choose the remaining sign.

A canonical local frame cannot remove a nontrivial global cocycle.

## Theta/Tate consequence

If the determinant-to-Tate normalization is defined on a punctured or
annular parameter domain, Grothendieck must compute its logarithmic-derivative
periods. Zero-freeness alone transports the zero divisor, but a two-sheet
factorization or globally oriented square-root section additionally requires
even winding on every fundamental loop. This is exactly where a Tate
\(\gamma\)-factor or source current could carry nontrivial displacement data.

This theorem does not assert that the actual theta/Tate domain is annular or
that its normalization has nonzero winding. It supplies the minimal audit if
the domain has nontrivial first homology.

## Falsifiers

- A base value \(u(z_0)=1\) is used to infer zero winding.
- Zero-freeness is used to infer a global logarithm on a multiply connected
  domain.
- A square-root sheet is introduced without checking winding parity.
- The vacuum sign is chosen before square-root existence is proved.
- Winding data are erased when composing normalization transports.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to identify the global residue left after the holomorphic-
unit theorem.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The residue is an integer winding, its parity is exactly the two-sheet
cocycle, and the tensor-unit/vacuum frame is correctly placed after the
topological obstruction gate.
