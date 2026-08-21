# Paired deck Mackey norm and the integral normalization obstruction

## Algebraic theorem

For a finite deck set \(G\), put

\[
A(G)=\operatorname{Fun}(G,\mathbf Q),\qquad B(G)=\mathbf Q[G],
\]

with their evaluation pairing.  A finite map \(q:G\to H\) supplies

\[
q^*:A(H)\to A(G),\quad q_!:A(G)\to A(H),
\]

and

\[
q_*:B(G)\to B(H),\quad
q^!:B(H)\to B(G),\qquad
q^!\Gamma_h=\sum_{q(g)=h}\Gamma_g.
\]

The two adjunctions are

\[
\langle q^*c,\Gamma\rangle_G=\langle c,q_*\Gamma\rangle_H,
\qquad
\langle q_!a,\Delta\rangle_H=\langle a,q^!\Delta\rangle_G.
\]

Together with finite-set Beck--Chevalley, these data form the minimal paired
coefficient--Betti correspondence object.  This is an algebraic Mackey-style
system; it imports no physical relative-chain pushforward.

If \(q\) is a surjective homomorphism and \(K=\ker q\), then

\[
q_!q^*=|K|\operatorname{id}_{A(H)},\qquad
q_*q^!=|K|\operatorname{id}_{B(H)}.
\]

Upstairs, both composites are the kernel norm

\[
N_K=\sum_{k\in K}k,qquad
q^*q_!=N_K\text{ on }A(G),\quad q^!q_*=N_K\text{ on }B(G),
\]

and \(N_K^2=|K|N_K\).

## Smallest hostile quotient

Take \(q:C_2\to1\).  A deck-symmetric fiber transfer has one weight \(w\).
Frozen identity normalization forces \(w=1\), because
\(q_!\delta_0=\delta_0\).  Normalized ambidexterity forces \(2w=1\), hence
\(w=1/2\).  The requirements are incompatible.

Thus unnormalized integral transfer preserves the selected delta vector but
has multiplicity two in pull--push.  Averaging removes that multiplicity only
by sending the selected delta vector to one half.  For every nontrivial
kernel the same conflict is \(1\) versus \(1/|K|\).

## Survival audit

The following survive unchanged:

- objectwise physical-readout congruence and its D3 commutator detector;
- simultaneous coefficient--Betti covariance;
- the algebraic finite-correspondence and Beck--Chevalley calculus;
- fiberwise prime-to-exponent repetition monoids, including odd indices for
  \((C_2)^5\).

The following do not follow:

- integral normalized ambidexterity across a nontrivial quotient;
- cross-deck physical naturality without a source-derived pushforward on
  relative chains;
- any semiring, Frobenius, Adams, lambda, Euler-product, or Phase-II
  promotion.

Rational averaging is available algebraically, but it changes the frozen
physical normalization.  Entry 1224's sheet-label coalescence therefore
cannot be promoted to \(q_*\) on physical relative chains by cardinality
alone.

## Verification

`checkers/paired_deck_mackey_norm.py` exhausts every cyclic surjection
\(C_n\to C_m\) with \(m\mid n\) and \(n\le12\), verifies both norm formulas,
the quadratic relation, and the coefficient--Betti adjunction, and pins the
hostile \(C_2\to1\) normalization conflict.
