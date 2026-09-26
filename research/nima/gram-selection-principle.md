# Gram selection principle: N-path interference without superposition

## The missing piece is now stated

For N alternative fillers \(f_1,\ldots,f_N\) between the same two packages, each produces a record state \(|f_i\rangle\) in the source-admitted positive pairing. Their **Gram matrix**

\[
G_{ij} = \langle f_j | f_i \rangle
\]

determines the combined interference entirely. For an interferometer with relative phases \(\theta_i\),

\[
I(\theta) = \sum_{i,j} G_{ij}\, e^{i(\theta_j-\theta_i)}.
\]

No superposition, no addition of amplitudes, no Born rule. The Gram matrix replaces the path integral's amplitude sum.

## What the checker confirms

For all 10 pairs of the 5 discrete fillers on the four-point carrier:

- Gram is positive semidefinite (all eigenvalues ≥ 0).
- For each pair: \(V = |G_{12}|\), \(D = \sqrt{1-V^2}\), and \(V^2 + D^2 = 1\).
- For each triple: the 3-slit intensity formula \(I = \sum_{i,j=1}^3 G_{ij}e^{i(\theta_j-\theta_i)}\) is well-defined and depends only on the Gram.

[full numeric results](results/gram-selection-principle.json)

## The continuous limit and the path integral

When the set of alternatives becomes a continuum (parameter \(x\) over the aperture), the Gram becomes a **kernel** \(G(x,y) = \langle f_y|f_x\rangle\). The interference formula becomes

\[
I(\theta) = \iint G(x,y)\, e^{i(\theta(y)-\theta(x))}\,dx\,dy.
\]

**QM is the rank-1 special case.** When the Gram kernel factorizes as

\[
G(x,y) = \psi^*(x)\,\psi(y)
\]

for some complex function \(\psi\), the formula reduces to

\[
I(\theta) = \left|\int \psi(x)\, e^{i\theta(x)}\,dx\right|^2,
\]

which is the Born rule plus the path integral together. The wavefunction \(\psi\) is the **Cholesky factor** of the Gram kernel.

**Our model allows all PSD kernels**, not only rank-1. This means:
- Mixed states (rank > 1) are natural, not secondary.
- The Born rule is a special case of a deeper geometric structure.
- Probability is not fundamental—it emerges when the Gram kernel happens to factorize.

## What this does not yet provide

1. **Which Gram kernels are source-admitted?** The positive pairing comes from the source. Not every PSD kernel corresponds to a source-available set of alternatives.

2. **The continuous aperture limit.** \(G(x,y)\) requires a density of alternatives. The finite carrier is discrete; constructing a continuum limit is the path integral problem renamed, not solved.

3. **Factorization into a "wavefunction."** For the rotor, the Gram of \(\langle U(\theta_2)|U(\theta_1)\rangle = e^{i(\theta_2-\theta_1)}\) factorizes with \(\psi(\theta) = e^{-i\theta}\). That is why the rotor behaves like a quantum amplitude. Not every filler family factorizes.

## Falsifier

The gram selection principle is falsified if a physical N-slit experiment produces a pattern inconsistent with the Gram kernel formula for the source-admitted overlaps between the alternatives. Any such experiment would be a measurement of the Gram.

## Verification

```text
uv run --with sympy,numpy python research/nima/checkers/check_gram_selection_principle.py
```