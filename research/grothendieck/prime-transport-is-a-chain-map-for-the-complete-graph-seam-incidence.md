# Prime Transport Is a Chain Map for the Complete-Graph Seam Incidence

## Label transport

Let `S` be a finite arithmetic label set and let

\[
\delta_S:\mathbb C^S\longrightarrow\mathbb C^{E(S)},
\qquad
(\delta_Sg)_{nm}=g_m-g_n.
\]

Prime multiplication sends `n` to `pn`. On the supported target submodule,
define

\[
(T_{p,s}g)_{pn}=p^{-s}g_n.
\]

Its edge lift is

\[
(T^{(1)}_{p,s}e)_{pn,pm}=p^{-s}e_{n,m}.
\]

Then

\[
\delta_{pS}T_{p,s}=T^{(1)}_{p,s}\delta_S.
\]

The same identity holds with the relative-Haar half-density factor included,
because multiplication by `p^(1/2-s)` is common to every transported vertex.

## Higher prime coherence

For distinct primes `p` and `r`, vertex transports commute:

\[
T_{p,s}T_{r,s}=T_{r,s}T_{p,s},
\]

and their edge lifts commute as well. The collision at label `prn` therefore
has zero braid residual. Prime-power iteration is likewise compatible.

Thus primitive and prime-square label transport preserve the finite-seam
incidence before aggregation.

## General naturality criterion

For a linear label map `A`, exterior naturality reads

\[
(\Lambda^2A)(\Omega\wedge g)
=(A\Omega)\wedge(Ag).
\]

It agrees with the target augmentation bivector precisely when `A Omega` is
the target augmentation vector, up to the declared common scalar. Injective
relabelings and permutations satisfy this on their supported images.

## Remaining obstruction

Arithmetic scale transport is not the failing constructor. The unresolved
map is Fourier–Poisson sewing, which generally mixes labels and may require a
doubled primal–dual label space. Its matrix must satisfy the augmentation-line
criterion before its exterior lift can be called the same seam incidence.

The next finite falsifier is therefore direct: truncate the primal and dual
lattices, write the actual Poisson sewing matrix `P`, and test whether

\[
P\Omega_{\mathrm{primal}}
\]

lies in the target augmentation line. If not, the scalar and bivector boundary
channels do not form a two-term chain under sewing; an additional control
component is required.

