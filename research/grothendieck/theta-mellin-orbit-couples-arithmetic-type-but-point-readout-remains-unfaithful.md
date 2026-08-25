# Theta Mellin orbit couples arithmetic type but point readout remains unfaithful

## The source-derived label generator

On the algebraic integer-labelled coefficient module, define

\[
 Qe_n=(\log n)e_n.
\]

This is not an added regularizer.  It is the infinitesimal generator of the
authorized Mellin-character action

\[
 M_ze_n=n^{iz}e_n=e^{izQ}e_n.
\]

For real `z`, `M_z` is unitary in every source-derived diagonal arithmetic
norm.

## The coupled analytic detector

Let `U` be theta-germ synthesis,

\[
 Ue_n(t)=\Phi(t+\log n).
\]

The active arithmetic--analytic detector is the full Mellin orbit

\[
 \boxed{
 \mathcal K_c(t,z)
 =UM_zc(t)
 =\sum_nc_n n^{iz}\Phi(t+\log n).}
\]

It couples exact label dynamics into the seam germ rather than storing labels
in a silent direct summand.  Its evolution is

\[
 \partial_z\mathcal K_c(t,z)
 =i\,UQM_zc(t).
\]

The `z`-jets therefore retain all logarithmic label moments.

## Algebraic faithfulness of the full orbit

For a finite packet with distinct labels, fix any `t` for which every
coefficient `c_n Phi(t+log n)` under consideration is defined.  As a function
of `z`, `K_c(t,z)` is an exponential polynomial with distinct frequencies
`log n`.  Such exponentials are linearly independent.  Hence

\[
 \mathcal K_c(t,z)\equiv0\text{ in }z
 \quad\Longrightarrow\quad
 c_n\Phi(t+\log n)=0\text{ for every }n.
\]

For the positive theta kernel, the factors `Phi(t+log n)` are nonzero on the
positive chamber, so

\[
 \boxed{
 \mathcal K_c\equiv0\Longrightarrow c=0}
\]

on every finite labelled packet.  The Mellin orbit is therefore a second
source-native realization of the faithful detector.

## One spectral point is still lossy

At any fixed `z_0`, two labels already admit a nonzero cancellation:

\[
 c_{n_1}=n_2^{iz_0}\Phi(t+\log n_2),
 \qquad
 c_{n_2}=-n_1^{iz_0}\Phi(t+\log n_1).
\]

Then

\[
 \mathcal K_c(t,z_0)=0
\]

although `c` and its complete Mellin orbit are nonzero.

Thus:

\[
 \boxed{
 \text{active arithmetic coupling restores orbit faithfulness, not
 point-evaluation faithfulness}.}
\]

This is not a flaw in the Mellin dynamics. It is the distinction between a
state and one matrix coefficient of its orbit.

## Consequence for RH

The Riemann readout is evaluated at one spectral parameter. Therefore neither
the full seam germ nor the full Mellin orbit can by itself prove its
nonvanishing at that point.  A source theorem must restrict the distinguished
state--detector pair, not merely enlarge the observable family until it
becomes faithful.

The only remaining non-generic data are now explicit:

1. the positive Fock/Euler vacuum fixes the coefficient packet;
2. Poisson sewing fixes the detector covector and its reciprocal boundary
   terms;
3. the two-sector metric polarization fixes the allowed comparison;
4. RH asks for transversality of this distinguished pair off the seam.

Arbitrary coefficient witnesses, including the two-label cancellation above,
show that no theorem valid on the whole coefficient module can establish that
transversality.

## Completion lesson

The Mellin orbit can distinguish adjacent labels only by resolving spectral
scales of order

\[
 |z|\,|\log(n+1)-\log n|\simeq |z|/n.
\]

Uniform discrimination therefore requires unbounded spectral reach as
`n->infinity`.  This is the dynamical form of packet 182's nonclosed-range
obstruction.

## Scope

This packet constructs the canonical arithmetic--analytic coupling and proves
finite full-orbit faithfulness. It also proves fixed-point unfaithfulness for
arbitrary coefficient packets. It does not show that the distinguished
positive Fock vacuum realizes such a cancellation, nor decide its Poisson-sewn
transversality.
