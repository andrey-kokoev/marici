# Xi-torsion lift iteration 14: the three objectives refer to two different codiagonals, and no common cokernel is declared

## Interface trace

A repository-wide trace shows that the phrase “Xi-divisor torsion in the
bordered cokernel” first arose in topology iterations 41--42. It is not the
cokernel of a previously declared source interface. Those iterations implicitly
identified two maps that the source keeps distinct.

## Codiagonal A: translated theta history

The established common-history map is

\[
J_\theta:K_\theta\to H_{\rm common},
\]

\[
J_\theta(c)
=
\sum_{p,k}\frac{p^{-k/2}}k
\left(c_{p,k}^+\tau_{k\log p}\Phi
+c_{p,k}^-\tau_{-k\log p}\Phi\right).
\]

Its deconvolved Fourier observer gives algebraic faithfulness and continuous
recovery in the stated graph topology. Objective 1 naturally refers to this
map.

But `H_border` is not currently an element of `H_common`; it is a four-chart
bordered Green packet.

## Codiagonal B: bordered Clark synthesis

Iterations 2--6 introduced the correctly typed map

\[
J_B:K_B\to B_{\rm border}^{(4)},
\]

whose atoms are

\[
T_{PB}^{\rm rig}(e^{z\cdot}\otimes K_{1,c_\lambda}).
\]

By construction, the assembled `H_border` belongs to `im J_B`. Four-chart
endpoint observation can recover its constant source coefficients in suitable
Bohr topologies.

Objective 2 is therefore a theorem about `J_B`, not `J_theta`.

## No common exact sequence

There is presently no declared horizontal map

\[
H_{\rm common}\longrightarrow B_{\rm border}^{(4)}
\]

that intertwines `J_theta` and `J_B`, nor a reverse map faithful on the bordered
factor. Consequently there is no source-defined exact sequence

\[
0\to K_\theta\xrightarrow{J_\theta}
B_{\rm border}^{(4)}\to Q_{\rm border}\to0
\]

in which all three objectives live.

The notation `[H_border] in coker J_theta` is therefore ill typed. Meanwhile
`[H_border] in coker J_B` is zero by the definition of `J_B`, so its vanishing
cannot supply a new confinement theorem.

## Why the labelled identity does not repair the bridge

The shellwise identity

\[
\Delta^{\rm lab}=\tau H^{\rm lab}
\]

proves coordinatewise Evans divisibility in the bordered source category. It
does not identify the bordered Clark coefficients with translated-theta
history coefficients or with relative-Haar energies.

Thus it closes a legitimate labelled Evans statement but does not create the
missing common cokernel.

## Exact missing square

To make the three objectives one theorem, construct a source-derived square

\[
\begin{array}{ccc}
K_\theta&\xrightarrow{J_\theta}&H_{\rm common}\\
\downarrow A&&\downarrow B\\
K_B&\xrightarrow{J_B}&B_{\rm border}^{(4)}
\end{array}
\]

with:

1. `B J_theta = J_B A`;
2. `A` sends the theta source state to the frozen Clark coefficient packet;
3. `B` is strict and horizontal;
4. the induced cokernel map is faithful on the Xi-torsion sector.

No such `A,B` pair is currently constructed.

## Verdict

The requested equivalence is not presently a well-formed single claim:
objective 1 concerns `J_theta`, objective 2 concerns `J_B`, and objective 3
uses an undeclared common cokernel. The next nonredundant task is construction
of the comparison square above, not further refinement of either topology in
isolation.