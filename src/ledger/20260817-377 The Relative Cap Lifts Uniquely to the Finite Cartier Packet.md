# The Relative Cap Lifts Uniquely to the Finite Cartier Packet

## Result

The coefficient gate left open in Entries 370 and 375 closes on the
independently constructed finite physical packet of Entry 131.

After projecting away the support-labelled \(x_4\) summand, Entry 176's
relative normal cap lifts canonically as

\[
\boxed{
\operatorname{cap}_{176}^{\rm PC}
=
\operatorname{cap}_{\rm norm}
\otimes
\operatorname{pur}_{x_3,\partial}^{\rm PC}.
}
\]

The first factor is Entry 176's unique positive primitive relative-normal
integration.  The second is Entry 131's unique positive
Bockstein-compatible Cartier purity isomorphism.  Entry 176 proves that the
repeated \(u_3\) packet is a spectator and that its mixed squares commute.
Therefore the tensor product is a chain map, commutes with the graph
Bockstein, and has unit coefficient.

Thus the reduced finite PC cone is acyclic.  This does not identify the
finite packet with the raw nonperfect \(q^!\) localization-dual object.  The
global realization or comparison functor between those categories remains
open.

## Why Entries 375--376 did not contradict this

Entries 375--376 tested the raw map

\[
R\operatorname{Hom}_R(R[x_3^{-1}],R)\longrightarrow R
\]

and correctly found its nonzero completion-dual cone.  The finite physical
packet is not obtained from that map by applying \(i^*\), \(i^!\), \(j^*\),
or \(R\Gamma_{(x_3)}\).  It is independently assembled before the raw
localization dual is formed:

\[
E_{3,\rm src}
=
B\langle g_3\rangle[1]
\oplus
[B\langle h_3\rangle\xrightarrow{u_3}B\langle p_3\rangle],
\qquad B=A/(x_3).
\]

Its two pieces are the occurrence Thom line and the original/Borel--Moore
can--var packet.  The target is the actual finite Cartier costalk

\[
i_{x_3}^{!}P_3,\qquad
P_3=
[A\langle g_3,h_3\rangle
\xrightarrow{(x_3,u_3)}
A\langle p_3\rangle].
\]

Entry 131 proves the canonical isomorphism

\[
\operatorname{pur}_{x_3,\partial}^{\rm PC}:
E_{3,\rm src}\otimes\operatorname{or}(x_3)[-1]
\xrightarrow{\sim}i_{x_3}^{!}P_3.
\]

The completion tail is absent because admissible physical coefficients must
come with this finite Rees/can--var lattice and its graph Bockstein.  It is
not deleted afterward by a quotient fitted to the desired answer.

## The tensor lift

Let

\[
C_{\rm rel}
=C_\bullet(I_{\rm norm},\partial I_{\rm norm}).
\]

Entry 176 gives

\[
H_1(C_{\rm rel})\cong\mathbb Z,\qquad
\operatorname{cap}_{\rm norm}:C_{\rm rel}\to\mathbb Z[1],
\qquad [I_{\rm norm}]\mapsto+1.
\]

The double-Rees determinant and Cartier shifts cancel:

\[
L^{-1}[1]\otimes L[-1]\simeq\mathcal O.
\]

The \(D_{03}\) and repeated-\(u_3\) factors are spectators.  Hence on the
finite coefficient packet the only support- and degree-compatible lift is

\[
C_{\rm rel}\otimes E_{3,\rm src}
\xrightarrow{
\operatorname{cap}_{\rm norm}\otimes
\operatorname{pur}_{x_3,\partial}^{\rm PC}}
i_{x_3}^{!}P_3[1],
\]

with the displayed shift removed by the recorded normal-Gysin convention.

## Bockstein compatibility and uniqueness

On the graph \(u_3=t_3x_3\), Entry 131 has

\[
\beta_{x_3}(g_3)=p_3,\qquad
\beta_{x_3}(h_3)=t_3p_3.
\]

The relative cap acts on the separate \(I_{\rm norm}\) tensor factor, while
\(\beta_{x_3}\) acts on \(E_{3,\rm src}\).  Therefore they commute with the
standard tensor sign.  The cap has degree \(-1\), exactly compensated by the
normal orientation shift already present in purity.

Entry 131 also computes every filtration- and support-preserving
Bockstein-compatible endomorphism:

\[
f_1=
\begin{pmatrix}e&0\\0&e\end{pmatrix},
\qquad
f_0=(e).
\]

Positive coorientation and endpoint normalization force \(e=1\).  Since
Entry 176 has the same positive normalization \(k=1\), its lifted map is the
unique purity generator, not merely a nonzero scalar multiple.

## Support projection

At the associated obstruction-packet level, support labels split

\[
\mathsf T_E=
\mathsf T_{\rm ctr}\oplus
\mathsf T_{x_3}\oplus
\mathsf T_{x_4}.
\]

Projection along the last direct summand is canonical at this associated
level and retains the center and \(x_3\) packets.  On the resulting finite PC
packet, \(\operatorname{cap}_{176}^{\rm PC}\) is an isomorphism, so its cone
is acyclic.

This statement does not construct a global quotient functor on the entire
raw ringed carrier.  It proves the local associated-packet correction that
such a functor must realize.

## Meta-level categorical conclusion

The physical category suggested by the existing construction is not the
Verdier quotient of all raw localization duals by their inconvenient
completion tails.  It is the category of finite, support-directed
Rees/can--var packets equipped with:

1. an occurrence Thom line;
2. the paired can--var structure;
3. the graph Bockstein;
4. normal orientation;
5. endpoint normalization.

These data independently select a unique unit map.  Forgetting them produces
the raw localization-dual obstruction of Entries 367 and 375.

## Remaining global gate

What remains is no longer the local coefficient scalar.  It is to construct
a global realization from the raw exceptional \(q^!\) geometry into the
finite PC/Rees category and prove that it:

1. realizes the \(x_4\)-support projection rather than imposing it;
2. retains the nonzero generic \(Q\)-leg;
3. restricts at \(x_3=0\) to
   \(\operatorname{cap}_{176}^{\rm PC}\);
4. supplies the Beck--Chevalley homotopy of Entry 160;
5. is compatible with the two endpoints and the \(D_3\) orbit.

The first one-road test is the localization-triangle square

\[
\delta_{\mathcal E}\alpha_U(q_J)
\simeq
\alpha_Z[1](-[\widetilde\xi_{03}]),
\]

where the closed component \(\alpha_Z\) is now fixed by the unit lift above.
The generic component and the homotopy remain unconstructed.

## Evidence boundary

\`research/voevodsky/check_d03_cap_cartier_packet_lift.rs\` verifies the
relative unit, the finite-packet identity matrices, Bockstein commutation,
and the support-labelled \(x_4\) projection.  The theorem also uses the
independently proved constructions and uniqueness statements of Entries 131
and 176.  No global raw-\(q^!\)-to-PC realization, generic \(Q\)-map, or
Beck--Chevalley cell is claimed.
