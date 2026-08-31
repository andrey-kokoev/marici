# Rank-26 p-normal quotient-rank gate

## Question

After raw p-normal row generation, does the first quotient-rank test leave a normal-choice-independent line that could map to the \(\tau_p\) horn?

## Claim boundary

This is a finite-cutoff rank test at ambient relation degree 8 over \(\mathbb F_{32003}\). It is not a two-prime theorem, not a higher-degree stabilization result, not a horn comparison map, not a relative Bockstein construction, and not a physical period.

## Disposition

At the p-normal point

\[
(3,6,-3), \qquad p=x+y+3z=0,
\]

the checker streamed:

- the special exact relation rows;
- first derivatives along \(n_x=(1,0,0)\);
- first derivatives along \(n_y=(0,1,0)\);
- first derivatives along the p-tangent direction \(n_x-n_y=(1,-1,0)\).

It used the same sparse pivot reducer as the rank-26 source code.

Computed ranks over \(\mathbb F_{32003}\), ambient relation degree 8:

| span | rank |
|---|---:|
| special exact image | 4276 |
| special + p-tangent derivatives | 4373 |
| special + \(n_x\) derivatives | 4373 |
| special + \(n_y\) derivatives | 4373 |
| special + p-tangent + \(n_x\) | 4373 |
| special + p-tangent + \(n_y\) | 4373 |
| special + p-tangent + \(n_x\) + \(n_y\) | 4373 |

Thus the p-tangent derivatives add 97 dimensions over the special exact image, but after quotienting by that p-tangent derived span, both integral p-normal derivative images add zero dimensions:

\[
\operatorname{rank}(S+T+n_x)-\operatorname{rank}(S+T)=0,
\]

\[
\operatorname{rank}(S+T+n_y)-\operatorname{rank}(S+T)=0.
\]

The normal-choice-independence condition holds, but vacuously: there is no surviving normal line at this cutoff to map to the \(\tau_p\) horn.

## Meaning

The raw relation-generation route was real, but the first quotient-rank test closes the ambient-degree-8, prime-32003 instance. The raw \(n_x\) and \(n_y\) derivative images are absorbed by the special exact image plus p-tangent derived span.

This does not prove a global no-go. The remaining admissible tests are higher ambient degrees and a second prime. Only if a stable surviving line appears there can one ask whether it maps to the primitive horn column `(1,1)`.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_rank26_p_normal_quotient_rank.py`

Result:

- `research/voevodsky/results/cosmology_rank26_p_normal_quotient_rank.json`

Command:

- `python research/voevodsky/check_cosmology_rank26_p_normal_quotient_rank.py`
