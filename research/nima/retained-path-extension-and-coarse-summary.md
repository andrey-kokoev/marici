# Retained path extension is not its coarse continuation operator

## One-step factorization

Use the ten actual endpoint-compatible two-step words of the glued seed. Let L copy each primitive coefficient unchanged to every admitted extension of that primitive, and let A sum complete path coefficients by their final occurrence:

    (Lx)_(a,b) = x_a,
    (Ay)_b = sum_(a composable with b) y_(a,b).

Then the previously checked incoming occurrence operator factors exactly:

    six primitive coefficients --L--> ten retained word coefficients --A--> six final-occurrence coefficients
    K = A L.

This L is an explicitly declared unchanged-coefficient extension to all POSSIBLE continuations. It is not an assertion that all continuations are physically executed, nor a derived amplitude/probability assignment. Relative to the earlier bilinear path product B(x,y), this lift uses y equal to one on every primitive coordinate.

## Injective construction, lossy summary

Exact ranks are L:6, A:6, AL:4. The aggregation kernel in the full ten-dimensional path space has dimension four; its intersection with the six-dimensional image of L has dimension two.

In primitive order (AB,BC,CA,BA,AD,DB), the numbers of admitted extensions are

    d=(2,1,2,2,1,2).

Each primitive has at least one extension. Define

    D=diag(d)^-1 L^T.

Then DL=I6. This is an averaging decoder on the image of L, not a normalization of the preparation. The checker rejects vectors outside that image: for example, changing one AB extension while leaving its sibling unchanged is a legitimate general path-space vector but not an output of this unchanged-coefficient lift.

Also L^T L=diag(d), not I6. Thus injectivity does not imply norm preservation. No compensating square-root weighting is introduced.

## Exactly where the two contrasts disappear

The two K-zero directions become nonzero path profiles:

    L(CA-BA) = [CA AB]+[CA AD]-[BA AB]-[BA AD],
    L(AB-DB) = [AB BA]+[AB BC]-[DB BA]-[DB BC].

Brackets denote distinct retained words. Each profile is recoverable by D. Only after A discards the prefix distinction do positive and negative coefficients cancel in the same final-occurrence cell.

Consequently the two directions are retained by source composition in this carrier; their disappearance under K is located at final-occurrence aggregation, not path construction. This sharpens the preceding observation audit without contradicting it: if only Kx is retained, they really are lost.

## Repeated extension: a commuting summary diagram

For the full set P_n of length-n words, define J_n by copying a path coefficient to every admitted one-arrow extension. Define A_n by aggregation to the last primitive occurrence. Exact checks establish, through length six,

    A_(n+1) J_n = K A_n.

The equality is checked on the entire current path coefficient space, not just the subspace originating from six primitive inputs. Every J_n has a left inverse given by averaging over each parent's extensions. Every parent is literally the prefix of its children; prefix recovery introduces no inverse-arrow or return-word cancellation law.

Let L_n=J_(n-1)...J_1, with L_1=I6. Then the tested composite maps satisfy

    A_n L_n = K^(n-1),
    rank(L_n)=6,
    rank(L_n P_zero)=2.

For n>=2 in the tested range, the coarse primitive response has rank four and annihilates both retained contrasts.

| Word length | Retained paths | Rank of lift from six primitives | Rank of coarse primitive response |
|---|---:|---:|---:|
|1|6|6|6|
|2|10|6|4|
|3|16|6|4|
|4|26|6|4|
|5|42|6|4|
|6|68|6|4|

The path space grows, but unchanged copying of six inputs does not create additional independently prepared coefficients. At each stage the full path space can describe more general preparations; those are not silently claimed to arise from this lift.

The mechanism for injectivity is the absence of sinks in this seed and retention of complete prefix IDs. It is not a general theorem that arbitrary graph extension or endpoint-only grouping is lossless. The fresh bounded tests cover word lengths one through six.

## Structural synthesis

There are now two compatible descriptions with explicitly different information content:

- **Retained construction:** injective maps between growing labelled path carriers, with recoverable prefixes.
- **Coarse summary:** a fixed six-occurrence matrix K, linked by commuting aggregation maps to every checked stage.

The global eigenvalues of K therefore describe this fixed coarse summary. They do not, by themselves, describe a square evolution operator on the growing complete path carriers. The four active and two zero spectral directions are not a reason to delete path records or declare a physical sector inaccessible.

The path provenance is retained alongside coefficients. Parent endpoints, primitive IDs and the original ordered registry are explicitly recovered at the first step; subsequent steps preserve full prefixes. These are formal retained words, not execution receipts.

## Verification and durable pointers

Extended checker:

    python research/nima/checkers/check_whole_seed_occurrence_spectrum.py

All prior exact spectral/observation checks and the new factorization, image decoder, contrast profiles, norm boundary and repeated-extension squares pass. Negative controls reject wrong coefficient counts and off-image unequal sibling payloads.

Report: `results/whole-seed-occurrence-spectrum.json`.

Preceding synthesis: `whole-seed-occurrence-spectrum-bridge.md`.
