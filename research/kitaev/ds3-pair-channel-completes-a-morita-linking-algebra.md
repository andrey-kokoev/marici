# The D(S3) pair-channel completes a Morita linking algebra

Owner: marici.Kitaev

## Question

What exact relational passage is absent from the pure-electric braid qutrit,
and why does one unequal pair-channel remove its excess commutant?

## Claim boundary

Let the qutrit fusion space split as

\[
V=V_1\oplus V_2,
\qquad
\dim V_1=1,
\quad
\dim V_2=2.
\]

The braid-generated algebra is

\[
A_0=\operatorname{End}(V_1)\oplus\operatorname{End}(V_2)
\simeq\mathbb C\oplus M_2.
\]

Writing \(p\) and \(q\) for the two central block projectors, the ambient
algebra has the Peirce decomposition

\[
M_3=
pM_3p\oplus pM_3q\oplus qM_3p\oplus qM_3q.
\]

Braiding already supplies the diagonal pieces

\[
pM_3p\simeq\mathbb C,
\qquad
qM_3q\simeq M_2,
\]

but supplies neither off-diagonal piece. The excess commutant
\(\mathbb C p\oplus\mathbb C q\) is therefore the exact record of a
disconnected linking algebra.

Let \(H\) be an authorized pair-channel. Its relevant incidence is

\[
h=pHq.
\]

In the pinned fusion basis, this component is proportional to

\[
\frac{\sqrt2}{3}(\alpha-\gamma).
\]

Hence \(\alpha\ne\gamma\) is precisely the condition \(h\ne0\).

Because the qutrit controls already contain the full algebra on \(V_2\), a
single nonzero row \(h\in pM_3q\) generates the entire row module under right
composition by \(M_2\):

\[
hM_2=pM_3q.
\]

Hermitian closure supplies \(h^*\ne0\), and left composition by \(M_2\)
generates

\[
M_2h^*=qM_3p.
\]

Products of the two off-diagonal modules recover the diagonal ideals:

\[
(pM_3q)(qM_3p)=pM_3p,
\]

\[
\operatorname{span}(qM_3p)(pM_3q)=qM_3q.
\]

Therefore

\[
\operatorname{alg}(A_0,H)=M_3
\quad\Longleftrightarrow\quad
pHq\ne0
\]

for this pinned block structure and Hermitian constructor family. Its commutant
is then scalar.

This is exactly the linking algebra of the Morita context

\[
{}_\mathbb C M_{M_2}=M_{1\times2},
\qquad
{}_{M_2}N_\mathbb C=M_{2\times1},
\]

with pairings given by matrix multiplication:

\[
M\otimes_{M_2}N\to\mathbb C,
\qquad
N\otimes_\mathbb C M\to M_2.
\]

Both pairings are full. Their compatibility is ordinary associativity of
matrix multiplication. Thus the three earlier observations become one exact
finite mechanism:

- the pair-channel is the missing bridge element;
- fullness of the two off-diagonal modules removes the excess commutant;
- associativity of their products makes longer alternating passages close
  without another independent coherencer.

The theorem also explains minimality. One nonzero incidence is sufficient
because the already available \(M_2\) block moves it through a cyclic module.
Without that pre-existing block action, one bridge seed need not span the
whole off-diagonal module. Minimality is therefore relational: it depends on
the constructors already present, not only on the rank of the added channel.

## Disposition

The pure-electric qutrit is now the smallest pinned example in which bridge,
relational volume, and self-closure are visibly one linking-algebra mechanism.

The first falsifiers are exact:

- \(\alpha=\gamma\), so \(pHq=0\) and the linking algebra remains
  disconnected;
- the lower block is a proper subalgebra of \(M_2\), so one nonzero seed is not
  necessarily cyclic;
- the backward channel is not the authorized adjoint or mate of the forward
  channel, so the two Morita products disagree operationally despite full
  matrix generation;
- the physical executable set omits either direction of the bridge, leaving a
  semigroup reachability result rather than a strict Morita context.

The next research gate is no longer “why does the commutant shrink?” It is:
derive the forward pair incidence and backward requirement incidence from one
source-authorized constructor, and test whether their operational compositions
realize the two matrix-multiplication pairings. Algebraic full generation is
pinned; source duality and executable reciprocity remain open.
