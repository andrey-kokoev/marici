# 3010 — The Frozen Downconversion Family Has Open NPT Synchronization Support

**Status:** source-derived finite theorem  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-bc0b58d42a519d1304abbf3c`

## Scope

Entry 3008 used a Bell projector to prove that negative-partial-transpose entanglement can synchronize the relative complex orientation of two optical ports. This entry replaces that isolated witness with the actual tunable downconversion family cited by the tomography source.

It treats the ideal pure polarization family. Experimental admixture, loss, and finite-bandwidth effects remain separate robustness questions.

## Frozen source family

White, James, Eberhard, and Kwiat derive the two-crystal source state

\[
|\psi(\varepsilon,\phi)\rangle
=
\frac{|HH\rangle+\varepsilon e^{i\phi}|VV\rangle}
{\sqrt{1+\varepsilon^2}},
\qquad
\varepsilon=\tan\chi,
\]

where the pump-polarization angle \(\chi\) controls the degree of entanglement and a pump quarter-wave plate controls \(\phi\). The same source independently authorizes polarization analysis at any point of the Poincaré sphere.

Primary provenance: A. G. White, D. F. V. James, P. H. Eberhard, and P. G. Kwiat, “Non-maximally entangled states: production, characterization and utilization,” arXiv:quant-ph/9908081, especially the source construction and state formula around its equation (1).

## Exact partial-transpose spectrum

Let

\[
\rho(\varepsilon,\phi)
=
|\psi(\varepsilon,phi)\rangle
\langle\psi(\varepsilon,phi)|.
\]

The eigenvalues of the second partial transpose are

\[
\operatorname{spec}\rho^{T_2}
=
\left{
\frac{1}{1+\varepsilon^2},
\frac{\varepsilon^2}{1+\varepsilon^2},
\frac{|\varepsilon|}{1+\varepsilon^2},
-\frac{|\varepsilon|}{1+\varepsilon^2}
\right\}.
\]

The negative eigenvalue is independent of the phase \(\phi\). The negativity is

\[
\mathcal N
=
\frac{|\varepsilon|}{1+\varepsilon^2}
=
\frac{|\sin 2\chi|}{2}.
\]

Therefore the source is NPT for every finite nonzero \(\varepsilon\), equivalently for

\[
0<\chi<\frac\pi2
\]

in the physical pump interval. Only the endpoint product states fail to synchronize orientation by positivity.

## Sewing consequence

The source family supplies an open, connected NPT region. On that region, one-sided reversal of the circular orientation maps the reconstructed state to a nonpositive operator. Hence the two local orientation torsors are synchronized throughout the entangled family.

Because every one of the sixteen tomography settings measures the same prepared state family, this NPT support is not confined to a special analyzer chart. The full source-authorized measurement tree can test the synchronized orientation.

The residual diagonal \(C_2\) acts by simultaneous complex conjugation on source and analyzers and remains a global presentation reversal.

## Relation to the Flavor hostile

Flavor supplies an alternating cubic carrier to distinguish orientation after bilinear alignment. The optical family uses a different sector-specific lens: positivity of an entangled composite rejects one-sided conjugation. Both instantiate the same typed distinction:

\[
\text{alignment data}
\neq
\text{orientation witness}.
\]

The witness is alternating in Flavor and positivity-supported in optics.

## Narrow conclusion

Relative complex orientation is not fixed by local tomography alone, but the frozen two-crystal source supplies an open physical region where entangled positivity fixes it. The mechanism is source-derived, robust across the ideal entangled parameter interval, and disappears exactly on the product-state boundary.

## Next falsifier

Add the source-reported small \(|HV\rangle\), \(|VH\rangle\), and mixed components. Compute the exact or certified NPT threshold under the admitted noise model. Determine whether orientation synchronization persists throughout the experimentally realized family or develops a positive-partial-transpose gap near the product endpoints.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-bc0b58d42a519d1304abbf3c`, value 3010.
- Primary source: arXiv:quant-ph/9908081.
- Exact spectrum: two positive Schmidt weights and the pair \(\pm|\varepsilon|/(1+\varepsilon^2)\).
- Boundary: synchronization vanishes only at the product endpoints in the ideal source family.
- Epistemic-graph admission: `ev-000000005759-4fb028b7-dc0f-4645-8c14-0dc7c1640e58`.
