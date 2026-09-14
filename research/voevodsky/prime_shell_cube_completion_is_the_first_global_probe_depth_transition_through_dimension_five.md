# Prime-shell cube completion is the first global probe-depth transition through dimension five

## Question

Do the canonical cube grades merely exhibit probe defects, or are they the first global cutoffs at which those defects can occur, including against noncubical rivals?

## Claim boundary

For cubical dimensions two through five and the declared character settings, exact rank computations immediately below and at each canonical grade, combined with kernel persistence under cutoff inclusion, establish the first global probe-depth transitions. This finite theorem does not establish the analogous assertion in every dimension.

## Kernel persistence

For cutoffs \(L<M\), the route graph \(G_L\) is a subgraph of \(G_M\). Extend an edge assignment on \(G_L\) by zero on every new edge. Every old vertex equation is unchanged. Every new vertex receives zero because no old edge is incident to a vertex absent from \(G_L\). Therefore, for every fixed family of character settings \(T\), zero extension defines a monomorphism

\[
\ker P_{L,T}\longrightarrow\ker P_{M,T}.
\]

Consequently, probe deficiency is nondecreasing with cutoff. Full column rank immediately below a candidate grade excludes every earlier cubical and noncubical blind route for the same settings.

## Threshold theorem through dimension five

Let \(L_n\) be the minimal canonical completion grade

\[
L_n=p_n\prod_{r=1}^{n}p_{r+1}.
\]

At \(L_n-1\), use the coarse evaluation together with \(n-2\) modulated settings. At \(L_n\), compare that probe with the probe having one additional modulated setting.

The exact results are:

| cubical dimension | grade \(L_n\) | deficiency below with \(n-2\) modulations | deficiency at grade with \(n-2\) modulations | deficiency at grade with \(n-1\) modulations |
|---:|---:|---:|---:|---:|
| 2 | 45 | 0 | 1 | 0 |
| 3 | 525 | 0 | 1 | 0 |
| 4 | 8085 | 0 | 1 | 0 |
| 5 | 165165 | 0 | 1 | 0 |

For dimensions four and five, deletion hostiles further show that removing the unique canonical cube-final edge restores the lower-depth probe rank, whereas deleting any other edge entering at the same grade leaves the defect.

## Combined explanation

Three independent statements now compose:

1. Arithmetic minimality: the first literal \(n\)-shell cube completes at \(L_n\).
2. Cubical nullity: an isolated \(n\)-cube has a unique blind full-support Walsh block under \(n-1\) total evaluations and becomes faithful under \(n\).
3. Filtration persistence: a blind class at any earlier cutoff would remain visible as a defect immediately below \(L_n\).

The exact full-graph rank at \(L_n-1\) is zero-defect, so the third statement eliminates all earlier rivals, including noncubical ones, in the tested dimensions. The rank-one defect at \(L_n\), together with edge deletion, identifies canonical cube completion as the transition carrier.

## Known equality

The phenomenon is the composition of a persistence monomorphism with the Boolean Walsh decomposition and generalized Vandermonde evaluation:

\[
\ker P_{L,T}
\hookrightarrow
\ker P_{M,T},
\qquad
E_{\square^n}
\cong
\bigoplus_{\varnothing\neq K\subseteq[n]}k^K,
\qquad
P_T|_K=(t_r^i)_{r,\,i\in K}.
\]

The “prime-index derivative” is therefore a character-jet presentation of a persistent full-support Walsh mode. Prime arithmetic determines the grade at which that mode becomes realizable; cubical interpolation determines the number of evaluations needed to detect it.

## Strongest falsification attempt

Recompute dimensions two and three directly over two large prime fields. Read the independently generated dimension-four and dimension-five result artifacts. For each dimension verify the zero/one/zero threshold profile. Independently verify edge-set inclusion at adjacent cutoffs, ensuring the persistence argument applies to the actual generated graphs.

## Disposition

The noncubical-earlier rival is eliminated through dimension five. The surviving general conjecture is that the same threshold theorem holds for every \(n\); its first uncomputed case is the six-cube grade \(3318315\).
