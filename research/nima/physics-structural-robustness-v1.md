# Structural robustness: uniform regions, conditioning and failure boundaries

## Disposition

Constructed a **partial mathematical witness** for `identifiability-and-robustness-test`. The full node stays open under its existing prerequisite gates. No measurement planning, calibrated nuisance bounds or empirical exclusions are supplied.

Contract: `contracts/physics-structural-robustness.v1.json`.
Checker: `checkers/check_physics_structural_robustness.py`.

The earlier rival table gave exact nominal distinctions. This packet establishes unrestricted inequalities on declared parameter boxes and records aliases outside—and even across—those boxes.

## Detector region

Let efficiency eta and recovery gamma lie in [1/4,1/2], and pre-event readiness r in [1/4,3/4]. These are mathematical regimes, not measured calibration claims.

For initial ready memory, retained memory gives `P(CC|11)=0`, while ready-reset gives `eta²`. For inputs 101, retained memory gives `eta² gamma`, while reset gives `eta²`. Hence the common-parameter gaps obey

```
CC gap  = eta²             >= 1/16
CNC gap = eta²(1-gamma)    >= 1/32.
```

For a photon/no-click, the posterior readiness is

`f(r)=((1-eta)r+gamma(1-r))/(1-eta*r)`.

If no-click is incorrectly replaced by ready memory, the next-photon click discrepancy is

`delta=eta*(1-f(r))=eta*(1-gamma)*(1-r)/(1-eta*r)`.

The derivatives of delta in eta, gamma and r have signs +,-,- respectively. In particular

`d delta/d eta=(1-gamma)*(1-r)/(1-eta*r)²`,
`d delta/d r=-eta*(1-gamma)*(1-eta)/(1-eta*r)²`.

The extrema therefore occur at the corresponding box corners, yielding

`1/26 <= delta <= 9/28`.

Each lower gap exceeds 2/100, so two predictions each enlarged by the frozen 1/100 discrepancy allowance remain disjoint **at a common fixed parameter**. This is not a guarantee for independently fitted nuisance sets.

## Conditioning, without a false repeated-contraction claim

The photon/no-click likelihood obeys `1-eta*r>=5/8`; photon/click likelihood obeys `eta*r>=1/16`. Thus both conditioning steps stay away from zero likelihood in this pre-event box.

The readiness derivative is

`f'(r)=(1-eta)*(1-gamma)/(1-eta*r)²`.

It increases with r and decreases with gamma. At the worst r=3/4 and gamma=1/4, its derivative with respect to eta has sign `2r-1-r*eta`, positive throughout eta<=1/2. Its maximum is therefore

`f'(r)<=24/25`.

The mean value theorem gives a one-step prior perturbation bound `|f(r1)-f(r2)|<=(24/25)|r1-r2|` at fixed eta,gamma. This does **not** prove repeated contraction: the readiness box is not invariant. At eta=1/4,gamma=1/2,r=3/4, the posterior is 11/13, outside the box. Reusing the 24/25 bound at the next event without rechecking the domain would be invalid.

## Optical parameter region

Take squared amplitudes `t1²,a²,r2²` independently in [1/3,2/3], with normalized mirrors/loss and unit-modulus propagation phases. This is a separate regime, **not** a box containing the prior t1=4/5 fixture.

The dark preparation u=t1,x=r1 makes the current reflected amplitude zero and the forward amplitude one. With next external inputs zero, the returning continuation's reflected occupation is

`t1² a² r2²`.

Deleting the stored field predicts zero. The product is between 1/27 and 8/27.

For a unit returning input, deleting the environment output loses squared norm

`(1-a²) r2² (1-t1²)`.

The same [1/27,8/27] bound follows from normalization and the squared-amplitude box. Both lower defects exceed 2/100. Phases change complex amplitudes but not these occupation bounds. The compressed open plant is not rejected; only its false closed-unitary interpretation is.

## Explicit aliases and failure regions

- Efficiency approaching zero makes count-based gaps arbitrarily small. The whole charter does not admit a uniform positive margin.
- At gamma=1 the CNC and no-click-readiness gaps vanish. At r=1 no-click already leaves ready memory.
- At eta*r=0 the click posterior is undefined; at eta*r=1 the no-click posterior is undefined.
- Vanishing optical factors remove the continuation or norm-defect controls.
- A single-bin click law `p=eta*r` does not identify eta and r separately: (1/4,1) and (1/2,1/2) both give p=1/4.
- Even within the detector parameter boxes, **CNC alone aliases independently fitted models**: retained memory with eta=1/2,gamma=1/4 and ready-reset with eta=1/4 both give P(CNC|101)=1/16. A common-parameter gap must not be advertised as full nuisance-set separation. The separate CC coordinate still distinguishes reset from retained memory when efficiency is bounded below.
- Local phase laws alias on total N<=1; CP completions alias on classical memory; discrete component maps retain the logarithm/clock-branch ambiguity from the prior source-law audit.

These are limitations of the claimed inverse/separation scope, not empirical findings. The necessary source and authority gates remain intact.

## Verification

Fresh exact rational checks cover 729 detector parameter points, 6561 prior-perturbation pairs and 729 optical squared-parameter points, plus zero-likelihood, vanishing-margin, cross-parameter alias and box-escape controls. The corner/derivative/product arguments above prove the full-box inequalities; the finite grids only corroborate them.

Corruption controls reject enlarging the regime without a new proof, adding empirical exclusions and dropping the scope limitations. Source hashes are checked before and after execution.

```
python research/nima/checkers/check_physics_structural_robustness.py
python research/aspect/scc/scc.py check physics-programme-v18
```
