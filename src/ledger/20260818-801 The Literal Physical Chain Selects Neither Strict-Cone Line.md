# The Literal Physical Chain Selects Neither Strict-Cone Line

## Composition of established maps

Entry 799 identifies two horizontal cohomology lines in the local weighted
principal cone:

\[
H^{-1}=\ker C_E\simeq\mathbb Q(t),
\qquad
H^0=\operatorname{coker}C_E\simeq\mathbb Q(t).
\]

Entry 747 independently proves that the closure of the literal normalized
physical chamber is disjoint from all three principal incidence supports

\[
Z_{12},\qquad Z_{13},\qquad Z_{23}.
\]

Therefore its point-supported comparison is the zero chain map before
cohomology is taken.  Functoriality then forces its induced maps on both
strict-cone lines to vanish:

\[
\boxed{
\Phi_{\rm literal}|_{H^{-1}}=0,
\qquad
\Phi_{\rm literal}|_{H^0}=0.
}
\]

Thus the answer to Entry 799's three-way test, for the literal source chain,
is **neither**.

## Meaning

This is stronger than saying that the available data fail to choose between
two algebraic lines.  The source-defined uncontinued chain positively chooses
neither: both pairings are zero by support.

It remains deliberately narrower than a vanishing theorem for the physical
wavefunction.  An analytically continued weighted nearby-cycle boundary at

\[
Z_{23}:(u,y,z)=(0,0,-1)
\]

could define a different supported chain map.  But Entries 747--749 show that
the required weighted lift, exceptional current, \(\mu_2\)-trace, and overlap
homotopy are not fixed by the frozen primary source.  A nonzero map cannot be
assigned from the present data.

## Frontier

The algebraic branch is now complete through the local cone:

\[
\text{full transformed connection}
\Rightarrow
\text{strict principal block}
\Rightarrow
H^{-1}\oplus H^0,
\]

while the literal physical comparison kills both summands.  Further progress
requires new physical input: a source-derived analytic continuation of the
relative Cayley--Menger cycle to the weighted soft/infinity exceptional
divisor.  More absolute connection algebra cannot manufacture that map.

## Evidence

`research/nima/audit_literal_chain_on_strict_cone.py` composes the exact cone
census with
`research/benincasa/marici-gm/physical-principal-cech-support.packet`.  Its
machine-readable result is
`research/nima/literal-chain-on-strict-cone.json`.

Allocator claim: `seqclaim-d78aa77fdcbceddeb9a156bf`.
