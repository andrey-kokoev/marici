# The Metaplectic Sign Has a Four-Capability Minimal Instrument

## Instrument contract

The endpoint metaplectic sign is observable when the following four
capabilities are jointly present:

```text
PhaseLift
  retains the linear representative I or -I rather than only its channel

CoherentPreparation
  prepares a selector with nonzero coherence between active and inactive branches

ConditionalCoupling
  applies the lifted endpoint operation on the active branch and identity on the inactive branch

ComplementaryReadout
  measures selector coherence in a basis sensitive to the relative branch phase
```

For a two-level selector, the canonical realization is

\[
|+\rangle
\xrightarrow{C_z}
\begin{cases}
|+\rangle,&z=+I,\\
|-\rangle,&z=-I,
\end{cases}
\xrightarrow{X\text{ readout}}
\begin{cases}
+1,\\
-1.
\end{cases}
\]

This proves sufficiency independently of endpoint dimension and endpoint state.

## Hostile deletion theorem

Each capability is individually necessary within this interface model:

- Without `PhaseLift`, \(I\) and \(-I\) enter as the same conjugation channel.
- Without `CoherentPreparation`, a branch-basis selector acquires no observable
  relative phase.
- Without `ConditionalCoupling`, both selector branches undergo the same
  endpoint operation.
- Without `ComplementaryReadout`, branch-population measurements give the same
  result for \(|+\rangle\) and \(|-\rangle\).

The exact checker deletes each port separately and recovers blindness in every
case. The packet is therefore deletion-minimal, although other physically
equivalent realizations may package the same four roles differently.

## DPC form

```text
D — Domain
  completed endpoint Hilbert space H
  finite selector Q
  admitted tensor product Q tensor H

P — Predicate
  distinguish the two linear lifts over one projective endpoint channel

C — Constructor packet
  PhaseLift + CoherentPreparation + ConditionalCoupling + ComplementaryReadout

Decisive falsifier
  delete any one constructor while preserving the other three;
  the two lifts must become operationally indistinguishable
```

## Source status

The quadratic source algebra supplies the mathematical `PhaseLift`. It does not
supply the remaining executable ports. The internal Gaussian-control route to
those ports is excluded by Entries 3718, 3725, and 3727.

Thus the first complete sign instrument is presently a typed conditional
extension, not an endogenous magnetic capability.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/minimal_metaplectic_sign_instrument_checks.py
```

The exact checker proves sufficiency and all four single-deletion failures.
