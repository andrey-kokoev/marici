# A positive Weil smoothing threshold must occur through a double contact

Let

```
U(sigma,xi)=(W_hat*q_sigma)(xi)
```

be a nonzero completed Weil Gaussian kernel, and suppose it is a classical
heat solution for `sigma>0`. Assume its positivity set is the upper ray
`[sigma_*,infinity)` and that, when `sigma_*>0`, loss of positivity is attained
at a finite character `xi_*` rather than escaping to infinity.

Then

```
U(sigma_*,xi_*)=0,
partial_xi U(sigma_*,xi_*)=0,
partial_xi^2 U(sigma_*,xi_*)>=0,                       (1)
```

and by the heat equation

```
partial_sigma U(sigma_*,xi_*)
 =partial_xi^2 U(sigma_*,xi_*)>=0.                    (2)
```

Thus a finite positive threshold can only be born through a tangential zero,
not a transverse sign crossing in `xi`.

## Strict positivity above the threshold

For any `sigma_2>sigma_1>=sigma_*`,

```
U(sigma_2)=q_(sigma_2-sigma_1)*U(sigma_1).             (3)
```

The Gaussian is strictly positive. If `U(sigma_1)` is a nonzero nonnegative
function or measure, then (3) is strictly positive at every finite `xi`.
Consequently a zero cannot occur at any `sigma>sigma_*`; it is confined to
the threshold boundary itself.

## Sharp reduction of the source attack

Suppose broad-smoothing positivity and the required tail compactness are
proved from the explicit formula. To force `sigma_*=0`, it is enough to rule
out simultaneous source-side solutions of

```
Theta(sigma,xi)=0,
partial_xi Theta(sigma,xi)=0                           (4)
```

at finite `sigma>0`. In the `(t,xi)` source formula, the second equation is
explicit: the endpoint differentiates elementary, the gamma Gaussian gains a
linear `(u-xi)` factor, and the prime cosine sum gains
`-log(n)sin(xi log n)`.

This is more constrained than proving a global inequality directly. A
hostile computation should search for near-simultaneous zeros of the value
and character derivative, with certified source tails. If none exist and
escape to infinity is excluded, backward continuation reaches zero variance
without losing positivity and yields Weil positivity.

## Necessary caveats

The contact reduction is conditional on:

- existence of a broad positive regime;
- continuity through the candidate threshold;
- sufficient decay or coercivity to prevent the minimizing character from
  escaping to infinity;
- nontriviality of the completed distribution.

These are separate analytic gates. The theorem does not itself prove RH or
assert that a positive threshold exists.
