# Theta first-order tail channel has no completion escape

## Oriented half-line operator

Let

\[
 A_s=-\partial_q+(1-s)
\]

on the decaying half-line domain, and put

\[
 a=1-\Re(s)>0.
\]

After the unitary gauge removing `Im(1-s)`, packet 164 gives

\[
 \lVert A_sG\rVert_2^2
 =\lVert h'\rVert_2^2+a^2\lVert h\rVert_2^2+a|h(0)|^2.
\]

In particular,

\[
 \boxed{
 \lVert A_sG\rVert_2\ge a\lVert G\rVert_2.}
\]

## Explicit inverse

For the gauged equation

\[
 -h'+ah=k,
 \qquad h(\infty)=0,
\]

the unique solution is

\[
 h(q)=e^{aq}\int_q^\infty e^{-at}k(t)\,dt.
\]

Equivalently this is one-sided convolution with the decaying kernel after
reversing the half-line orientation.  The energy identity yields

\[
 \boxed{\lVert A_s^{-1}\rVert\le a^{-1}.}
\]

Thus `A_s` is injective, has closed range, and possesses a bounded inverse on
its range.  Its graph completion cannot acquire a nonzero state with zero
bulk image.

## Cutoff completion

If cutoff states satisfy

\[
 A_sG_X=G_X+f_X
\]

and the right sides are Cauchy in `L2`, then `G_X` is Cauchy in `L2`.  The
identity also controls the gauged derivative and endpoint, so the limit lies
in the same graph domain and

\[
 G_X(0)\longrightarrow G(0).
\]

Therefore the hostile finite-complex mechanism

\[
 \varepsilon_X\longrightarrow0,
 \qquad \lVert h_X\rVert\longrightarrow\infty
\]

cannot occur in this oriented first-order tail channel at fixed `s` in the
critical strip.

## Uniformity

On a compact set `K` with

\[
 \sup_{s\in K}\Re(s)\le1-\delta,
\]

the inverse bound is uniform:

\[
 \sup_{s\in K}\lVert A_s^{-1}\rVert\le\delta^{-1}.
\]

No uniform statement is made as `Re(s)->1`.

## Remaining obstruction

Completion escape is closed for the native one-sided tail operator.  It may
still occur in:

1. the comparison between direct and Fourier--Tate-dual sectors;
2. the valuation/Fock and distributional boundary ports;
3. the mixed modular seam current;
4. the passage from the completed scalar zero to the fully labelled doubled
   state.

Hence the unresolved RH mechanism is no longer ordinary loss of closed range
inside either first-order tail channel.  It is the source coherence coupling
those individually well-controlled channels.
