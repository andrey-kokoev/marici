# Theta unit evaluation must precede scalar Euler--Maclaurin synthesis

## Two completions were being conflated

There are two different limits in the first Adams construction.

The labelled carrier has finite truncations

\[
\mathcal L_N=\prod_{1\le n\le N}\mathcal H_n
\]

with restriction maps that forget the last coordinates. Its completion is the
compatible labelled object

\[
\mathcal L=\varprojlim_N\mathcal L_N.
\]

The scalar theta channel instead applies the summation map

\[
\Sigma_N(h_1,\ldots,h_N)=\sum_{n\le N}h_n
\]

and then routes the continuum wall and endpoint half-cell by
Euler--Maclaurin. These are not two presentations of one quotient.

## Unit evaluation survives labelled completion exactly

For every \(N\ge1\), let

\[
\epsilon_{1,N}
=
\mathcal M_1^{-1}\operatorname{ev}_1.
\]

If \(r_{N+1,N}:\mathcal L_{N+1}\to\mathcal L_N\) is restriction, then

\[
\epsilon_{1,N+1}
=
\epsilon_{1,N}r_{N+1,N}.
\]

Hence the finite unit evaluations form a compatible cone and induce

\[
\epsilon_1:\mathcal L\longrightarrow\mathcal H_{\mathrm{source}}.
\]

No limit estimate is required: the first coordinate is literally stationary
for all cutoffs \(N\ge1\). In every product or projective topology,
\(\operatorname{ev}_1\) is continuous.

For the diagonal orbit \(\Delta f=(\mathcal M_nf)_n\),

\[
\epsilon_1\Delta f=f.
\]

Thus the labelled completion retains the Adams counit exactly.

## Scalar synthesis destroys the counit

The unit evaluation generally does not descend through \(\Sigma_N\). Already
at cutoff two, for any nonzero analytic vector \(h\),

\[
v=(h,-h)
\]

satisfies

\[
\Sigma_2v=0,
\qquad
\operatorname{ev}_1v=h\ne0.
\]

Therefore

\[
\ker\Sigma_N
\not\subseteq
\ker\operatorname{ev}_1
\]

whenever at least two label fibers share a scalar target. No map
\(\bar\epsilon_1\) can satisfy

\[
\bar\epsilon_1\Sigma_N=\epsilon_{1,N}
\]

on the full labelled carrier.

Euler--Maclaurin wall routing repairs convergence of \(\Sigma_N\); it does not
repair this algebraic kernel obstruction. Adding the continuum integral and
endpoint half-cell changes the scalar boundary packet, not the fact that
label cancellation erases the first coordinate.

## Correct constructor order

The authorized architecture is therefore

\[
\begin{array}{ccc}
\text{labelled source}
&\xrightarrow{\text{labelwise Green square}}&
\text{labelled boundary}\\
&\searrow\epsilon_1&\downarrow\Sigma_{\mathrm{ren}}\\
&&\text{scalar theta observer}.
\end{array}
\]

The two outgoing arrows have different jobs:

- \(\epsilon_1\) is the constructor counit recovering the single Stieltjes
  boundary copy;
- \(\Sigma_{\mathrm{ren}}\) is the Euler--Maclaurin-renormalized theta observer.

Neither factors through the other.

Consequently the first Adams edge must be formed before scalar theta
augmentation. Scalar completion may then observe that edge, but it cannot
authorize or reconstruct it.

## Compatibility with the Green square

All labelwise analytic arrows commute with finite restrictions. Therefore the
exact identity

\[
\mathcal C^{-1}\mathcal M_ns_p=\mathcal M_nb_p
\]

passes to \(\mathcal L\), and unit evaluation gives

\[
\epsilon_1
\left(
  (\mathcal C^{-1}\mathcal M_ns_p)_n
\right)
=
b_p.
\]

The ordered primitive then yields

\[
d_p=-\frac12S_{\mathrm{ord}}b_p.
\]

Wall, jump, and prime labels remain available because no scalar label quotient
has occurred along this constructor path.

## Consequence for sewing

Any downstream sewing map that needs both the Adams constructor and scalar
theta completion must receive the pair

\[
(\epsilon_1,\Sigma_{\mathrm{ren}})
\]

or, equivalently, receive the labelled carrier before applying its own typed
readouts. Sewing only the scalar theta sum irreversibly loses the constructor
counit.

A proposed sewing quotient \(q\) permits unit evaluation only if

\[
\ker q\subseteq\ker\epsilon_1.
\]

The scalar synthesis quotient fails this condition by the two-label hostile
above.

## Verdict

The renormalized theta cutoff does retain \(n=1\), but only on the labelled
projective carrier, where that coordinate is stationary and continuously
evaluated. It does not retain unit evaluation after scalar synthesis.

This closes the earlier completion question by fixing the arrow order rather
than forcing an impossible descent:

\[
\text{labelwise completion}
\longrightarrow
\begin{cases}
\text{unit counit},\\
\text{renormalized scalar observer}.
\end{cases}
\]

The first Adams edge is now defined through the unit branch. The next global
gate is to construct a sewing interface that accepts both branches without
identifying the scalar observer with the constructor counit.
