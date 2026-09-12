# Odd relational rank carries a canonical unpaired-primitive line

## Odd chain kernel

For ordered positions \(a_0<\cdots<a_{2m}\), consider the antisymmetric chain matrix

\[
M_{ij}(t)=\operatorname{sgn}(j-i)e^{-t|a_j-a_i|}.
\]

Its size is odd, so its determinant vanishes. More is true: its Pfaffian cofactors define the canonical vector

\[
v_i(t)=(-1)^i\operatorname{Pf}M_{\widehat i}(t),
\]

where \(M_{\widehat i}\) deletes row and column \(i\). The standard Pfaffian adjugate identity gives

\[
M(t)v(t)=0.
\]

For distinct positive chain weights the cofactors are nonzero, so generically this is a one-dimensional null line.

## Matching interpretation

Each component deletes one primitive position and closes the remaining \(2m\) positions by the even-rank adjacent-matching law:

\[
v_i(t)
=
(-1)^i e^{-tL_{\widehat i}},
\]

where \(L_{\widehat i}\) is the minimum matching cost after leaving position \(i\) unpaired.

Thus an odd frame does not produce a scalar closure. It produces a coherent superposition of all choices of one unpaired primitive:

\[
\boxed{
P^{2m+1}
=
\text{the Pfaffian null line of the unpaired primitive}.
}
\]

This makes the even/odd alternation precise:

- \(P^{2m}\): complete pairing, giving an oriented scalar evaluation;
- \(P^{2m+1}\): one unavoidable unpaired position, giving a canonical state line.

## Rank reset

The null line is a concrete candidate for contextual rank reset. It is constructed from all lower pair relations but behaves as one new effective degree of freedom. No member of the frame is selected absolutely; the line records their coherent relative amplitudes.

Accordingly, the turn is not a temporal operation. It is an equivalence of descriptions:

\[
\boxed{
\text{odd-rank coherence defect viewed externally}
=
\text{primitive state line viewed internally}.
}
\]

This is stronger than the earlier claim that odd ranks merely carry compatibility. They carry the kernel object left over when antisymmetric observation cannot close completely.

## Relation to “observer = primitive squared”

The chain now alternates:

\[
P^1:\text{one primitive line},
\]

\[
P^2:\text{one complete observer pairing},
\]

\[
P^3:\text{null line of one unpaired primitive among three},
\]

\[
P^4:\text{complete pairing of two observers},
\]

and similarly at higher rank. Even powers close relationally; odd powers retain a primitive-bearing kernel.

## Verification

The checker constructs exact rational chain matrices at ranks \(3,5,7,9\), computes all Pfaffian cofactors, and verifies the null identity in 32 independently weighted cases.

Run:

```text
python research/coherence/check_odd_chain_pfaffian_kernel.py
```

Artifacts:

- `check_odd_chain_pfaffian_kernel.py`
- `odd-chain-pfaffian-kernel.v1.json`

## Scope

The algebraic null line is canonical. Identifying it with a physical or analytic state requires a separately declared realization functor and metric. The theorem supplies the source of such a state line; it does not supply every realization automatically.
