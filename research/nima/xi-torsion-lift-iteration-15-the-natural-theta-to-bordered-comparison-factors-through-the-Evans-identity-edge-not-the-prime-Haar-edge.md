# Xi-torsion lift iteration 15: the natural theta-to-bordered comparison factors through the Evans identity edge, not the prime-Haar edge

## Natural comparison available from the source

The stable histories satisfy

\[
u_-(q;z)-u_+(q;z)=\tau(z)e^{zq}.
\]

Applying the rigged pair-to-border crossing with the fixed Clark primitive gives

\[
T_{PB}^{\rm rig}
\bigl((u_--u_+)\otimes K_{1,c}\bigr)
=
\tau(z)
T_{PB}^{\rm rig}
\bigl(e^{z\cdot}\otimes K_{1,c}\bigr).
\]

This is exactly

\[
\Delta_{a,b,c}=\tau H_{a,b,c}.
\]

Hence there is a genuine comparison from theta-forced Evans histories to the
bordered Clark packet. It is horizontal and source-derived.

## Why it does not supply the square requested in iteration 14

The comparison acts on the **difference of the two stable histories**. To
recover the exponential first leg from that difference away from the divisor,
one writes

\[
e^{z\cdot}=\frac{u_--u_+}{\tau(z)}.
\]

Using this quotient as an operator-level bridge is forbidden: it is singular
at Xi zeros and defines the desired divisor lift by division by `tau`.

The factor `H_border` is independently defined there because `e^(z dot)` is an
explicit source vector, not because a holomorphic inverse to the stable-history
difference was constructed.

Thus the available arrow proves divisibility of one distinguished section but
not a strict horizontal comparison between the complete translated-theta and
bordered source ranges.

## Identity edge versus prime edge

The fixed-forcing graph places both histories on one carrier, but the known
relation compares

\[
u_-\quad\text{with}\quad u_+.
\]

The relative-Haar closure requires comparison of

\[
J_\Phi(u_+)
\quad\text{with}\quad
T_pJ_\Phi(u_-).
\]

Its defect is

\[
\Omega_p(z)
=J_\Phi(u_+(z))-T_pJ_\Phi(u_-(z)).
\]

The required theorem is

\[
\Omega_p=\tau H_p.
\]

No current comparison from `J_theta` to `J_B` changes the identity edge into
this prime-dilation edge.

## Consequence for the proposed cokernel

A cokernel built from the Evans identity edge has the shellwise lift already
proved in iteration 13. A cokernel built from the prime-Haar edge has the right
confinement consequence, but Xi-divisibility of its defect is precisely the
open RH-bearing statement.

Conflating the two cokernels makes objective 3 appear equivalent to objectives
1--2. They are not equivalent: the edge map is different.

## Exact obstruction to a holomorphic bridge

Any bridge derived solely by solving

\[
u_--u_+=\tau e_z
\]

for `e_z` has a `1/tau` pole. A regular bridge must instead construct `e_z` or
the Clark packet independently and then prove compatibility with prime
dilation. The independent construction exists; the prime-dilation
compatibility does not.

## Revised target

The only comparison square with an RH consequence is

\[
\begin{array}{ccc}
\text{Evans stable pair}&\xrightarrow{J_\Phi}&\text{fixed-forcing graph}\\
\downarrow&&\downarrow T_p\\
\text{bordered Clark packet}&\longrightarrow&\text{relative-Haar carrier},
\end{array}
\]

with the route defect `Omega_p` proved Xi-divisible before specialization.
Strict Köthe/Silva topology can preserve such an identity once constructed; it
cannot derive the missing prime edge from the identity edge.

## Verdict

The natural source comparison explains `H_border` and its Xi divisibility, but
it closes the wrong edge for confinement. The next executable work should
analyze `Omega_p` directly, rather than seek more scalar codiagonal topology.