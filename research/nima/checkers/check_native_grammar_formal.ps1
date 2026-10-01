param([switch]$Worker)
$ErrorActionPreference = 'Stop'
# Same child-local discovery repair as check_native_component_arithmetic.ps1.
# PowerShell caches PATHEXT on startup; do not modify the user's environment.
if (!$Worker) {
  $PreviousPathExt = $env:PATHEXT
  $env:PATHEXT = '.COM;.EXE;.BAT;.CMD'
  try {
    $Arguments = @('-NoProfile', '-File', ('"' + $PSCommandPath + '"'), '-Worker')
    $Child = Start-Process -FilePath (Join-Path $PSHOME 'pwsh.exe') -ArgumentList $Arguments -NoNewWindow -Wait -PassThru
    exit $Child.ExitCode
  } finally { $env:PATHEXT = $PreviousPathExt }
}
& (Join-Path $PSScriptRoot 'check_native_table_equivalence.ps1')
# The last native exit code is an expected negative Agda control (42).
# The called checker throws on wrong rejection and writes its audit only on success.
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$AuditPath = Join-Path $Root 'research/nima/results/native-table-formal-audit.json'
$Audit = Get-Content $AuditPath -Raw | ConvertFrom-Json
if ($Audit.status -ne 'full-typed-native-table-equivalence-checked' -or $Audit.controls.Count -ne 6) {
  throw 'Complete native grammar formal audit missing'
}
exit 0
