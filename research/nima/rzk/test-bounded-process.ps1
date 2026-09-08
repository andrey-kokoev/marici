$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'bounded-process.ps1')
$repo = (Resolve-Path (Join-Path $PSScriptRoot '../../..')).Path
$exe = (Get-Process -Id $PID).Path
$fixture = Join-Path $PSScriptRoot 'fixtures/runner-child-control.ps1'
$checks = 0
foreach ($file in @('check-boundary-framed.ps1','bounded-process.ps1','test-bounded-process.ps1','fixtures/runner-child-control.ps1')) {
  $tokens = $null; $errors = $null
  [Management.Automation.Language.Parser]::ParseFile((Join-Path $PSScriptRoot $file), [ref] $tokens, [ref] $errors) | Out-Null
  if ($errors.Count -ne 0) { throw "Parse failure in $file : $($errors | Out-String)" }; $checks++
}
$cases = @()
foreach ($mode in @('success','failure','timeout')) {
  $timeout = if ($mode -eq 'timeout') { 1500 } else { 5000 }
  $r = Invoke-NimaBoundedProcess -Executable $exe -WorkingDirectory $repo `
    -Arguments @('-NoProfile','-File',$fixture,'-Mode',$mode) -TimeoutMilliseconds $timeout
  $expected = if ($mode -eq 'success') { 0 } elseif ($mode -eq 'failure') { 7 } else { 124 }
  if ($r.exit_code -ne $expected) { throw "Wrong exit for $mode : $($r.exit_code)" }; $checks++
  if ($r.timed_out -ne ($mode -eq 'timeout')) { throw "Wrong timeout flag: $mode" }; $checks++
  if (-not $r.stdout.Contains('probe-λ')) { throw "Missing UTF8/partial stdout: $mode" }; $checks++
  if (-not $r.stderr.Contains('diagnostic-λ')) { throw "Missing UTF8/partial stderr: $mode" }; $checks++
  if ($r.duration_ms -le 0) { throw "Missing duration: $mode" }; $checks++
  $cases += @{ mode = $mode; result = $r }
}
$temp = Join-Path $repo ('research/nima/results/runner-input-test-' + [guid]::NewGuid().ToString() + '.txt')
try {
  'original' | Set-Content -LiteralPath $temp
  $snapshot = Get-NimaInputSnapshot -Paths @($temp)
  if (-not (Test-NimaInputSnapshot -Snapshot $snapshot)) { throw 'Unchanged snapshot rejected' }; $checks++
  'modified' | Set-Content -LiteralPath $temp
  if (Test-NimaInputSnapshot -Snapshot $snapshot) { throw 'Changed snapshot accepted' }; $checks++
  Remove-Item -LiteralPath $temp
  if (Test-NimaInputSnapshot -Snapshot $snapshot) { throw 'Missing input accepted' }; $checks++
}
finally { if (Test-Path -LiteralPath $temp) { Remove-Item -LiteralPath $temp } }
$record = @{
  status = 'passed'; assertions = $checks; checked_at = [DateTimeOffset]::UtcNow.ToString('o')
  cases = $cases
  scope = 'Runner controls only; no Rzk or arithmetic closure executed'
}
$record | ConvertTo-Json -Depth 7 | Set-Content (Join-Path $repo 'research/nima/results/bounded-process-tests.json')
Write-Output "Passed $checks runner controls; no Rzk invocation."
