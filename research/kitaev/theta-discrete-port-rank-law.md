# A finite discrete label code does not observe arbitrary theta coefficient packets

Owner: `marici.Kitaev`

## Bounded question

Can a fixed finite discrete arithmetic port repair the adjacent-label collapse
while remaining faithful on arbitrary finite theta/Fock coefficient packets?

## Two different tasks

For (N\) labelled basis states, a classical code with (r\) bits can assign a
distinct word to every label when

\[
2^r\ge N.
\]

Thus (r\ge\lceil\log_2N\rceil\) is necessary and sufficient for identifying
which single basis label was presented.

But a linear source packet is

\[
c=\sum_{j=1}^Nc_je_j.
\]

If the discrete port has (r\) scalar rows, its linearized observation matrix
is (D_N:\mathbb F^N\to\mathbb F^r\). Faithfulness on all coefficient packets
requires

\[
\ker D_N=0,
\]

and hence

\[
r\ge N.
\]

Uniform observability is stronger still:

\[
D_N^*D_N\ge cI_N
\]

with cutoff-independent (c>0\). It also forces (r\ge N\).

Therefore logarithmic classical label coding and linear amplitude
reconstruction are different capabilities.

## Smallest hostile witness

Three distinct nonzero two-bit codewords may be chosen as columns

\[
D=
\begin{pmatrix}
1&0&1\\
0&1&1
\end{pmatrix}.
\]

Every basis label has a distinct readout, yet

\[
D(-1,-1,1)^T=0.
\]

Thus two bits identify each of three classical labels but miss a nonzero
superposition. Pairwise code separation is not joint linear faithfulness.

## Arithmetic consequence

For (N\) prime labels, the individual valuation rows \(\nu_p\) form a
one-hot incidence matrix and faithfully reconstruct prime-supported
coefficients, but the number of required independent rows grows with (N\).
A fixed finite family of prime cylinders eventually leaves an infinite
unobserved prime subspace.

Equivalently, one may retain a single typed discrete port

\[
\mathcal H_{\rm discrete,X}\simeq\mathbb C^{N_X}
\]

with the labelled basis intact. This is one port categorically, but its target
dimension grows with the cutoff. Calling it “one port” must not conceal its
linear resource cost.

Prime-power typing enlarges the basis further. A valuation vector can compress
structured arithmetic labels, but faithfulness on arbitrary amplitudes over
all admitted labels still requires a target of at least the source dimension
unless dynamics restricts the state family.

## Hybrid completion

The honest repair is

\[
\mathcal H_{\rm source,X}
=\mathcal H_{\rm Gram,X}\oplus\mathcal H_{\rm discrete,X}.
\]

The analytic component carries smooth theta/Tate transport. The discrete
component retains the exact label amplitudes needed by admitted arithmetic
constructors. With the one-hot discrete norm, adjacent analytic collapse is
visible in the discrete summand with a fixed lower bound.

This repair is architectural, not free. Its completion is an infinite labelled
\(\ell^2\) or Fock port, and every operator coupling it to the boundary trace
must be shown continuous/closable.

## Three capability levels

1. **Basis-label identification:** \(\lceil\log_2N\rceil\) classical bits.
2. **Arbitrary linear coefficient reconstruction:** at least (N\) scalar
   rows, or target dimension at least (N\).
3. **Physical executable observation:** requires source-derived instruments
   realizing those rows and paying their locality/interface cost.

The first level cannot be used as evidence for the second or third.

## Falsifiers and escape conditions

- Any proposed (r<N\) linear port has a kernel by rank-nullity.
- Pairwise distinct code columns do not imply full column rank.
- Cutoff-dependent one-hot ports are faithful finitely but require a typed
  inductive-limit completion.
- A source-dynamical manifold of dimension (d_X<N_X\) may need only (d_X\)
  independent linear observations; its invariance and dimension must be
  derived.
- Nonlinear measurement of one unknown basis label changes the state model and
  does not reconstruct a coherent superposition.

## Disposition

No fixed finite-dimensional discrete port can uniformly observe arbitrary
theta coefficient packets as the label cutoff grows. The viable discrete
repair is the full labelled Fock/\(\ell^2\) port, or a source-derived lower-
dimensional admissible state manifold. The former preserves information at a
growing interface cost; the latter remains a dynamical observability theorem.

## Claim strength

Exact finite-dimensional rank theorem and resource lower bound. It does not
assert that arbitrary labelled superpositions are physically admitted by the
theta source.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_discrete_port_rank.py`.
The result is written to
`research/kitaev/results/theta-discrete-port-rank.json`.
