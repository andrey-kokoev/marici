# Deeper theta mechanism: ordered Krein signature forbids the two-moment collision

## Status

Exact signed-measure theorem and pre-resolvent sufficient condition. An
off-seam zero of the ordered framed transfer requires the positive and negative
parts of its spectral measure to match both their Cauchy-windowed mass and
their Cauchy-windowed barycenter. If the two Krein signatures occupy ordered,
disjoint carrier spectral regions, this simultaneous collision is impossible.

This condition is strictly weaker than positivity of the full spectral measure
and is stated before forming the resolvent transfer. It is therefore a genuine
candidate source law rather than a Herglotz restatement.

## Signed decomposition

Let

\[
F(z)
=
\int_{\mathbb R}
\frac{d\mu(t)}{t-z}
\]

be the ordered framed transfer, with Jordan decomposition

\[
d\mu=d\mu_+-d\mu_-.
\]

Both \(\mu_+\) and \(\mu_-\) are positive measures. They represent the
positive- and negative-signature spectral sectors of the modular metric on the
endpoint-cyclic state.

## Off-seam zero equations

Write

\[
z=x+iy,
\qquad
y\ne0,
\]

and define the positive Cauchy window

\[
p_{x,y}(t)
=
\frac{1}{(t-x)^2+y^2}.
\]

The equation \(F(z)=0\) gives

\[
\int p_{x,y}\,d\mu_+
=
\int p_{x,y}\,d\mu_-
\]

and

\[
\int (t-x)p_{x,y}\,d\mu_+
=
\int (t-x)p_{x,y}\,d\mu_-.
\]

Let the common positive mass be \(M_{x,y}\). If it is nonzero, the first
identity permits normalization of both weighted measures to probability
states. The second identity then becomes equality of their barycenters:

\[
\frac{1}{M_{x,y}}
\int t p_{x,y}(t)\,d\mu_+(t)
=
\frac{1}{M_{x,y}}
\int t p_{x,y}(t)\,d\mu_-(t).
\]

Thus an off-seam zero is exactly a collision of two locally reweighted
signature sectors at monopole and dipole order.

## Ordered-signature theorem

Assume there is a real threshold \(\tau\) and a gap \(\delta>0\) such that

\[
\operatorname{supp}\mu_+
\subseteq
(-\infty,\tau]
\]

and

\[
\operatorname{supp}\mu_-
\subseteq
[\tau+\delta,\infty).
\]

Multiplication by the strictly positive window \(p_{x,y}\) does not change
either support. Therefore the positive-sector barycenter is at most \(\tau\),
while the negative-sector barycenter is at least \(\tau+\delta\).

They cannot be equal. Hence

\[
F(z)\ne0
\]

for every nonreal \(z\).

The same theorem holds with the two signs reversed.

## Touching supports

If the supports meet only at \(\tau\), equality of the two weighted
barycenters can occur only when both weighted measures are concentrated at the
common boundary point. A source rule forbidding cancellation of opposite
signature atoms at the same typed carrier label then restores strict
nonvanishing.

This is where arithmetic typing may matter: two contributions at the same
scalar spectral coordinate need not be the same labelled state and cannot be
cancelled unless a source-authorized incidence identifies them.

## Physical interpretation

A Hamiltonian--Krein instability requires modes of opposite signature to meet
at the same frequency before leaving the stable axis. Spectral separation of
the signatures prevents the collision even though the energy is indefinite.

The theta analogue is:

- positive and negative modular charges may both exist;
- an off-seam dark mode requires them to balance within the same Cauchy
  spectral window;
- ordered signature prevents their weighted centers from meeting;
- therefore neutral invisible memory cannot be constructed.

This is a more faithful physical mechanism than global energy positivity.

## Exact hostile explains the requirement

The three-atom hostile has poles

\[
-1,
\qquad
0,
\qquad
1
\]

and signs

\[
+1,
\qquad
-1,
\qquad
+1.
\]

The positive signature surrounds the negative signature. There is no spectral
ordering threshold. The two positive atoms can match the central negative atom
in both weighted mass and barycenter at \(z=\pm i\).

By contrast, two atoms of opposite sign are automatically ordered. Their
single transmission zero lies on the real axis. The first nonreal hostile
requires an interlacing or repeated signature pattern.

## Source-local candidate law

The new finite question is:

> Does labelled theta/Tate incidence force the modular signature on the
> endpoint-cyclic carrier spectrum to have one ordered transition, rather than
> an alternating pattern?

This can be tested before forming \(F\):

1. diagonalize the finite carrier \(A_X\);
2. compute the source-derived spectral weights
   \(\langle P_jb_X,K_XP_jb_X\rangle\);
3. retain their arithmetic and boundary types;
4. count sign transitions in carrier order;
5. test whether seam augmentation joins touching opposite types without
   erasing their labels;
6. seek a cutoff-independent separation or monotone-signature law.

No zero location enters this procedure.

## Beyond a hard support gap

Strict support separation is sufficient but may be too strong. Weaker
pre-resolvent laws could still forbid barycenter equality:

- stochastic ordering of every Cauchy-windowed signature pair;
- a monotone likelihood-ratio relation;
- total positivity of the kernel transporting source labels to carrier
  frequency;
- variation diminution limiting the signed spectral measure to one sign
  transition;
- or a typed interlacing theorem that makes every neutral collision occur only
  on the seam.

Each formulation has a finite hostile: any three typed weights with the pattern
positive, negative, positive and a realized off-seam zero.

## Completion gate

Finite ordered signature is insufficient if the separation gap collapses with
cutoff. The completed theorem needs either

\[
\inf_X\delta_X>0
\]

on the relevant spectral region, or a gap-free stochastic-order law stable
under weak convergence and the source rigging.

Opposite signature mass may also escape to infinity and return through the
primitive or square boundary currents. Those currents must remain part of the
ordered spectral measure rather than being removed by determinant
regularization.

## Falsifiers

The ordered-signature route fails if:

- the actual finite modular weights already alternate in carrier order;
- a positive-negative-positive labelled triple survives every source
  constraint;
- the sign threshold depends on zero locations;
- finite thresholds exist but their separation collapses at completion;
- or hostile reciprocal perturbations preserve the same source ordering law
  while introducing an off-seam zero.

## Decisive conclusion

The first genuinely weaker physical mechanism has emerged. RH does not require
the framed spectral energy to be positive everywhere. It would be enough for
opposite modular signatures to remain ordered so that their Cauchy-windowed
mass and barycenter can never collide away from the seam.

The next exact calculation is the sign-transition pattern of the
source-derived modular weights on the finite endpoint-cyclic theta carrier.
