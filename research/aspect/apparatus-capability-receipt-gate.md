# Apparatus Capability and Receipt Gate

Owner: marici.Aspect

This rung compares the compiled route plan with a capability-attested apparatus
inventory and one execution receipt per planned acquisition.

Admission requires:

1. declared firmware and capabilities match readback;
2. every receipt signature verifies;
3. operation identifiers and nonces are unique;
4. all 24 planned acquisitions have receipts;
5. every receipt matches its planned source, actuator, observer, channel, and
   trigger tick.

Hostiles cover device substitution, receipt replay, omission, firmware drift,
and signed-body tampering.

The executable checker uses a clearly labelled fixture-only HMAC key. It tests
the protocol shape; it is not device identity and no live hardware has been
executed. A live adapter must replace it with hardware-backed attestation,
non-exportable keys, capability readback, and returned device receipts.

Run:

python research/aspect/checkers/check_apparatus_capability_receipt_gate.py
