# Symplectic neutral connector: exact relation and restoring-law test

## Question and scope

The operator proposes a neutron-like role stabilizing a path and its reverse, analogous to a neutral wire in two-way symplectic connectivity. This experiment tests the saved five-coordinate reference maps before identifying that role with a physical neutron.

Active obligations: attachment transport for the canonical relation and route/coherencer compatibility for reversal/composition. The auxiliary dynamical calculation is a separate declared model, not native particle progression. Initial protocol: `inputs/symplectic-neutral-connector-protocol-v1.json`.

The carrier is V=C^5, regarded as ten real reference coordinates `(q,p)=(Re(z),Im(z))`, with

\[
\omega(z,w)=\operatorname{Im}(z^*w),\qquad
J=\begin{pmatrix}0&I_5\\-I_5&0\end{pmatrix}.
\]

This mathematical form is declared. Real and imaginary amplitudes are not thereby derived physical positions/momenta. It is not an identification of the native P/N/E 36/36/8-coordinate carriers. Positive Euclidean reference norm and unit penalty strength are additional inputs; no physical coupling, energy unit or physical-time map is supplied.

## Actual source operations

The checker reads and verifies the fresh cavity receipt, collects its native PN/inverse-PN and NE factors, retains the conditional comparison T, and parses the declared source N reader advance. Four distinct five-coordinate permutations are tested:

- PN/inverse-PN: `[3,1,2,0,4]`;
- NE: `[0,4,2,3,1]`;
- N reader advance: `[0,3,4,1,2]`;
- conditional cavity comparison T: `[2,1,0,4,3]`.

Eight complete saved PE factor products are checked against their recorded endpoint maps. T's conditional admission is not changed, and algebraic inverses are not registered as native reverse operations. Absolute origins and histories are not reset when a coefficient matrix returns to identity.

All four maps are orthogonal on the real reference space and preserve J. This is expected for their complex permutation representation; it does not distinguish a neutron from P/E operations.

## Reversible neutral boundary relation

For a source map S, put opposite orientations on the boundary ports:

\[
\Omega_\partial=\omega\oplus(-\omega),\qquad
L_S=\{(x,Sx):x\in V\}.
\]

The graph has real dimension10 in a20-dimensional space and

\[
\omega(x,x')-\omega(Sx,Sx')=0.
\]

It is therefore Lagrangian. Endpoint swap is antisymplectic for this oriented boundary form and carries the graph to the inverse relation. The symplectic adjoint `J^-1 S^T J` is exactly S^-1. Correct reverse composition reverses factor order; using the same order is rejected on the noncommuting N/T pair.

“Neutral” here means cancellation of the signed boundary pairing, not electric charge zero, a zero signal, or a derived electrical current law. The relation preserves the complete reference input.

## A restoring candidate is extra structure

Declare

\[
H(x,y)=\tfrac12\|y-Sx\|^2,\qquad B=(-S\ I),\qquad K=B^TB.
\]

For all four source maps, `BB^T=2I`, `rank(K)=10`, `K^2=2K`. The penalty vanishes on the connector graph. Its Hessian has ten zero modes and ten eigenvalues2. Zero modes retain arbitrary matched signals; they are not a nuclear binding gap or an energetic preference among isotope configurations.

Three typed uses of this penalty give different answers:

| Structure | Exact effect on mismatch d=y-Sx | Interpretation |
|---|---|---|
| Opposite-sign boundary form | d is constant; auxiliary trajectories shear | Boundary balance does not restore disagreement |
| Same-sign two-copy dynamical form | d'=-2Jd | Bounded reversible relative oscillation, not attraction |
| Auxiliary gradient step of size1/4 | d maps to d/2 | Relaxation, but not symplectic on the retained two-port space |

The boundary form and dynamical form serve different types. They are not interchangeable sign conventions to tune an answer. Neither has been derived as the physical neutron phase-space structure.

### Opposite-sign form: a shear

For `A_partial=-Omega_partial K`, exact identities give

\[
A_\partial^2=0,\qquad BA_\partial=0,\qquad
F(s)=I+sA_\partial.
\]

Thus mismatch and penalty remain constant while some trajectories grow linearly in the auxiliary flow parameter s. A tested basis fixture has squared norms3,9,33 at s=1,2,4, with penalty1/2 throughout. The exact nilpotent formula, not extrapolation of those samples, supplies the shear conclusion. Distance to the matched relation is constant; individual matched points have no restoring force against this drift.

### Same-sign product: a reversible relative oscillator

Declare instead the auxiliary dynamical product form `Omega_dyn=omega direct-sum omega`. For `A_dyn=-Omega_dyn K`,

\[
BA_{\rm dyn}=-2JB,\qquad A_{\rm dyn}^3=-4A_{\rm dyn}.
\]

The common matched modes remain fixed and the relative modes oscillate with constant norm. An exact quarter-turn map

\[
F_{1/4}=I-\tfrac12K+\tfrac12A_{\rm dyn}
\]

preserves this dynamical form and the penalty, has an exact inverse, and satisfies `F_(1/4)^4=I`. This is a mathematical auxiliary oscillator, not four native realization steps or a physical clock. It bounds mismatch but does not make it converge to zero. At zero mismatch the candidate Hamiltonian leaves the matched signal fixed; it does not itself generate the native signal-transfer process.

### Auxiliary gradient: contraction without symplecticity

The step `F_grad=I-K/4` halves mismatch and quarters the penalty. Its determinant is `2^-10`, so it cannot preserve a nondegenerate symplectic form on this closed retained space; direct checks fail for both declared forms. The finite step still has an algebraic inverse, but that inverse amplifies mismatch. No physical relaxation, bath, entropy production or temporal direction is inferred from choosing this auxiliary iteration.

## Hostiles and surviving interpretation

- Scaling one unpaired real coordinate breaks J preservation and makes the graph's boundary pairing nonzero.
- A paired squeeze `diag(2I, I/2)` preserves J but multiplies a selected squared norm by4 per composition. Its symplectic adjoint is the inverse, not its Euclidean transpose. Symplecticity alone therefore does not imply bounded repeated transfer.
- The saved N/T maps do not commute; reverse composition with the wrong factor order fails.
- All eight saved PE products retain their exact source factor maps and pass the same canonical-relation check. No occupied-support permission is added.

The scoped candidate is a **reversible neutral reference connector plus a separately declared positive mismatch law**. The same-sign product model supplies bounded relative stability; the symplectic boundary relation alone does not select that law. Gradient attraction is a different, nonsymplectic retained-space mechanism.

A physical neutron identification would still require a source-derived connection to the actual particle fields, dynamical symplectic structure and Hamiltonian/readout units. Those missing maps are not supplied by a successful reference-space calculation. No isotope stability, charge, binding energy, electron-octahedron geometry or native occupancy law is promoted.

## Reproduction

```sh
python research/strominger/checkers/check_symplectic_neutral_connector.py
```

The checker is dependency-free and uses exact rational arithmetic. `results/symplectic-neutral-connector/verification.json` retains the protocol, source hashes, source-map provenance, canonical-relation identities, all three auxiliary penalty tests and hostile controls. Owner-local SCC model: `symplectic-neutral-connector`. Other-owner sources, native operation lists and viewer admission remain unchanged.
