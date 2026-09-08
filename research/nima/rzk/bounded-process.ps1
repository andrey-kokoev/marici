function Invoke-NimaBoundedProcess {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory)] [string] $Executable,
    [Parameter(Mandatory)] [string] $WorkingDirectory,
    [string[]] $Arguments = @(),
    [ValidateRange(1,300000)] [int] $TimeoutMilliseconds = 30000
  )
  $psi = [Diagnostics.ProcessStartInfo]::new()
  $psi.FileName = $Executable
  $psi.WorkingDirectory = $WorkingDirectory
  $psi.UseShellExecute = $false
  $psi.CreateNoWindow = $true
  $psi.RedirectStandardOutput = $true
  $psi.RedirectStandardError = $true
  $psi.StandardOutputEncoding = [Text.Encoding]::UTF8
  $psi.StandardErrorEncoding = [Text.Encoding]::UTF8
  foreach ($arg in $Arguments) { $psi.ArgumentList.Add($arg) }
  $process = [Diagnostics.Process]::new()
  $process.StartInfo = $psi
  $clock = [Diagnostics.Stopwatch]::StartNew()
  try {
    if (-not $process.Start()) { throw "Failed to start $Executable" }
    $stdout = $process.StandardOutput.ReadToEndAsync()
    $stderr = $process.StandardError.ReadToEndAsync()
    $timedOut = -not $process.WaitForExit($TimeoutMilliseconds)
    if ($timedOut) {
      # The child may have exited between WaitForExit and Kill.
      if (-not $process.HasExited) {
        try { $process.Kill($true) }
        catch [InvalidOperationException] { if (-not $process.HasExited) { throw } }
      }
      $process.WaitForExit()
    }
    $outText = $stdout.GetAwaiter().GetResult()
    $errText = $stderr.GetAwaiter().GetResult()
    $clock.Stop()
    return [PSCustomObject]@{
      exit_code = $(if ($timedOut) { 124 } else { $process.ExitCode })
      process_exit_code = $process.ExitCode
      timed_out = $timedOut
      duration_ms = $clock.ElapsedMilliseconds
      stdout = $outText
      stderr = $errText
    }
  }
  finally { $clock.Stop(); $process.Dispose() }
}

function Get-NimaInputSnapshot {
  param([Parameter(Mandatory)] [string[]] $Paths)
  return @($Paths | ForEach-Object {
    [PSCustomObject]@{ path = $_; sha256 = (Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash.ToLower() }
  })
}

function Test-NimaInputSnapshot {
  param([Parameter(Mandatory)] [object[]] $Snapshot)
  foreach ($entry in $Snapshot) {
    if (-not (Test-Path -LiteralPath $entry.path -PathType Leaf)) { return $false }
    if ((Get-FileHash -LiteralPath $entry.path -Algorithm SHA256).Hash.ToLower() -ne $entry.sha256) {
      return $false
    }
  }
  return $true
}
