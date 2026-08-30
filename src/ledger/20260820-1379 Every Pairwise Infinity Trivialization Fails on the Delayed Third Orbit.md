# 1379 — Every Pairwise Infinity Trivialization Fails on the Delayed Third Orbit

## Status

Verified modular pair-first elimination result at \((p,z)=(1019,13)\). Characteristic-zero torsor comparison remains open.

## Typing correction

Entry 1373 proposed seeking a row functional whose restrictions to all proper faces vanish.

Taken literally in the serialized boundary-row space, that condition is too strong: the three two-orbit faces cover every boundary row, so coordinatewise vanishing on every face would force the functional itself to vanish.

The correctly typed object is instead the incompatibility of the three affine torsors of pairwise boundary trivializations.

## Pair-first elimination

Freeze the representative triple

\[
(\mathcal O_1,\mathcal O_2,\mathcal O_3).
\]

For each weight \(k\in\{1,2,3\}\), order the complete boundary system so that the other two occurrence orbits are imposed first and the weight-\(k\) orbit is imposed last.

The first contradictory reduced row is then:

\[
\begin{array}{c|c|c|c}
\text{delayed weight}&\text{direction}&\text{sheet}&\text{level}\\
\hline
1&10&8&2\\
2&8&17&2\\
3&8&25&2.
\end{array}
\]

The sheet weights are

\[
\operatorname{wt}(8)=1,
\qquad
\operatorname{wt}(17)=2,
\qquad
\operatorname{wt}(25)=3.
\]

Hence in every ordering the first contradiction comes from the deliberately delayed third orbit.

Each emitted certificate is normalized and directly verified:

\[
\lambda A=0,
\qquad
\lambda r=1.
\]

## Narrow conclusion

\[
\boxed{
\text{any two occurrence orbits admit a trivialization, but adjoining the third destroys it.}
}
\]

No orbit is a privileged source of the obstruction. The modular class is therefore ternary in the torsor-gluing sense.

This is stronger and better typed than merely observing that the full triple system is inconsistent.

## Remaining noncanonicity

The first contradictory row depends on elimination ordering and is not itself an invariant class.

The invariant candidate is the obstruction to finding a common point in the three pairwise affine trivialization torsors, modulo changes of pairwise sections.

The next exact target is therefore a characteristic-zero comparison complex

\[
T_{12}\oplus T_{13}\oplus T_{23}
\longrightarrow
K
\longrightarrow
B_{123},
\]

with the pairwise section changes retained, followed by the cohomology class of the inhomogeneous triple boundary datum.

No quotient may be fitted from the displayed trigger rows.

## Artifacts

- `research/benincasa/results/five-site-asymmetric-pair-first-ternary-obstruction.json`
- `research/benincasa/results/five-site-asymmetric-kummer-resolved-ibp-pilot.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`

Allocator claim: `seqclaim-b12c86e560f15e082884f783`.
