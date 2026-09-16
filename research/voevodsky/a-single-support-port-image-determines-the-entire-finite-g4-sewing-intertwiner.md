# A single support-port image determines the entire finite G4 sewing intertwiner

## Question

Must the four character phases of the finite metaplectic G4 interface be identified independently?

## Claim boundary

No on a generic rational-coset Fourier orbit. The shifted-support comb is cyclic for the order-four action, so its image determines the entire intertwiner and all four character phases. Existence still requires one source-derived support-port image with the correct orbit Gram matrix.

## Cyclic source vector

For generic \(r\ne-r\pmod q\), the Fourier orbit is

$$
P_r,
\quad C_{-r}=\mathcal FP_r,
\quad P_{-r}=\mathcal F^2P_r,
\quad C_r=\mathcal F^3P_r.
$$

These four ports are distinct and span the finite orbit module. Hence \(P_r\) is a cyclic vector.

Its character projections are

$$
P_\lambda P_r
=
\frac14\left(
P_r+\lambda^{-1}C_{-r}
+\lambda^{-2}P_{-r}
+\lambda^{-3}C_r
\right),
$$

which are nonzero for all \(\lambda\in\{1,-1,i,-i\}\).

## Intertwiner from one seed

Let \(\widetilde W_u\) be the order-four metaplectic radial lift. Choose one candidate radial seed \(v_r\), and define

$$
C_v(\mathcal F^jP_r)
=\widetilde W_u^jv_r,
\qquad 0\le j<4.
$$

Because the four source orbit vectors form a basis, this determines one linear map. It satisfies

$$
C_v\mathcal F=\widetilde W_uC_v
$$

including the closing step, since both actions have fourth power one.

Conversely, every intertwiner is obtained this way with

$$
v_r=C(P_r).
$$

Thus the four character phases are the projections of one seed:

$$
\widetilde P_\lambda v_r
=C(P_\lambda P_r).
$$

## Unitary acceptance test

The map \(C_v\) is unitary exactly when the orbit Gram matrices agree:

$$
\left[
\langle\mathcal F^aP_r,\mathcal F^bP_r\rangle
\right]_{a,b=0}^3
=
\left[
\langle\widetilde W_u^av_r,
\widetilde W_u^bv_r\rangle
\right]_{a,b=0}^3.
$$

Equivalently, the four character norms must match:

$$
\|P_\lambda P_r\|
=
\|\widetilde P_\lambda v_r\|
$$

for every \(\lambda\), after the declared source normalization.

## Source-identification boundary

A valid \(v_r\) must be obtained by applying the proposed labelled-to-radial interface to the actual shifted-support port. Choosing \(v_r\) merely to satisfy the Gram equations would fit the intertwiner. No existing packet supplies this support-port-to-radial seed map.

## Disposition

The finite external G4 sewing comparison is reduced from four independent phase choices to one source image \(P_r\mapsto v_r\) plus an exact orbit-Gram test. Once that seed is source-derived and passes the test, the full order-four intertwiner is forced.