$ErrorActionPreference = 'Stop'
$project = Resolve-Path (Join-Path $PSScriptRoot '../../buzzard/marici_formal')
$source = Resolve-Path (Join-Path $PSScriptRoot 'FinitePosetNerve.lean')
$psi = [System.Diagnostics.ProcessStartInfo]::new()
$psi.FileName = 'lake'
$psi.ArgumentList.Add('env')
$psi.ArgumentList.Add('lean')
$psi.ArgumentList.Add($source.Path)
$psi.WorkingDirectory = $project.Path
$psi.UseShellExecute = $false
$psi.CreateNoWindow = $true
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$p = [System.Diagnostics.Process]::new()
$p.StartInfo = $psi
if (-not $p.Start()) { throw 'failed to start Lean' }
$stdoutTask = $p.StandardOutput.ReadToEndAsync()
$stderrTask = $p.StandardError.ReadToEndAsync()
$p.WaitForExit()
$stdout = $stdoutTask.GetAwaiter().GetResult()
$stderr = $stderrTask.GetAwaiter().GetResult()
if ($stdout) { Write-Output $stdout }
if ($stderr) { Write-Error $stderr }
if ($p.ExitCode -ne 0) { throw "Lean failed: $($p.ExitCode)" }
Write-Output 'MARICI_FINITE_POSET_NERVE_LEAN_OK'
