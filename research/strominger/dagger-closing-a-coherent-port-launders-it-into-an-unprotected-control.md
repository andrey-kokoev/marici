# Dagger-Closing a Coherent Port Launders It into an Unprotected Control

## The next obstruction

Separating preparation, protected evolution, and readout by object type is not
yet sufficient if the ambient category freely supplies daggers and all
well-typed composites.

Let (i:E\to S) be a coherent preparation port into a two-sector selector
object. In the selector basis take

\[
i=\begin{pmatrix}1\\1\end{pmatrix}.
\]

The externally visible round trip is the scalar

\[
i^\dagger i=2.
\]

But dagger closure also generates the selector endomorphism

\[
ii^\dagger=
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

which does not commute with the selector projector. A coherent port has thereby
been laundered into an unprotected internal control.

By contrast, a sector-pure port produces a diagonal round trip, but carries no
relative coherence and cannot expose the metaplectic sign.

## Categorical consequence

The desired instrument does not live in an ordinary dagger category whose
ports are freely promoted to endomorphisms by adjunction and composition. It
needs a role-sensitive composition law. Two candidate homes are:

- a colored operad or process theory in which preparation, protected core, and
  readout occupy distinct slots;
- a double category in which protected maps are vertical arrows and ports are
  horizontal correspondences, with only source-declared squares authorizing
  their interaction.

In the second formulation, a companion or conjoint identifying a port with an
ordinary internal arrow must not be inferred automatically. Such an inference
would reproduce the forbidden round trip.

## Refined missing constructor

The source packet must now specify not only objects and arrows but which
composites exist. In particular it must answer:

```text
Is the port dagger available?
May port and adjoint compose inside the selector object?
If a round trip exists, does it land in the protected algebra?
Is a conditional expectation applied, and what coherence does it erase?
```

Thus executable closure is not closure under every type-correct composite.
It is closure under a source-authorized partial composition law.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/coherent_port_dagger_closure_no_go_checks.py
```
