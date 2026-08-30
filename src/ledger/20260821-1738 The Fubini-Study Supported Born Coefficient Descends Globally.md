# 1738 — The Fubini-Study Supported Born Coefficient Descends Globally

## Projective-loop test

For a nonzero measurement tangent \(v\) and state direction \(\psi\), define

\[
c([v],[\psi])
=\frac{|\langle v|\psi\rangle|^2}
{\langle v|v\rangle\langle\psi|\psi\rangle}.
\]

Equivalently,

\[
\boxed{c([v],[\psi])=\operatorname{Tr}(P_vP_\psi).}
\]

## Descent

Independent nonzero rescalings and central phases of \(v\) and \(\psi\) leave
their projectors fixed.  Hence \(c\) is a globally defined function on the
product of projective spaces.  An exact \(\mathbb Z_4\) phase-loop audit gives

\[
\operatorname{Hol}(c)=1.
\]

The unsquared overlap \(\langle v|\psi\rangle\) does not become a scalar; it is
a section of the relative amplitude line and may carry Berry or flat
holonomy.  Hermitian squaring is what makes the Born coefficient descend.

## Narrow result

Once the source supplies the projective tangent direction and the
Fubini–Study metric removes speed, the supported Born coefficient is globally
single-valued.  It requires no additional Berry trivialization, coherence
cell, or Cut carrier stratum.

At its zero locus the scalar remains defined, but the phase of the unsquared
overlap is undefined; Entry 1732's supported-local-system distinction still
applies there.

## Durable artifacts

- `research/benincasa/checkers/projective_supported_scalar_descent.rs`
- `research/benincasa/results/projective-supported-scalar-descent.json`
- `research/benincasa/projective-supported-scalar-descent.md`

## Next falsifier

Replace rank-one state and measurement projectors by higher-rank subspaces.
Test whether principal-angle invariants provide the complete globally
descending supported readout or whether nonabelian Berry data survives beyond
the density pair.
