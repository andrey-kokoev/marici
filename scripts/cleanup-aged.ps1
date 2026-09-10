[CmdletBinding()]
param(
  [ValidateRange(1, 10080)]
  [int]$OlderThanMinutes = 15,

  [Alias('Summary')]
  [switch]$ShowSummary,

  [switch]$Detailed,

  [switch]$NoPush
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$repo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$gitCommand = Get-Command git.exe -ErrorAction SilentlyContinue
$gitPath = if ($gitCommand) { $gitCommand.Source } else { Join-Path ${env:ProgramFiles} 'Git\cmd\git.exe' }
if (-not (Test-Path -LiteralPath $gitPath -PathType Leaf)) {
  throw "Could not resolve git.exe; checked PATH and '$gitPath'."
}
$cutoff = (Get-Date).ToUniversalTime().AddMinutes(-$OlderThanMinutes)
$maxPathsPerCommit = 200
$temporaryPattern = '(^|/)(tmp|temp|\.check-tmp[^/]*)(/|$)|(^|/).*\.(tmp|bak|swp)$|(^|/)tmp\.json$'
$commitMessages = @{
  '.narada' = 'Checkpoint Narada metadata'
  'background' = 'Checkpoint background artifacts'
  'executions' = 'Checkpoint execution records'
  'public' = 'Checkpoint public artifacts'
  'research/aspect' = 'Advance Aspect programme'
  'research/benincasa' = 'Advance cosmology programme'
  'research/flavor' = 'Advance flavor programme'
  'research/grothendieck' = 'Advance RH programme'
  'research/nima' = 'Advance common synthesis'
  'research/strominger' = 'Advance string programme'
  'src/ledger' = 'Checkpoint mature ledger frontier'
}

function Invoke-Git {
  param([Parameter(ValueFromRemainingArguments)][string[]]$Arguments)

  $startInfo = [System.Diagnostics.ProcessStartInfo]::new()
  $startInfo.FileName = $gitPath
  $startInfo.UseShellExecute = $false
  $startInfo.RedirectStandardOutput = $true
  $startInfo.RedirectStandardError = $true
  $startInfo.ArgumentList.Add('-C')
  $startInfo.ArgumentList.Add($repo)
  foreach ($argument in $Arguments) {
    $startInfo.ArgumentList.Add([string]$argument)
  }

  $process = [System.Diagnostics.Process]::new()
  $process.StartInfo = $startInfo
  $started = $process.Start()
  if (-not $started) { throw 'Could not start git.exe.' }
  $stdoutTask = $process.StandardOutput.ReadToEndAsync()
  $stderrTask = $process.StandardError.ReadToEndAsync()
  $process.WaitForExit()
  $stdout = $stdoutTask.GetAwaiter().GetResult()
  $stderr = $stderrTask.GetAwaiter().GetResult()
  $exitCode = $process.ExitCode
  $process.Dispose()

  if ($exitCode -ne 0) {
    $detail = if ($stderr.Trim()) { $stderr.Trim() } else { $stdout.Trim() }
    throw "git $($Arguments -join ' ') failed with exit code ${exitCode}: $detail"
  }
  if ($stdout.Trim()) { return ($stdout -split '\r?\n' | Where-Object { $_ }) }
}

function Invoke-GitQuiet {
  param([Parameter(ValueFromRemainingArguments)][string[]]$Arguments)

  $null = Invoke-Git @Arguments
}

function Invoke-GitAdd {
  param([string[]]$Paths)

  $startInfo = [System.Diagnostics.ProcessStartInfo]::new()
  $startInfo.FileName = $gitPath
  $startInfo.UseShellExecute = $false
  $startInfo.RedirectStandardInput = $true
  $startInfo.RedirectStandardOutput = $true
  $startInfo.RedirectStandardError = $true
  $startInfo.ArgumentList.Add('-C')
  $startInfo.ArgumentList.Add($repo)
  $startInfo.ArgumentList.Add('-c')
  $startInfo.ArgumentList.Add('core.longpaths=true')
  $startInfo.ArgumentList.Add('add')
  $startInfo.ArgumentList.Add('--pathspec-from-file=-')
  $startInfo.ArgumentList.Add('--pathspec-file-nul')

  $process = [System.Diagnostics.Process]::new()
  $process.StartInfo = $startInfo
  $started = $process.Start()
  if (-not $started) { throw 'Could not start git.exe for pathspec staging.' }
  $stdoutTask = $process.StandardOutput.ReadToEndAsync()
  $stderrTask = $process.StandardError.ReadToEndAsync()
  $process.StandardInput.Write(([string]::Join([char]0, $Paths) + [char]0))
  $process.StandardInput.Close()
  $process.WaitForExit()
  $stdout = $stdoutTask.GetAwaiter().GetResult()
  $stderr = $stderrTask.GetAwaiter().GetResult()
  $exitCode = $process.ExitCode
  $process.Dispose()

  if ($exitCode -ne 0) {
    $detail = if ($stderr.Trim()) { $stderr.Trim() } else { $stdout.Trim() }
    throw "git add failed with exit code ${exitCode}: $detail"
  }
}

function Get-DirtyRecords {
  $statusOutput = @(& $gitPath -C $repo -c core.quotepath=false status --porcelain=v1 -z -uall)
  $raw = if ($statusOutput.Count -eq 0) { '' } else { [string]::Join('', $statusOutput) }
  if ($LASTEXITCODE -ne 0) { throw 'git status failed' }

  foreach ($item in ($raw -split [char]0 | Where-Object { $_ })) {
    if ($item.Length -lt 4) { continue }
    $path = $item.Substring(3)
    if ($path -match ' -> ') { $path = ($path -split ' -> ')[-1] }
    $path = $path.Replace('\', '/')
    [pscustomobject]@{ Status = $item.Substring(0, 2); Path = $path }
  }
}

foreach ($stateName in @('MERGE_HEAD', 'rebase-merge', 'rebase-apply')) {
  $statePath = Invoke-Git rev-parse --git-path $stateName
  if (Test-Path -LiteralPath (Join-Path $repo $statePath)) {
    throw "Refusing cleanup while Git state '$stateName' is active."
  }
}

$dirty = @(Get-DirtyRecords)
$staged = @($dirty | Where-Object { $_.Status[0] -notin @(' ', '?') })
if ($staged.Count -gt 0) {
  throw "Refusing to absorb $($staged.Count) pre-staged path(s)."
}

$eligible = [System.Collections.Generic.List[object]]::new()
$protected = [System.Collections.Generic.List[string]]::new()
$temporary = [System.Collections.Generic.List[string]]::new()

foreach ($record in $dirty) {
  $fullPath = Join-Path $repo $record.Path
  if ($record.Path -match $temporaryPattern) {
    $temporary.Add($record.Path)
    continue
  }
  if (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
    $protected.Add($record.Path)
    continue
  }
  $mtime = (Get-Item -LiteralPath $fullPath).LastWriteTimeUtc
  if ($mtime -le $cutoff) {
    $parts = $record.Path -split '/'
    $group = if ($parts[0] -eq 'research' -and $parts.Count -ge 2) {
      "research/$($parts[1])"
    } elseif ($parts[0] -eq 'src' -and $parts.Count -ge 2 -and $parts[1] -eq 'ledger') {
      'src/ledger'
    } else {
      $parts[0]
    }
    $eligible.Add([pscustomobject]@{ Path = $record.Path; Group = $group })
  } else {
    $protected.Add($record.Path)
  }
}

$commits = [System.Collections.Generic.List[object]]::new()
foreach ($grouping in ($eligible | Group-Object Group | Sort-Object Name)) {
  $paths = @($grouping.Group.Path | Sort-Object -Unique)
  $baseMessage = if ($commitMessages.ContainsKey($grouping.Name)) {
    $commitMessages[$grouping.Name]
  } else {
    "Checkpoint $($grouping.Name)"
  }

  for ($offset = 0; $offset -lt $paths.Count; $offset += $maxPathsPerCommit) {
    $last = [Math]::Min($offset + $maxPathsPerCommit - 1, $paths.Count - 1)
    $chunk = @($paths[$offset..$last])

    # Recheck immediately before staging so files changed after cutoff remain untouched.
    $stable = @($chunk | Where-Object {
      $candidate = Join-Path $repo $_
      (Test-Path -LiteralPath $candidate -PathType Leaf) -and
        ((Get-Item -LiteralPath $candidate).LastWriteTimeUtc -le $cutoff)
    })
    foreach ($path in ($chunk | Where-Object { $_ -notin $stable })) { $protected.Add($path) }
    if ($stable.Count -eq 0) { continue }

    Invoke-GitAdd $stable
    $part = if ($paths.Count -gt $maxPathsPerCommit) { " $([Math]::Floor($offset / $maxPathsPerCommit) + 1)" } else { '' }
    Invoke-GitQuiet commit -m "$baseMessage$part"
    $sha = (Invoke-Git rev-parse HEAD | Select-Object -Last 1).Trim()
    $commits.Add([pscustomobject]@{ Group = $grouping.Name; Count = $stable.Count; Commit = $sha })
  }
}

$pushed = $false
if ($commits.Count -gt 0 -and -not $NoPush) {
  Invoke-GitQuiet push
  $pushed = $true
}

$remaining = @(Get-DirtyRecords)
$remainingOld = @($remaining | Where-Object {
  $candidate = Join-Path $repo $_.Path
  (Test-Path -LiteralPath $candidate -PathType Leaf) -and
    ((Get-Item -LiteralPath $candidate).LastWriteTimeUtc -le $cutoff) -and
    ($_.Path -notmatch $temporaryPattern)
})

$result = [ordered]@{
  status = if ($remainingOld.Count -eq 0) { 'ok' } else { 'incomplete' }
  cutoff = $cutoff.ToString('o')
  committed_files = if ($commits.Count -gt 0) { ($commits | Measure-Object Count -Sum).Sum } else { 0 }
  commits = $commits.Count
  pushed = $pushed
  tip = if ($commits.Count -gt 0) { $commits[-1].Commit } else { (Invoke-Git rev-parse HEAD | Select-Object -Last 1).Trim() }
  protected_files = @($remaining).Count
  remaining_eligible = $remainingOld.Count
  temporary_skipped = $temporary.Count
}

if ($Detailed) {
  $result.details = [ordered]@{
    commits = @($commits)
    protected_paths = @($protected | Sort-Object -Unique)
    temporary_paths = @($temporary | Sort-Object -Unique)
    remaining_eligible_paths = @($remainingOld.Path)
  }
}

if ($ShowSummary -or $Detailed) {
  [pscustomobject]$result | ConvertTo-Json -Depth 6 -Compress
}
if ($remainingOld.Count -gt 0) { exit 2 }
