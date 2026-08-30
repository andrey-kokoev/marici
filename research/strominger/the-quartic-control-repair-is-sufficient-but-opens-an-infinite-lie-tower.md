# The Quartic Control Repair Is Sufficient but Opens an Infinite Lie Tower

## Exact sufficiency

On the even selector code \(n_v=2,4\), define

\[
H_{\mathrm{ctrl}}
=
\frac{N_v-2}{2}\left(N_u+\frac12\right).
\]

This operator is diagonal in the joint number basis, so it preserves the code
without leakage. At angle \(2\pi\),

\[
e^{-2\pi iH_{\mathrm{ctrl}}}
=
\begin{cases}
I,&n_v=2,\\
-I,&n_v=4.
\end{cases}
\]

Thus one quartic cross-mode interaction is mathematically sufficient to
implement the controlled metaplectic sign internally on the declared two-grade
code. It is not a global selector on the completed \(v\)-tower; Entry 3725
records the required spectral-projector refinement.

## Closure cost

Let

\[
A=N_uN_v.
\]

The quadratic source algebra contains multiplication by \(u^2\). Since

\[
[A,u^2]=2u^2N_v,
\]

iteration gives

\[
\operatorname{ad}_A^k(u^2)=2^k u^2N_v^k.
\]

The Bernstein degrees are \(2k+2\), hence unbounded. Adjoining the quartic
control interaction to \(\mathfrak{sp}_4\) therefore generates an
infinite-dimensional non-Gaussian Lie algebra.

The repair is not a finite extra node attached to the old control algebra. It
changes the type of the control system.

## Two legitimate scopes

For the single controlled loop, no infinite closure is needed. The diagonal
self-adjoint polynomial \(H_{\mathrm{ctrl}}\) exponentiates directly, and the
code action is exact.

If the source declares closure under arbitrary composition and commutator with
all quadratic controls, then it must also declare a common domain and
exponentiation policy for the unbounded polynomial tower. The former smooth
quadratic domain is a candidate core, but executable authority and analytic
closure have not been established for the generated family.

Thus the choices are:

```text
typed primitive quartic gate
  narrow authority
  exact controlled sign
  no claim of full Lie closure

quartic-extended control algebra
  broad compositional authority
  infinite polynomial tower
  new domain and completion obligations
```

This is a direct application of the authority calculus: permission to execute
one quartic constructor must not be laundered into authority over its entire
unbounded Lie closure.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/quartic_control_sufficiency_and_growth_checks.py
```

The exact checker verifies the controlled phases, code preservation, and the
iterated commutator family through degree eighteen.
