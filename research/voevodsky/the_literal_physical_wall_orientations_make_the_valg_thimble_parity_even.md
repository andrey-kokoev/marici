# The literal physical wall orientations make the v_alg thimble parity even

## Fresh physical-chain input

The exact literal Cayley--Menger chain packet

`research/benincasa/results/rank26-literal-residue-chain-wall-segments.json`

selects exactly two real wall segments in the strict physical triangle chamber:

\[
\begin{array}{c|c|c}
\text{wall}&\text{residue orientation}&\text{sheet sequence}\\ \hline
g_1&-da&D_+\to D_-\\
g_2&+db&D_-\to D_+
\end{array}
\]

Each segment has exactly one sheet switch.

## Oriented wall-tail sum

In the algebraic orientation used by the universal one-wall packet,

\[
q_{v_{\rm alg}}(w_{101})=-1,
\qquad
q_{v_{\rm alg}}(w_{110})=+1.
\]

Applying the literal physical residue orientations gives the physical wall chain

\[
w_{\rm phys}=-w_{101}+w_{110}.
\]

Therefore

\[
q_{v_{\rm alg}}(w_{\rm phys})
=(-1)(-1)+(+1)(+1)=2.
\]

In particular,

\[
\boxed{
q_{v_{\rm alg}}(w_{\rm phys})\equiv0\pmod2.
}
\]

Thus the two explicitly oriented real wall segments contribute an even \(v_{\rm alg}\) coefficient to twice the candidate thimble lift. They cannot by themselves produce the nonzero \(v_{\rm alg}\) extension bit.

## What this obtains

This is the first source-normalized parity evaluation using the actual physical chain orientations rather than an abstract exchange sign. Under direct assembly of the two wall pieces, the \(v_{\rm alg}\) column is

\[
2v_{\rm alg},
\]

so its mod-two extension coordinate is zero.

## Remaining endpoint gate

The two wall segments must be sewn through their common endpoints and through the nodal infinity thimble. A primitive endpoint or infinity-Gysin correction could change the lift by one algebraic class. Therefore the unconditional integral column still requires checking that the sewing correction has zero \(v_{\rm alg}\) parity.

The remaining test is now narrower than constructing an arbitrary thimble:

\[
\text{compute only the }v_{\rm alg}\text{ parity of the endpoint/infinity sewing correction}.
\]

If it is zero, the physical thimble has \(v_{\rm alg}\)-bit \(0\). If it is one, it flips the even wall contribution to the nontrivial class.

Verification:

- `research/voevodsky/checkers/check_physical_wall_valg_parity.py`
- `research/voevodsky/results/physical_wall_valg_parity.json`
