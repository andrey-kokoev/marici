# Lockstep controller redundancy is a repetition-code complex

Owner: `marici.Kitaev`

## Algebraic formulation

For (n) controller replicas, define

\[
0\longrightarrow\mathbf F_2
\xrightarrow{E_n}\mathbf F_2^n
\xrightarrow{H_n}\mathbf F_2^{n-1}
\longrightarrow0,
\]

where

\[
E_n(b)=b\mathbf1_n,
\qquad
(H_nx)_j=x_j+x_{j+1}.
\]

Then (H_nE_n=0), (operatorname{rank}H_n=n-1), and

\[
\ker H_n=operatorname{im}E_n
=\operatorname{span}\{\mathbf1_n\}.
\]

This is the binary repetition code ([n,1,n]).

## Detection and correction theorem

Its distance is (d=n). Therefore

\[
n\ge s+1
\quad\Longleftrightarrow\quad
\text{every error of weight at most }s\text{ is detected},
\]

and

\[
n\ge2t+1
\quad\Longleftrightarrow\quad
\text{every error of weight at most }t\text{ is uniquely corrected}.
\]

The earlier statements are the first cases:

- (n=2): detect one flip;
- (n=3): correct one flip.

The common-mode error (mathbf1_n) has zero syndrome because it is not a
boundary defect: it is the nonzero logical codeword, acting as logical (X).

## Four-port fanout

After decoding, the command enters the incidence map

\[
F:\mathbf F_2\to\mathbf F_2^4,
\qquad F(b)=b\mathbf1_4.
\]

Thus a controller logical (X) becomes simultaneous inversion of all four
actuator commands. The complete abstract pipeline is

\[
\text{command}\xrightarrow{E_n}
\text{replicas}\xrightarrow{H_n/\mathrm{decode}}
\text{logical command}\xrightarrow F
\text{four actuators}.
\]

## Carrier versus quantum lens

The repetition complex, syndrome quotient, distance theorem, and fanout
incidence map are shared Carrier geometry. The quantum coefficient lens is
needed only to interpret actuator-command inversion as encoded Pauli or CPTP
faults, specify recovery/exRec semantics, and assign interface cost.

## Exact verification

The checker exhausts every word and every error radius for (1\le n\le7),
verifying exactness, (d=n), detection iff (s<n), and correction iff
(2t<n).

## Falsifiers and boundary

- (ker H_n\ne\operatorname{span}\{\mathbf1_n\}).
- A nonzero error of weight below (n) has zero syndrome.
- Radius-(t) balls overlap when (2t<n), or remain disjoint when (2t\ge n).
- Replica faults are correlated, so Hamming weight is not the physical fault
  metric.
- The controller is coherent quantum data, invalidating the classical
  repetition-code lens.

## Artifacts

- Checker: `checkers/check_lockstep_controller_repetition_complex.py`
- Result: `results/lockstep-controller-repetition-complex.json`
- Result SHA256:
  `A24ED5841DB757557C3DEAEC585140E1580D6D50785E0B403DBF26C66A9788D2`
- Graph admission: `ev-000000003505-f2bad01e-6b4f-4688-ae2c-f6d3443f7a6b`
- Ledger: entry 2524, `seqclaim-33212f11b9b370dea5194cb4`
