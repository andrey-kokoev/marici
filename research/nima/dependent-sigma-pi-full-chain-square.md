# A well-typed full-chain dependent distributivity square

This replaces the false fixed-index interchange with a precise candidate for closure-preserving productization. It does not claim to be the only or final interpretation of the operator's proposal.

## Data

I : U
J : I -> U
K : Pi(i:I). J(i) -> U
L : Pi(i:I). Pi(j:J(i)). K(i,j) -> U
B : Pi(i:I). Pi(j:J(i)). Pi(k:K(i,j)). L(i,j,k) -> U

The ground object is

X := Pi(i:I). Sigma(j:J(i)). Pi(k:K(i,j)). Sigma(l:L(i,j,k)). B(i,j,k,l).

The combined choice types are

F := Pi(i:I). J(i),
G(f) := Pi(i:I). Pi(k:K(i,f(i))). L(i,f(i),k),
W(f,g) := Pi(i:I). Pi(k:K(i,f(i))). B(i,f(i),k,g(i)(k)).

Target:

N := Sigma(f:F). Sigma(g:G(f)). W(f,g).

These abbreviations retain their definitions. In particular G depends on f and W depends on both f and g. No independent fixed index replaces them.

## Route A: outer choice first

A0 = X.

A1 = Sigma(f:F). Pi(i:I). Pi(k:K(i,f(i))).
       Sigma(l:L(i,f(i),k)). B(i,f(i),k,l).

A2 = Sigma(f:F). Pi(i:I).
       Sigma(h:Pi(k:K(i,f(i))). L(i,f(i),k)).
       Pi(k:K(i,f(i))). B(i,f(i),k,h(k)).

A3 = Sigma(f:F). Sigma(g:G(f)). W(f,g).

Each edge is an instance of dependent distributivity, lifted through the displayed surrounding binders.

## Route B: inner choice first

B0 = X.

B1 = Pi(i:I). Sigma(j:J(i)).
       Sigma(h:Pi(k:K(i,j)). L(i,j,k)).
       Pi(k:K(i,j)). B(i,j,k,h(k)).

Define C(i) := Sigma(j:J(i)). Pi(k:K(i,j)). L(i,j,k).

B2 = Pi(i:I). Sigma(c:C(i)).
       Pi(k:K(i,fst(c))). B(i,fst(c),k,snd(c)(k)).

B3 = Sigma(c:Pi(i:I). C(i)).
       Pi(i:I). Pi(k:K(i,fst(c(i)))).
         B(i,fst(c(i)),k,snd(c(i))(k)).

B4 = Sigma(f:F). Sigma(g:G(f)). W(f,g).

B1 -> B2 associates dependent sums; B2 -> B3 is dependent distributivity. B3 -> B4 splits the complete dependent choice c into f and g while retaining its witness family. It is not the deletion of c's dependence.

## Retained comparison

Let a:X~=N and b:X~=N be the composites of the explicitly retained Route A and Route B equivalences. For an input x, both expose

f(i) = fst(x(i)),
g(i)(k) = fst(snd(x(i))(k)),
w(i)(k) = snd(snd(x(i))(k)).

Reconstruction sends (f,g,w) to lambda i. (f(i), lambda k. (g(i)(k),w(i)(k))).

Thus there is a pointwise comparison beta:Pi(x:X).a(x)=b(x). The inverse laws use dependent pair eta and function extensionality; equality of the equivalence records can then be obtained using the proposition-valued nature of isEquiv. This is a written HoTT argument, not a checked formal proof here.

A retained observer package can consist of the two lists of intermediate types and edge equivalences, together with beta. Naming that package does not erase its chains. Nor does it automatically make the package a new family of the same input grammar. Defining that closure operation is the next obligation before claiming a repeating coherence tower.

## Evidence and limits

The finite checker uses genuinely dependent index lengths: K varies with the selected j, and the witness fibres vary with i,j,k,l. It independently enumerates 18 source values and 18 target values, reconstructs every source from every intermediate stage, compares both routes, and rejects an index-erasing shortcut. This set-valued example cannot exhibit distinct higher fillers: such phenomena require higher-valued data beyond this finite test.

Checker: `research/nima/checkers/check_dependent_sigma_pi_full_chains.py`.
Result: `research/nima/results/dependent-sigma-pi-full-chains.json`.
