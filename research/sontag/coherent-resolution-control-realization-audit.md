# Coherent Resolution is a static coordinate realization, not yet a control plant

## Question

What control-theoretic content follows from the finite Coherent Resolution without assigning state, actuation, output, feedback, or physical time by analogy?

## Claim boundary

The admitted objects are finite configuration modules, their exact boundary and mixed-curvature coordinates, a tested rational physical kernel, and a boundary-transport deformation coordinate. This packet proves a finite-cutoff static realization theorem and an obstruction to promoting it to a dynamic control system. It does not assert a nonlinear or continuous plant, a completed system, physical time, controllability, dynamic observability, feedback stability, or robustness.

## Problem

The phrase “two boundary channels plus bulk curvature” resembles an input/state decomposition, while the tested kernel admits Schur elimination. Neither resemblance supplies a transition law or actuator. The audit must determine what is intrinsic and stop at the first missing typed object.

## Bold conjecture

Coherent Resolution already determines a finite static linear realization: every triangular history field is equivalent, by an integral unimodular coordinate change, to its two characteristic boundary traces together with its interior mixed curvature. Its Schur-complement sign crossover is a correlation/readout crossover, not an invariant zero. Dynamic control claims require additional source-derived maps.

## Named rivals

1. The two boundary traces are a complete two-input realization of every field.
2. Boundary values are the state and bulk curvature is an input.
3. The Schur-complement sign crossover is an invariant-zero crossing.
4. Any matrix factorization of the finite kernel supplies a plant realization.

## Typed finite realization

For cutoff rank `m`, let the configuration module be the free module on intervals

\[
X_m=\mathbb Z\{(i,j):1\leq i\leq j\leq m\}.
\]

Define the descriptor module

\[
D_m=B_m^-\oplus B_m^+\oplus G_m,
\]

where the first summand records the row with `i=1`, the second records the column with `j=m` excluding their shared corner, and `G_m` records interior mixed differences. The source-derived map is

\[
T_m:X_m\longrightarrow D_m.
\]

The exact recurrence reconstructs the field from its descriptor. For `m=2` through `m=10`, the checker finds determinant `+1` or `-1`; hence `T_m` is an integral coordinate isomorphism at each tested cutoff. The existing general recurrence supplies the arbitrary-finite-rank theorem, but no colimit claim follows.

This is not an input/state decomposition. The three summands are jointly faithful coordinates on one configuration object. No summand has a source-derived update law, control authority, or physical-time orientation.

## Strongest falsification attempt

The boundary-only rival fails at `m=3`. The field supported at `(2,2)` has both characteristic boundary traces equal to zero and mixed curvature equal to one. Thus boundary records leave a nonzero kernel whose dimension equals the number of bulk-curvature coordinates. The obstruction is exact, not numerical.

The physical kernel deformation is

\[
K(t)=K_0+t(K_1-K_0),
\]

where `t` is a boundary-transport deformation coordinate, not physical time. Eliminating the middle endpoint gives

\[
e(t)=K_{31}(t)-\frac{K_{32}(t)K_{21}(t)}{K_{22}(t)}.
\]

The checker verifies that `e(t)` changes sign on the admitted segment while `det K(t)` is nonzero and `K(t)` retains rank three at the crossing. Therefore the crossover changes direct-versus-mediated correlation after elimination; it does not create a kernel of the static operator.

An invariant zero would require a source-derived system pencil, for example

\[
\begin{pmatrix}
\lambda I-A & -B\\
C & D
\end{pmatrix},
\]

with typed state, actuation, output, and parameter authority. Coherent Resolution supplies none of `A`, `B`, `C`, or `D` in this sense. Reusing the symbols for incidence maps or coordinate projections would manufacture the conclusion.

## Control verdicts

- **State:** no dynamic state is source-derived. `X_m` is a finite configuration module.
- **Input:** no actuator or admissible intervention family is source-derived. Boundary and curvature data are descriptor coordinates.
- **Output:** the existing scalar augmentation and tested kernel projections are static readouts; faithfulness depends on retaining the complete descriptor.
- **Parameter:** boundary transport is a deformation coordinate. It has no physical-time meaning.
- **Interconnection:** matrix composition, boundary update, and Schur elimination are admitted finite algebraic operations. Feedback is not.
- **Controllability:** undefined without a transition/vector-field family and admissible controls.
- **Observability:** complete static distinguishability holds for the full descriptor `T_m`; boundary-only distinguishability fails. Dynamic observability is undefined.
- **Minimal realization:** the full static descriptor has rank `dim X_m`; the boundary-only projection is nonminimal as a faithful representation because it quotients the bulk-curvature kernel. No dynamic minimal-realization theorem is available.
- **Invariant zeros:** undefined for the admitted data. The tested Schur crossover is nonsingular.
- **Robustness:** undefined until a perturbation class, norm, and margin are source-derived. Exact unimodularity is not a noise bound.
- **Completion:** every finite rank has an exact descriptor, but no uniform bounded inverse, cofinal topology, or completed-system theorem has been supplied.

## Disposition

The conjecture survives at finite static strength. Rivals 1–3 are refuted. Rival 4 is rejected as non-source-derived. The first missing typed object is a source-derived transition or vector-field family on a declared state object with admissible actuation and output maps. Acceptance requires those maps, their parameter domain, and a proof that the physical kernel is their transfer or static response without fitting. Until then Coherent Resolution is a coordinate architecture, not a control plant.

Verification:

- `research/sontag/checkers/coherent_resolution_control_audit.py`
- `research/sontag/results/coherent_resolution_control_audit.json`
- source inputs: `research/nima/check_nnmhv_characteristic_boundary_reconstruction.py`, `research/nima/results/nnmhv-kernel-wall-tail-boundary.json`, and `research/nima/check_nnmhv_schur_reflow_bridge.py`
