# The Selective Projective Gate Is Disconnected from Identity inside the Reflection-Fixed Locus

## Discrete projective character

Let (X) exchange the two magnetic sheets. A projectively
reflection-equivariant unitary (U) satisfies

\[
XUX=\lambda U.
\]

Applying sheet exchange twice forces (lambda^2=1). Hence
(lambda\in\{+1,-1\}). Along any continuous path remaining in the
projectively fixed locus, (lambda) is continuous and therefore constant.

At the identity,

\[
XIX=I,
\]

so (lambda=+1). At the selective gate,

\[
XZX=-Z,
\]

so (lambda=-1). Consequently no continuous projectively
reflection-equivariant path connects ([I]) to ([Z]).

## Why endpoint descent was not enough

Entry 3766 proves that ([Z]) is a well-defined reflection-invariant endpoint.
The present theorem shows that it lies in a different connected component of
the reflection-fixed projective operation space. Endpoint invariance does not
imply invariant constructibility.

The standard phase path

\[
U(t)=\operatorname{diag}(1,e^{i\pi t})
\]

connects (I) to (Z), but at intermediate parameter values it is not a
projective eigenoperator of sheet exchange. It implements the gate only by
departing from reflection symmetry.

## Source consequence

A phase-lifted Hamiltonian path supplied by the magnetic source cannot produce
the selective gate while retaining the same reflection-equivariance contract
at every point. One of the following must be source-declared:

1. a reflection-breaking implementation path whose endpoint restores the
   projective symmetry;
2. a change of carrier or reflection action, not merely an inert ancilla with
   fixed action;
3. a primitive non-Hamiltonian or discontinuous constructor directly between
   the two fixed components.

This is now the first genuine implementation obstruction. Conditionalization
identifies the desired mathematical endpoint, but any continuous realization
must cross a symmetry-breaking interface.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/reflection_equivariant_selective_path_no_go_checks.py
```
