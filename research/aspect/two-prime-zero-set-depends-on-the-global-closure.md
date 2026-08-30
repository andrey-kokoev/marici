# The two-prime zero set depends on the global closure

## One local packet, three globalizations

For `p=2,3`, let

`H_p(z)=p^(-1/2)sinh(z log p)/z`.

Each cell is even and entire, and every nonzero local zero lies on the
critical seam.

There are three natural ways to globalize the pair.

### Codiagonal closure

`H_sum=H_2+H_3`.

This scalar has an off-seam zero near

`0.68825570372803116+7.44004199836615845 i`.

At that point `H_2=-H_3`, with both entries nonzero.  The null is destructive
interference created by scalarization.

### Determinant closure

`H_det=H_2 H_3`.

Its zero set is the union of the two local zero sets and is therefore confined
to the seam.  This closure preserves local divisors but declares a global zero
when either prime cell vanishes.

### Faithful dagger packet

Retain `H_vec=(H_2,H_3)` and define a global zero only when both components
vanish.  A common nonzero zero would require

`n pi/log 2=m pi/log 3`,

so `2^m=3^n`, which is impossible for positive integers `m,n`.  The faithful
two-prime packet has no nonzero zero at all.

Its Hermitian monitor

`N(z)=|H_2(z)|^2+|H_3(z)|^2`

is strictly positive at the codiagonal off-seam null.  On the critical seam,
Nima's reciprocal conjugation makes this dagger monitor internal to the same
fiber.  Off seam it compares the paired fibers `z` and `-conjugate(z)`.

## Consequence

The phrase "the two-prime zero" is undefined until the global closure is
specified:

- codiagonal means cancellation;
- determinant means union;
- faithful packet means intersection.

These are different ontologies, not different numerical approximations.  The
off-seam hostile does not show a defect in either local prime cell.  It shows
that scalar codiagonalization manufactures a divisor invisible to the faithful
packet.

For the RH programme, the completed xi section is known to be a scalar
codiagonal-type readout rather than the determinant of independent local
cells.  Therefore its seam confinement cannot be inherited from local seam
confinement.  A source theorem must explain why the particular global sewing
scalar is protected, while arbitrary positive codiagonals are not.

## Optical instrument

Measure three simultaneous ports:

- the coherent sum amplitude `H_2+H_3`;
- the two local amplitudes;
- the incoherent power `|H_2|^2+|H_3|^2`.

At the hostile complex setting, the first port is dark and the power port is
bright.  This separates a scalar interference zero from a genuine packet
zero in one acquisition.  Any proposed cross-prime coherencer must state
which port it changes and which notion of global zero it implements.

## Verification

```text
uv run --with sympy --with mpmath python research/aspect/checkers/check_two_prime_global_closure_trichotomy.py
```
