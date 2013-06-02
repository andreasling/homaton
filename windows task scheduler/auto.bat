@echo off
ping -n 1 -w 1000 192.168.0.101
if %errorlevel% equ 1 (
"\Program Files (x86)\Git\bin\curl.exe" --data "off" --request POST http://192.168.0.104:8080/api/all
)

rem findstr "Reply from 192.168.0.104:" || "\Program Files (x86)\Git\bin\curl.exe" --data "off" --request POST http://192.168.0.104:8080/api/all
rem pause
