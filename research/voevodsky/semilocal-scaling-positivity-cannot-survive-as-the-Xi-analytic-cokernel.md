# Semilocal scaling positivity cannot survive as the Xi analytic cokernel

## Closest GL1 source construction

The Connes--Consani--Moscovici semilocal scaling construction is closer to the Riemann source than the relative-trace model from the preceding audit.

For every finite set of places \(S\), it gives a canonical positive Hilbert realization of scaling with spectral measure

\[
dm_S(u)
=c_S
\left|
L_\infty(1/2-iu)
\prod_{p\in S\setminus\{\infty\}}L_p(1/2-iu)
\right|^2du.
\]

The source map

\[
E(f)(x)=x^{1/2}\sum_{n\ge1}f(nx)
\]

and explicit Hermite combinations factor through \(\Xi\). In an entire-function quotient, multiplication by the scaling coordinate recovers the zeta-zero spectrum. These are genuine source-derived statements.

## Exact topology obstruction

Every finite Euler factor is nonzero on the real scaling axis, so \(dm_S\) is mutually absolutely continuous with Lebesgue measure. Hence each finite-place scaling generator is unitarily equivalent to ordinary multiplication by \(u\) on \(L^2(\mathbb R,du)\): it has purely continuous spectrum and no zero eigenmodes.

More decisively, because \(\Xi(u)\neq0\) almost everywhere,

\[
\overline{\Xi L^2(\mathbb R,dm_S)}
=L^2(\mathbb R,dm_S).
\]

Therefore the positive Hilbert cokernel is trivial:

\[
L^2(\mathbb R,dm_S)/
\overline{\Xi L^2(\mathbb R,dm_S)}=0.
\]

The nontrivial zero cokernel exists only in an analytic topology where point evaluation is continuous. The positive semilocal \(L^2\) topology forgets measure-zero evaluations; the analytic topology remembers them but does not inherit the positive norm.

This is a precise obstruction to using the semilocal Plancherel measure as the desired source-positive Weil measure.

## All-places obstruction

The naive finite-place limit also fails at the central point:

\[
\prod_{p\le P}(1-p^{-1/2})^{-1}\longrightarrow\infty.
\]

Adding places changes the positive density but never changes the multiplication operator's absolutely continuous spectral type. Discrete Xi modes can appear only through a nonunitary operation—analytic boundary condition, radical quotient, compression, or conditioning limit.

Such an operation is exactly where positivity is lost or becomes RH-strength.

## Audit of recent literature

Fresh web search recovered:

- Connes--Consani--Moscovici, *Zeta spectral triples*, arXiv:2511.22755;
- Connes--van Suijlekom, *Quadratic forms, real zeros and echoes of the spectral action*, CMP 406 (2025), 312;
- recent independent finite-scale/convergence audits indexed in 2026.

The existing theorem-level sweep already checks the strongest claims:

- finite Carathéodory--Fejér and truncated-form results are unconditional;
- real-zero conclusions assume a simple isolated even ground state;
- the global spectral-convergence step is explicitly identified by the authors as one that would establish RH.

No fresh source claims a positive analytic Xi cokernel or proves the required convergence.

## Revised positive-constructor boundary

The source currently supplies two incompatible halves:

\[
\begin{array}{c|c}
\text{positive semilocal }L^2 & \text{analytic Xi quotient}\\
\hline
\text{self-adjoint continuous scaling} & \text{discrete zero evaluations}\\
\text{no evaluation vectors} & \text{continuous evaluation}\\
\text{trivial Xi cokernel} & \text{nontrivial cokernel}\\
\text{positive norm} & \text{no proved source-positive norm}
\end{array}
\]

The missing object is not another finite-place weight. It is a source-derived analytic boundary norm for which:

1. the Xi image is closed with nontrivial cokernel;
2. multiplication by \(w=s(s-1)\) descends symmetrically;
3. rational-boundary sewing kills the Green boundary form;
4. the descended operator is self-adjoint, with no deficiency modes.

Off-critical zeros are exactly nonreal adjoint deficiency modes of this compressed multiplier. Thus proving self-adjoint descent is already the RH-bearing step.

## Consequence for universal rung four

The semilocal measure cannot be pushed directly into the coupled rung-four observer: doing so either gives the trivial quotient or changes to an analytic norm whose positivity/self-adjointness is unproved. This is the first precise obstruction at the interface between an independently positive arithmetic measure and the completed Xi observer.

## Durable sources

- `research/grothendieck/connes-semilocal-scaling-quotient-audit.md`
- `research/grothendieck/finite-place-scaling-colimit-no-go.md`
- `research/grothendieck/theta-positive-l2-cokernel-collapse.md`
- `research/grothendieck/theta-euler-orbit-cokernel-zero-spectrum.md`
- `research/grothendieck/theta-rkhs-cokernel-symmetry-gate.md`
- `research/grothendieck/references/double_contact_sweep.agent.final.md`
