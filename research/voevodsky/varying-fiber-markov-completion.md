# Uniform varying-fiber Markov completion

## Question

Does the varying-fiber finite fragment admit a bounded one-sided completion without identifying unequal fibers?

## Claim boundary

Let \((H_i)_{i\ge0}\) be finite-dimensional real Hilbert spaces, with no bound required on their dimensions, and rectangular transfers \(A_i:H_{i+1}\to H_i\) satisfying \(\lVert A_i\rVert\le\rho<1\). The construction does not cover pointwise-only contraction or arbitrary fiber-changing vertical maps.

## Construction

On the Hilbert direct sum \(\bigoplus_iH_i\), define

\[
K_{ii}=I_{H_i},
\qquad
K_{ij}=A_i\cdots A_{j-1}:H_j\to H_i
\]

for \(i<j\), with transposed lower blocks. The typed product satisfies

\[
\lVert K_{ij}\rVert\le\rho^{|i-j|}.
\]

The operator-valued Schur test gives

\[
\lVert K\rVert\le\frac{1+\rho}{1-\rho},
\]

independently of the fiber dimensions. Every finite principal block compression is a positive Markov covariance, so the completed operator is positive on the direct sum.

## Coherence

Contiguous block compression recovers the exact restricted typed chain. Nested comparisons, associators, and Beck–Chevalley cells remain identities. A vertexwise orthogonal family \(U_i\in O(H_i)\) defines the direct-sum unitary \(\bigoplus_iU_i\), so gauge companions and conjoints commute with completion.

## Hostile boundary

The fiber labels and dimensions remain part of every block type. A coordinate permutation that sends a block into a differently dimensioned fiber is not an admitted gauge. Pointwise contraction approaching norm one does not provide the geometric majorant and is refused absent another Schur certificate.

## Disposition

Uniform completion, positivity, contiguous Beck–Chevalley, and orthogonal gauge equipment coherence extend to varying finite-dimensional fibers. The remaining Markov-side gates are non-orthogonal vertical maps and noncontiguous/general pullbacks; cross-sector realization remains separate.

## Verification

- `research/voevodsky/checkers/check_varying_fiber_markov_completion.py`
- `research/voevodsky/results/varying_fiber_markov_completion.json`
