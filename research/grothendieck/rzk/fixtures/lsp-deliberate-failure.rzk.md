# Rzk LSP deliberate-failure fixture

This file is intentionally invalid. The Pi/Rzk LSP smoke test requires a
nonempty diagnostic response for the undefined type below.

```rzk
#lang rzk-1
```

```rzk
#define marici-lsp-deliberate-failure
  : MissingRzkType
  := missing-rzk-term
```
