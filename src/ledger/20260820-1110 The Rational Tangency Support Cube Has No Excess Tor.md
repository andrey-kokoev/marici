# 1110 — The Rational Tangency Support Cube Has No Excess Tor

## Input

Entry 1109 derived the normalized local factors at the rational tangency

\[
(u,v,a,b)=\left(\frac23,0,0,-\frac13\right).
\]

After splitting the doubled branch, the generic local equation has the form

\[
XY=\rho qU_-U_+,
\]

where

\[
U_-=3p+q-2A,
\qquad
U_+=3p+q+2A.
\]

Here \(\rho\) is the exceptional normal, \(q\) is the restriction of the
labelled \(L_1\) occurrence to the doubled conductor, and \(U_\pm\) are the two
coefficient branches found in Entry 1109.

## Hard claim

The intersection of the two coefficient branches creates no excess Tor and no
associated-grade cohomology over the existing exceptional and \(L_1\) faces.

## Étale-coordinate test

In the coordinate order \((\rho,q,p,A)\), the gradients of
\((\rho,q,U_-,U_+)\) form

\[
J=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&1&3&-2\\
0&1&3&2
\end{pmatrix}.
\]

Therefore

\[
\boxed{\det J=12\neq0.}
\]

The four factors are an étale local coordinate system. In particular, their
intersection is a regular sequence; the coincidence of \(q\) with
\(L_1|_{T=0}\) does not create an unlabelled multiplicity.

## Occurrence-resolved cube

For the ordered factors

\[
(\rho,q,U_-,U_+),
\]

the augmented signed Koszul cube has dimensions

\[
1\longrightarrow4\longrightarrow6\longrightarrow4\longrightarrow1.
\]

Exact computation gives differential ranks

\[
\boxed{(1,3,3,1)}
\]

and verifies every consecutive composition is zero. Hence

\[
\boxed{H^\bullet=0.}
\]

## Narrow conclusion

The rational tangency closes algebraically at the associated grade:

\[
\boxed{
\text{no excess Tor}
\quad+\quad
\text{no residual support-cube class}
\quad+\quad
\text{no new carrier datum}.
}
\]

The factors \(U_\pm\) remain meaningful coefficient branches, but their
intersection is ordinary normal crossing geometry. This result does not claim
that a physical relative chain activates or trivializes any integrated period.

## Verification

Checker:

research/benincasa/marici-gm/src/bin/rank12_u2over3v0_support_cube.rs.

Packet:

research/benincasa/rank12-u2over3-v0-support-cube.json.

Ledger claim: seqclaim-1b99aa30963519fb4a1f9b99.

Epistemic event:

ev-000000000809-4e3e3fac-e4fb-4de9-bb14-daadaf782cc5.

## Next finite falsifier

Proceed to the cyclic partner center \((u,v)=(-1,0)\). Derive its labelled
critical fiber point and Newton normal form independently; do not obtain it by
transporting the present formulas. Only afterward compare the two centers
through the source cyclic occurrence map.
