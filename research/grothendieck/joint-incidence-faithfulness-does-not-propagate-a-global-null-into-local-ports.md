# Joint incidence faithfulness does not propagate a global null into local ports

## Complete local monitor family

Let \(h(u)\) be an integrable response density on the positive half-line. For
each bounded interval \(I\), define the incidence-resolved monitor

\[
M_I(h)=\int_I h(u)\,du.
\]

The complete interval family is jointly faithful:

\[
M_I(h)=0
\]

for every bounded interval \(I\) implies \(h=0\) almost everywhere. This is
the continuous analogue of reconstructing a finite labelled packet from a
complete score tower.

## Global darkness does not activate the family

The scalar codiagonal is only the global monitor

\[
M_{(0,\infty)}(h)=\int_0^\infty h(u)\,du.
\]

Its vanishing does not imply that the local monitors vanish. The smallest
witness is

\[
h(u)=
\begin{cases}
1,&0<u<1,\\
-1,&1<u<2,\\
0,&u>2.
\end{cases}
\]

Then

\[
M_{(0,\infty)}(h)=0,
\]

while

\[
M_{(0,1)}(h)=1,
\qquad
M_{(1,2)}(h)=-1.
\]

Thus availability of a jointly faithful incidence closure does not propagate
one aggregate null into its constituent ports.

## Application to the theta commutator

The commutator codiagonal density is, up to a fixed factor,

\[
h_{a,t}(u)=k(u)\sinh(au)\sin(tu).
\]

A completed scalar zero implies only

\[
\int_0^\infty h_{a,t}(u)\,du=0.
\]

For \(a\ne0\), the full commutator packet remains nonzero. Resolving it into
canonical cells or a complete local moment tower would detect that packet,
but the scalar zero does not say those additional readouts are dark.

On the seam, \(a=0\), the density itself vanishes and hence every local port
is dark. Therefore the implication

\[
\int h_{a,t}=0
\quad\Longrightarrow\quad
M_I(h_{a,t})=0
\]

for all source-authorized \(I\) is another exact form of the RH-strength
action law, not a consequence of joint faithfulness.

## Transfer from Benincasa and Aspect

Benincasa's complete score tower proves reconstruction after all score ports
are supplied. It does not infer those scores from one scalar observation.

Aspect's Rosenbrock tester makes the same distinction operationally: a dark
transmission can coexist with a bright internal packet. Adding an incidence
monitor reveals the packet but does not make the transmission cease to be
dark.

The theta programme must therefore keep three statements separate:

1. the incidence monitor family exists;
2. the family is jointly faithful;
3. a scalar-null source state is forced into the common kernel of the family.

The first two are available in idealized form. The third is the missing
action and cannot be obtained by calling the closure faithful.

## Corrected target

The surviving theorem needs a source-derived dynamics or boundary condition
that actively couples the scalar-null port to every required incidence port.
Equivalently, it must prove that the canonical scalar-null family lands in the
joint kernel, rather than merely prove that the joint kernel is trivial.

This is a transport/descent statement between observation ports, not a larger
static census of them.

## Operator stimulus

The operator instructed us to continue the Aspect-tester attack. Resolving the
commutator by cells exposed a second projection mistake: completeness of the
monitor family had been confused with propagation of a measured zero across
that family.
