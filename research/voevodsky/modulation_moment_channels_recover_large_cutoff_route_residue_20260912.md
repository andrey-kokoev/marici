# Two modulation moments recover large-cutoff route residue

## Question

After one coded modulation fails, how many structured shell-only or scale-only channels recover the tested cycle spaces?

## Claim boundary

At every tested cutoff through \(7680\), ordinary history together with first and second modulation moments has full rank on the entire edge carrier. This holds separately for shell-index moments and theta-scale moments. It is a finite-cutoff theorem supported by exact modular rank; it does not establish a cutoff-independent channel depth on the infinite graph.

## Moment families

Let \(j\geq1\) denote the consecutive-prime shell index and \(k\geq1\) the common theta multiplicity. Define diagonal modulations

\[
D_{j,r}(e)=j(e)^r,
\qquad
D_{k,r}(e)=k(e)^r.
\]

For either label \(x=j\) or \(x=k\), test the stacked incidence operator

\[
\mathcal M_{x,R}
=
\begin{pmatrix}
\partial\\
\partial D_{x,1}\\
\cdots\\
\partial D_{x,R}
\end{pmatrix}.
\]

The \(r=0\) row block is ordinary common history modulo its injective analytic transform. Route residue is detected exactly when \(\mathcal M_{x,R}\) has full column rank.

## Census

Sparse elimination over two large prime moduli agrees at every stage:

| cutoff | edges | shell maximum power | scale maximum power |
|---:|---:|---:|---:|
| 960 | 279 | 2 | 2 |
| 1920 | 563 | 2 | 2 |
| 3840 | 1136 | 2 | 2 |
| 7680 | 2287 | 2 | 2 |

Power one alone has the previously reported deficiencies \(1,5,16,40\). Adding power two removes every observed deficiency. Thus three recorded histories—unmodulated, linearly modulated, and quadratically modulated—are jointly faithful at these cutoffs.

## Operational meaning

An apparatus need not resolve every edge separately if it can implement two independently calibrated amplitude profiles over one coarse label:

\[
x\longmapsto x,
\qquad
x\longmapsto x^2.
\]

The three readouts must remain separate. Summing them into one channel would lose the Vandermonde information.

The shell implementation addresses prime-shell index but not individual theta scales. The scale implementation addresses common theta multiplicity but not individual shells. Either was sufficient in the finite census.

## Hostile boundary

The stable depth two pattern may reflect a structural bound on the local multiplicative incidence equations, but the census does not prove that. A countercycle could first appear at a larger cutoff or in the completed limit. Promotion requires an exact theorem that

\[
\ker\mathcal M_{j,2}=0
\quad\text{or}\quad
\ker\mathcal M_{k,2}=0
\]

on the full arithmetic edge module, followed by a completed lower-frame estimate for stable reconstruction.

## Disposition

The single-code conjecture is superseded by a two-moment conjecture. Its risky consequence survived four larger cutoffs and two independent modular fields. The next discriminating step is an arithmetic proof or a larger hostile designed around vertices incident to at least four distinct shell or scale labels. Physical covariance still requires measured response normalization and noise across the three channels.
