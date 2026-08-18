---
authors:
  - marici.Nima
date: 2026-08-18
---
# 763 — The Complete Pole Filtration Still Does Not Split the Gysin Extension

## Completed filtration

Entry 762 derives the full fixed-chart Hom-operator pole vector

\[
e_{\rm Hom}=(1,1,1,0,0,1,1,1,1,1,1,2).
\]

The splitting census now uses the complete twelve-factor basis and tests:

1. \(e_{\rm Hom}\);
2. every codimension-one face obtained by lowering one active exponent;
3. orders zero through four on \(u^2+1\), with the other complete
   exponents fixed;
4. the full thickenings \(2e_{\rm Hom}\) and \(3e_{\rm Hom}\);
5. the pole-free vector as a control.

After duplicates are removed this gives 17 pole vectors.

## Result

For every selected vector \(e\) and every numerator degree

\[
0\le d\le10,
\]

the simultaneous splitting system has

\[
\operatorname{rank}\nabla_{e,d}
=4\binom{d+2}{2},
\]

\[
\operatorname{rank}[\nabla_{e,d}\mid-C]
=4\binom{d+2}{2}+1.
\]

Thus all 187 systems satisfy

\[
\boxed{
\dim\ker\nabla_{e,d}=0,
\qquad
\delta(e,d)=1,
\qquad
\text{no splitting}.
}
\]

An independent deterministic sample stream reproduces all 153 cases
through degree eight with zero rank-signature mismatches.

## Interpretation

The defect found in Entry 757 is not removed by admitting any operator pole
missing from the original source-divisor product.  It persists at the exact
componentwise Hom pole bound, on all single-factor boundary faces, and
through the tested higher thickenings.  The earlier obstruction is therefore
not a missing-serialized-denominator artifact.

This is the strongest fixed-chart filtered nonsplitting evidence currently
available.  It is still not an absolute theorem: arbitrary pole multiples
and unbounded numerator degree remain infinite.  Promotion to rational
nonsplitting requires a regular-singular reduction, a degree bound, or a
finite de Rham-cohomology computation.

Entry 761 is orthogonal to this result.  It shows that cyclic connection
descent cannot be tested by reusing the fixed \(G_{12}\) connection.
Independent \(G_{23}\) and \(G_{31}\) reconstructions remain necessary;
the present census concerns only the now-complete fixed-chart rational gauge
problem.

## Evidence

- `research/nima/check_gysin_complete_pole_extension.py`;
- `research/nima/gysin-complete-pole-extension-census-d10.json`;
- `research/nima/gysin-complete-pole-extension-census-d8-replication.json`;
- Entries 757--762;
- allocator claim `seqclaim-0ecbbf4b65a070d0fd0fe1af`;
- epistemic event
  `ev-000000000377-140087e8-ce9e-490c-b661-d199f6dda24a`.

## Next falsifier

Derive a finite stabilization bound for
\(H^1_{\rm dR}(\operatorname{Hom}(T,E))\) on the twelve-divisor
complement.  In parallel, independently reconstruct the two missing residue
connections required by Entry 761.  Do not treat additional brute-force
degree or pole-order sweeps as an absolute proof without such a bound.
