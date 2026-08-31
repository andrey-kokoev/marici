# Rank-26 p-normal two-prime quotient-rank gate

## Question

Does the ambient-degree-8 p-normal quotient-rank absorption persist over a second prime?

## Claim boundary

This packet is a two-prime finite-cutoff check at ambient relation degree 8. It does not test higher ambient degrees, does not construct a horn comparison map, does not prove an unbounded rank-26 no-go, does not construct a relative Bockstein, and does not construct a physical period.

## Disposition

Yes. Re-running the p-normal quotient-rank gate over both

\[
\mathbb F_{32003}, \qquad \mathbb F_{32009}
\]

gives the same rank signature at the p-normal point `(3,6,-3)`.

| prime | rank(S) | rank(S+T) | T over S | nx over S+T | ny over S+T | nx+ny over S+T |
|---:|---:|---:|---:|---:|---:|---:|
| 32003 | 4276 | 4373 | 97 | 0 | 0 | 0 |
| 32009 | 4276 | 4373 | 97 | 0 | 0 | 0 |

Here:

- `S` is the special exact image;
- `T` is the p-tangent derived span from `nx-ny=(1,-1,0)`;
- `nx=(1,0,0)` and `ny=(0,1,0)` are integral unit p-normal directions.

Thus, after quotienting by the special exact image and p-tangent derived relations, both unit p-normal derivative images add zero dimensions over both primes.

## Meaning

The degree-8 instance is now closed with a two-prime witness. The raw p-normal derivative rows are source-computable, but their quotient class vanishes after imposing the p-tangent derived span. Therefore there is no degree-8 surviving normal line to map to the formal \(\tau_p\) horn.

This still does not close higher ambient degrees such as 10 or 12, nor does it prove an unbounded theorem.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_rank26_p_normal_two_prime_quotient.py`

Result:

- `research/voevodsky/results/cosmology_rank26_p_normal_two_prime_quotient.json`

Command:

- `python research/voevodsky/check_cosmology_rank26_p_normal_two_prime_quotient.py`
