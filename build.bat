@echo off
echo ===== RPG Maker 翻译助手构建脚本 =====
echo 正在启动构建过程，请稍候...

rem 检查Python是否已安装
echo 检查Python环境...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 错误: 未检测到Python安装。
    echo 请先安装Python 3.7或更高版本，可从 https://www.python.org/downloads/ 下载。
    pause
    exit /b 1
)

rem 检查必要的文件夹是否存在
echo 检查必要的文件夹...

if not exist RPGRewriter (
    echo 警告: 未找到RPGRewriter文件夹!
    echo 请确保RPGRewriter文件夹位于当前目录。
    choice /C YN /M "是否继续构建?"
    if %ERRORLEVEL% EQU 2 exit /b 1
)

if not exist EasyRPG (
    echo 警告: 未找到EasyRPG文件夹!
    echo 请确保EasyRPG文件夹位于当前目录。
    choice /C YN /M "是否继续构建?"
    if %ERRORLEVEL% EQU 2 exit /b 1
)

if not exist RTPCollection (
    echo 警告: 未找到RTPCollection文件夹!
    echo 请确保RTPCollection文件夹位于当前目录。
    choice /C YN /M "是否继续构建?"
    if %ERRORLEVEL% EQU 2 exit /b 1
)

if not exist Works (
    echo 注意: 未找到Works文件夹，将自动创建。
    mkdir Works
)

rem 询问构建模式
echo.
echo 请选择构建模式:
echo 1 - 多文件模式 (创建包含多个文件的文件夹，启动更快且包含所有依赖) [推荐]
echo 2 - 单文件模式 (所有内容打包到一个.exe文件，但启动时间较长)
choice /C 12 /M "请选择:"

set BUILD_ARGS=
if %ERRORLEVEL% EQU 2 (
    echo 已选择单文件模式
    set BUILD_ARGS=--onefile
) else (
    echo 已选择多文件模式（默认）
)

rem 运行构建脚本
echo.
echo 开始构建，这可能需要几分钟时间...
python build_exe.py %BUILD_ARGS%

if %ERRORLEVEL% NEQ 0 (
    echo 构建过程中出错，请检查错误信息。
    pause
    exit /b 1
)

echo.
echo 构建过程完成！
if "%BUILD_ARGS%"=="--onefile" (
    echo 您可以在 dist 目录中找到可执行文件。
) else (
    echo 您可以在 dist\RPGTranslationAssistant 目录中找到可执行文件及依赖资源。
    echo 注意: 分发时需要包含整个文件夹。
)
echo.

rem 自动打开dist文件夹
if exist dist (
    echo 正在打开dist文件夹...
    start "" "dist"
)

pause 