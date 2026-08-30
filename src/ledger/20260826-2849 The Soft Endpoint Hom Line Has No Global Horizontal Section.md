# 2849 — The Soft Endpoint Hom Line Has No Global Horizontal Section

> **Retracted by the occurrence-resolution audit.** The loop around
> \(\kappa=-5/4\) exchanges the two labelled collision occurrences
> \(a=\pm\sqrt{A_+}\); it does not act on a closed positive-sheet rank-one
> object. The rank-zero conclusion below applies only to an anti-invariant
> summand selected after the sheet truncation and cannot close the full
> endpoint comparison. See the subsequent correction entry.

## Surviving question from Entry 2847

Entry 2847 excluded an ordinary base-rational comparison between the two soft endpoint period lines. The remaining possibility was a horizontal section of the twisted local system

\[
\operatorname{Hom}(E_-,E_+).
\]

## Decisive loop

Take a small loop around

\[
\kappa=-\frac54.
\]

At this point

\[
r_+^2=5+4\kappa
\]

has a simple zero. Therefore analytic continuation sends

\[
r_+\longmapsto-r_+
\]

and the positive-endpoint period has character (-1).

Meanwhile

\[
r_-^2=5-4\kappa=10
\]

is a unit. The marked negative-endpoint period is unramified around the same loop and has character (+1).

Consequently

\[
\chi_{\operatorname{Hom}(E_-,E_+)}=-1.
\]

Its monodromy-invariant subspace has rank zero.

## Local versus global

On a simply connected chamber with chosen square-root sheets, the ratio

\[
J=\frac{c_+}{c_-}
\]

is a local horizontal section of the Hom connection. But continuation around the test loop sends

\[
J\longmapsto-J.
\]

Thus the local section does not descend to a nonzero global morphism of the two endpoint local systems.

## Narrow conclusion

The global endpoint-combination hypothesis is closed. Neither an ordinary rational Gysin scalar nor a globally horizontal Kummer-twisted comparison exists over the frozen complex base.

A chamberwise endpoint sum can still be written after choosing physical sheets, but that choice is extra readout data. It is not determined by the marked-relative coefficient geometry established here. The two local endpoint periods remain valid separately.

Reopening this conclusion requires an independently derived physical sheet trivialization or relative-chain pairing whose monodromy cancels the Hom character. A chosen branch convention alone is insufficient.

## Durable artifacts

- `research/benincasa/check_soft_endpoint_hom_monodromy.py`
- `research/benincasa/soft-endpoint-hom-monodromy.json`
