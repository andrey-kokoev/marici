# Native dual-line adapter: NE works conditionally; NN needs retained context

**Exact test in the existing native five-slot grammar. Not an admitted signed-P/E or whole-octahedron binding.** The source permutations are read from the live native assembly and phase-advance modules, not fitted to the Hopf experiment.

## Inputs and candidate boundary

Reuse the existing `neutron-contrast-electron-transport` and `full-five-channel-candidate` matrices, plus the actual retained electron projector store. Those constructions identify the active-window contrast with a native sector contrast as an explicit candidate assumption. This test inherits that assumption; it does not derive it anew from the five-side operator specification.

The neutron active slots are `[1,2,3]`, the electron active slots `[3,2,4]`. On an ordered active triple `(a,b,c)`, use the existing contrast coordinates

```
z0 = (a-b)/sqrt(2)
z1 = (a+b-2c)/sqrt(6).
```

Retain three additional coordinates: the active mean `(a+b+c)/sqrt(3)` and both outside coefficients. This is an exact unitary decomposition `C^5 = C^2 + C^3`, not a compression of five arbitrary coefficients into a spinor. A zero contrast with nonzero complement has no Hopf ray; it is not a zero retained packet.

## Positive result: the actual NE map reaches the retained spinor source

The native NE row permutation is `[0,4,2,3,1]`. If D_N and D_E are the two contrast readers, its induced contrast map R satisfies

```
D_E Pi_NE = R D_N
R^dagger R = I
 det R = -1.
```

In the complete five-coordinate decomposition, NE acts as this reflection on the contrast and identity on the retained three-coordinate complement.

The determinant minus one matters: R is unitary, not SU(2). Multiplying it by i to obtain an SU(2) matrix would change retained phase and is not justified. For the paired frame `F(z)=[z,Jz]`, the exact rule is instead

```
F(Rz) = R F(z) diag(1, conjugate(det R)).
```

The right-hand determinant correction is retained, not suppressed.

Let J_e be the actual normalized electron encoder and E_frame the existing candidate electron contrast frame. Compute `W=J_e^dagger E_frame` and verify its unitarity and `E_frame=J_e W`. The stored full-five field candidate satisfies the exact matrix identities

```
S_NE B_N = J_e W D_N
(postNE electron block) Pi_NE = J_e W D_N
W R^dagger D_E Pi_NE = W D_N.
```

Thus the candidate NE output really reaches the prior retained electron spinor source, in an explicitly calculated basis. It is not inferred merely from both spaces having dimension two. The remaining three coefficient directions stay in the joint candidate, not in the electron spinor alone.

## Discriminating failure: no fixed two-channel NN adapter exists

The actual NN advance is `[0,3,4,1,2]`. It mixes the chosen contrast with its three-dimensional complement.

A concrete input is

```
v = (0,0,0,0,1).
```

Its incoming contrast is zero. After NN its active slot 2 is one, so its outgoing contrast is

```
(-1/sqrt(2), 1/sqrt(6)), norm squared = 2/3.
```

Consequently there is no fixed complex-linear two-by-two map A satisfying `A D_N = D_N Pi_NN` on the full five-slot domain. In particular, a standalone SU(2) rotation of the extracted spinor cannot implement this reader. The failure is information flow from retained context, not a phase that can be fixed by choosing another gauge.

## Lossless alternative already available

Let T be the full unitary five-coordinate contrast/complement chart. Then

```
T Pi_NN T^dagger
```

is an exact unitary five-by-five update, with nonzero blocks coupling the contrast and complement. The checker retains and exports all its entries and verifies inverse reconstruction and norm preservation.

Alternatively, a co-moving chart `T_next=T Pi_NN^dagger` gives `T_next Pi_NN=T`. This transports the *frame*, rather than claiming the fixed active reader is unchanged. Two NN advances return the coefficient chart but do not erase the distinct absolute native operation history. A future packet implementation must retain that history as well as the coordinates.

## Disposition

The dual-line frame can describe the existing **extracted N contrast and conditional NE output**. It cannot replace the full native five-coefficient packet. The natural next model is a retained spinor/contrast plus its three context coefficients, with explicitly transported frames—not a spinor-only wiring.

Still unbound: the operator's revised signed P/E pair to this five-slot grammar, the source-geometric selection of the candidate window/sector map, the retained occurrence/history adapters, and their simultaneous global/boundary compatibility. No inverse NE execution, particle creation, filling, grouping or rendering is admitted.

## Replay

```sh
python research/strominger/checkers/check_native_dual_line_context_adapter.py --record
```

Only the new receipt `results/native-dual-line-context-adapter-v1/verification.json` is written. Other source stores are checked unchanged. The receipt includes the NE and NN packet matrices, exact source-encoder alignment, invisible-input counterexample and source hashes, with admission flags false.
