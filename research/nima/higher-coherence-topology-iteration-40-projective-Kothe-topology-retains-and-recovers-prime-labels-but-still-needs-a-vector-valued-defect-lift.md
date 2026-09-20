# Higher-coherence topology iteration 40: projective Köthe topology retains and recovers prime labels, but still needs a vector-valued defect lift

## Candidate topology

Index prime-power channels by `lambda=(p,k)`, with

\[
L_\lambda=k\log p,
\qquad
a_\lambda=k^{-1}e^{-L_\lambda/2}.
\]

Use the projective exponential Köthe space with seminorms

\[
q_\delta(c)
=\sum_\lambda |c_\lambda|e^{\delta L_\lambda},
\qquad \delta>0.
\]

This topology is adapted to the actual theta incidence rather than imposing a
false uniform Hilbert lower bound.

## Established recovery

Multiplication by `a_lambda` is continuous. On the source-generated labelled
history range its inverse is also continuous with finite seminorm loss:

\[
q_\delta(a^{-1}d)
\le C_\varepsilon
q_{\delta+1/2+\varepsilon}(d).
\]

Therefore the labelled incidence has zero radical and a continuous recovery
port in this projective topology. Prime/grade cutoffs commute with incidence
and recovery.

This improves materially on iteration 39: source labels can be recovered
without any uniform Hilbert frame margin.

## Central residual packet

A labelled residual packet would have coordinates

\[
R_{p,k}(z)
=
(1-p^{-2\operatorname{Re}z})E_{p,k}(b_z).
\]

Coordinate evaluations are continuous in the Köthe topology. Hence

\[
R(z)=0
\quad\Longleftrightarrow\quad
R_{p,k}(z)=0\ \text{for all }(p,k).
\]

If this packet is in the source-generated range and its synthesized history is
zero, the recovery map forces every coordinate to vanish. One positive
coordinate then yields `Re(z)=0`.

## The exact missing square

The available bordered identity is scalar:

\[
\Delta_{\rm border}(z)=\tau(z)H_{\rm border}(z).
\]

At a Xi zero it kills the bordered scalar defect. To exploit Köthe recovery one
must construct a commuting square

\[
\begin{array}{ccc}
R(z)&\xrightarrow{\mathcal I}&\text{labelled history}\\
\downarrow&&\downarrow C\\
\Delta_{\rm border}(z)&=&\text{common bordered target},
\end{array}
\]

where `C` is injective on the particular source-generated residual range.

The current scalar codiagonal is not known to have that injectivity. The
Köthe recovery map acts before codiagonalization and does not factor through a
single scalar readout.

## Nuclear and limit advantages

For a nuclear/Montel choice of Köthe weights, bounded sets have compactness
properties that can improve cutoff limits and tensor products. This may close
technical infinite-cone sewing problems and can make weak/strong dual
convergence coincide on controlled bounded families.

These advantages preserve a labelled identity once constructed; they do not
lift a scalar identity back through a noninjective codiagonal.

## Hostile test

Choose two labelled coordinates with nonzero entries whose common-history or
scalar images cancel. The Köthe packet remains nonzero and all coordinate
projections detect it, while the scalar defect is zero. Rapid decay does not
prevent this finite-support hostile. Only injectivity of `C` on the residual
range excludes it.

## Verdict for topology 40

Projective Köthe topology is the strongest completion so far for retaining and
recovering arithmetic labels. It removes the Hilbert-margin objection and is a
credible carrier for an infinite cone tower. But confinement still requires a
vector-valued defect lift or a proof that the bordered codiagonal is injective
on the residual range.

The next nonredundant topology to test is a sheaf of locally convex Köthe
modules over the spectral parameter, asking whether analytic continuation of
all coordinate germs makes that codiagonal injective even though pointwise
scalar evaluation does not.