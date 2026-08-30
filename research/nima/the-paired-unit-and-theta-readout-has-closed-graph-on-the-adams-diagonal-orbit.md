# The paired unit-and-theta readout has closed graph on the Adams diagonal orbit

## The minimal sewing interface

Let \(\mathcal H_P\) be the source graph space for one completed prime packet,
and let

\[
\Delta:\mathcal H_P\longrightarrow\mathcal L,
\qquad
\Delta f=(\mathcal M_nf)_{n\ge1},
\]

be its retained theta-label orbit. On \(\operatorname{ran}\Delta\), there are
two source-authorized readouts:

\[
\epsilon_1\Delta f=f,
\qquad
\Sigma_{\mathrm{ren}}\Delta f=\Theta_{\mathrm{ren}}f.
\]

The first is tensor-unit evaluation. The second is the
Euler--Maclaurin-renormalized scalar theta observer.

The minimal interface that retains both is

\[
J_Pf
=
\left(
f,\Theta_{\mathrm{ren}}f
\right)
\in
\mathcal H_P\oplus\mathcal H_\theta.
\]

Equivalently,

\[
J_P
=
(\epsilon_1,\Sigma_{\mathrm{ren}})\Delta.
\]

This is a graph embedding, not a scalar quotient.

## Closed-range theorem

Assume the established Euler--Maclaurin estimate makes

\[
\Theta_{\mathrm{ren}}:
\mathcal H_P\to\mathcal H_\theta
\]

bounded in the quarter-gap graph topology. Equip the target sum with its
ordinary product norm. Then

\[
\|J_Pf\|^2
=
\|f\|_{\mathcal H_P}^2
+
\|\Theta_{\mathrm{ren}}f\|_{\mathcal H_\theta}^2
\ge
\|f\|_{\mathcal H_P}^2.
\]

Hence \(J_P\) is bounded below by one. Its range is closed, and the inverse on
its range is simply first-coordinate projection:

\[
J_P^{-1}(f,\Theta_{\mathrm{ren}}f)=f.
\]

The comparison condition number is controlled without inverting theta
synthesis:

\[
\|J_P\|
\le
\sqrt{1+\|\Theta_{\mathrm{ren}}\|^2},
\qquad
\|J_P^{-1}\|_{\operatorname{ran}J_P}\le1.
\]

Thus the unit branch supplies exactly the lower bound that scalar synthesis
lacks.

## Cutoff naturality

At finite label cutoff \(N\ge1\), define

\[
J_{P,N}f
=
\left(
f,\Theta_{\mathrm{ren},N}f
\right).
\]

The first component is independent of \(N\). Euler--Maclaurin graph
convergence gives

\[
\Theta_{\mathrm{ren},N}f
\longrightarrow
\Theta_{\mathrm{ren}}f.
\]

Therefore

\[
J_{P,N}f\longrightarrow J_Pf
\]

in the product graph topology, while every finite interface obeys the same
lower bound

\[
\|J_{P,N}f\|\ge\|f\|.
\]

There is no completion loss of closed range on this diagonal orbit.

## Adams boundary recovery

For the complete differentiated source \(s_p=Pb_p\), the labelwise Green
identity yields

\[
\mathcal C^{-1}\mathcal M_ns_p=\mathcal M_nb_p.
\]

Applying the paired interface to the recovered diagonal orbit gives

\[
J_Pb_p
=
\left(
b_p,\Theta_{\mathrm{ren}}b_p
\right).
\]

The first component then produces the ordered Stieltjes boundary

\[
d_p=-\frac12S_{\mathrm{ord}}b_p,
\]

while the second records its completed scalar theta observation. Neither
component is reconstructed from the other.

## Relation to the common boundary pushout

The earlier arithmetic--analytic pushout has a possible closed-range defect
because its oriented relation may become soft under completion. On the Adams
diagonal orbit, replacing a scalar comparison leg by \(J_P\) prevents that
specific failure: the relation retains a source copy with lower bound one.

Concretely, if the analytic leg is \(J_P\) and the arithmetic leg begins with
the same source vector \(f\), then the oriented relation contains

\[
f\longmapsto
\bigl((f,\Theta_{\mathrm{ren}}f),-b_{\mathrm{arith}}f\bigr).
\]

Projection to the first analytic coordinate recovers \(f\). Therefore this
relation is bounded below whenever the remaining typed target norms are
nonnegative:

\[
\|R_Pf\|\ge\|f\|.
\]

Its image is closed.

This closes only the Adams diagonal subrelation. It does not prove closed
range for the complete RH comparison relation containing endpoint,
archimedean, reciprocal-seam, radical, and cross-prime coordinates.

## Why the direct scalar interface fails

If one replaces \(J_P\) by \(\Theta_{\mathrm{ren}}\) alone, cancellation among
labels can create nonzero source packets with zero scalar observation. No
uniform lower bound follows. Euler--Maclaurin convergence controls the upper
analytic limit but cannot restore an erased source coordinate.

The graph interface is minimal in a precise sense: removing the unit component
removes the known left inverse.

## Remaining global gate

The first Adams constructor now reaches a completion-stable local sewing
interface:

\[
\text{labelled Green square}
\longrightarrow
\text{closed graph }(f,\Theta_{\mathrm{ren}}f).
\]

The next theorem must extend this split lower bound from the Adams diagonal
subrelation to the complete typed boundary relation. It must show that
endpoint attachment, reciprocal sewing, archimedean completion, and radical
reduction either preserve the source coordinate or replace it by another
uniformly faithful port.

## Verdict

Pairing tensor-unit recovery with renormalized theta observation produces a
canonical closed graph with lower bound one. This is the first
completion-stable arithmetic--analytic sewing cell for the constructed Adams
edge.

The scalar observer is retained, but it is prevented from carrying authority
that belongs to the labelled constructor.
