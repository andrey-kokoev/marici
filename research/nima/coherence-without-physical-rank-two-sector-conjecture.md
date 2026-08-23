# Coherence Without Physical Rank: A Two-Sector Conjecture

## Two independent instances

### Tate reflection

The loaded reflection comparison requires a conductor homotopy, but the
source-defined physical pullback has one primitive line and the comparison
homotopy adds no physical rank.

### Cosmological bubble boundary

The spurious-corner complex has an intrinsic rank-one (H^1).  Nevertheless,
the source supplies one common boundary vector at the common regularity
point, and its boundary map factors exactly through (H^0):

\[
B_{\rm source}\xrightarrow{\sim}H^0(C^\bullet_{\rm sp}),
\qquad
B_{\rm source}\longrightarrow H^1(C^\bullet_{\rm sp})=0.
\]

Here (H^1) records failure to glue independently assigned divisor-local
data; it is not an additional physical boundary condition.

The mechanisms differ.  Tate uses a nontrivial comparison homotopy whose
physical rank contribution vanishes.  The bubble source never enters the
higher corner degree.  Their common feature is therefore only:

\[
\boxed{
\text{derived coherence can be mathematically nontrivial while adding no
source-selected physical rank.}
}
\]

## Conjecture

For a source-defined physical readout

\[
R_{\rm phys}:\mathcal C_{\rm derived}\longrightarrow
\mathcal H_{\rm phys},
\]

higher coherence classes contribute physical degrees of freedom only when
the source supplies a typed pairing, boundary current, or connecting
morphism into their grade.  Their mere nonvanishing in
(\mathcal C_{\rm derived}) is insufficient.

This is a source-selection claim, not a claim that higher coherence is
unphysical in every sector.

## Operational criterion

Let (S) be the pairing-forced comparison candidate and

\[
\Omega=\partial_HS-S\partial_G
\]

its boundary commutator.  Entry 1323 proves that a selected target cocycle
(ell) defines a source-homology readout precisely when

\[
\boxed{\ell\Omega=0.}
\]

This is weaker than (Omega=0), and weaker than requiring (S) to induce a
homology map.  Consequently there are three distinct gates:

1. strict coherence: (Omega=0);
2. state transport: (S) induces a homology map;
3. selected physical readout: (ellOmega=0).

The phrase “coherence without physical rank” refers only to the third gate
for the source-selected (ell).  It must not be inferred from failure of
either stronger gate.

## Falsifier

Use the six-point string class of Entry 912:

\[
\text{ordinary maximal-flag pullback}=0,
\qquad
\operatorname{rank}\operatorname{gr}^{(1)}=1.
\]

Entries 913--914 already transport this line around its labelled maximal-flag
orbit and show that it carries the trivial (D_3) character.  The remaining
gate is therefore to complete the orbit census of maximal compatible channel
triples and derive the physical Pochhammer/relative-chain pairing of the
resulting occurrence-covariant associated-grade packet.

- If the source pairing with that grade is nonzero and canonical, higher
  coherence is physically selected there; the conjecture survives in its
  conditional form and falsifies any stronger “coherence is always
  invisible” law.
- If the source pairing factors through ordinary degree zero or vanishes,
  the same pattern is replicated in a third sector.
- If the pairing depends on an unprescribed continuation or splitting, the
  physical status remains unresolved rather than zero.

Equivalently, once the source-normalized string readout covector and relative
boundary matrices are available, evaluate (ell\Omega) on the
associated-grade packet.  A nonzero value is a direct falsifier of descent;
a zero value establishes the selected observable even if the full Betti
comparison remains obstructed.

## Sources

- `research/nima/tate-reflection-coherence-is-invisible-on-the-physical-line.md`
- `src/ledger/20260820-1074 The Source Bubble Boundary Factors Exactly through Degree Zero.md`
- `src/ledger/20260819-912 The First Three-Normal String Class Lives in Associated Grade.md`
- `src/ledger/20260820-1313 The Forced Betti Pushforward Has One Boundary-Commutator Obstruction.md`
- `src/ledger/20260820-1323 A Selected Cocycle Can Descend Without a Betti Homology Map.md`
