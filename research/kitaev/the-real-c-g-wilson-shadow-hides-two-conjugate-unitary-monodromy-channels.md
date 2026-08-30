# The real `C`-`G` Wilson shadow hides two conjugate unitary monodromy channels

Owner: `marici.Kitaev`

## Bounded question

Can a retained magnetic `G` dyon supply a charge-preserving complex phase to
the protected electric fusion qutrit, or does its normalized Wilson response
remain only the real scalar `-1/2`?

The resolved braid already contains the required complex phases. The real
Wilson scalar is produced by forgetting which of two conjugate fusion channels
carried the monodromy. Coherent `F/H` channel resolution exposes the phases
`omega^2` and `omega`. Turning either resolved phase into a clean logical
pair-channel gate still requires coherent preparation and uncomputation of the
magnetic fusion workspace.

## Frozen fusion and twist data

The exact `D(S3)` fusion ring gives

\[
C\otimes G=F\oplus H.
\]

The relevant twists are

\[
\theta_C=1,
\qquad
\theta_F=1,
\qquad
\theta_G=\omega,
\qquad
\theta_H=\omega^2.
\]

All four objects have quantum dimension two except that only the equality of
the `F` and `H` dimensions is needed below.

## Resolved monodromy phases

In a multiplicity-free braided fusion category, double braiding of `a` and `b`
on fusion channel `c` acts by the balancing scalar

\[
m_c^{a,b}
=
{\theta_c\over\theta_a\theta_b}.
\]

Therefore the two channels of `C` and `G` have phases

\[
m_F^{C,G}
=
{1\over\omega}
=
\omega^2
\]

and

\[
m_H^{C,G}
=
{\omega^2\over\omega}
=
\omega.
\]

The resolved monodromy is thus

\[
M_{C,G}
=
\omega^2 P_F^{C,G}
+\omega P_H^{C,G}.
\]

It is unitary. Its spectrum contains exactly the two conjugate cube-root
phases sought by the complex-quadrature tester.

## Why the closed Wilson response is real

The normalized monodromy scalar is the quantum-dimension-weighted trace over
the unresolved fusion channels. Since

\[
d_F=d_H=2
\]

and

\[
d_Cd_G=4,
\]

the unresolved value is

\[
\mu_{C,G}
=
{d_F\omega^2+d_H\omega\over d_Cd_G}
=
{\omega+\omega^2\over2}
=
-{1\over2}.
\]

This reproduces the independently frozen modular value

\[
\mu_{C,G}
=
{6S_{C,G}\over d_Cd_G}
=
-{1\over2}.
\]

No phase was absent. The scalar closure averaged two conjugate unitary
channels and retained only their real trace.

This is a concrete instance of the difference between ordered holonomy and an
additive scalar diagnostic shadow.

## Action on the electric pair channels

The protected qutrit uses the first-pair fusion labels

\[
e\in\{A,B,C\}.
\]

For the two one-dimensional electric channels,

\[
A\otimes G=G,
\qquad
B\otimes G=G.
\]

Because

\[
\theta_A=\theta_B=1,
\]

their resolved monodromy phase is one:

\[
m_G^{A,G}=m_G^{B,G}=1.
\]

Only the `C` pair channel splits into the two complex branches `F,H`.
Therefore a coherently retained and resolved `G`-dyon loop has precisely the
algebraic selectivity needed for a qutrit pair-channel bridge:

- identity on logical pair channels `A` and `B`;
- `omega^2` or `omega` on logical pair channel `C`, depending on the resolved
  magnetic fusion channel.

If one channel could be selected and every workspace returned cleanly, the
logical action would be one of

\[
U_F=\operatorname{diag}(1,1,\omega^2)
\]

or

\[
U_H=\operatorname{diag}(1,1,\omega).
\]

Either action is nonreal and distinguishes the braid-invariant line from its
standard doublet. It supplies the missing complex tester direction and a
discrete nontrivial pair-channel bridge.

It does not by itself supply continuously tunable `U(3)` control.

