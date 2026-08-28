# Channel Access Cannot Construct the Controlled Metaplectic Sign

## The phase-erasure interface

A unitary operation exposed only as a physical channel is

\[
\mathcal U_U(\rho)=U\rho U^\dagger.
\]

It identifies every pair \(U\) and \(e^{i\phi}U\). In particular,

\[
\mathcal U_I=\mathcal U_{-I}.
\]

Thus a compiler whose only input is the endpoint conjugation channel receives
exactly the same input for the trivial lift and the nontrivial metaplectic
central lift.

## Controlled outputs do not respect the quotient

Controlled representatives are

\[
C_I=|0\rangle\langle0|\otimes I
+|1\rangle\langle1|\otimes I,
\]

and

\[
C_{-I}=|0\rangle\langle0|\otimes I
-|1\rangle\langle1|\otimes I.
\]

The first is identity on the control; the second is its Pauli \(Z\). They send
\(|+\rangle\) to \(|+\rangle\) and \(|-\rangle\), respectively. Therefore
controlled-unitary formation is not a well-defined operation on projective
unitary channels.

No deterministic channel-level supermap can solve this: identical inputs
cannot be mapped to the two required distinguishable outputs.

## Endpoint consequence

Entry 3703 showed that a controlled central action would expose the
metaplectic sign after Hilbert completion. The present no-go locates the first
nonfaithful arrow preventing that construction:

```text
linear metaplectic implementation
  -> conjugation channel
     forgets the central phase
  -> attempted controlled compiler
     cannot reconstruct the forgotten lift
```

The missing contract is not merely “permission to control the channel.” It
must supply a phase-lifted implementation, for example:

- a specified Hamiltonian path whose endpoint is the chosen lift;
- a dilation with a fixed coherent phase reference;
- a primitive controlled implementation whose inactive branch is typed;
- an equivalent source-derived lift through the metaplectic double cover.

Transporting the channel does not transport this authority.

## Higher-tower prediction

Conditionalization is functorial only on a category whose morphisms retain
linear phase, path, or dilation data. It cannot be a functor on the projective
channel quotient. Hence the executable-coherence tower must sit above a
lift-refinement tower:

```text
projective operation
  <- phase-lifted implementation
     <- coherently controllable implementation
```

This predicts the same failure whenever a lower interface quotients a central
datum that a higher conditional constructor would turn into relative data.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/controlled_global_phase_no_go_checks.py
```

The checker exactly verifies equal input channels, distinct controlled
outputs, and opposite control readouts.
