# Finite Theta Packets Are Reachable and Jointly Observable Before Mellin Selection

## Finite arithmetic state space

Let \(\Omega\subset\mathbb N\) be finite and divisor closed, with (1\in\Omega\).
Let (V_\Omega\) have basis (e_n\) for (n\in\Omega\). For each prime (p\),
define the truncated constructor

\[
A_pe_n=
\begin{cases}
e_{pn},&pn\in\Omega,\\
0,&pn\notin\Omega.
\end{cases}
\]

The source input is (e_1\).

## Reachability

For every (n\in\Omega\), choose its prime factorization

\[
n=p_1\cdots p_r
\]

with repetition. Divisor closure ensures every partial product lies in
\(\Omega\), and therefore

\[
A_{p_r}\cdots A_{p_1}e_1=e_n.
\]

The prime-constructor orbit of the source input spans all of (V_\Omega\).
The finite arithmetic packet is reachable.

## Joint Gaussian observability

For (x>0\), define

\[
C_xe_n=e^{-\pi n^2x}.
\]

If a state (v=\sum_{n\in\Omega}c_ne_n\) satisfies

\[
C_xv=0
\]

for every (x>0\), linear independence of the distinct exponential
trajectories forces (c_n=0\) for all (n\). Thus the family \(\{C_x\}_{x>0}\)
is jointly observable.

The finite labelled theta realization is minimal relative to the declared
constructor and observation families: every state is reachable and every
nonzero state is seen by some Gaussian port.

## Mellin selection

The scalar completed readout applies a source-derived integral transform to the
Gaussian output family. Schematically,

\[
L_s(v)=\int C_xv\,d\mu_s(x),
\]

with reciprocal sewing and boundary terms included in the genuine completed
formula.

Even though the family \(C_x\) is jointly faithful, one selected functional
\(L_s\) can vanish on a nonzero state. Such a state is a selected-channel
transmission zero, not an unreachable or unobservable state of the full
apparatus.

## Consequence

Reachability, full observability, and integrality do not forbid scalar zeros.
They prove something more precise: the darkness is relational and port
specific. Nothing disappears from the complete source packet.

This matches Aspect's exact passive multiport hostile, where a selected output
is dark while a complementary output remains bright. The theta system has an
independently derived version of the same typing distinction.

## Revised explanation target

The remaining law must constrain the distinguished Mellin selection among all
jointly faithful Gaussian ports. Candidate properties such as passivity,
minimality, reciprocity, or full-output losslessness are insufficient by
themselves; Aspect's hostile systems already falsify those implications.

The source-specific target is a minimum-phase or outer property of the
completed Mellin selector relative to the Gaussian multiport, derived from
Poisson sewing and boundary currents rather than assumed as positivity.
