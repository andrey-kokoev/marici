# Free propagation and Green transfer

Owner: `marici.Aspect`

## Bounded question

How should source-to-field propagation be typed so that ordered optical
construction, reciprocal Green transfer, attenuation, detector kernels, and
resonant failure remain distinct? This packet gives a finite exact apparatus;
it does not claim continuum or infinite-time completion.

## Source authority and typed ports

The paraxial ray port is `R^2`, with ordered coordinates `(height, slope)` in a
declared longitudinal frame. Free propagation over signed distance `L` is

`P(L)=[[1,L],[0,1]]`.

A thin lens of nonzero signed focal length `f` is

`F(f)=[[1,0],[-1/f,1]]`.

The source plane, propagation direction, length unit, slope convention, and
lens sign convention are calibration authority. Changing them requires an
explicit coordinate transport; identical displayed matrices in incompatible
frames are not the same apparatus.

The constructor order acts right to left. Propagation composes as
`P(L2)P(L1)=P(L1+L2)`, but a lens and a nonzero propagation generally do not
commute. Their determinant-one property preserves the oriented paraxial phase
area. It does not preserve Euclidean ray length and is not by itself an energy
statement.

## Green transfer

For a frozen frequency and boundary condition, let `K:S->F` be the discrete
wave operator from field amplitudes to source amplitudes. When `K` is
invertible, `G=K^-1:S->F` is the Green transfer and `field=G source`.
Reciprocity is a typed comparison between exchanged source and detector ports
in a common energy metric. In the exact two-port witness

`K=[[2,-1],[-1,2]]`, `G=(1/3)[[2,1],[1,2]]`

is symmetric. The directed-coupling hostile

`K_nr=[[2,-2],[-1,2]]`, `G_nr=[[1,1],[1/2,1]]`

is invertible but not reciprocal in the displayed common coordinates.
Invertibility alone therefore does not imply reciprocity.

## Loss and environment

A retained amplitude `a` is not a closed one-port unitary when `|a|<1`.
Introduce an environment port with amplitude `ell` and
`a^2+ell^2=1`. The two-port dilation

`[[a,ell],[-ell,a]]`

preserves total intensity. For the 3-4-5 witness, the retained probability is
`9/25`, the environment probability is `16/25`, and their sum is one.

## Detector projection and smallest hostile

A detector row `h:F->R` observes only its declared scalar. The fields
`(1,1)` and `(1,-1)` have the same value under `h=(1,0)` while their hidden
components differ. A scalar-preserving detector output therefore cannot
identify the propagated field. Two independent rows are minimally faithful on
the declared two-dimensional real field class; they remain blind to degrees
of freedom excluded before that class was declared.

## Resonance and completion gate

At `K_res=[[1,-1],[-1,1]]`, the determinant vanishes. There is no bounded
inverse on the full source space: the common mode is a null field direction,
and incompatible sources need not have solutions. Regularization, radiation
conditions, causal prescriptions, finite bandwidth, and limiting absorption
are additional constructors rather than repairs inferred from a finite matrix.

Completion requires a declared frequency domain, boundary/radiation
condition, source and detector function spaces, convergence mode, and a
uniform resolvent bound away from or through named singularities. A finite
frequency witness proves none of these continuum or infinite-time gates.

## Hostile dispositions and claim boundary

- Reordering a lens and propagation without transporting the frame changes
  the map and is rejected.
- Calling an invertible directed Green operator reciprocal is rejected by its
  nonzero transpose residual.
- Dropping the environment while claiming retained intensity conservation is
  rejected by the exact missing probability.
- Identifying fields from one detector scalar is rejected by an explicit
  kernel pair.
- Inverting the resonant operator on the full source space is rejected by its
  zero determinant.

Run `python research/aspect/checkers/free_propagation_green_transfer.py`.
The result is
`research/aspect/results/free_propagation_green_transfer.json`.
