# Reciprocal lossy-cavity control audit

Owner: `marici.Sontag`

Physical plant owner: `marici.Aspect`

## Frozen source and compatibility preflight

This audit consumes `research/aspect/reciprocal-lossy-cavity-plant.md` and its
6/6 exact checker without changing a port, coefficient, parameter, metric, or
temporal order. The state is the one-dimensional returning amplitude `x`;
inputs are incident field `u` and loss-environment field `w`; complete outputs
are reflected, transmitted, and loss-environment amplitudes. The sampled order
is input mirror, forward phase, end mirror, return phase, loss dilation, next
state. All displayed numerical coefficients use the same rational calibration
and phases `p=q=1`.

The frozen sampled plant is

`x+=36/125 x + 48/125 u + 4/5 w`,

with state-output column `C=(4/5,9/25,-48/125)^T` and incident feedthrough
`D_u=(-3/5,12/25,-64/125)^T`.

## Exact sampled-system disposition

Well-posedness holds in open loop because the ordered optical constructor has
no unresolved algebraic signal. Incident-port controllability holds because
`B_u=48/125` is nonzero. Each individual physical detector row is already
state-observing for the scalar cavity state because every entry of `C` is
nonzero; the minimum state-output history is therefore one sample. Detectability
follows from observability, not from stability.

The homogeneous pole is `A=36/125`, strictly inside the unit disk. Hence the
sampled scalar state is asymptotically stable. The four-port unitary dilation
supplies the source-derived storage law, with `V(x)=|x|^2`:

`V(x+)-V(x)=|u|^2+|w|^2-|y_r|^2-|y_t|^2-|y_e|^2`.

This identity is verified from the complete dilation, not fitted by solving a
Lyapunov equation after seeing the plant.

## Dark reflected-port locus

The reflected amplitude is `y_r=(4/5)x-(3/5)u`. Its dark locus is
`x=(3/4)u`. For every nonzero `u` on this locus the state is nonzero and the
forward intracavity amplitude is `(5/4)u`; at Aspect's witness
`(u,x)=(4/5,3/5)` it equals one. Scalar darkness therefore does not imply zero
state. It also does not contradict state observability: with known `u`, the
same detector equation reconstructs `x` away from no parameter at this frozen
calibration.

## Polarization analyzer is a different source object

The cavity state above is scalar. Aspect's Jones extension has source `C^2`.
One analyzer row has a one-dimensional kernel; replacing it by another single
row rotates rather than removes that kernel. Two independent analyzer rows are
minimal for polarization faithfulness. This does not lengthen the scalar
cavity-state history: it repairs a different source type.

## Feedback well-posedness and hostile

For positive output feedback `u=v+K y`, a chosen detector feedthrough `D`
requires the scalar solve `1-KD` to be nonzero. At the reflected port
`D=-3/5`, the singular locus is `K=-5/3`; at the transmitted port `D=12/25`,
it is `K=25/12`. Forming a closed-loop state matrix on either locus is
prohibited. Away from it the algebra is well posed, but no controller authority
or closed-loop stability is inferred here.

## Required hostiles

1. The physical dark locus above gives zero reflected amplitude with nonzero
   state and stored field.
2. Appending an unactuated, unobserved marginal coordinate `h+=h` preserves the
   stable external cavity transfer while making the realization nondetectable.
   This minimal countermodel refutes transfer stability implying internal
   stability; it is not part of Aspect's plant.
3. The reflected feedback gain `K=-5/3` makes the loop solve singular.
4. For a lossless high-finesse Pythagorean family
   `t1=2n/(n^2+1)`, `r1=(n^2-1)/(n^2+1)`, with compatible unit-modulus phases,
   every finite `n` has full scalar reflected-port observability. For a fixed
   horizon `N`, however, its Gramian satisfies
   `W_N=t1^2 sum_(k=0)^(N-1)|A|^(2k) <= N t1^2`, which tends to zero as
   `n` tends to infinity. Rank is therefore not a uniform observability bound.

## Continuum-delay completion

The exact relation is `x(t+T)=A x(t)+B_u u(t)+B_w w(t)`. The sampled
well-posedness, port energy balance, and contraction statement survive at
stroboscopic times. For the homogeneous delay equation, every shift by `T`
multiplies the history norm by `|A|`, so exponential decay per round trip
survives when `|A|<1`; its rate collapses as high finesse drives `|A|` to one.

One instantaneous scalar observation cannot reconstruct the continuum delay
state, which is an initial history on an interval of length `T`. A complete
detector trace over one full delay window reconstructs that history when its
state coefficient is nonzero. Thus one-sample observability is retained only
for the stroboscopic scalar realization, not silently promoted to the delay
state space.

## Verdict and limitations

The frozen numerical plant has exact open-loop factorization, incident-port
controllability, one-sample scalar observability, detectability, strict sampled
stability, and a source-derived storage/supply identity. Feedback is
parameter-stratified by the loop-solve denominator. Uniform observability and
continuum instantaneous-state reconstruction are obstructed.

This audit does not cover quantum noise statistics, nonlinear response,
linewidth asymptotics beyond the declared family, controller synthesis, or
arbitrary continuum temporal modes.
