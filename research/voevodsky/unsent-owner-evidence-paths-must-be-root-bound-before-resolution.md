# Unsent owner evidence paths must be root-bound before resolution

The prepared local payload uses relative evidence paths. Fresh `check_unsent_payload_path_binding.py` binds those references to this checkout's canonical `research/voevodsky` root, checks all three current evidence hashes, and refuses parent traversal, absolute paths, backslashes and a different project root. It also checks resolved targets stay inside the research root, so a symlink resolving outside would be refused; no physical symlink was created or tested. This is a local file-read safety check, not a fully race-free open against concurrent link replacement.

A copied payload with identical relative names and perhaps even identical bytes is NOT automatically the same local source locus. Conversely resolving paths safely cannot authenticate any referenced issuer evidence: the row owner, source event and generation are still unknown and the payload stays `LOCAL_PREPARED_UNSENDABLE`. An authorized future communication would require a fresh Site-qualified recipient and independently admitted owner scope.

Next test a FILE-SWAP between path validation and byte reading (TOCTOU) with a synthetic resolver/read model: only content-addressed immutable byte snapshots or atomic safe-open procedures can support a robust evidence attachment, but neither grants owner authority. Analytic S,A,R,C,G remains deferred.
