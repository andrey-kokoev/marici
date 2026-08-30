# Leave-one-dimension tomography of the Fourier boundary mate

## Question

What shadow is cast when each of the four Fourier boundary dimensions is removed, and how does the answer depend on whether removal occurs at the source, behavior, or task level?

## Claim boundary

Use the source-authorized boundary quotient

\[
W=\operatorname{span}\{1,\delta_0,K,V\}
\]

with Fourier action

\[
\mathcal F1=\delta_0,\qquad
\mathcal F\delta_0=1,\qquad
\mathcal FK=V,\qquad
\mathcal FV=-K.
\]

There are two inequivalent notions of one-dimensional deletion.

### Native-coordinate deletion

Deleting one of \(1,\delta_0,K,V\) does not leave a Fourier-invariant three-plane.

| Removed coordinate | Transport edge that exits the retained space | Observable shadow |
|---|---|---|
| \(1\) | \(\delta_0\mapsto1\) | endpoint value has no reciprocal bulk partner |
| \(\delta_0\) | \(1\mapsto\delta_0\) | bulk constant has no endpoint trace |
| \(K\) | \(V\mapsto-K\) | principal-value orientation lacks its centered-tail source |
| \(V\) | \(K\mapsto V\) | centered tail loses the odd orientation response |

In every case the compressed transport

\[
P_j\mathcal F P_j
\]

fails to satisfy the original Fourier law on the retained object. The defect is the rank-one off-diagonal component

\[
(I-P_j)\mathcal F P_j.
\]

This defect is the coordinate's transport shadow. Closing the retained space under \(\mathcal F\) regenerates the deleted coordinate. Thus none of the four native coordinates is individually optional if the constructor theory includes the full Fourier action.

The coordinates occur as two transport pairs:

\[
\{1,\delta_0\},\qquad \{K,V\}.
\]

Deleting both members of one pair does preserve Fourier closure, but removes an entire physical incidence channel: bulk/endpoint in the first case, tail/orientation in the second.

### Character-line deletion

Over \(\mathbb C\), choose

\[
e_+=1+\delta_0,\qquad
e_-=1-\delta_0,
\]

\[
e_i=K-iV,\qquad
e_{-i}=K+iV.
\]

These have Fourier characters \(+1,-1,i,-i\), respectively. Deleting any one character line leaves an invariant three-dimensional subspace. Hence no covariance defect exposes the deletion.

This is the dangerous shadow: the reduced theory remains internally coherent but is no longer conservative over the original boundary object. Its missing information is a one-dimensional extension torsor carrying precisely the deleted character.

| Deleted character | Lost distinction | What may remain deceptively valid |
|---|---|---|
| \(+1\) | symmetric bulk-endpoint overlap | all other Fourier covariance laws |
| \(-1\) | antisymmetric bulk-endpoint mismatch | invariant scalar combinations in retained blocks |
| \(+i\) | one oriented tail quadrature | the opposite orientation and both even blocks |
| \(-i\) | reciprocal oriented tail quadrature | the opposite orientation and both even blocks |

A scalar observer of one character is exactly such a three-line deletion viewed from its image: it supplies no evidence about the other characters.

### Source, behavior, and bilateral deletion

Model a fully coherent mate initially as the identity \(I:W\to W\). For a character line \(L_\chi\), let \(W_{\widehat\chi}\) be the sum of the other three lines.

1. Source deletion gives the inclusion

\[
I_{\mathrm{src}-\chi}:W_{\widehat\chi}\hookrightarrow W.
\]

It has zero kernel, one-dimensional cokernel, and index \(-1\). Its shadow is an unsynthesizable behavior port: the boundary demands a character the source no longer constructs.

2. Behavior deletion gives the projection

\[
I_{\mathrm{beh}-\chi}:W\twoheadrightarrow W_{\widehat\chi}.
\]

It has one-dimensional kernel, zero cokernel, and index \(+1\). Its shadow is an invisible source mode: a logical sector exists but no behavior port records it.

3. Bilateral deletion gives

\[
I_{\mathrm{both}-\chi}:W_{\widehat\chi}\xrightarrow{\cong}W_{\widehat\chi}.
\]

It has index zero and is perfectly coherent. Its shadow is contextual: the theory has changed its task object and can no longer state questions involving \(L_\chi\). This is legitimate only when an independently declared task localization authorizes the quotient.

These are three distinct meanings of a missing dimension:

\[
\text{source deficit},\qquad
\text{observation kernel},\qquad
\text{task erasure}.
\]

Scalar equality cannot distinguish them.

### Removal from the comparison rather than from an endpoint

A fourth operation keeps both endpoint spaces but deletes the \(\chi\)-block of the mate itself. The resulting map has both a one-dimensional kernel and a one-dimensional cokernel, so its total index is zero. Nevertheless it is not invertible.

This shows why index zero is necessary but insufficient. The full obstruction signature is

\[
\left(
\dim\ker A_\chi,
\dim\operatorname{coker}A_\chi,
c(A_\chi),
\text{source authority}
\right)
\]

for every character. Total index retains only the difference of the first two entries.

### Interaction with the tiny tail

Apply leave-one-character-out tomography to the corrected mate \(\beta_X\). For each \(\chi\):

1. remove the \(\chi\)-block from the observer and recompute the typed residual;
2. remove it from the source constructor packet and compute the resulting cokernel;
3. delete the tail contribution only in that block and test kernel, cokernel, and generalized gain;
4. test whether other blocks can reconstruct it without violating Fourier equivariance;
5. repeat under cutoff refinement.

The tail is a frame selector if deleting it reverses or frees a sign but does not change block rank. It is a finite transversality repair if deletion creates matched kernel and cokernel in one block. It is an extensive completion constructor only if its removal destroys a uniform lower bound on a noncompact family of modes.

### All shadows at once

The four native-coordinate deletions reveal transport dependence. The four character deletions reveal logical-sector dependence. The three endpoint placements reveal whether the defect is controllability, observability, or task semantics. Their product is the minimal deletion atlas:

\[
4\ \text{sectors}
\times
3\ \text{placements}
\times
2\ \text{bases of interpretation}.
\]

The bases are not redundant: native coordinates expose constructor edges, while character coordinates expose invariant logical sectors.

## Disposition

Removing each dimension one at a time shows that the four-dimensional boundary packet is minimal in two different senses. In the native basis every coordinate is forced by Fourier closure. In the character basis every line is an independent logical sector whose deletion can remain perfectly covariant and therefore invisible to internal consistency checks.

The highest-information next audit is characterwise bilateral comparison with asymmetric deletion. For each character, source-only deletion should produce index \(-1\), behavior-only deletion index \(+1\), and deletion of the mate block a matched kernel-cokernel pair of index zero. Any different signature identifies hidden mixing, an unauthorized quotient, or a missing incidence law.