## The channel-return obstruction

The branch labels are not one common ancillary coordinate across all three
logical pair sectors:

- `A` and `B` fuse with `G` only through `G`;
- `C` fuses with `G` through `F` or `H`.

An implementation must therefore perform a coherent controlled recoupling,
not merely prepare one fixed magnetic fusion label independently of the
unknown qutrit state.

For a logical superposition, a primitive resolved process can produce

\[
\alpha|A_L\rangle|G\rangle_R
+\beta|B_L\rangle|G\rangle_R
+\gamma|C_L\rangle
\left(
u|F\rangle_R+v|H\rangle_R
\right).
\]

If the reference channel is measured or discarded, it records whether the
pair occupied `C` and dephases the logical qutrit. To obtain a diagonal unitary
on the qutrit alone, a source-derived fusion and reassociation corridor must:

1. coherently route the `C` branch through one declared `F` or `H` monodromy
   eigenchannel;
2. leave the `A,B` branches in their unique `G` route;
3. apply the double braid;
4. reverse every channel-resolution and reassociation step;
5. return the dyon, fusion workspace, and controller to one common state.

The last condition is again the rank-one environment Gram condition. Fusion
rules and balancing phases determine the desired action but do not prove
clean corridor closure.

## Why the retained dyon is better than the closed loop

A closed Wilson loop creates a reference pair, braids, and fuses it back to
vacuum. Its scalar amplitude sums over the unresolved `F/H` alternatives and
is generally nonunitary. It yields the real value `-1/2` on the `C` channel.

A retained `G` dyon keeps the full monodromy operator available. It can, in
principle, preserve the resolved channel coherently and expose one of the
unit-modulus phases.

The price is an enlarged protected carrier containing the magnetic reference,
its compensating total charge, and a fusion-tree frame. The dyon is not a
catalyst until exact return has been proved.

## Orientation

Ribbon reversal exchanges `G` and `H` and complex conjugates the two bridge
candidates. An unoriented implementation may realize either

\[
U_F
\]

or

\[
U_H.
\]

Both have the same pair-channel selectivity and the same usefulness for
rank-one visibility certification. Signed logical-phase identification
requires an orientation anchor.

## Constructor hierarchy

The present result freezes four distinct levels.

1. **Fusion support:** `C` with `G` has channels `F,H`.
2. **Resolved ordered holonomy:** the two channels carry phases `omega^2` and
   `omega`.
3. **Closed scalar readout:** forgetting the channel gives `-1/2`.
4. **Protected logical bridge:** requires coherent channel selection and clean
   uncomputation on the fusion qutrit.

Levels one through three are source-derived. Level four remains an executable
constructor problem.

## Exact falsifiers

- The `C`-`G` monodromy claimed intrinsically real.
- Either resolved channel assigned a phase other than `omega` or `omega^2`.
- The real scalar `-1/2` claimed to prove loss or decoherence.
- A closed Wilson insertion called a unitary logical phase gate.
- `F/H` channel measurement claimed to preserve an unknown qutrit
  superposition.
- One magnetic fusion channel prepared independently of the logical pair
  sector without a recoupling map.
- Fusion and twist data claimed to prove clean channel uncomputation.
- The discrete bridge claimed to provide continuous full-qutrit control.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies resolved routes versus scalar closure,
retained reference versus fused-away probe, channel garbage, diagonal logical
selectivity, and the clean-return compiler condition.

The quantum coefficient lens supplies the `C`-`G` fusion channels, balancing
phases, quantum-trace weights, dyonic monodromy, and fusion-qutrit
interpretation.

## Result

The retained magnetic braid contains the missing complex phase natively. The
real Wilson value is its unresolved conjugate-channel average. A resolved
`F` or `H` route would give exactly the nonreal `C`-channel phase needed by the
electric fusion qutrit. The remaining physical task is a coherent
charge-preserving recoupling corridor whose workspace returns with rank-one
Gram matrix.

No build or checker was run for this research-only packet.
