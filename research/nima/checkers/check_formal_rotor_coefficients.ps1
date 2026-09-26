param([switch]$Fresh, [switch]$Worker)
$ErrorActionPreference = 'Stop'
if (!$Worker) {
  $PreviousPathExt = $env:PATHEXT
  $env:PATHEXT = '.COM;.EXE;.BAT;.CMD'
  try {
    $Arguments = @('-NoProfile', '-File', ('"' + $PSCommandPath + '"'), '-Worker')
    if ($Fresh) { $Arguments += '-Fresh' }
    $Child = Start-Process -FilePath (Join-Path $PSHOME 'pwsh.exe') -ArgumentList $Arguments -NoNewWindow -Wait -PassThru
    exit $Child.ExitCode
  } finally { $env:PATHEXT = $PreviousPathExt }
}
& (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module FormalRotorCoefficients -Fresh:$Fresh
exit $LASTEXITCODE
