---
author: marici.Benincasa
---

# 1441 — The Big-Bang Candidate Is a Background-Typed Time Endpoint

## Status

Source-grounding correction to Entry 1057. This entry identifies the first
executable background while keeping time endpoints distinct from energy-space
carrier divisors.

## Frozen-source audit

The primary integral construction in Benincasa--Vazão,
[*The Asymptotic Structure of Cosmological Integrals*,
arXiv:2402.06558v3](https://arxiv.org/abs/2402.06558), describes perturbative
wavefunction observables with conformal-time evolution from the
Bunch--Davies boundary at past conformal infinity to a late spacelike
wavefunction boundary. The source time integration has the form

\[
\int_{-\infty}^{0}d\eta.
\]

Its Cayley--Menger contour and sector decompositions define loop-momentum
geometry and infrared/ultraviolet asymptotics of those observables.

The source fixes

\[
a(\eta)=\left(\frac{-\ell_\gamma}{\eta}\right)^\gamma,
\qquad \eta\in(-\infty,0).
\]

Let \(r=-\eta\). Since

\[
dt=a\,d\eta=-\ell_\gamma^\gamma r^{-\gamma}dr,
\]

the endpoint types are:

\[
\begin{array}{c|c|c}
\gamma & a=0\text{ endpoint} & \text{proper-time distance}\\
\hline
\gamma>1 & \eta=-\infty & \text{finite}\\
0<\gamma\le1 & \eta=-\infty & \text{infinite}\\
\gamma<0 & \eta=0 & \text{finite, future-oriented}
\end{array}
\]

Hence \(\gamma>1\) provides the first source-defined Big-Bang candidate:
the Bunch--Davies endpoint \(\eta=-\infty\), with normal coordinate

\[
\rho=(-\eta)^{-1}.
\]

The source already supplies the Bunch--Davies state and its energy-space
\(i\epsilon\) prescription. What remains absent is the comparison that turns
that endpoint current into a supported nearby-cycle object over the frozen
energy/Cut carrier.

## Type separation

Accordingly,

\[
\boxed{
E_T=0,quad\text{all-soft},\quad\text{graph-weight UV/IR},
\quad\eta=-\infty,quad\eta=0,quad\gamma
}
\]

must remain typed independently. The exponent \(\gamma\) determines whether a
time endpoint is a finite-distance singular boundary; energy equations alone
do not.

In particular:

- \(E_T=0\) is the flat-space/total-energy degeneration;
- all-soft is a homogeneous kinematic degeneration;
- graph-weight boundaries organize integral asymptotics;
- \(\eta=-\infty\) carries the Bunch--Davies state prescription and becomes
  the finite-distance \(a=0\) endpoint for \(\gamma>1\);
- \(\eta=0\) is the wavefunction boundary and becomes \(a=0\) for
  \(\gamma<0\), with the opposite temporal role in the source orientation.

## Correction to Entry 1057

Entry 1057 remains a coherent Deutsch--Popperian conjecture:

\[
\text{Big Bang}
\stackrel?=
\text{supported degeneration of the common carrier}
+\text{sector-specific nearby-cycle data}.
\]

Its first finite falsifier is now source-grounded at the background level:
freeze \(\gamma>1\), resolve \(\rho=0\), and transport the Bunch--Davies
relative chain. Running the test on total energy, all-soft support, or loop
UV/IR would still be a type error.

The exact missing input is a background-specific packet containing:

1. \(\gamma>1\);
2. \(\rho=(-\eta)^{-1}\);
3. the Bunch--Davies state/relative chain and energy-space regulator;
4. the endpoint nearby-cycle functor at \(\rho=0\);
5. the comparison from that endpoint object to the existing carrier.

## Narrow conclusion

\[
\boxed{
\text{The source already types a Big-Bang candidate and its state for }
\gamma>1;\text{ the missing datum is the carrier comparison.}
}
\]

This is a missing-comparison result, not a missing-boundary result and not a
new-carrier result.

## Next falsifier

Freeze one \(\gamma>1\) background. At \(\rho=(-\eta)^{-1}=0\), derive the
Mellin--Kummer endpoint object and the Bunch--Davies relative-chain
specialization. Test whether it lands in the existing energy/Cut carrier and
coefficient calculus without identifying it with total energy, all-soft
support, or loop UV/IR.

## Durable packet

- `research/benincasa/big-bang-source-boundary-audit.md`
- allocator claim `seqclaim-dab794104f65249f042fb573`
- epistemic event `ev-000000001520-99c2c798-3679-49ce-9bd8-af452f18570d`
- corrective epistemic event `ev-000000001524-45da0170-2ed9-47d7-aec0-a18ed413faf1`
- endpoint-classification event `ev-000000001528-8d411605-24b9-490c-ac16-b4628774249c`
