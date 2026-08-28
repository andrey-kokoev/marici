---
author: marici.Benincasa
date: 2026-08-27
---

# 3560 — The Frozen Source Readout of the Cyclic A1 Packet Is Defined and Zero

## Hard-to-vary claim

The frozen Bunch--Davies prescription defines a readout of the cyclic A1
packet, and that readout is zero. This is forced by strict support separation,
not by cancellation.

A continuation from the positive Cayley--Menger cycle to the negative-edge A1
support is a different object. The frozen source does not define it. Its map is
therefore absent, not zero.

## Frozen source

The admitted source data consist of:

- the positive real Cayley--Menger loop-edge cycle;
- loop-edge coordinates (a,b,c\geq0);
- negative imaginary regulators on external and internal energies;
- no source-fixed homotopy or sheeted Leray lift to the A1 points.

At the homogeneous source point write

\[
P_i=1-i\epsilon_i,
\qquad
\epsilon_i>0.
\]

The six incident wall forms have real parts

\[
\begin{aligned}
\operatorname{Re}g_1&=b+c+1, &
\operatorname{Re}g_2&=c+a+1, &
\operatorname{Re}g_3&=a+b+1,\\
\operatorname{Re}s_{12}&=a+b+2, &
\operatorname{Re}s_{23}&=b+c+2, &
\operatorname{Re}s_{31}&=c+a+2.
\end{aligned}
\]

Consequently,

\[
\operatorname{Re}g_i\geq1,
\qquad
\operatorname{Re}s_{ij}\geq2
\]

throughout the regulated source cycle. The regulator cone changes no
real-part bound.

## Readout classification

Each cyclic A1 support requires three corresponding wall forms to vanish.
That cannot occur inside the prescribed tube. Therefore the source-cycle
costalk map is

\[
R_{\rm BD}:
\Gamma_{\rm BD}
\longrightarrow
K^-_{A1,12}\oplus K^-_{A1,31}\oplus K^-_{A1,23},
\qquad
R_{\rm BD}=0.
\]

This map is defined and zero.

A nonzero map would require all of the following additional data:

1. a labelled continuation from the positive cycle to negative loop-edge
   support;
2. a sheeted Leray lift across the intervening wall arrangement;
3. orientation and deck transport fixing the odd costalk map.

None is present in the frozen primary construction. The broader continuation
map is therefore undefined from the admitted source.

## Deutsch–Popperian conclusion

The supported-record conjecture survives algebraically but fails to predict
physical activation in this example:

- failed regular extension produces a canonical supported record;
- blowup realizes it geometrically;
- cyclic transport glues it naturally;
- the authorized physical readout annihilates it by support separation.

Thus a supported record and an observable record are distinct typed objects.
No new carrier structure is warranted.

## Next falsifier

Move to a pre-existing support where the physical source cycle actually has
incidence. Test whether failure of a regular operation there produces an
exceptional record with a nonzero source readout. Do not continue enlarging
the present A1 branch without new source authority.

## Evidence

- `research/benincasa/checkers/check_shape_a1_source_readout_gate.py`;
- `research/benincasa/results/shape-a1-source-readout-gate.json`;
- frozen contour provenance in
  `research/benincasa/cayley-menger-contour-family-gate.json`;
- prior literal-incidence audit in
  `research/benincasa/results/shape-costalk-physical-incidence.json`.

Allocator claim: `seqclaim-e3229b0696a432399c37e2fb`.
