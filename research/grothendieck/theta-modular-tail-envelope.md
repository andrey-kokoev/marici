# Modular theta-tail envelope and the quadratic Jensen theorem

Author: `marici.Grothendieck`

## Tail factorization

Write

\[
 \Phi=\phi_1(1+r_2)(1+S),
 \qquad
 S=\frac{T_3}{1+r_2},
 \qquad
 T_3=\sum_{n\ge3}\frac{\phi_n}{\phi_1}.
\]

For

\[
 r_n(x)=n^2\frac{2n^2x-3}{2x-3}e^{-(n^2-1)x},
\]

termwise differentiation gives, for `0<=j<=4`,

\[
 |D^jT_3|
 \le2(8x)^je^{-8x}C_j,
 \qquad
 C_j=\sum_{n\ge3}n^{4+2j}e^{-(n^2-9)\pi}.
\]

The elementary bounds

\[
 C_0<82, C_1<730, C_2<6562, C_3<59050, C_4<531442
\]

follow by splitting off `n=3` and geometrically majorizing the remaining
labels.

## Fourth-order absorption at the modular seam

With `g=(1+r_2)^{-1}`, logistic differentiation and Leibniz's rule bound the
first four derivatives of `S`. Substitution into

\[
\begin{aligned}
 D^4\log(1+S)={}&\frac{D^4S}{1+S}
 -\frac{4(DS)(D^3S)+3(D^2S)^2}{(1+S)^2}\\
 &+\frac{12(DS)^2D^2S}{(1+S)^3}
 -\frac{6(DS)^4}{(1+S)^4}
\end{aligned}
\]

gives the exact rational envelope

\[
 \left|D^4\log(1+S)\right|<\frac{1329}{250}.
\]

Subtracting it from the two-label reserve leaves

\[
 \boxed{
 V''''(u)>
 \frac{200122855506517}{125000000000000}>\frac85
 \qquad(0\le u\le u_*).
 }
\]

Modular evenness gives `V'''(0)=0`; hence

\[
 V'''(u)>\frac85u>0
 \qquad(0<u\le u_*).
\]

## Post-crossover repair

For the two-label system,

\[
 D^3\log(1+r_2)=-pC-qA(dA^2-3B).
\]

On `x>=pi`, one has `dA^2-3B>0`, and more sharply

\[
 -D^3\log(1+r_2)>6800x^2e^{-3x}.
\]

The complete `n>=3` perturbation satisfies

\[
 |D^3\log(1+S)|<125000000x^3e^{-8x}.
\]

Their ratio is less than

\[
 18400xe^{-5x}<\frac1{50}.
\]

Therefore

\[
 V'''(u)>0\qquad(u_*\le u\le1/2).
\]

## Global outward-score theorem

Let

\[
 Q(u)=uV''(u)-V'(u).
\]

Since `Q'=uV'''` and `Q(0)=0`, the preceding results prove `Q>0` through
`u=1/2`. The labelwise far-chamber estimate proves `Q>0` for `u>=1/2`.
Thus

\[
 \boxed{
 -u(\log\Phi)''(u)+(\log\Phi)'(u)>0
 \qquad(u>0).
 }
\]

For Gaussian-normalized moments

\[
 b_n=\frac{\mathbb E[U^{2n}]}{(2n-1)!!},
\]

this implies strict log-concavity:

\[
 b_{n+1}^2>b_nb_{n+2}.
\]

Therefore every degree-two Jensen polynomial of the completed theta source
is hyperbolic with negative-root orientation.

## Scope

This is the first complete infinite Jensen layer. It does not imply the
degree-three inequalities, the full Laguerre--Pólya hierarchy, or RH.
