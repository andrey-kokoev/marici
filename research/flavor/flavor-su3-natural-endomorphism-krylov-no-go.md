# \(SU(3)\)-natural endomorphism Krylov no-go: WP1083

## Question

Can the current WP1080 \(SU(3)\) source data derive WP1081's Krylov
evolution, cyclic seed, and retained history?

## Nima reply evidence

Nima event 10655 gives an exact current-source no-go.

On one irreducible \(SU(3)\) triplet, any linear endomorphism natural under
the admitted \(SU(3)\) symmetry commutes with the representation. By Schur's
lemma it is scalar:

\[
A=\lambda I.
\]

Its spectrum is \(\{\lambda,\lambda,\lambda\}\), not simple. For every seed
\(x\),

\[
\det[x,Ax,A^2x]
=
\det[x,\lambda x,\lambda^2x]
=
0.
\]

The triplet also has no \(SU(3)\)-invariant ray, so the admitted symmetry does
not select a cyclic seed. The bifundamental pairing and \(\epsilon_3\) do not
alter this without an additional vector, flag, or symmetry-breaking tensor.

## Conditional-witness boundary

WP1081's witness

\[
A=\operatorname{diag}(1,2,3),
\qquad
x=(1,1,1),
\]

works because it inserts precisely the missing data:

- an ordered eigenflag;
- a cyclic ray.

Those data are not derived from the currently admitted \(SU(3)\)-symmetric
source.

## Named missing source operation

An authorized \(SU(3)\)-breaking preparation consisting of:

1. a simple-spectrum endomorphism or ordered eigenflag;
2. a cyclic-ray preparation;
3. a nondestructive history dilation storing three composition grades.

Existing \(SU(6)\) branching, bifundamental pairing, \(\epsilon\) carriers,
and localization do not declare that operation or its authority.

## Classification

Current-source no-go. The H1a handoff is answered. A successor localization
packet may still derive the flag and ray in one source frame; this no-go does
not exclude that future construction.

Checker: `research/flavor/checkers/wp1083_su3_natural_endomorphism_krylov_no_go.py`

Result: `results/wp1083_su3_natural_endomorphism_krylov_no_go.json`
