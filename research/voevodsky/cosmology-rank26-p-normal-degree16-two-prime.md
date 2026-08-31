# Rank-26 p-normal degree-16 two-prime quotient gate

## Question

Does the p-normal quotient-rank absorption persist at ambient degree 16 over two primes?

## Claim boundary

This packet is a finite-cutoff check at ambient relation degree 16 over two primes. It does not prove stabilization for all ambient degrees, does not construct a horn comparison map, does not construct a relative Bockstein, and does not construct a physical period.

## Disposition

Yes. Re-running the p-normal quotient-rank gate at ambient relation degree 16 over

\[
\mathbb F_{32003}, \qquad \mathbb F_{32009}
\]

gives the same rank signature at the p-normal point `(3,6,-3)`.

| prime | rank(S) | rank(S+T) | T over S | nx over S+T | ny over S+T | nx+ny over S+T |
|---:|---:|---:|---:|---:|---:|---:|
| 32003 | 14662 | 14781 | 119 | 0 | 0 | 0 |
| 32009 | 14662 | 14781 | 119 | 0 | 0 | 0 |

Here:

- `S` is the special exact image;
- `T` is the p-tangent derived span from `nx-ny=(1,-1,0)`;
- `nx=(1,0,0)` and `ny=(0,1,0)` are integral unit p-normal directions.

Thus, after quotienting by `S+T`, both p-normal derivative images add zero dimensions over both primes.

## Meaning

The finite-cutoff pattern is now:

| ambient degree | T over S | surviving p-normal line |
|---:|---:|---:|
| 8 | 97 | no |
| 10 | 101 | no |
| 12 | 107 | no |
| 14 | 113 | no |
| 16 | 119 | no |

This extends the two-prime absorption pattern beyond the stored rank-26 source-word basis ambient degree 14. The p-tangent-derived quotient still kills the p-normal derivative image, so there is no admissible line to compare with the formal \(\tau_p\) horn.

This is strong finite evidence, not an unbounded stabilization theorem.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_rank26_p_normal_degree16_two_prime.py`

Result:

- `research/voevodsky/results/cosmology_rank26_p_normal_degree16_two_prime.json`

Command:

- `python research/voevodsky/check_cosmology_rank26_p_normal_degree16_two_prime.py`
