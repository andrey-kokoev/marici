# Phase-lift obstruction and coherent order-switch repair

## Question

Can the anticommutation phase be exposed without choosing controlled representatives of projective logical operations?

Logical unitaries are initially specified only up to phase. The projection

\[
U(d)\longrightarrow PU(d)
\]

forgets precisely the phase that a controlled-\(U\) operation would make observable.

## Claim boundary

### No multiplicative phase section for the toric Pauli quotient

Let \(V\simeq\mathbf F_2^4\) be the abelian group of logical Pauli labels modulo phase. Suppose a section

\[
s:V\longrightarrow U(4)
\]

were both a lift of projective labels and a group homomorphism. Since \(V\) is abelian,

\[
s(v)s(w)=s(v+w)=s(w+v)=s(w)s(v).
\]

But odd-intersection labels require anticommuting lifts. Therefore no multiplicative section exists.

Any chosen section instead obeys

\[
s(v)s(w)=c(v,w)s(v+w)
\]

for a nontrivial phase cocycle \(c\). Rephasing the section changes \(c\) by a coboundary but does not remove its commutator class. Projective loop data alone fixes the class, not a controlled representative for each loop.

### Coherent order switch

A higher-order constructor can compare composition orders while using the same occurrences of \(U\) and \(V\):

\[
\mathsf S_{U,V}
\bigl(|0\rangle\otimes|\psi\rangle\bigr)
=
|0\rangle\otimes UV|\psi\rangle,
\]

\[
\mathsf S_{U,V}
\bigl(|1\rangle\otimes|\psi\rangle\bigr)
=
|1\rangle\otimes VU|\psi\rangle.
\]

Applied to \(|+\rangle\otimes|\psi\rangle\), commuting loops return control \(|+\rangle\); anticommuting loops return \(|-\rangle\), independently of \(|\psi\rangle\).

Under independent phase changes

\[
U\mapsto e^{i\alpha}U,
\qquad
V\mapsto e^{i\beta}V,
\]

both branches acquire the same factor \(e^{i(\alpha+\beta)}\). The control record is unchanged. Thus the order-switch comparison is gauge-invariant without controlled-\(U\) or controlled-\(V\).

The repair is not free. \(\mathsf S\) is a higher-order constructor acting on operations and coherently routing their composition order. It is not determined by the two projective channels under ordinary fixed-order composition. A physical realization must establish:

1. the same occurrences of \(U\) and \(V\) are used in both branches;
2. path-dependent phases are calibrated or symmetry-cancelled;
3. the control retains coherence across the two composition orders;
4. no branch reveals order information to an environment;
5. the switch preserves the toric logical subspace.

This packet gives an algebraic escape from the controlled-unitary phase circularity. It does not construct a laboratory order switch or assert that indefinite physical time order is required; the relevant type is coherent constructor-composition order.

## Disposition

There are two distinct lifts:

- representative lift: choose phase-framed unitaries and construct controlled versions;
- process lift: coherently compare two orders of the same projective constructors.

The first is obstructed by the non-split Pauli central extension if multiplicativity is demanded. The second measures the extension class without selecting individual phase representatives, but requires a higher-order process constructor.

The first falsifier is one of:

1. the proposed section is called multiplicative despite anticommuting images;
2. the two switch branches use independently compiled copies with unrelated phases;
3. environmental records distinguish the composition orders;
4. the switch is inferred from projective channels without an admitted higher-order constructor;
5. composition order is silently interpreted as physical time;
6. a gauge-dependent branch phase is mistaken for the cocycle.

The next finite interface object should specify \(\mathsf S\) as a typed supermap on the admitted loop-operation slots and audit whether its phase covariance and logical-subspace preservation hold.
