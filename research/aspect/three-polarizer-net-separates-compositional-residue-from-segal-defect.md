# Three-polarizer net separates compositional residue from Segal defect

## Question

Does the probe-configuration semantics describe an existing non-Schur Interaction Net, or was it tailored to elimination cross-effects?

## Claim boundary

This packet interprets the source-defined ideal three-polarizer net in `research/kitaev/three-polarizer-interaction-net.md`. It treats polarizer order as typed composition order, not physical time. It establishes a finite exact state-transformer model, not a general optical or SCC theorem.

## Source rule

For an ideal linear-polarization state \((I,\phi)\), the instrument at angle \(\theta\) produces

\[
P_\theta(I,\phi)=
\left(
I\cos^2(\theta-\phi),
\theta
\right),
\]

while its visible scalar record is only

\[
o_\theta(I,\phi)=I\cos^2(\theta-\phi).
\]

The state transformer retains the angle required by the next instrument. The scalar projection does not.

## Configurations

After the initial \(0^\circ\) polarizer, normalize the state to \((1,0^\circ)\). Let probe \(p\) insert the \(45^\circ\) instrument and probe \(q\) apply the \(90^\circ\) terminal instrument.

The relevant assignments are:

\[
P_{90}(1,0^\circ)=(0,90^\circ),
\]

\[
P_{45}(1,0^\circ)=(1/2,45^\circ),
\]

\[
P_{90}P_{45}(1,0^\circ)=(1/4,90^\circ).
\]

Thus inserting the middle polarizer changes the continuation state and makes the final record nonzero.

## What this rotates in the proposal

At the faithful state-transformer level, the joint configuration is ordinary composition:

\[
K(p,q)=P_{90}\circ P_{45}.
\]

There is no failure of factorization. The joint constraint is determined by the unary transformer for \(p\), the unary transformer for \(q\), and their typed interface.

At the scalar-record projection, the intermediate record \(1/2\) omits the angle \(45^\circ\). No map from intensity alone determines the next Malus factor for arbitrary posterior angle. The projected semantics therefore loses the composition interface. The missing polarization state is a continuation residue, not a Segal defect of the faithful semantics.

This separates two Interaction Net phenomena:

1. **compositional residue**: state retained so the next instrument is well typed;
2. **matching defect**: a joint constraint not reconstructed from compatible lower configurations.

The Schur example exhibits a nonzero additive cross-effect. The polarizer example exhibits lawful composition whose scalar projection erases required state. A useful Interaction Net semantics must represent both without identifying them.

## Hostile fixtures

- Direct \(0^\circ\to90^\circ\) composition must yield zero.
- The \(0^\circ\to45^\circ\to90^\circ\) route must yield \(1/4\).
- Replacing the posterior angle \(45^\circ\) by the original \(0^\circ\) must incorrectly return zero and is rejected.
- Two states with equal intensity and different angles must be separated by some subsequent polarizer, proving intensity is not a faithful coordinate.
- Calling the nonzero three-polarizer record a non-Segal defect at the full state level is rejected because direct transformer composition computes it exactly.

## Disposition

The second net is successfully typed, but it revises the conjecture: not every Interaction Net interaction is a matching defect. Some cells carry continuation state required for lawful composition, and defects may appear only after a nonfaithful readout projection. Probe semantics therefore needs both configuration matching maps and explicit state-transformer interfaces.
