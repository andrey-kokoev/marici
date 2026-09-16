# Horizontal and vertical composition for gapless spectral completions

## Spectral completion object

A gapless completed positive object is a tuple

\[
\mathfrak S
=
(H,R,Z,\{E_\eta\}_{\eta>0}),
\]

where

\[
R\succeq0,
\qquad
Z=1_{\{0\}}(R),
\qquad
E_\eta=1_{[\eta,\infty)}(R).
\]

Every stage

\[
H_\eta=E_\eta H
\]

is coercive:

\[
\langle u,Ru\rangle
\ge
\eta\|u\|^2.
\]

The stages increase as \(\eta\downarrow0\) and strongly exhaust

\[
(1-Z)H.
\]

## Exact spectral morphism

An exact spectral morphism

\[
F:\mathfrak S\longrightarrow\mathfrak S'
\]

consists of a bounded map satisfying

\[
FR=R'F,
\]

\[
FZ=Z'F,
\]

and

\[
FE_\eta=E'_\eta F
\]

for every declared threshold.

The projection relation follows from bounded Borel functional calculus once the intertwining theorem is available on the declared domains. It remains explicit in the certificate because unbounded-domain transport requires its own proof.

## Sequential composition

For exact spectral morphisms

\[
\mathfrak S_0
\xrightarrow{F}
\mathfrak S_1
\xrightarrow{G}
\mathfrak S_2,
\]

one has

\[
(GF)R_0=R_2(GF),
\]

\[
(GF)Z_0=Z_2(GF),
\]

and

\[
(GF)E_{0,\eta}
=E_{2,\eta}(GF).
\]

Thus exact spectral certificates compose without loss of threshold.

## Controlled spectral morphism

Regulator comparisons may distort the spectral scale. A controlled spectral morphism carries a monotone threshold function

\[
\varphi_F:(0,\infty)\to(0,\infty)
\]

with

\[
F(H_\eta)
\subseteq
H'_{\varphi_F(\eta)}.
\]

For composable controlled morphisms, the composite threshold law is

\[
\varphi_{GF}
=
\varphi_G\circ\varphi_F.
\]

A cofinality certificate requires

\[
\varphi_F(\eta)\longrightarrow0
\]

as \(\eta\downarrow0\). This ensures that the morphism reaches the full radical complement in the spectral limit.

## Horizontal conductor composition

A horizontal conductor comparison is admitted when it supplies:

1. a common threshold set or a declared cofinal refinement;
2. stage maps
   \[
   F_\eta:H_\eta\to H'_\eta;
   \]
3. commutation with threshold inclusions;
4. preservation of the stage forms;
5. transport of the zero spectral projection.

Two horizontal maps compose stagewise. Their form-preservation cells paste by ordinary composition.

## Vertical successor composition

A vertical successor may change regulator or source stage. It is admitted when its stage maps satisfy

\[
T_{\eta,\lambda'\lambda}:
H_{\eta,\lambda}
\to
H_{\varphi_{\lambda'\lambda}(\eta),\lambda'}
\]

and

\[
T_{\lambda''\lambda'}T_{\lambda'\lambda}
=T_{\lambda''\lambda}
\]

on a common cofinal spectral refinement.

The threshold controls must satisfy

\[
\varphi_{\lambda''\lambda}
=
\varphi_{\lambda''\lambda'}
\circ
\varphi_{\lambda'\lambda}.
\]

## Interchange

For a square with horizontal maps \(F,F'\) and vertical maps \(T,T'\), spectral interchange is the stage identity

\[
T'_{\eta}F_\eta
=
F'_{\eta}T_\eta
\]

on a common threshold refinement. This is the gapless analogue of completion-certificate transport.

## Output

Successful composition returns:

- the composite stage maps;
- the composite threshold-control function;
- the radical transport cell;
- stagewise form-preservation cells;
- the cofinality certificate;
- the interchange cell when a square is supplied.

This gives the gapless completion branch a genuine partial categorical composition law. Global associativity follows strictly for exact maps and follows for controlled maps once threshold functions and chosen cofinal refinements are composed strictly.
