# The Residue--Valuation Closure Is an Infinite Local Affine Tree

## Source operations

On \(\mathcal S(\mathbb Q_p)\), use normalized dilation and additive
translation

\[
(D_af)(x)=|a|_p^{1/2}f(ax),
\qquad
(\tau_hf)(x)=f(x+h).
\]

Both operations are defined before valuation compression. Their exact
semidirect-product law is

\[
D_a\tau_h=\tau_{h/a}D_a,
\]

or equivalently

\[
D_a\tau_hD_a^{-1}=\tau_{h/a}.
\]

Fourier transport supplies the remaining native relations

\[
\mathcal F_p\tau_h=M_{\chi_h}\mathcal F_p,
\qquad
\mathcal F_pD_a=D_{a^{-1}}\mathcal F_p.
\]

Thus additive residue transport, valuation dilation, and Fourier sewing form
one local affine--Weyl packet.

## Closure of the first missing residue

Take the prime dilation \(a=p\) and the first inverse-integral translation
\(h_1=p^{-1}\). Conjugation gives

\[
D_p\tau_{h_k}D_p^{-1}
=
\tau_{h_{k+1}},
\qquad
h_k=p^{-k}.
\]

Therefore any carrier containing \(D_p\), \(\tau_{p^{-1}}\), and their
authorized compositions must also contain

\[
\tau_{p^{-2}},\tau_{p^{-3}},\ldots.
\]

No finite residue register is closed under the source operations.

## Unramified-vacuum witness

Let \(f_0=1_{\mathbb Z_p}\). The \(k\)-fold expanding dilation has support
\(p^{-k}\mathbb Z_p\). Compositions of the depth-\(k\) translation generate
all representatives of

\[
p^{-k}\mathbb Z_p/\mathbb Z_p
\]

and the translates \(\tau_r f_0\) are the \(p^k\) disjoint coset indicators
whose union is that expanded ball. They are linearly independent.
Since \(k\) is arbitrary, the source-generated residue--valuation carrier is
infinite-dimensional.

Its finite levels form the rooted \(p\)-ary residue tree. Valuation records
depth, while residue records the branch. The valuation quotient retains the
depth and erases precisely the branch data required by additive translation.

## The commutator residual

For \(\Delta_h=\tau_h-I\), the affine law gives

\[
D_p\Delta_h=\Delta_{h/p}D_p.
\]

Hence

\[
D_p\Delta_h-\Delta_hD_p
=
(\Delta_{h/p}-\Delta_h)D_p.
\]

The residual is not a scalar anomaly and is not supported on one fixed
finite boundary port. It is the difference between adjacent translation
shells. Iteration gives

\[
D_p^n\Delta_h=\Delta_{h/p^n}D_p^n,
\]

so every finite conductor cutoff leaves a terminal next-shell term.

The exact coherence cell is the affine semidirect law itself. Treating its
finite-cutoff terminal shell as a fitted boundary scalar destroys
cutoff-natural composition.

## Consequence for the RH lane

The prime-two non-descent is repaired locally only by retaining the full
residue tree, not by adding one comparison coordinate. This changes the next
completion problem:

- the archimedean additive incidence belongs to a continuous translation
  carrier;
- each finite place contributes a rooted residue tree with valuation depth;
- the Euler loop is the radial depth return;
- the missing forcing current must be a boundary functional on the combined
  affine carrier, compatible with Fourier inversion and restricted products.

The current finite data do not yet supply that completed boundary functional.
In particular, primitive and square cyclic returns see radial depth but not
the terminal residue shell.

## Falsifier and next gate

Any proposed finite-dimensional local repair is falsified by conjugating its
deepest admitted translation with \(D_p\): the result requires the next
translation shell. Any proposed scalar anomaly is falsified if it cannot
distinguish the \(p^k\) residue branches at fixed depth.

The next admissible object is the inductive system of finite residue trees
together with its Fourier-dual projective system. The decisive question is
whether their restricted-product boundary admits a source-derived current
whose finite-cutoff coboundary is exactly the terminal-shell residual.
