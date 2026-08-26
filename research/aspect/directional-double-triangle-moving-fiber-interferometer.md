# Directional double-triangle moving-fiber interferometer

Owner: `marici.Aspect`

## Bounded question

What is the smallest coherent optical instrument that distinguishes four
claims which must not be conflated: horizontal forgetting of marked modes,
an allowed elliptic-to-marked extension, holonomy internal to the marked
kernel, and failure of global relative gluing?

The finite instrument is motivated by Benincasa Entry 2919.  It is an optical
coherence witness for the required block structure, not a construction of the
double-triangle Gauss--Manin connection from geometric source data.

## Source authority and typed ports

Use four calibrated coherent modes in the ordered frame

`(k_1,k_2,e_1,e_2)`.

The `k` modes are the two marked-path imbalances of two triangular
interferometric cells.  The `e` modes are two compact loop modes shared by the
double triangle.  Forgetting the marks is the fixed projection

`R=[0 I_2] : K direct-sum E -> E`.

The infinitesimal moving-fiber connection is

`A_total=[[A_K,B],[0,A_E]]`,

with

`A_K=[[0,1],[-1,0]]`,
`A_E=[[0,2],[-2,0]]`,
`B=[[1,0],[1,1]]`.

All entries are fixed before detector selection.  The lower-left block is
zero; the upper-right block is deliberately nonzero.

## Horizontal forget-marks law

The checker verifies exactly

`R A_total=A_E R`.

Equivalently, for the first-order calibrated transport
`T(epsilon)=I+epsilon A_total`,

`R T(epsilon)=(I+epsilon A_E)R`.

A marked-kernel input therefore produces no elliptic output under
infinitesimal transport.  This is the forbidden direction.  Conversely, an
elliptic input may produce a marked output through `B`; that response measures
the permitted extension and does not violate horizontality.

## Constructor order and phase frame

Prepare a typed port, apply the parameter-displacement transport, then project
or analyze.  Applying `R` before transport discards the marked extension and
cannot test horizontality of the full system.  All four coherent output
amplitudes must be measured in one phase frame.  Intensity-only detection
cannot reconstruct the signs in `A_K`, `A_E`, or `B`.

## Kernel holonomy and torsion fixture

One closed parameter loop is represented on the marked kernel by the exact
quarter-turn

`H_K=[[0,-1],[1,0]]`.

It satisfies `H_K^2=-I` and `H_K^4=I`.  Thus the instrument contains a finite
order-four kernel-holonomy fixture.  It demonstrates how torsion would be
detected, but it does not assert that the geometric double triangle has this
holonomy.  A generic shear fixture is also checked to have infinite order and
therefore separates persistence from finite torsion.

## Global gluing discriminator

An admissible overlap transport must preserve the kernel of `R`.  The good
transition

`G_good=[[P,Q],[0,I]]`

has that property.  The hostile transition

`G_bad=[[I,0],[L,I]]`, with nonzero `L`,

maps a marked input into the elliptic quotient and gives `R G_bad != R`.
Hence local triangular connection matrices do not establish a global
relative Gauss--Manin extension unless every chart transition preserves the
forget-marks morphism and the overlap cocycle closes.

## Detector family and smallest hostile

Two elliptic homodyne rows after marked preparation are the minimal detector
for the forbidden lower-left block.  Two marked rows after elliptic
preparation detect the allowed extension `B`.  Complete four-port coherent
tomography distinguishes both simultaneously.

The smallest hostile to horizontality is one marked input whose transported
elliptic amplitude is nonzero.  The checker inserts an exact unit lower-left
coupling and records the nonzero horizontal residual.  The smallest global
hostile is `G_bad`, which preserves invertibility but not the kernel of `R`.

## Conserved and dissipated quantities

This connection model tracks coherent amplitudes and directional subspace
transport.  It does not claim that `I+epsilon A_total` is exactly unitary for
finite `epsilon`; the nonzero extension block makes that especially clear.
A laboratory realization must add a unitary dilation or measure its bath
ports before asserting power conservation.

## Completion gate

The packet does not construct the double-triangle marked divisor, derive its
connection, prove that its kernel holonomy is order four, or establish global
chart transitions.  Benincasa must supply those source matrices.  The optical
instrument supplies exact acceptance tests: zero forbidden block, measured
allowed extension, kernel-restricted loop holonomy, and overlap compatibility.

Run
`python research/aspect/checkers/directional_double_triangle_moving_fiber_interferometer.py`.
The result is
`research/aspect/results/directional_double_triangle_moving_fiber_interferometer.json`.
