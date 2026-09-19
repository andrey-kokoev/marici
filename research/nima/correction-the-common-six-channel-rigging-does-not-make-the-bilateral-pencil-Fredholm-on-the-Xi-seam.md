# Correction: the common six-channel rigging does not make the bilateral pencil Fredholm on the Xi seam

## Closedness versus Fredholmness

The weighted Sobolev intersection

\[
\mathcal X_{r,m}
=H^r\cap L^2((1+x^2)^m dx)
\]

makes all six ports and their transpose columns continuous. It can support a
closed graph realization of the local pencil. It does not make the bilateral
history block Fredholm on the critical seam.

The principal block is

\[
A-z=\partial_q-z,
\qquad
\operatorname{spec}(A)=i\mathbb R.
\]

For `z in iR`, zero lies in its essential spectrum. Polynomial Sobolev and
polynomial spatial weights do not move the asymptotic translation spectrum.
The arithmetic incidence is Hilbert--Schmidt/compact, so adjoining it cannot
remove zero from the essential spectrum. Hence the paired pencil

\[
P(z)=
\begin{pmatrix}
A-z&-B\\
-B^\dagger&D_U(z)
\end{pmatrix}
\]

is not an ordinary Fredholm family there.

## Consequence for the odd-doubled complex

The odd-doubled Grushin differential is algebraically and graph-theoretically
well typed, but its Fredholm admission on the Xi seam cannot be obtained from
the six-channel polynomial rigging. Therefore no ordinary determinant-line
comparison with Xi is authorized on that carrier.

## Correct promotion

The exact Xi object is the boundary Evans mismatch between the two stable
history charts:

\[
E_{\rm hist}(z)
=u_-(0;z)-u_+(0;z)
=\tau(z).
\]

At a zero, the histories glue across the seam while the parameter remains in
continuous spectrum. The correct completed complex must therefore be a
weighted/scattering boundary complex with separate left and right domains,
not one unweighted full-line Fredholm pencil.

Use opposite exponential chart weights with rate `eta>0` below the theta decay
rate. Conjugation shifts the asymptotic derivative symbols to

\[
\partial_q-z-\eta
\quad(q\to+\infty),
\qquad
\partial_q-z+\eta
\quad(q\to-\infty).
\]

For `|Re z|<eta`, zero leaves both asymptotic essential spectra. The remaining
finite index defect is carried by the seam boundary ports and is precisely
what the Grushin/Clark border must balance.

## Revised gate

Construct the two weighted half-line graph domains, their six-channel seam
trace, and the bordered matching operator. Then prove:

1. chartwise Fredholmness and fixed bordered index zero;
2. equality of the boundary characteristic with `tau(z)`;
3. the lower arithmetic equation on the glued state;
4. limiting-absorption compatibility as the weights return to the physical
   boundary value;
5. preservation of the Clark defect primitive in the boundary rigging.

Thus port continuity is closed, but the next construction is a scattering
Fredholm complex rather than an ordinary full-line one.