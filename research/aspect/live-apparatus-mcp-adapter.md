# Live Optical Apparatus MCP Adapter

Owner: marici.Aspect

The site fabric currently contains no optical-apparatus surface. This packet
defines the exact missing binding.

The adapter separates four operations:

1. read capability and hardware attestation;
2. resolve a route plan without dispatch;
3. dispatch only from a matching dry-run reference and explicit operator
   authority;
4. read device-signed execution receipts.

Dispatch cannot be inferred from transport, capability inspection, or a
successful dry run. Wildcard targets are forbidden. The inventory digest is
bound into execution, and every receipt carries a unique replay nonce.

The conformance checker validates the interface and its negative fixtures. It
does not start apparatus software or execute hardware.
