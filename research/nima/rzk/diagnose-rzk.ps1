$ErrorActionPreference = 'Stop'

function Invoke-HeadlessRzk([string]$Exe, [string]$Arguments) {
  $psi = [System.Diagnostics.ProcessStartInfo]::new()
  $psi.FileName = $Exe
  $psi.Arguments = $Arguments
  $psi.UseShellExecute = $false
  $psi.CreateNoWindow = $true
  $psi.RedirectStandardOutput = $true
  $psi.RedirectStandardError = $true
  $process = [System.Diagnostics.Process]::new()
  $process.StartInfo = $psi
  if (-not $process.Start()) { throw 'Failed to start Rzk' }
  $stdout = $process.StandardOutput.ReadToEnd()
  $stderr = $process.StandardError.ReadToEnd()
  $process.WaitForExit()
  [PSCustomObject]@{ ExitCode = $process.ExitCode; Stdout = $stdout; Stderr = $stderr }
}

$cmd = Get-Command rzk -ErrorAction SilentlyContinue
$fallback = Join-Path $HOME '.local/bin/rzk.exe'
$exe = if ($null -ne $cmd) { $cmd.Source } else { $fallback }
if (-not (Test-Path $exe)) { throw "Rzk executable not found: $exe" }
$item = Get-Item $exe
Write-Output "EXE=$exe LENGTH=$($item.Length)"
$result = Invoke-HeadlessRzk $exe 'version'
Write-Output "PROCESS_EXIT=$($result.ExitCode)"
Write-Output "PROCESS_STDOUT=$($result.Stdout.Trim())"
Write-Output "PROCESS_STDERR=$($result.Stderr.Trim())"
if ($result.ExitCode -ne 0) { throw "Rzk version failed: $($result.ExitCode)" }
if ($result.Stdout.Trim() -ne '0.11.3') { throw "Rzk version mismatch: $($result.Stdout.Trim())" }
