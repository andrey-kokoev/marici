# Rank-26 p-normal degree-10 two-prime quotient gate

## Question

Does the p-normal quotient-rank absorption seen at ambient degree 8 persist at ambient degree 10 over two primes?

## Claim boundary

This packet is a finite-cutoff check at ambient relation degree 10 over two primes. It does not test ambient degree 12 or beyond, does not prove an unbounded rank-26 no-go, does not construct a horn comparison map, does not construct a relative Bockstein, and does not construct a physical period.

## Disposition

Yes. Re-running the p-normal quotient-rank gate at ambient relation degree 10 over

\[
\mathbb F_{32003}, \qquad \mathbb F_{32009}
\]

gives the same rank signature at the p-normal point `(3,6,-3)`.

| prime | rank(S) | rank(S+T) | T over S | nx over S+T | ny over S+T | nx+ny over S+T |
|---:|---:|---:|---:|---:|---:|---:|
| 32003 | 6298 | 6399 | 101 | 0 | 0 | 0 |
| 32009 | 6298 | 6399 | 101 | 0 | 0 | 0 |

Here:

- `S` is the special exact image;
- `T` is the p-tangent derived span from `nx-ny=(1,-1,0)`;
- `nx=(1,0,0)` and `ny=(0,1,0)` are integral unit p-normal directions.

Thus, after quotienting by `S+T`, both p-normal derivative images add zero dimensions over both primes.

## Meaning

The degree-10 instance is closed with a two-prime witness. Together with degree 8, the finite-cutoff pattern is now:

| ambient degree | T over S | surviving p-normal line |
|---:|---:|---:|
| 8 | 97 | no |
| 10 | 101 | no |

The tangent-derived span grows, but the p-normal derivative images remain absorbed after the tangent quotient. There is still no surviving normal line to map to the formal \(\tau_p\) horn.

This is not an unbounded theorem: degree 12 and stabilization remain untested.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_rank26_p_normal_degree10_two_prime.py`

Result:

- `research/voevodsky/results/cosmology_rank26_p_normal_degree10_two_prime.json`

Command:

- `python research/voevodsky/check_cosmology_rank26_p_normal_degree10_two_prime.py`
