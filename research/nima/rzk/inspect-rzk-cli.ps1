param([string]$Project, [string]$TryFile)
$ErrorActionPreference = 'Stop'
$rzkCommand = Get-Command rzk -ErrorAction SilentlyContinue
$exe = if ($null -ne $rzkCommand) { $rzkCommand.Source } else { Join-Path $HOME '.local/bin/rzk.exe' }
if (-not (Test-Path $exe)) { throw "Rzk executable not found: $exe" }
& $exe '--help'
Write-Output "--- TYPECHECK HELP ---"
& $exe 'typecheck' '--help'
if (-not [string]::IsNullOrWhiteSpace($Project)) {
  Write-Output "--- RZK YAML ---"
  Get-Content (Join-Path $Project 'rzk.yaml') | Select-Object -First 120
}
if (-not [string]::IsNullOrWhiteSpace($TryFile)) {
  Write-Output "--- FILE SELECTOR PROBE ---"
  Push-Location $Project
  try {
    $clock = [Diagnostics.Stopwatch]::StartNew()
    & $exe 'typecheck' $TryFile
    Write-Output "FILE_SELECTOR_EXIT=$LASTEXITCODE ELAPSED_MS=$($clock.ElapsedMilliseconds)"
  } finally { Pop-Location }
}
