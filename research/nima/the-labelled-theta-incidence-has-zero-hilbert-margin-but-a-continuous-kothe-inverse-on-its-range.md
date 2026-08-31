# The labelled theta incidence has zero Hilbert margin but a continuous Köthe inverse on its range

## Question

Does the prime/grade-diagonal theta-history synthesis retain a uniform lower bound at completion?

## Claim boundary

Not in the unweighted labelled Hilbert geometry: its exact coefficients tend to zero, so the minimum modulus vanishes and the range is not Hilbert closed. On the projective exponential Köthe source, however, the inverse on the source-generated labelled range is continuous with a finite exponential-order shift. These are compatible results in different topologies. Neither authorizes transporting Köthe invertibility into G4's declared Hilbert target norm.

## Exact diagonal coefficient

For \(\lambda=(p,k)\), put

\[
L_\lambda=k\log p,
\qquad
a_\lambda=\frac1k p^{-k/2}=\frac1k e^{-L_\lambda/2}.
\]

After normalizing the translated history atom in each labelled fiber, the synthesis singular value is proportional to \(|a_\lambda|\). Since

\[
|a_{p,k}|\longrightarrow0
\]

along either \(p\to\infty\) or \(k\to\infty\), the labelled Hilbert synthesis has

\[
\inf_{p,k}|a_{p,k}|=0.
\]

Therefore it is not bounded below on the infinite labelled Hilbert direct sum. Finite cutoff injectivity does not produce a uniform Hilbert frame margin.

## Projective exponential topology

Use seminorms

\[
q_\delta(c)=\sum_{p,k}|c_{p,k}|e^{\delta L_{p,k}},
\qquad \delta>0.
\]

Forward multiplication is continuous because \(|a_{p,k}|\le1\):

\[
q_\delta(ac)\le q_\delta(c).
\]

For the inverse on the labelled source-generated range,

\[
|a_{p,k}^{-1}|=k e^{L_{p,k}/2}.
\]

For every \(\varepsilon>0\), there is \(C_\varepsilon\) such that

\[
k\le C_\varepsilon e^{\varepsilon L_{p,k}},
\]

because \(L_{p,k}\ge k\log2\). Hence

\[
q_\delta(a^{-1}d)
\le C_\varepsilon
q_{\delta+1/2+\varepsilon}(d).
\]

Every shifted seminorm already belongs to the projective family. Thus diagonal coefficient multiplication is a continuous automorphism between the coefficient Köthe space and its labelled source-generated history range.

## Range and radical consequences

Every coefficient is nonzero, so the synthesis radical is zero on the projective source. Its inverse is continuous in the Fréchet topology, and the source-generated labelled range is topologically isomorphic to the coefficient space.

This does not imply a bounded inverse on one fixed Hilbert rung. The inverse consumes more than one half exponential order, while a Hilbert lower bound would forbid any rung loss. The two claims must remain distinct:

- projective source faithfulness and closed source-generated graph;
- Hilbert Green coercivity and closed Hilbert range.

Only the first is established.

## Codiagonal qualification

The Köthe inverse uses label projections to recover each coefficient. After codiagonalization into a common history, those projections may be unavailable and translated columns may approach linear dependence. Therefore the automorphism theorem does not descend through an unproved scalar or G4 codiagonal.

## Direction rescore

- Uniform labelled Hilbert lower bound: 0/10; explicitly false.
- Projective Köthe inverse on the labelled range: completed.
- G4 Hilbert closed-range claim: 10/10 but requires an additional observer, stronger metric, or exposed source-recovery port.
- Further attempts to prove a lower bound from the coefficients alone: 0/10.
- Trace/right-inverse construction retaining labels: 8/10; available only in the projective or graph topology.

## Disposition

The completion gate is now topology-sharp. Source identity survives exactly in the projective labelled graph, while Hilbert coercivity fails. A conservative G4 realization must either retain the source label recovery in its graph topology or supply an independently derived Hilbert observer; it cannot infer closed Hilbert range from finite injectivity. No RH conclusion is authorized.
