$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot '../bounded-process.ps1')
$repo = (Resolve-Path (Join-Path $PSScriptRoot '../../../..')).Path
$exe = Join-Path $HOME '.local/bin/rzk.exe'
$r = Invoke-NimaBoundedProcess -Executable $exe -WorkingDirectory $repo -Arguments @('typecheck', (Join-Path $PSScriptRoot 'generic-data-probe.rzk.md')) -TimeoutMilliseconds 5000
[Console]::Out.Write($r.stdout)
[Console]::Error.Write($r.stderr)
exit $r.exit_code
