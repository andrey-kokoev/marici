"""Explicit stronger audit mode: complete legal replay plus source agreement."""
from offline_replay import replay
from source_interpreter import interpret

def semantic_replay(trace):
 result=replay(trace)
 if not result['complete']:raise ValueError('semantic replay requires a complete trace')
 declaration=trace['declaration']
 expected=interpret(declaration['bits'],declaration['program'])
 if result['terminal']!=expected:raise ValueError('replayed terminal differs from source semantics')
 return dict(result,source_semantics='matched',assurance='executable-cross-check-not-formal-proof')

if __name__=='__main__':
 import sys,json
 from pathlib import Path
 print(json.dumps(semantic_replay(json.loads(Path(sys.argv[1]).read_text()))))
