# Photon one-direction trial: a retained mode, not an isolated edge

## Result

**A one-direction packet works for a selected cyclic mode of the actual retained photon candidate.** Its phase varies while its spectral mode remains fixed:

\[
[\ell_+;d_{\mathrm{phase}}],\qquad v=\lambda g_+,\quad |\lambda|=1.
\]

This is an invariant sector of the actual source continuation, not an arbitrary one-parameter curve cut from a non-invariant family. The supporting complex and the selected-mode label remain essential.

The full independent complex mode pair does not fit this one-direction presentation: at fixed positive norm it has three independent real directions. This trial therefore does not establish a universal one-tuple for every photon configuration.

Eighteen exact checks pass. A fresh native replay in a temporary tree also passes its seventeen checks and reproduces the complete existing source receipt, including its source hashes. Native owner files and receipts remain unchanged.

## Actual source

The source is Strominger's retained two-face seed:

    A -> B -> C -> A
    B -> A -> D -> B

Its six-occurrence order is (AB,BC,CA,BA,AD,DB). Its cell complex is a two-triangle disk with shared edge AB, not a one-simplex. The dimension of this retained cell complex is distinct from the configuration dimension tested here.

The existing continuation K has K[b,a]=1 when target(a)=source(b), and its supplied modes obey

\[
Kg_+=\omega g_+,\quad Kg_-=\bar\omega g_-,\quad
\omega=(-1+i\sqrt3)/2,\quad K^3g_\pm=g_\pm.
\]

These are cyclic mode labels. The source alone does not derive physical helicities, a continuous spatial rotation action, null momentum or photon preparation. Later conditional Maxwell/Lorentz/Fock adapters import additional structure; this trial does not replay or silently inherit those physical assumptions.

Primary sources:

- `research/strominger/photon-shared-edge-seed.md`
- `research/strominger/results/photon_shared_edge_seed.json`
- `research/nima/photon-two-packet-construction.md`
- `research/nima/results/photon-two-packet-candidate.json`

## Recoverable fixed-mode interface

The trial reconstructs K from the actual arrow registry and its plus-mode spectral projector from a polynomial in K. The other real eigenvalues satisfy x²-x-1=0, so they are removed by that quadratic, without introducing sqrt(5).

The resulting rank-one projector factors as P+=g+ L+, with

\[
L_+g_+=1,\qquad L_+K=\omega L_+,\qquad
P_+^2=P_+,\qquad KP_+=P_+K=\omega P_+.
\]

For unit phase lambda, define

\[
i_\lambda=\lambda g_+,\qquad
o_\lambda=\bar\lambda L_+.
\]

These typed linear maps obey

\[
o_\lambda i_\lambda=1,\qquad
i_\lambda o_\lambda=P_+,\qquad
(i_\lambda o_\lambda)^2=i_\lambda o_\lambda.
\]

The source encoder, decoder, continuation and fourfold recovery identities therefore admit a concrete one-direction interface on this selected mode. These are exact linear capability identities, not an apparatus or physical emission derivation. The analogous conjugate sector can be constructed from the conjugate projector.

## A real one-parameter chart

Write j=i sqrt(3), so j²=-3. Then

\[
\lambda(t)=\frac{1-3t^2+2tj}{1+3t^2}
\]

has unit modulus for every real t and a nonzero derivative at t=0. It covers the phase circle except -1. A second chart -lambda(t) covers that point; overlap is t -> -1/(3t).

The native step is the actual chart endpoint lambda(1)=omega. K acts on the selected mode as lambda -> omega lambda, and three steps recover the full amplitude.

The continuum of phase states and arbitrary phase preparation/transport must be distinguished from the native three-element phase subgroup. The existing K supplies the latter. The trial explicitly supplies the general phase-family port maps rather than claiming every continuous phase operation was derived from finite incidence.

## A second one-direction family already in the retained real plane

Write g+=u+jw. In v=a u+b w, the source averaged invariant metric is diag(3,1). The normalized real-plane family

\[
v=\operatorname{Re}(\lambda g_+),\qquad
3a^2+b^2=3
\]

is also one-dimensional and preserved by K. Its conjugate modal coefficients are tied: they are lambda/2 and bar(lambda)/2. It does not allow two independent complex polarization amplitudes.

This family is distinct from varying common phase on one complex mode. A later physical adapter may interpret these real-plane variations as polarization changes, but that interpretation is not derived by this cyclic source test.

The invariant metric is an explicit source averaging convention, not a derived physical energy or Born metric. The trial reproduces the source hostile: g++g- has counting norm squared 18 before K and 12 afterward. The naive six-slot counting norm cannot silently replace the invariant logical metric.

## Why the shared edge alone fails

Both g+ and g- restrict to the same shared-edge occurrence values:

    (AB,BA) = (1,-1).

After K their shared-edge values differ by omega versus bar(omega). Thus no deterministic shared-edge-only continuation reproduces both full modes.

The same failure occurs within the normalized real plane, without changing the mode-family context. Choose lambda=(1+j)/2 and lambda=(1-j)/2, and take real parts. Both have

    (AB,BA) = (1/2,-1/2),

but after K their first shared-edge coefficients are -1 and 1/2, respectively. The erased information is consumed by the very next native continuation.

A selected-mode label plus the retained complex can resolve information that the bare edge lacks. This is precisely why `[label; direction]` is stronger than an unlabelled segment or its two endpoint values.

## Does this make the photon a 1-simplex?

A local phase arc from g+ to omega g+ can be represented by an oriented edge with two endpoints. Three native steps form a cyclic return. The continuous connecting arcs are supplied, not physical time evolution extracted from the incidence data.

The whole phase circle is not a single interval. The retained two-triangle disk is not replaced by one edge. Neither a discrete three-step equality nor a drawing supplies all higher path/filling witnesses.

The bounded conclusion is:

> A one-direction fixed-mode packet with a retained supporting complex is viable. A bare shared-edge representation of the whole candidate is not faithful.

## Fair comparison with the electron trial

A fixed normalized electron mode also has a one-phase family. The difference in the tested native interfaces is operational: the photon source continuation preserves a spectral line, whereas the full electron binary tetrahedral action does not preserve a one-complex-dimensional carrier.

If both photon modes receive independent complex coefficients, the positive-norm logical state family has three real directions, just like the full normalized electron-like C² carrier. The checker constructs three normalized rational curves and verifies independent tangent rank three. Consequently photon n=1 versus electron n=3 is defensible only with an explicit sector/interface distinction, not by counting differently restricted state families without disclosure.

For n=1 the proposed certificate accounting gives 1+1+1=3. This is not a native arrow count, photon energy or mass; it neither derives nor refutes masslessness.

## Reproduce

    python research/voevodsky/checkers/check_photon_one_direction_trial.py

Result: `research/voevodsky/results/photon-one-direction-trial-v1.json`.

The checker verifies fresh source pins, isolated native replay, actual registry continuation, spectral projector/decoder, phase charts, native returns, recoveries/fourfold identities, invariant real-plane norm, both edge-erasure hostiles, full-mode tangent rank and unchanged bound inputs. Verification is exact finite algebra with declared curve samples and all-input linear identities, not proof-assistant certification or a physical photon identification.

The existing Three.js page has not been changed by this trial.
