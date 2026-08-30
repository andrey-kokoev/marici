# Global Internal Control Needs a Spectral Grade Projector

## Code-relative versus global selection

The quartic selector used in Entry 3721 is

\[
P_{mathrm{code}}(N_v)=\frac{N_v-2}{2}.
\]

It takes the desired values zero and one on selector grades \(2\) and \(4\).
On spectator grades it takes values \(-1,2,3,\ldots\). Its two-pi evolution
therefore applies additional spectator-dependent phases. The gate is exact
only after declaring that the state is supported on the two-grade code and
that intervening operations preserve that support.

The global operation that acts only on active grade \(4\) requires

\[
P_4=1_{\{4\}}(N_v),
\qquad
H_{mathrm{global}}=P_4\left(N_u+\frac12\right).
\]

This is a bounded spectral projector followed by an unbounded conditional
generator. It is not a finite polynomial in \(N_v\).

## Polynomial no-go

If a finite polynomial \(p\) represented \(P_4\) on the completed even grade
tower, it would vanish at every grade

\[
0,2,6,8,10,\ldots
\]

while satisfying \(p(4)=1\). A nonzero finite polynomial cannot have infinitely
many roots. Therefore no stable finite-degree polynomial selector exists.

At cutoff \(2k\), Lagrange interpolation gives an exact selector of degree
\(k\). The degree grows with the cutoff, so the finite repairs do not stabilize
inside the polynomial Weyl algebra.

## Refined executable alternatives

There are now two sharply different contracts:

```text
code-relative quartic control
  selector grades: 2 and 4
  required invariant: state and all intervening operations preserve code support
  gate degree: four

global spectral control
  active grade: 4
  spectators: identity
  required constructor: spectral functional calculus for N_v
  required domain: domain of P_4(N_u+1/2)
```

Neither contract follows from the other. In particular, exact behavior on the
code cannot be promoted to a global capability without proving support
invariance or supplying the spectral projector.

## Tower interpretation

This is another presentation-versus-object distinction. Cutoff Lagrange
polynomials are charts for the projector, not a stable constructor. The global
object is the spectral idempotent. Completion forces a change from polynomial
control data to functional-calculus data.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/global_grade_selector_no_go_checks.py
```

The checker constructs exact cutoff selectors through grade twenty-four and
verifies their strictly increasing degree.
