# Current Python backend cannot certify the gamma special functions

## Question

Can the executed erfc-series reconciliation be upgraded immediately to directed interval arithmetic with the admitted Python environment?

## Capability preflight

Two bounded preflights were executed through structured-command:

1. `mpmath.iv.erfc` on a point interval;
2. import of the Arb-backed `python-flint` package.

The first failed with `mpmath.libmp.libhyper.NoConvergence` inside interval `hyp1f1`. The second failed with `ModuleNotFoundError: flint`.

Thus the available `mpmath` interval context cannot evaluate the required complementary error function even at a point interval, and no Arb binding is present in the admitted ephemeral SymPy environment.

## Consequence

The high-precision gamma reconciliation is not a certificate. Increasing `mp.dps`, checking agreement with quadrature, or manually padding decimal output does not create directed-rounding authority.

The first missing typed object is an admitted interval backend supporting at least:

- outward-rounded elementary arithmetic and exponentials;
- scaled `erfc`, or enough primitives to enclose it;
- digamma and Hurwitz zeta, unless the tail is replaced by elementary integral bounds.

## Backend-independent fallback design

Special-function dependency can be reduced rather than bypassed:

1. evaluate the finite gamma integral on `[0,40]` with validated quadrature using interval exponentials;
2. use the elementary tail bound already derived, avoiding interval `erfc` via

\[
\operatorname{erfc}(u)\le \frac{e^{-u^2}}{\sqrt\pi u};
\]

3. alternatively enclose scaled `erfc` by separate small-argument Taylor bounds and large-argument alternating asymptotics;
4. propagate the resulting four gamma intervals through the certified determinant error budget.

Implementing validated quadrature still requires a directed interval arithmetic primitive. Ordinary `mpmath` floats are not a substitute.

## Execution evidence

- `mpmath.iv.erfc(iv.mpf([1,1]))`: failed with `NoConvergence`;
- `import flint`: failed because the module is absent.

No package installation or unapproved execution fallback was attempted.

## Disposition

Record interval certification as capability-blocked in the current admitted environment. Continue analytic reduction of the enclosure, or obtain operator authorization for an admitted Arb/python-flint execution surface. The existing numerical signs remain uncertified.