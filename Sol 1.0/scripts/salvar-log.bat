@echo off
setlocal
set LOGDIR=D:\Projetos\SOL\logs
set LOGFILE=%LOGDIR%\conversa-%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%.md

echo Criando novo log em: %LOGFILE%
echo # Log de Conversa – %DATE% > "%LOGFILE%"
echo **Modelo:** Meta-Llama-3-8B-Instruct (IQ3_M) >> "%LOGFILE%"
echo **Prompt:** sol-prompt.txt >> "%LOGFILE%"
echo. >> "%LOGFILE%"
code "%LOGFILE%"
endlocal
