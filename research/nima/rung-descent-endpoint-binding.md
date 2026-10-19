# Rung12-to-rung4 endpoint binding: retention passes, reader identification fails

## Disposition

The new endpoint audit passes **16 exact checks**, but the intended full descent
is **not established**. It tests the existing diagram and unchanged reader,
rather than adding another observer and relabelling the result as completion.

There is a concrete failure of the current proposed observation factorization:
two retained histories have the same original rung-4 aggregate reading and
different exchange mismatch responses.

## Actual rung contracts inspected

The clarified diagram is

    12 --9--> 6
     |       |
    11 --8--> 5
     |       |
    10 --7--> 4.

Its existing executable fixture starts with 137 shared-leg matrix rows.
Horizontal transport performs two declared incoming-family promotions; both
inherited-key and common-target policies satisfy the retained squares. These
checks do not select one physically intended T9 operation.

The actual-pair path adapter uses those same transport functions on different
input rows. Each path is encoded as a retained labelled leaf with identity
matrix value. This is not an identification of that input with the original
137-row fixture. Nor is the later conditional orphan completion an identified
instance of the original rung12 source.

## Unchanged reader tested directly

The existing reader is the member-weighted matrix mean minus a fixed reference
2I at rung4. It is not retuned in this audit.

Use the actual proton histories

    h=(AB,BC,CA)^2,
    k=(AB,BC,CA)^4.

Both paths are recovered exactly after either rung policy. For the current
one-path adapter both have weighted value I, so

    J4(h)=J4(k)=-I.

Their existing carrier/record exchange responses, on the unchanged unit
AB-record preparation, have different six-coordinate mismatch vectors. The
receipt records both vectors and both policies' matrix readings.

Therefore there is no function f of this aggregate alone satisfying

    mismatch(history)=f(J4(history))

for all tested histories: equal arguments would require equal outputs. This
obstruction is not restricted to linear postprocessing.

The full retained rung object still contains the history, so a separately
declared leaf/history reader can recover the response. The failure concerns
identifying that response with the unchanged J4 aggregate, not loss of data
by the retained transport.

## Why the three-reading seam closure does not fill this gap

The closed seam observer was derived for a conditional deleted-edge completion
with a declared edge comparison and orphan rotation extension. It supplies an
exact observer within that model. No supplied operation-preserving map identifies
that model with the original 137-row source or its reader with J4.

Its successful internal closure cannot substitute for either endpoint binding.
Likewise, source word depth is not a rung number, and a twelve-coordinate raw
space is not automatically rung12.

## Remaining exact obligations

1. **Source:** identify the intended rung12 object and provide the actual
   operation-preserving map from the source construction, or specify that it is
   a different admitted rung12 input with its own contract.
2. **Transport:** supply the intended T9 construction; coherent reindexings then
   give the other presentations, but do not choose that construction.
3. **Observer:** supply the authorized rung4 readout and show that it agrees with
   the intended source response after transport. If it is the existing aggregate,
   the displayed collision must be addressed by a justified source encoding—not
   hidden by reanchoring or arbitrary coefficients. If it is finer, its interface
   and physical meaning must be stated independently.

No source-independent physical calibration or new law was introduced. Further
recovery checks would not resolve these endpoint choices.

## Reproduction

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_rung_descent_endpoint_binding.py

Receipt: `results/rung-descent-endpoint-binding.json`.
The exchange, phase, spin and original rung dependencies are freshly rebuilt.
The audit distinguishes successful verification from the failed reader-binding
gate. No claim of complete physical rung12-to-rung4 descent is made.
