# Geometry and fault cancellation give separate compiler exponents

Owner: `marici.Kitaev`

## Question

How does higher-order echo or composite-pulse cancellation modify the
codimension robustness floor for a dense lower-dimensional control family?

## Claim boundary

Let a `k`-parameter executable family approximate a compact
`d`-dimensional target, with `k<d`. Assume its covering cost obeys the
geometric lower bound

\[
T(\varepsilon)
\gtrsim
\varepsilon^{-(d-k)/k}.
\]

Now suppose that after the admitted cancellation protocol, the unavoidable
worst-case residual fault scales as

\[
E_{\rm fault}(T,\delta)
\gtrsim
\delta^r T^a,
\]

over the relevant small-error and pre-wrapping regime. Here `r` is the
fault-cancellation order and `a` is the growth exponent with compilation
size. Robust accuracy requires this residual to remain no larger than
`\varepsilon`. Substitution gives the conditional floor

\[
\varepsilon
\gtrsim
\delta^{\frac{rk}{k+a(d-k)}}.
\]

The two mechanisms are independent:

- `d-k` measures missing executable directions;
- `r` measures local cancellation order;
- `a` measures how the surviving fault accumulates with compiler size.

For uncompensated static error, `r=a=1`, recovering
`\varepsilon\gtrsim\delta^{k/d}`. Raising `r` improves the floor without
adding a control direction. Reducing `a` prevents long recurrent
compilations from amplifying the residual as severely. Setting `k=d`
removes the recurrence codimension penalty but not the local calibration
error.

This theorem is conditional on a lower sensitivity law, not merely an upper
error estimate. A protocol claiming a better exponent must exhibit which
coefficient vanishes and bound the first nonvanishing adversarial term.
Composite-pulse overhead may also alter the covering-cost parameter and must
be charged to `T`.

For the D(S3) central phase problem, `k=5,d=8`, so

\[
\varepsilon
\gtrsim
\delta^{\frac{5r}{5+3a}}.
\]

An echo that cancels the first-order coefficient can improve the exponent, but
it does not make the three missing central directions executable. It trades a
higher-order fault constructor against recurrence cost. Adding three
independent central controls solves the dimensional problem instead.

## Disposition

Every robust closure compiler should report the signature

\[
(k,d;r,a)
\]

together with evidence for both the covering law and the first nonvanishing
fault term. This separates two repairs that were previously conflated:

1. enlarge the control image by adding constructors;
2. suppress sensitivity by adding cancellation coherence.

Reject a claimed robustness exponent when it is inferred from formal echo
symmetry without a remainder bound, or from density without charging the
sequence length used to realize that symmetry.
