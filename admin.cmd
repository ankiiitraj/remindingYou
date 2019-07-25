set mydir=%~dp0

Powershell -Command "& { Start-Process \"%mydir%a.cmd\" -verb RunAs}"
