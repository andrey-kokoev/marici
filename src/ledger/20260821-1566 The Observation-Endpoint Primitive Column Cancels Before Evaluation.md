# 1566 — The Observation-Endpoint Primitive Column Cancels Before Evaluation

## Question

Do the total-energy observation-endpoint classes found in Entries 1563--1564
survive as a coefficient extension, or cancel when the bulk--bulk and mixed
location sectors are placed in one labelled primitive basis?

## Common basis

Each observation-endpoint term was labelled by

\[
(f_{\partial},n_{\partial};f_{\rm out},n_{\rm out}),
\]

where:

- \(f_{\partial}\) is the initial-endpoint frequency vector;
- \(n_{\partial}\) is its normal power;
- \(f_{\rm out}\) and \(n_{\rm out}\) identify the unevaluated outer primitive
  at the observation time.

The two asymptotic inner-primitive terms in the bulk--bulk grade-zero column
were summed before comparison with the mixed column. Source spatial weights
and perturbative signs were retained. No outer primitive was evaluated and no
functional identity among periods was assumed.

## Result

There are thirty-two canonical labelled primitive classes across grades one
and zero. For every class \(\alpha\),

\[
\boxed{
C^{BB}_{\alpha}+C^{BS}_{\alpha}=0.
}
\]

At the frozen generic sample point the largest numerical residual is

\[
3.56\times10^{-15}.
\]

The cancellation occurs coefficientwise before evaluating the observation
endpoint:

\[
\boxed{
\mathcal C^{\rm obs}_{BB}
+\mathcal C^{\rm obs}_{BS}=0.
}
\]

The surface--surface sector has no observation primitive and therefore adds
nothing to this column.

## Consequence

The apparent lower-grade total-energy support

\[
\omega=\pm(p+q+k)
\]

is an intermediate labelled route, not a surviving coefficient object. The
complete cubic location sum returns to

\[
\boxed{\operatorname{Supp}\subseteq\{0,\pm2p\}}
\]

through normal grades two, one, and zero.

Thus this finite-time lane currently requires neither a new Carrier wall nor
an observation-endpoint extension local system. The remaining task is purely
coefficient-level: combine the surviving lower-endpoint coefficients and
compare them with the printed \(J_i\) and counterterm basis.

## Artifacts

- `research/benincasa/checkers/finite_time_bulk_bulk_lower_grades.rs`
- `research/benincasa/checkers/finite_time_mixed_lower_grades.rs`
- `research/benincasa/checkers/finite_time_observation_endpoint_cancellation.rs`
- `research/benincasa/results/finite-time-observation-endpoint-cancellation.json`

Ledger sequence claim: `seqclaim-7a36edc4958c501af0f32eff`.
