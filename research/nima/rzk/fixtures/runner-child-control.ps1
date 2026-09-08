param([ValidateSet('success','failure','timeout')] [string] $Mode)
[Console]::OutputEncoding = [Text.Encoding]::UTF8
[Console]::Out.WriteLine('probe-λ')
[Console]::Error.WriteLine('diagnostic-λ')
if ($Mode -eq 'failure') { exit 7 }
if ($Mode -eq 'timeout') { Start-Sleep -Seconds 10 }
exit 0
