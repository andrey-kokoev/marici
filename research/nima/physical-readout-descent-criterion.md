# Physical Readout Descent Criterion

Let

\[
q:V\twoheadrightarrow W
\]

be a source-declared quotient of response, cycle, or state spaces, and let
\(\ell\in V^*\) be the frozen physical readout.  Then the following are
equivalent:

1. there is a functional \(\bar\ell\in W^*\) with
   \(\ell=\bar\ell\circ q\);
2. \(\ell\) annihilates \(\ker q\);
3. \(\ell\in\operatorname{im}q^*\).

For a surjection, \(\bar\ell\) is unique.  Therefore

\[
\boxed{
\text{physical descent}
\iff
\text{source quotient exists and the readout annihilates its kernel}.
}
\]

The finite checker exhausts all surjective matrices and functionals over
\(\mathbb F_2\) in dimensions at most three and over \(\mathbb F_3\) in
dimensions at most two.  It verifies the three equivalent conditions and
the factorization identity on every vector.

## Sector controls

- **Positive:** radiative gravity has
  \(q:V\to V/\langle l=0,1\rangle\), while the source operator
  \(\mathcal O\) annihilates the discarded modes.  Its charge readout
  descends.
- **Negative:** at every nontrivial five-site Kummer branch quotient,
  \(\delta_0\) distinguishes sheets in the collapsed kernel.  The frozen
  cosmological chamber readout does not descend.

## Scope

This criterion does not manufacture \(q\).  A geometrically meaningful
quotient still requires a source-defined chain, support, boundary, and
orientation map.  Nor does an algebraic transfer \(q_!\) replace the test:
transfer has different variance from factorization of \(\ell\) through
\(q\).

The criterion is therefore an admission gate, not a universal constructor.

Artifacts:

- `research/nima/check_physical_readout_descent_criterion.py`
- `research/nima/results/physical-readout-descent-criterion.json`
