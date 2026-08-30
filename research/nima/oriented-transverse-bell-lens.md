# The oriented transverse plane generates the local Bell lens

## Construction

Let \(V\) be the real two-dimensional physical transverse polarization
quotient with its positive metric and an orientation. The orientation and
metric define

\[
J^2=-1.
\]

After complexification, the helicity projectors are

\[
P_+=\frac{1-iJ}{2},
\qquad
P_-=\frac{1+iJ}{2}.
\]

They are Hermitian, orthogonal, exhaustive, and exchanged by complex
conjugation. Reversing the transverse orientation sends \(J\mapsto-J\) and
therefore exchanges the helicity labels without changing the unordered
two-outcome measurement.

In the helicity basis, a linear-polarization analyzer at phase \(\varphi\) is

\[
O(\varphi)=
\begin{pmatrix}
0&e^{-i\varphi}\\
e^{i\varphi}&0
\end{pmatrix},
\qquad
E_\pm(\varphi)=\frac{1\pm O(\varphi)}2.
\]

The exact checker verifies that \(O(\varphi)\) is Hermitian with square one
and that \(E_\pm\) are orthogonal exhaustive projectors.

## Typing result

The local conjugation and analyzer effects do not require a new Carrier
divisor. They follow from one sector coefficient datum:

\[
\boxed{\text{oriented real metric transverse plane}.}
\]

Entries 53–54 provide a Ward-reduced transverse quotient and a
reference-independent metric trace. They do not currently serialize the
orientation/Hodge operator \(J\). Thus the remaining comparison is narrower
than Entry 1572's initial list but is still not closed by analogy.

The analyzer angles are legitimate physical inputs chosen by Alice and Bob;
the Carrier should permit their local action and guarantee naturality, not
select their values. The MES angles in Entry 1571 are therefore not a Carrier
defect.

## Next square

The decisive local square is

\[
\begin{array}{ccc}
Q_{\rm Ward}&\xrightarrow{\operatorname{Cut}}&Q_L\otimes Q_R\\
\downarrow\scriptstyle{(-)\otimes\overline{(-)}}&&
\downarrow\scriptstyle{(-)\otimes\overline{(-)}}\\
\mathsf{Dens}(Q_{\rm Ward})&\xrightarrow{\operatorname{Cut}\otimes\overline{\operatorname{Cut}}}&
\mathsf{Dens}(Q_L)\otimes\mathsf{Dens}(Q_R),
\end{array}
\]

with the \(J\)-induced effects retained. The algebraic lower arrow is already
functorial by Entry 1572. What must be sourced is the compatibility of \(J\)
with physical Cut and the accepted-event trace.
