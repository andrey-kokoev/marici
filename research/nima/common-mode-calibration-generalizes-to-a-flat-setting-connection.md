# Common-mode calibration generalizes to a flat setting connection

## Question

Must target and control settings have identical nuisance phases, or can a
known comparison between different nuisance frames suffice?

## Claim boundary

Identical nuisance is sufficient but not necessary. A source-derived
calibration transport between settings permits exact correction. With three or
more settings, those transports must satisfy a flatness condition before they
can be treated as one calibration system.

## Setting frames

Let setting \(i\) have source response \(\omega_i\), nuisance frame
\(\kappa_i\), and observed comparison

\[
z_i=\kappa_i\omega_i.
\]

Define the nuisance transport from setting \(j\) to setting \(i\) by

\[
\eta_{ij}=\kappa_i\kappa_j^{-1}.
\]

Then the corrected relative source response is

\[
\omega_i\omega_j^{-1}
=
z_i z_j^{-1}\eta_{ij}^{-1}.
\]

Common-mode calibration is the special case \(\eta_{ij}=1\).

## Flatness gate

If all setting transports arise from one family of nuisance frames, then

\[
\eta_{ij}\eta_{jk}=\eta_{ik},
\qquad
\eta_{ij}\eta_{ji}=1.
\]

For three settings, the calibration holonomy must vanish:

\[
\eta_{01}\eta_{12}\eta_{20}=1.
\]

A fitted connector for one target-control pair can always reproduce a desired
answer. The triangle is the first test that pairwise connectors arise from one
shared calibration system.

## Gauge behavior

Changing every nuisance frame by a common factor leaves all
\(\eta_{ij}\) unchanged in the abelian phase model. In a noncommutative model,
the transports conjugate according to the chosen left or right action, while
identity holonomy remains invariant.

The connection therefore records relational calibration without choosing an
absolute apparatus phase.

## Exact \(C_4\) model

Write phases additively modulo four:

\[
z_i=\kappa_i+\omega_i,
\qquad
\eta_{ij}=\kappa_i-\kappa_j.
\]

Correction becomes

\[
\omega_i-\omega_j=z_i-z_j-\eta_{ij}.
\]

Exhaustive enumeration verifies this for every source and nuisance assignment.
The hostile connectors

\[
\eta_{01}=0,\qquad\eta_{12}=0,\qquad\eta_{02}=1
\]

are individually legal phase values but violate triangle composition. No
single family \((\kappa_0,\kappa_1,\kappa_2)\) realizes them.

## Cross-sector consequences

- Optical target and control routes need not be physically identical if their
  phase transfer is independently calibrated and flat across settings.
- Flavor source and detector configurations can be compared through matching
  transports, but independently fitted pairwise calibrations do not form one
  experiment.
- Software constructor trees may use distinct normalization contexts when an
  authorized comparison connection composes coherently.
- Boundary-line controls may live in different local frames if the
  determinant-line transports and their triangle identities are
  source-derived.

## DPC

For multi-setting calibration:

1. type each nuisance frame and observed response;
2. derive each required \(\eta_{ij}\) independently of the desired source
   answer;
3. verify inverse and triangle laws;
4. correct relative source responses using the connection;
5. reject pairwise fitted connectors lacking a common frame realization;
6. retain holonomy as the finite falsifier;
7. ask for higher coherence only if transport composition is weak.

## Disposition

The correct general object is a flat calibration connection over setting
space. Common mode is its trivial connection. This removes an unnecessarily
strong equality assumption while adding a precise three-setting falsifier.

## Verification

The checker check_setting_calibration_connection.py exhausts all \(4^6=4096\)
three-setting source and nuisance assignments in \(C_4\), verifies correction,
inverse laws, and flatness, and rejects an unrealizable hostile connector
triangle.
