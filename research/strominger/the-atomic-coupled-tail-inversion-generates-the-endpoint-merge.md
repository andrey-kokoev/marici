# Atomic Coupled Tail Inversion Generates the Endpoint Merge

## Missing correspondence

The unary local presentation groupoid separated the endpoint Smith-profile fiber
into two components \(E_0\) and \(E_1\). Their representatives differ by the
common sign of the two nonrepeated generators.

Define the coupled constructor

\[
J:(a^{\epsilon_0},b^{\epsilon_1},c^{\epsilon_2})
\longmapsto
(a^{\epsilon_0},b^{-\epsilon_1},c^{-\epsilon_2}).
\]

Exact Moore-face evaluation proves that \(J\) preserves the legal signed
presentation set and the framing classifier.

## Nonfactorization theorem

On the endpoint stratum there are legal states such as

\[
((1,2,3),(1,1,1)).
\]

The two unary candidate intermediates

\[
((1,2,3),(1,-1,1)),
\qquad
((1,2,3),(1,1,-1))
\]

are both Moore-illegal, while the coupled target

\[
((1,2,3),(1,-1,-1))
\]

is Moore-legal. Therefore \(J\) cannot be implemented as a path of legal unary
tail inversions. It is an atomic two-port constructor relative to the legal
state category.

## Closed quotient theorem

Adjoin \(J\) to endpoint reversal, exchange of nonrepeated slots, and reversal
of the repeated-generator sign. The generated typed groupoid has exactly three
connected components with sizes

\[
16,\qquad 8,\qquad 8.
\]

These components coincide exactly with the three reflection Smith-depth-profile
fibers. Hence the profile-minimal port is also source-generated once coupled
constructors, rather than only unary-factorized moves, are admitted.

The explanation is not that two disconnected source states happen to share a
response. Their identification is the orbit of a legal collective operation
whose illegal unary factors never exist as admissible states.

## Observation-level boundary

The constructor does not preserve the full response matrix. All thirty-two
legal signed presentations have distinct full \(4\times4\) response matrices,
and no atomic pair-flip edge has equal matrices at its two endpoints. The
three groupoid components contain respectively sixteen, eight, and eight
distinct full matrices.

Exact integral Smith reduction yields five packets. The pair flip preserves
the exact Smith packet on all eight equal-polarity through presentations, but
on neither the endpoint nor opposite-polarity stratum. It becomes uniformly
invisible only after taking 2-adic valuations of the Smith factors.

Thus the coupled constructor generates the kernel groupoid of the 2-adic
depth profile. It is only partially invisible at exact integral Smith level
and is never invisible to the full response.

## Replay

Run:

    python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py

The checker verifies sixty-nine exact gates.
