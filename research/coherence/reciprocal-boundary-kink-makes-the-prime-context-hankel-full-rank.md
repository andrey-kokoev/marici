# The reciprocal boundary kink makes finite prime-context Hankel matrices full rank

## Fixed source test

The previous unbounded-rank result used the entire broken graph source class. To test whether growth disappears for one simple source, take

\[
f(x)=e^{-|x|}.
\]

On the signed log-prime lattice, a displacement vector \(\nu\in\mathbb Z^4\) has multiplicative coordinate

\[
r_\nu=\prod_{p\in\{2,3,5,7\}}p^{\nu_p}.
\]

The response is exactly rational:

\[
f\!\left(\sum_p\nu_p\log p\right)
=\min(r_\nu,r_\nu^{-1}).
\]

For context vectors \(u,v\), form

\[
H_k(u,v)=f\!\left(\sum_p(u_p+v_p)\log p\right),
\qquad \|u\|_1,\|v\|_1\le k.
\]

## Exact result

The exact rational ranks are

| depth | contexts | Hankel rank |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 9 | 9 |
| 2 | 41 | 41 |
| 3 | 129 | 129 |

Every tested finite Hankel matrix is full rank.

Thus rank growth is not only caused by asking for arbitrary source functions. One fixed reciprocal exponential source already distinguishes every signed prime context through depth three.

## Why the two-state model fails here

Inside one oriented chamber,

\[
e^{-x}
\]

is multiplicative under translation and has rank-one behavior. Reciprocal completion introduces the fold

\[
x\mapsto|x|.
\]

Different labelled words cross that fold at different locations. The resulting kink stores their ordering relative to the boundary and destroys the finite exponential recurrence.

Therefore:

```text
oriented positive translations       -> rank one
one common translation plus reversal -> rank two
independent signed prime translations
observed through the absolute fold   -> full finite-context rank
```

The boundary is acting as a memory surface.

## Consequence

Collapsing all prime shifts to the single Lie generator \(A\) preserves their orbit geometry but not their complete labelled contextual behavior. The latter requires either:

- an infinite-dimensional realization;
- a depth-graded pro-realization;
- or a justified quotient that forbids contexts from resolving individual signed words.

Any proposed finite controller or observer must declare which of these behavioral distinctions it discards.

## Verification

```text
python research/coherence/check_absolute_prime_shift_hankel_rank.py
```

Artifacts:

- `check_absolute_prime_shift_hankel_rank.py`
- `absolute-prime-shift-hankel-rank.v1.json`
