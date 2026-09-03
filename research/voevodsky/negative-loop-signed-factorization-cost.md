# Signed-factorization cost of the negative loop

## Question

If positive commutative factorization is impossible but signed quasiprobability is allowed, what minimum negativity is forced by the value \(-1/8\)?

## Claim boundary

This packet treats normalized real signed models whose response variable lies in \([0,1]\), as it does for a product of classical positive events bounded by one. It does not cover arbitrary unbounded responses or complex quasiprobability norms.

## Signed model

Let hidden states \(\lambda\) carry real signed weights \(w_\lambda\) with

\[
\sum_\lambda w_\lambda=1,
\]

and classical loop responses \(r_\lambda\in[0,1]\). Define total negative mass

\[
N=\sum_{w_\lambda<0}|w_\lambda|.
\]

Then

\[
\Omega=\sum_\lambda w_\lambda r_\lambda\ge -N,
\]

because positive-weight terms are nonnegative and each negative-weight response has magnitude at most its negative weight. Therefore

\[
\Omega=-\frac18
\quad\Longrightarrow\quad
N\ge\frac18.
\]

For normalized real signed weights, total variation is

\[
\lVert w\rVert_1=1+2N,
\]

so

\[
\lVert w\rVert_1\ge\frac54.
\]

## Tightness

The bound is attained by two hidden states:

\[
(w_0,r_0)=\left(\frac98,0\right),
\qquad
(w_1,r_1)=\left(-\frac18,1\right).
\]

Their weights sum to one and their expected loop value is \(-1/8\). Thus the lower bounds \(N=1/8\) and \(\lVert w\rVert_1=5/4\) are exact for this response class.

## Contaminated witness

If an observed scalar remains negative at \(\Omega_{\mathrm{obs}}<0\), the same argument gives

\[
N\ge-\Omega_{\mathrm{obs}}.
\]

As contamination approaches the classical boundary zero, the certified negativity cost vanishes continuously. The robustness margin and signed-cost bound are therefore two views of the same separating hyperplane.

## Pyramid consequence

The loop witness provides three distinct outputs:

1. a nonfaithful coherence coordinate;
2. exclusion of positive commutative factorization;
3. a quantitative lower bound on signed classical simulation cost under a bounded-response model.

These strengths require different fields. A proposed schema addition is:

- `rival_model_class`;
- `response_range`;
- `witness_value`;
- `minimum_negative_mass`;
- `minimum_total_variation`;
- `tightness_fixture`;
- `scope_exclusions`.

## Disposition

Any normalized real signed commutative model with responses in \([0,1]\) reproducing the exact loop must use negative mass at least \(1/8\) and total variation at least \(5/4\). The bound is tight. This quantifies the cost of escaping Kitaev's positive-record no-go without claiming computational separation.

## Verification

- `research/voevodsky/checkers/check_negative_loop_signed_cost.py`
- `research/voevodsky/results/negative_loop_signed_cost.json`
