# Polynomial divisor counting gives strong Schwartz-dual convergence of the infinite atomic boundary current

## Objective

Extend the finite moving-index current

\[
\mu_N
=
\sum_{j\le N}
n_j
\delta_{t_j}
\]

to an infinite symmetry-completed divisor current in the strong Schwartz dual.

No positivity or zero-location assumption is used. Only a polynomial counting bound is required.

## Divisor counting hypothesis

Let \(D\) be a discrete multiset on \(\mathbb R\) with integer multiplicities \(n_t\). Assume

\[
N_D(R)
=
\sum_{
|t|
\le R
}
|n_t|
\le
C
(1+R)^d
\log^e(2+R)
\]

for some finite \(C,d,e\).

The classical completed-zeta zero count satisfies such a bound, with growth of order \(R\log R\).

## Atomic current

Define formally

\[
\mu_D
=
\sum_{t\in D}
n_t
\delta_t.
\]

For \(\phi\in\mathcal S(\mathbb R)\), set

\[
\langle
\mu_D,
\phi
\rangle
=
\sum_{t\in D}
n_t
\phi(t).
\]

The series converges absolutely.

Indeed, choose an integer \(M>d+2\). Then

\[
|\phi(t)|
\le
q_{M,0}(\phi)
(1+|t|)^{-M}.
\]

Decomposing into unit shells gives

\[
\sum_{t\in D}
|n_t|
|\phi(t)|
\le
q_{M,0}(\phi)
\sum_{k\ge0}
igl(
N_D(k+1)-N_D(k)
igr)
(1+k)^{-M},
\]

and the final series converges by the counting hypothesis.

Therefore

\[
\mu_D
\in
\mathcal S'(
\mathbb R
).
\]

## Strong-dual convergence

Let

\[
\mu_{D,R}
=
\sum_{
|t|
\le R
}
n_t
\delta_t.
\]

Then

\[
\mu_{D,R}
\longrightarrow
\mu_D
\]

in the strong dual

\[
\mathcal S'(
\mathbb R
)_\beta.
\]

To prove this, let \(B\subset\mathcal S\) be bounded. For every \(M\),

\[
C_{B,M}
=
\sup_{
\phi\in B,
t\in\mathbb R
}
(1+|t|)^M
|\phi(t)|
<
\infty.
\]

Hence

\[
\sup_{
\phi\in B
}
|
\langle
\mu_D-
\mu_{D,R},
\phi
\rangle
|
\le
C_{B,M}
\sum_{
|t|>R
}
|n_t|
(1+|t|)^{-M}.
\]

The right side tends to zero for \(M>d+2\). This is precisely strong-dual convergence.

## Symmetry-completed current

Suppose \(D\) is invariant under

\[
t
\longmapsto
-t
\]

with matched multiplicities. Then

\[
\mu_D
=
\sum_{t>0}
n_t
(
\delta_t+
\delta_{-t}
)
+
n_0
\delta_0.
\]

It is dagger invariant under boundary reflection.

An oriented crossing current attaches a sign \(\sigma_t\in\{+1,-1\}\):

\[
\mu_D^{cross}
=
\sum_{t
e0}
\sigma_t
n_t
(
\delta_t+
\delta_{-t}
).
\]

The same convergence theorem applies because only absolute multiplicities enter the estimate.

## Weighted and derivative atoms

More generally, consider

\[
\mu
=
\sum_{t\in D}

a_t
\delta_t^{(k_t)}.
\]

Assume:

1. \(|a_t|\le C(1+|t|)^m\);
2. \(k_t\le k_{max}\);
3. the same polynomial counting bound holds.

Then

\[
\mu
\in
\mathcal S'(
\mathbb R
),
\]

and symmetric truncations converge strongly. One chooses

\[
M>d+m+k_{max}+2
\]

and uses the corresponding derivative Schwartz seminorm.

Thus finite-order resonance jets and polynomially weighted crossing multiplicities are also admitted.

## Source pairing

For Mellin--Schwartz source vectors,

\[
Q_D(p,q)
=
\langle
\mu_D,
\overline{m_q}m_p
\rangle
\]

has the absolutely convergent expansion

\[
Q_D(p,q)
=
\sum_{t\in D}
n_t
m_p(t)
\overline{m_q(t)}.
\]

The finite truncations converge uniformly on bounded subsets of

\[
\mathscr G_r^{\mathcal S}
\times
\mathscr G_r^{\mathcal S}.
\]

Therefore the infinite atomic current defines a continuous completed source form.

## Successor transport

For a convolution multiplier \(m_a\) of polynomial Schwartz-multiplier growth, the observed current becomes

\[
M_{|m_a|^2}'
\mu_D
=
\sum_{t\in D}
n_t
|m_a(t)|^2
\delta_t.
\]

If \(|m_a(t)|\) has polynomial growth on the boundary, the transported coefficients still satisfy a polynomial bound. Hence the successor preserves the tempered-current class and strong truncation convergence.

## Uniform deformation families

Let \(D_\lambda\) vary with a parameter \(\lambda\) in a compact set \(K\). Strong-dual boundedness and uniform tail convergence follow if:

1. the counting constants \(C,d,e\) are uniform on \(K\);
2. multiplicity weights have a uniform polynomial bound;
3. no infinite cluster enters a compact boundary interval;
4. the divisor points vary continuously after local labeling, except at declared finite collisions.

Under these hypotheses,

\[
\{\mu_{D_\lambda}:\lambda\in K\}
\]

is bounded in \(\mathcal S'_\beta\), and truncation tails vanish uniformly on bounded Schwartz packets.

Finite boundary crossings are continuous after their Poisson profiles are completed by the corresponding delta atoms.

## Relation to the completed zero divisor

The completed-zeta divisor has the required polynomial counting growth. Therefore any boundary atomic current obtained by projecting a symmetry-closed subset of its divisor to real spectral coordinates is tempered, provided the projected multiplicities remain locally finite.

This statement does not assert that such atoms occur for the actual completed multiplier. It types the current if a deformation or contour crossing produces them.

## Green and lattice consequence

At the terminal spectral node, finite atomic index rows may be replaced by the strongly convergent current

\[
\mu_D
\in
\mathscr I_\partial.
\]

All signed source pullbacks converge on the Mellin--Schwartz rung. Dagger and admitted successors commute with the limit.

Thus infinite divisor accumulation does not require new lattice cells. It requires only the current-coordinate completion already attached to \(C_{13,7}^{aug}\).

## What remains open

The result does not provide:

1. a positive Hilbert norm for \(\mu_D\);
2. trace-class realization of the infinite current on the physical carrier;
3. a uniform graph-Hilbert bound outside the Schwartz test rung;
4. positivity of the combined Green form;
5. convergence when projected divisor points fail local finiteness.

## Disposition

Polynomial divisor counting is sufficient to complete the infinite atomic boundary current in the strong Schwartz dual. The finite crossing model therefore extends to symmetry-completed infinite divisor packets at the rigged-distribution level.
