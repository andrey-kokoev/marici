# Reciprocal lossy cavity plant

Owner: `marici.Aspect`

## Bounded question

What exact discrete round-trip plant follows from a one-mode two-mirror cavity
when mirror ports, delay, phase, absorption or leakage, and detector
projections remain typed? This packet freezes the physical plant. It makes no
observability, stability, or controller-authority claim.

## Ports and temporal order

At sample `k`, `u_k` is the field incident from the source and `x_k` is the
field returning to the input mirror after the preceding round trip. The input
mirror acts first:

`y_r,k = -r1 u_k + t1 x_k`

`f_k = t1 u_k + r1 x_k`.

Here `y_r` is the reflected detector port and `f` is the forward intracavity
field. After the declared half-trip phase, the end mirror produces

`y_t,k = t2 p f_k`,

`b_k = r2 p f_k`,

where `p` is the calibrated phase factor. The backward field then traverses
the return propagation and the loss dilation. With round-trip delay `T`, phase
`q`, retained amplitude `a`, and loss-port vacuum `w_k`,

`x_(k+1) = a q b_k + ell w_k`,

`y_e,k = -ell b_k + a w_k`,

with `a^2 + ell^2 = 1`. Thus the compressed scalar plant is

`x_(k+1) = A x_k + B u_k + ell w_k`,

`[y_r,k, y_t,k]^T = C x_k + D u_k`,

where

`A = a q r2 p r1`, `B = a q r2 p t1`,

`C = [t1, t2 p r1]^T`, and `D = [-r1, t2 p t1]^T`.

The delay is not erased: `x_(k+1)` is available only after the ordered
mirror-1, forward-propagation, mirror-2, return-propagation, and loss sequence.
The detector rows are projections of the output ports, not state identities.

All scalar optical ports are one-dimensional complex amplitude spaces. Thus
`A:C->C`, `B:C^2->C` for `(u,w)`, `C:C->C^3`, and `D:C^2->C^3` after the
vacuum/environment columns are retained. The displayed compressed equations
show only the driven `u` column and the loss injection into the state; the
four-port dilation in the checker is the authoritative complete feedthrough.

Admissible mirror parameters are real `rj,tj` with `rj^2+tj^2=1` in the
declared common energy normalization. Propagation phases satisfy `|p|=|q|=1`;
loss amplitudes are real nonnegative `a,ell` with `a^2+ell^2=1`. The exact
checker specializes to rational values and phases `p=q=1`, but the symbolic
plant equations above retain the parameter domain.

Before sampling, the returning field obeys the delay relation
`x(t+T) = a q r2 p (t1 u(t) + r1 x(t)) + ell w(t)`, where `T>0` is the
physical round-trip delay and the inputs are understood on compatible delayed
time slices. The discrete recurrence is its exact stroboscopic restriction at
`t=kT`, not a claim that arbitrary continuum dynamics has finite horizon.

## Unitary dilation before compression

Each lossless mirror is an orthogonal two-port scattering matrix after its
ports share an energy normalization. Mirror 2 has an unused exterior input
`v2`; the attenuation stage has environment input `w`. Composing mirror 1,
mirror 2, and the loss beam splitter maps `(u,x,v2,w)` to
`(y_r,y_t,x_next,y_e)`. The exact checker proves this four-port map is
orthogonal for rational 3-4-5 coefficients. Dropping `v2`, `w`, and `y_e` is a
loss compression, not a unitary evolution on the retained ports.

## Three exact witnesses

These are also the smallest hostile falsifiers for claims that a dark scalar
erases storage, that a single analyzer is faithful, or that reciprocity can be
tested without a common energy metric.

### Dark measured port with stored field

Choose `(u,x)=(t1,r1)`. Then `y_r=0`, while `f=t1^2+r1^2=1`. A dark reflected
port therefore coexists with nonzero intracavity energy.

### Scalar-equivalent readouts with distinct internal state

For the minimal polarization extension, one analyzer row `h=(1,0)` maps both
Jones states `(1,1)` and `(1,-1)` to the same scalar amplitude. Their hidden
polarization components differ. Replacing `h` by another single nonzero row
only rotates its one-dimensional kernel; it does not repair faithfulness. Two
linearly independent analyzer rows, here `H=[[1,0],[0,1]]`, are the smallest
jointly faithful readout. The analyzer map has source `C^2` and target `C` for
one row, or target `C^2` for the jointly faithful pair.

### Reciprocity requires a common energy metric

A reciprocal mirror matrix is symmetric in common energy-normalized port
coordinates. Under unequal coordinate scaling `D`, its displayed matrix is
`S'=D S D^-1`. It need not satisfy Euclidean symmetry. With the transported
energy metric `G=D^-T D^-1`, it instead satisfies `G S' = S'^T G`. The checker
exhibits a nonzero Euclidean adjoint residual and zero metric-adjoint residual.
Any reciprocal-adjoint claim that omits the common metric is therefore
ill-typed.

## Frozen handoff to control audit

The handoff plant is the scalar delayed state `x`, input `u`, environment
input `w`, outputs `(y_r,y_t,y_e)`, and matrices `A,B,C,D` above, together with
the ordered component list and energy metric. These data authorize a later
control audit; they do not themselves establish observability, stability,
well-posed feedback, or controller authority.

## Verification and limitations

Run `python research/aspect/checkers/reciprocal_lossy_cavity_plant.py`.
The checker writes
`research/aspect/results/reciprocal_lossy_cavity_plant.json`.

This is a one-mode sampled, exactly calibrated plant. It omits linewidth
limits, continuum temporal modes, quantum noise statistics, nonlinear mirror
response, and a controller.

## Completion gate

Continuum promotion requires the physical delay-state history space, causal
input/output boundary conditions, a bandwidth-uniform propagation and loss
law, detector impulse responses, and cutoff-independent storage and error
bounds. The frozen recurrence is exact only on its declared stroboscopic
single-mode class.
