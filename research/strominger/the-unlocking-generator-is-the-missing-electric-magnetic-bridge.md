# The Unlocking Generator Is the Missing Electric-Magnetic Bridge

## Basis-independent localization

In the ordered sheet basis, the selective gate is

\[
Z_{\mathrm{sheet}}=\operatorname{diag}(1,-1).
\]

Pass to the electric/magnetic parity basis using the Hadamard transform. Then

\[
H Z_{\mathrm{sheet}}H^{-1}
=
X_{E/M}
=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Thus the reflection-unlocking term is exactly the mixed dyad

\[
|E\rangle\langle M|+|M\rangle\langle E|.
\]

It exchanges the electric and magnetic character lines and anticommutes with
the reflection-parity operator.

## Why the existing dagger does not supply it

The magnetic source already supplies:

- complementary electric and magnetic projectors;
- both parity readout covectors;
- a source-authorized Hermitian dagger on the Cartan endpoint tower;
- sectorwise dagger round trips.

These constructors remain diagonal in the electric/magnetic decomposition.
Taking a dagger of one port may produce its vector or rank-one projector, but
does not produce the cross term between the two ports. The algebra generated
by the two complementary projectors remains diagonal.

Creating (X_{E/M}) requires a coherent comparison between the two character
sectors. Inferring it from the existence of both ports would repeat the
port-to-control authority laundering of Entry 3752.

## Exact remaining source constructor

The continuous path obstruction of Entry 3773 is therefore carried by one
specific missing source term:

```text
electric-magnetic bridge
  type: reflection-odd self-adjoint endomorphism
  local form: |E><M| + |M><E|
  square: identity on the sheet multiplicity space
  role: generate the reflection-unlocked implementation interface
  authority: independent source interaction, not reconstructed from readouts
```

If supplied, exponentiating this bridge generates a path that leaves the
reflection-fixed locus and reaches the selective projective component. If it
is absent, the endpoint gate remains mathematically defined but physically
unreachable from the established source algebra.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/electric_magnetic_bridge_generator_no_go_checks.py
```
