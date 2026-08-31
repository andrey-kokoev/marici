# The comoving window kernel is the missing middle transformation

## Correction

The claim that the analytic four-front square and arithmetic Euler square still
lack any middle natural transformation was too strong.  The repository already
contains the source-derived comoving kernel

\[
(\mathcal K\mu)(q)=\int W_t(q)\,d\mu(t),
\]

with

\[
\mathcal K\delta_{kL}=W_{kL}.
\]

This map starts on the arithmetic scale-measure carrier and lands in the
analytic endpoint multiplier carrier.  It is prime-diagonal, reciprocal-odd,
cutoff-natural, and contractive in the declared source seminorms.  Therefore
it is precisely the missing middle arrow, in the source-to-analytic direction.

## Differentiated front map

Differentiation in the analytic coordinate gives

\[
D\mathcal K\delta_t
=DW_t
=U_{-t}f_0-U_tf_0
=q_t.
\]

Hence, grade by grade,

\[
\boxed{
D\mathcal K\delta_{kL}=q_{kL}.
}
\]

For the strict first-Adams coefficient vector

\[
S_{12}=\operatorname{diag}(-1,+1),
\]

the signed arithmetic packet

\[
-\delta_L+\delta_{2L}
\]

maps exactly to

\[
-q_L+q_{2L}=b_p.
\]

Thus the four-front orientation twist is not merely compatible with the
comoving kernel; it is its differentiated image.

## Source coefficients remain external

The primitive and square Euler scale measures carry their own coefficients,
for example

\[
\mu_{p,1}=p^{-1/2}\delta_L,
\qquad
\mu_{p,2}=\frac12p^{-1}\delta_{2L}.
\]

The kernel does not absorb these coefficients:

\[
D\mathcal K\mu_{p,k}
=a_{p,k}q_{kL},
\qquad
a_{p,k}=\frac1k p^{-k/2}.
\]

The sheet-odd Euler current applies the logarithmic boundary derivative,
which multiplies grade \(k\) by \(2kL\).  Therefore

\[
2kL\,a_{p,k}=2Lp^{-k/2},
\]

exactly the coefficient appearing in

\[
\kappa_p^{(k)}=2Lp^{-k/2}\Phi'(kL).
\]

This shows that the endpoint-window and Euler-sampling coefficients have one
translation-algebra provenance; the cancellation of \(k\) is source-derived,
not fitted after trace evaluation.

## Correct diagram

The pre-scalarized strict-grade diagram is

\[
\begin{array}{ccc}
\text{Euler scale measure at }kL
&\xrightarrow{\ D\mathcal K\ }&
\text{Gaussian reciprocal front }q_{kL}\\
\downarrow\,2kL && \downarrow\,\text{twisted history trace}\\
\text{Euler odd boundary current}
&\xrightarrow{\ B_{\Phi'}^\times\ }&
\text{theta/Wronskian odd line}.
\end{array}
\]

The top arrow and its sign/label behavior are constructed.  The left
coefficient agrees exactly with the arithmetic sampling coefficient.

## What remains open

The existence of the middle arrow is therefore closed.  What is not yet proved
is that the lower square commutes as a Green adjunction.  In particular, one
still needs the common relative pairing that identifies the transpose of the
differentiated comoving kernel with evaluation against \(\Phi'\), while
preserving:

- multiplier-valued endpoint typing;
- half-density twisted graph domains;
- adjoint order and reciprocal orientation;
- primitive/square separation;
- radical annihilation and graph closure.

This is exactly the “remaining relative Green pairing” already isolated in
the comoving-window packet.  Defining the diagonal ratio
\(S_{12}D_{p,12}\) does not prove that adjunction, but the comparison arrow
itself no longer needs to be invented.

## Revised earliest local gate

The earliest local theorem is now:

> Prove on a common source core that the relative Green transpose of
> \(D\mathcal K\) is the Euler-to-theta sampling functional
> \(B_{\Phi'}^\times\), grade by grade for \(k=1,2\).

After this adjunction, the already computed twisted traces and determinant
margins complete the local scalar assembly.  The connected tail, radical
descent, and global closed range remain open.  No RH conclusion is authorized.
