# Convex duality of the negative loop witness

## Question

Are the additive gap, contamination threshold, signed negative mass, and generalized robustness independent numbers or different coordinates of one convex separation?

## Claim boundary

This packet concerns the one-dimensional scalar projection of the positive commutative model, whose admitted response interval is \([0,1]\). It does not identify the full process-level robustness of the associator implementation.

## Scalar classical set

The positive commutative image in the loop coordinate is

\[
\mathcal K=[0,1].
\]

The witness point is \(\Omega_*=-a\) with \(a=1/8\). The affine functional \(W(\Omega)=\Omega\) separates \(\Omega_*\) from \(\mathcal K\).

## Four equivalent scalar quantities

1. **Boundary gap.** The distance to the nearest classical point is \(a\).

2. **Signed negative mass.** Any normalized signed decomposition over responses in \([0,1]\) has negative mass at least \(a\), and this is tight.

3. **Generalized robustness parameter.** Mix the witness with a classical response \(b\in[0,1]\):

\[
\frac{-a+s b}{1+s}.
\]

To enter \(\mathcal K\), the numerator must be nonnegative. The smallest \(s\) is obtained at \(b=1\), giving

\[
R_{\mathcal K}=a=\frac18.
\]

4. **Contamination fraction.** Writing \(p=s/(1+s)\), the threshold corresponding to \(s=a\) is

\[
p_*=\frac{a}{1+a}=\frac19.
\]

The signed-model total variation is \(1+2a=5/4\).

Thus

\[
a=N_{\min}=R_{\mathcal K}=\frac18,
\qquad
p_*=rac{a}{1+a}=\frac19,
\qquad
\lVert w\rVert_{1,\min}=1+2a=\frac54.
\]

## Dual-witness interpretation

The same separating functional produces both a no-go theorem and a resource lower bound. This explains why a nonfaithful scalar coordinate can still be quantitatively complete for one rival cone: it need not reconstruct the source point to compute distance along the witnessed direction.

The equality is special to this normalized one-dimensional model. In the full process space, different implementations can share \(\Omega=-1/8\) while having different distances to the physically defined classical-process set. Process-level robustness requires the complete process object and admissible mixing class.

## Pyramid consequence

A partial-representation record should distinguish:

- `observable_space_robustness`;
- `process_space_robustness`;
- `separating_witness`;
- `rival_convex_set`;
- `normalization`;
- `duality_gap`;
- `tight_primal_fixture`.

Only the scalar observable-space quantities are currently certified.

## Disposition

The numbers \(1/8\), \(1/9\), and \(5/4\) are not unrelated diagnostics. They are exact transforms of one scalar convex separation. This unifies the witness margin and signed-cost results while blocking promotion to full implementation robustness.

## Verification

- `research/voevodsky/checkers/check_negative_loop_convex_duality.py`
- `research/voevodsky/results/negative_loop_convex_duality.json`
