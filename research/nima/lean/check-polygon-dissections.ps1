$ErrorActionPreference = 'Stop'
$project = Resolve-Path (Join-Path $PSScriptRoot '../../buzzard/marici_formal')
$source = Resolve-Path (Join-Path $PSScriptRoot 'PolygonDissections.lean')
$psi = [System.Diagnostics.ProcessStartInfo]::new()
$psi.FileName = 'lake'
$psi.ArgumentList.Add('env'); $psi.ArgumentList.Add('lean'); $psi.ArgumentList.Add($source.Path)
$psi.WorkingDirectory = $project.Path
$psi.UseShellExecute = $false; $psi.CreateNoWindow = $true
$psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true
$p = [System.Diagnostics.Process]::new(); $p.StartInfo = $psi
if (-not $p.Start()) { throw 'failed to start Lean' }
$outTask = $p.StandardOutput.ReadToEndAsync(); $errTask = $p.StandardError.ReadToEndAsync()
$p.WaitForExit(); $out = $outTask.GetAwaiter().GetResult(); $err = $errTask.GetAwaiter().GetResult()
if ($p.ExitCode -ne 0) {
  (($out + "`n" + $err) -split "`r?`n" | Select-Object -First 15) | ForEach-Object { Write-Output $_ }
  throw "Lean failed: $($p.ExitCode)"
}
if ($out) { Write-Output $out }
Write-Output 'MARICI_POLYGON_DISSECTIONS_LEAN_OK'
