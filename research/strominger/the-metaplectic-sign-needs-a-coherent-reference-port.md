# The Metaplectic Sign Needs a Coherent Reference Port

## Correction to the observability claim

The endpoint quadratic action has a genuine linear lift obstruction:

\[
Mp(4,\mathbb R)\longrightarrow Sp(4,\mathbb R),
\qquad
e^{-2\pi iH_u}=-I.
\]

This establishes a carrier-level binary datum. It does not establish an
observable binary datum.

For a vector \(\psi\), the two linear states \(\psi\) and \(-\psi\) determine
the same projective ray and the same density operator:

\[
[\psi]=[-\psi],
\qquad
|\psi\rangle\langle\psi|
=
|-\psi\rangle\langle-\psi|.
\]

Moreover, the central sign has trivial adjoint action on every internal
observable \(O\):

\[
(-I)O(-I)^{-1}=O.
\]

Thus the projective and internal-observable readouts both factor through
\(Sp(4,\mathbb R)\). They cannot expose the double-cover sign.

## Exact relative-observability theorem

Adjoin a reference sector \(K\) on which the loop acts trivially. On
\(H\oplus K\), compare

\[
(\psi,\phi)
\quad\hbox{and}\quad
(-\psi,\phi).
\]

Every block-diagonal observation remains blind to the sign. An off-diagonal
observation with a nonzero matrix element between \(H\) and \(K\) changes sign.
Therefore, within this two-sector model, the metaplectic sign is observable
exactly when the admitted observation algebra contains a cross-sector morphism
that pairs the acted-on sector with a coherent reference sector.

The minimum exposing packet has two separately typed pieces:

```text
reference sector: preserves a phase standard outside the metaplectic loop
coherence port: reads an off-diagonal relation between endpoint and reference
```

A reference without the coherence port is insufficient. A coherence port
without a source-authorized reference has no defined relative phase.

## Closure taxonomy

This separates the two closures that had been compressed in the earlier
language:

```text
invariant closure: the linear endpoint action lifts to Mp(4,R)
projective closure: the induced Sp(4,R) action is well defined on rays
executable closure: sign readout needs a reference plus a cross-sector port
```

The first is proved. The second follows automatically by quotienting the
center. The third is conditional: no magnetic source construction has yet
authorized the required reference packet.

The sign is therefore a genuine global lift obstruction but not yet a
source-visible coherence bit. This is the precise failure boundary.

## Hostile tests

The exact checker verifies that:

- vectors distinguish \(\psi\) from \(-\psi\);
- rays, density states, and internal adjoint observations do not;
- a reference sector alone does not help;
- an off-diagonal reference port flips under the central sign.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/metaplectic_sign_observability_checks.py
```

Results are written to
`research/strominger/results/metaplectic_sign_observability_checks.json`.
