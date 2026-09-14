# Differentiating the semilocal dual--canonical pairing produces the prime current as its metric connection

## Finite-place pairing multiplier

For one finite prime, write

\[
L_p^+(s)=L_p(1/2+is),
\qquad
L_p^-(s)=L_p(1/2-is).
\]

On the real line,

\[
L_p^-(s)=\overline{L_p^+(s)}.
\]

The dual Hardy--Titchmarsh transition contributes `(L_p^+)^(-1)`, while the canonical transition contributes `L_p^-` in the bilinear pairing convention of Proposition 4.4. Their residual pairing multiplier is

\[
J_p(s)=
\frac{L_p^-(s)}{L_p^+(s)}.
\]

For a finite prime set `S`, put

\[
\boxed{
J_S(s)=
\prod_{p\in S}
\frac{L_p(1/2-is)}
     {L_p(1/2+is)}.
}
\]

On the real axis,

\[
|J_S(s)|=1.
\]

Thus the semilocal two-space pairing retains no Euler amplitude but does retain the complete Euler phase.

## Pairing connection

Define the phase connection

\[
\boxed{
V_S(s)=
\frac1{2i}
J_S(s)^{-1}J_S'(s)
=
\frac1{2i}
\partial_s\log J_S(s).
}
\]

Because `J_S` is unimodular on the real axis, `V_S` is real.

For one prime,

\[
J_p(s)
=
\frac{1-p^{-1/2-is}}
     {1-p^{-1/2+is}},
\]

with the displayed orientation, and direct logarithmic expansion gives

\[
\boxed{
V_p(s)
=(\log p)
\sum_{k\ge1}
p^{-k/2}
\cos(ks\log p)
}
\]

up to the global sign resulting from interchanging the two pairing orientations.

Therefore

\[
V_S=
\sum_{p\in S}V_p.
\]

## Exact differentiated-pairing identity

Let

\[
B_{J_S}(f,g)
=
\int_\mathbb R
f(s)g(s)J_S(s)ds
\]

on smooth functions for which boundary terms vanish. Let

\[
D=-i\partial_s.
\]

Then

\[
\begin{aligned}
B_{J_S}(Df,g)
+B_{J_S}(f,Dg)
&=
-i\int
\partial_s(fg)J_Sds\\
&=
 i\int
fgJ_S'ds.
\end{aligned}
\]

Using

\[
J_S'=2iV_SJ_S,
\]

we obtain

\[
\boxed{
B_{J_S}(Df,g)
+B_{J_S}(f,Dg)
=
-2
B_{J_S}(V_Sf,g).
}
\]

Equivalently,

\[
\boxed{
B_{J_S}((D+V_S)f,g)
+
B_{J_S}(f,(D+V_S)g)
=0.
}
\]

Thus `D+V_S` is skew-compatible with the bilinear semilocal pairing. The von-Mangoldt current is exactly the metric connection required to differentiate the preserved dual/canonical pairing.

## Boundary form

On a finite interval `[-T,T]`, integration by parts gives the exact Green identity

\[
\boxed{
B_{J_S,T}(Df,g)
+B_{J_S,T}(f,Dg)
=
-i
\left[f(s)g(s)J_S(s)
\right]_{-T}^{T}
-2B_{J_S,T}(V_Sf,g).
}
\]

Hence the local prime current and the boundary term are not separate additions: they are the interior and boundary pieces of one differentiated pairing.

After contour displacement from the real line to the strip boundaries, the limiting boundary functional is the natural location for the endpoint residues at `plus-or-minus i/2`.

## Archimedean extension

Include the gamma scattering phase

\[
J_\infty(s)=
\frac{L_\infty(1/2-is)}
     {L_\infty(1/2+is)}.
\]

Define

\[
J_{loc,S}=J_\infty J_S,
\qquad
V_{loc,S}=
\frac1{2i}
\partial_s\log J_{loc,S}.
\]

The same Green identity gives

\[
B_{J_{loc,S}}(Df,g)
+B_{J_{loc,S}}(f,Dg)
=
-2B_{J_{loc,S}}(V_{loc,S}f,g),
\]

so gamma and primes are one metric connection in the dual/canonical pairing.

## Prime-tower compatibility

Adjoining `q` gives

\[
J_{S\cup\{q\}}=J_SJ_q
\]

and therefore

\[
\boxed{
V_{S\cup\{q\}}
=V_S+V_q.
}
\]

Since scalar phase multipliers commute, adding primes in either order gives the same paired connection. This is the exact differentiated `2x2` tower law.

## Hermitian form audit

The pairing

\[
B_J(f,g)=
\int fgJ
\]

is bilinear, not by itself a positive Hermitian product. Positivity in Proposition 4.7 arises only after transporting both arguments through the source dual/canonical transforms and using the Fourier symmetry.

Therefore the Green identity constructs the correct Weil current but does not imply its positivity. Replacing `B_J` by

\[
\int f\bar g|J|ds
=
\int f\bar gds
\]

would erase the phase and hence erase all prime terms.

## Operator formulation

Let `mathcal J_S` denote the source duality map from the canonical tower to the anti-dual of the dual tower. Then the connection is formally

\[
\boxed{
V_S
=
\frac1{2i}
\mathcal J_S^{-1}
[D,\mathcal J_S].
}
\]

This is better typed than a one-space similarity: `mathcal J_S` maps between the two contragredient Hilbert spaces, and its commutator is interpreted on a common test core.

## Remaining comparison with the Weil trace

For an analytic convolution-square observer, the prime contribution is now exactly the insertion of the pairing connection `V_S`. What remains to be derived from the semilocal trace source is the observer placement and endpoint completion:

\[
W_S(g*g^*)
=
-\operatorname{Tr}_{paired}
\left(
\vartheta(g)^*
V_{loc,S}
\vartheta(g)
\right)
+
E_{end}(g),
\]

with signs and constants fixed by the primary trace formula.

The paired trace is not an ordinary positive trace. A rung-four construction must use the Green identity before collapsing the two towers, so that its boundary term and interior phase current can combine into a positive bulk energy.

## Disposition

Differentiating the semilocal dual/canonical pairing succeeds exactly:

\[
\boxed{
\text{pairing metric connection}
=
\frac1{2i}\partial_s\log J_S
=
\text{full finite-prime von-Mangoldt current}.
}
\]

The same identity includes gamma after adjoining `J_infinity`, and its finite-window Green boundary is the correct place for endpoint residues. The unresolved step is to identify the semilocal trace observer and prove that the completed Green form is a positive ordinary energy rather than a signed bilinear pairing.
