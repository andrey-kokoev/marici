# Energy-bounded inverse-limit completion

## Question

What additional structure removes phantom compatible families from the inverse system of shrinking-radical spectral quotients?

## Claim boundary

This packet verifies the weighted sequence model and extracts the categorical boundedness gate. It does not assert positivity of the completed Weil form.

## Bare inverse-limit defect

Let \(V=c_{00}\) and let \(R_N\) consist of sequences whose first \(N\) coordinates vanish. Then

\[
V/R_N\cong\mathbb C^N
\]

with bonding maps deleting the last coordinate. The unrestricted inverse limit is \(\mathbb C^{\mathbb N}\), not \(c_{00}\) or \(\ell^2\). The compatible all-one prefixes are a phantom relative to both spaces.

## Energy-bounded sublimit

Choose positive weights \(\lambda_n\) and finite energies

\[
E_N(x^{(N)})=\sum_{n=1}^{N}\lambda_n|x_n|^2.
\]

Compatibility identifies a family with one coordinate sequence. Monotone convergence gives

\[
\sup_NE_N(x^{(N)})<\infty
\quad\Longleftrightarrow\quad
\sum_{n\ge1}\lambda_n|x_n|^2<\infty.
\]

Thus the energy-bounded inverse limit is canonically \(\ell^2(\lambda)\). For \(\lambda_n=n\), all-one prefixes remain compatible but have energy \(N(N+1)/2\), so they are excluded.

## Completion cell

An inverse-limit completion cell therefore requires:

1. coherent finite quotient energies;
2. a uniform bounded-energy predicate;
3. representation of every bounded family in the closed common-core completion;
4. identification of zero-energy families with the completed radical;
5. independence from cutoff exhaustion.

These fields replace unrestricted inverse-limit compatibility. Composition is partial: pasted systems must agree on their energy predicates and completion maps.

## Weil boundary

Using the completed Weil form itself as the positive energy would be circular because its positivity is the target assertion. The candidate fixed-support Sobolev completion mentioned by Grothendieck may provide a non-RH ambient norm; it must be compared to the finite quotient energies without assuming Weil positivity.

## Disposition

The projective-limit defect and its exact repair are established in the weighted model. The next executable branch is to audit the fixed-support Sobolev operator construction as a source-derived ambient energy and test whether finite spectral quotient maps are uniformly bounded in it.

## Verification

- `research/voevodsky/checkers/check_energy_bounded_inverse_limit_completion.py`
- `research/voevodsky/results/energy_bounded_inverse_limit_completion.json`
- `research/grothendieck/inverse-spectral-quotient-limit-needs-an-energy-boundedness-gate.md`
