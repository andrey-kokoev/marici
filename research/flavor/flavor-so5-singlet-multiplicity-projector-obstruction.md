# SO(5) singlet-multiplicity projector obstruction: WP739

## Question

Does embedding WP736's product group into the simple parent (SO(5)) make the
Clebsch selector and its additional matter fully source-authorized?

## Representation restriction

The relevant subgroup chain is

\[
SO(5)\supset SO(4)\simeq SU(2)_A\times SU(2)_B
\supset SO(3)_{\mathrm{diag}}.
\]

The vector representation restricts as

\[
5\downarrow SO(4)=4\oplus1=(2,2)\oplus(1,1).
\]

WP736 uses the diagonal restriction of the bifundamental,

\[
(2,2)\downarrow SO(3)_{\mathrm{diag}}=3\oplus1.
\]

Consequently the complete simple-group packet is

\[
5\downarrow SO(3)_{\mathrm{diag}}=3\oplus1\oplus1.
\]

The simple completion necessarily adds a second low-energy singlet with the
same physical (SO(3)) label as the desired model-A mediator.

## Exact commutant

Choose a basis in which (SO(3)) acts on the first three coordinates and
fixes the last two. A real matrix commuting with every (SO(3)) generator has
the form

\[
X=
\begin{pmatrix}
aI_3&0\\
0&B
\end{pmatrix},
\qquad B\in M_2(\mathbb R).
\]

The orthogonal commutant therefore contains a full (O(2)) acting on the two
singlets. For

\[
R(\theta)=
\begin{pmatrix}
I_3&0\\
0&\begin{matrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{matrix}
\end{pmatrix},
\]

every angle gives the same admitted (SO(3)) representation data.

If a parent invariant supplies a fixed singlet coupling vector
(c=(c_4,c_5)), the coupling of a chosen light singlet
(s_\theta=(\cos\theta,\sin\theta)) is

\[
\kappa_A(\theta)=c\mathbin\cdot s_\theta.
\]

For the exact witness (c=(1,0)), its squared magnitude is

\[
|\kappa_A(\theta)|^2=\cos^2\theta,
\]

which ranges continuously from one to zero without changing the parent
representation or the residual physical group. The low-energy Clebsch ratio
and portal contrast are therefore not functions of the representation packet
alone.

## Projector gate

Selecting one model-A singlet requires a rank-one projector

\[
P_\theta=s_\theta s_\theta^T
\]

in the multiplicity space. No rank-one projector is invariant under the full
(O(2)) commutant. The only scalar projector-like operator commuting with that
commutant is proportional to (I_2), which selects the whole two-singlet
isotypic component rather than one physical channel.

Sequential breaking vectors, a discrete parity, or a mass matrix can fix
(P_\theta), but then that object is an additional source constructor. Its
potential, vacuum, eigenvalue gap, RG transport, and threshold matching must be
derived independently of the desired portal answer. Calling the chosen
singlet the (SO(4)) singlet does not suffice after the full symmetry has been
broken to the physical diagonal group, because both states then carry the same
observable representation label and may mix.

## Disposition

The minimal (SO(5)) simple-group embedding is not yet a stronger selector
than WP736. It replaces the product-group freedom by a multiplicity-space
projector fiber. Until a source-derived breaking sector fixes that projector,
the apparent simple-group Clebsch relation does not descend to the physical
one-singlet readout.

This obstruction precedes magnitude, fixed-point, basin, and detector tests.
If an independently derived projector is supplied, the next calculation is
the complete (SO(5)\times U(1)_Y\times SU(3)_c) beta system with the full
spinor and vector multiplets. Without it, computing that fixed point would
select a parent packet whose map to the desired portal remains nonfaithful.

The smallest exact falsifier is the commuting rotation (R(\pi/2)), which
sends the witness coupling of the chosen singlet from one to zero while
preserving all residual representation labels.

Reproduce with:
`uv run --with sympy python research/flavor/checkers/wp739_so5_singlet_multiplicity_projector_obstruction.py`.

Generated result:
`results/wp739_so5_singlet_multiplicity_projector_obstruction.json`.
