# An off-seam zero is a dark commutator codiagonal with a bright commutator packet

## Transported two-sheet packet

For \(z=a+it\), retain the unaggregated oscillatory sheet state

\[
v_t(u)=
\begin{pmatrix}
e^{itu}\\
e^{-itu}
\end{pmatrix},
\]

the horizontal Mellin transport

\[
T_a(u)=
\begin{pmatrix}
e^{au}&0\\
0&e^{-au}
\end{pmatrix},
\]

and the sheet exchange \(S\).

The transported value packet is

\[
T_av_t=
\begin{pmatrix}
e^{zu}\\
e^{-zu}
\end{pmatrix}.
\]

Its source-weighted codiagonal is twice the completed value channel.

## Exact commutator packet

Direct calculation gives

\[
[T_a,S]v_t
=2\sinh(au)
\begin{pmatrix}
e^{-itu}\\
-e^{itu}
\end{pmatrix}.
\]

Applying the codiagonal row produces

\[
(1,1)[T_a,S]v_t
=-4i\sinh(au)\sin(tu).
\]

After integration against the positive kernel \(k(u)\), this is

\[
-4iS_a(t),
\]

where \(S_a(t)\) is the antisymmetric real quadrature of the completed scalar
section.

If the scalar section vanishes, both of its real quadratures vanish. Hence

\[
F(a+it)=0
\quad\Longrightarrow\quad
\int_0^\infty
k(u)(1,1)[T_a,S]v_t(u)\,du=0.
\]

Thus the aggregate commutator monitor is automatically dark at every scalar
zero.

## The full packet remains bright off the seam

Pointwise,

\[
\|[T_a,S]v_t(u)\|^2
=8\sinh^2(au).
\]

Therefore

\[
\mathcal E_{\mathrm{ex}}(a)
=8\int_0^\infty k(u)\sinh^2(au)\,du.
\]

For the positive theta kernel,

\[
\mathcal E_{\mathrm{ex}}(a)>0
\]

whenever \(a\ne0\).

A hypothetical off-seam zero consequently has a dark commutator codiagonal
and a bright commutator packet.

This is Aspect's transmission-zero and incidence-alias pattern in the theta
control channel.

## Correction to the seven-axis map

The earlier classification used one incidence field for two different
relations:

1. Source incidence: the canonical moving integer endpoint constructor is
   matched.
2. Observation incidence: the scalar codiagonal aliases a nonzero
   commutator packet.

These can coexist. Therefore the current theta event requires either two
incidence axes or a nested incidence object. Calling incidence simply
`matched` hides the measurement alias; calling it simply `aliased` hides the
source provenance.

The corrected event is:

- scalar value: dark;
- value-current packet: bright;
- source incidence: matched;
- commutator observation incidence: aliased off seam;
- history: retained;
- path and coefficient: native;
- action: missing.

## Exact remaining theorem

RH is equivalent to codiagonal faithfulness on the canonical scalar-null
family:

\[
F(a+it)=0
\quad\Longrightarrow\quad
[T_a,S]v_t=0
\]

after applying the complete source-authorized incidence closure.

Without that final qualification the implication is false, as the two-atom
hostile shows. With it, the statement is still RH-strength. Its advantage is
that it identifies the missing action as a descent or faithfulness theorem:
the canonical incidence ports must prevent a dark aggregate from hiding a
bright exchange packet.

## Operator stimulus

The operator asked us to continue through Aspect's updated tester. Retaining
the full commutator packet rather than only its norm revealed the exact
Rosenbrock pattern and split one apparent incidence axis into source and
observation incidence.
