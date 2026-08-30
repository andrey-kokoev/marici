# 1688 — The First Dyson-to-Moment Kernels Are Conserved Hamiltonian Powers

## Kernel/cokernel falsifier

Entry 1687 constructs the filtered adjoint transform. Its legitimate finite
grades are

\[
F_{D,n}:P_{\le D}\longrightarrow P_{\le D+n},
\qquad
f\longmapsto D^nf,
\]

with source monomials labelled by ((q\text{-degree},p\text{-degree})).

For the free-plus-cubic derivation

\[
D=p\partial_q-q^2\partial_p,
\]

the polynomial

\[
\widetilde H=3p^2+2q^3
\]

is conserved:

\[
D\widetilde H=0.
\]

Hence

\[
1,\widetilde H,\ldots,
\widetilde H^{\lfloor D/3\rfloor}
\]

give

\[
\left\lfloor\frac D3\right\rfloor+1
\]

linearly independent characteristic-zero kernel vectors in (P_{\le D}).

The exact sparse matrices were ranked independently over

\[
10^9+7
\quad\text{and}\quad
10^9+9.
\]

For all 114 maps with

\[
0\le D\le18,
\qquad
1\le n\le6,
\]

both modular ranks agree and attain the rank upper bound forced by the explicit
Hamiltonian powers. Since reduction modulo a prime cannot increase rational
rank, this sandwiches the characteristic-zero rank exactly.

Thus, throughout the tested window,

\[
\boxed{
\dim\ker F_{D,n}
=\left\lfloor\frac D3\right\rfloor+1.
}
\]

The checker also verifies 840 explicit conserved-power annihilations.

## Cokernel

The cokernel dimensions range from 3 to 142 and grow with the padded target

\[
P_{\le D+n}.
\]

This growth is filtration mismatch: the target contains monomials not requested
by the source grade. It does not stabilize to a finite relative class in the
tested presentation.

## Narrow result

\[
\boxed{
\text{the first filtered kernels are ordinary conservation laws, not new coefficient sectors.}
}

No stable kernel or cokernel class beyond Hamiltonian invariants is identified.
This does not prove the formula at arbitrary (D,n), nor does it compare the
completed topologies of the two modules.

## Durable artifacts

- `research/benincasa/checkers/dyson_moment_kernel_cokernel.rs`
- `research/benincasa/results/dyson-moment-kernel-cokernel.json`
- `research/benincasa/dyson-moment-kernel-cokernel.md`

## Next falsifier

Remove the conserved submodule and filtration padding canonically. Compare

\[
P_{\le D}/\mathbb Q[\widetilde H]_{\le D}
\]

with the reachable image filtration rather than the whole padded target. Test
whether the reduced transform is an isomorphism at each finite grade or has a
stable relative defect.
