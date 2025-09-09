@echo off
echo =================================
echo Parser 2GIS - Windows Build Script
echo Enhanced Edition with Pagination
echo =================================

:: Проверка Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python не найден. Установите Python 3.8+
    pause
    exit /b 1
)

:: Проверка и создание виртуального окружения
if not exist ".venv" (
    echo Создание виртуального окружения...
    python -m venv .venv
)

:: Активация виртуального окружения
echo Активация виртуального окружения...
call .venv\Scripts\activate.bat

:: Обновление pip
echo Обновление pip...
python -m pip install --upgrade pip

:: Установка зависимостей для сборки
echo Установка зависимостей для сборки...
pip install pyinstaller setuptools wheel

:: Установка проекта в режиме разработки
echo Установка parser-2gis в dev режиме...
pip install -e .

:: Проверка установки
echo Тестирование установки...
python -c "from parser_2gis import main; print('Модуль загружен успешно')"
if errorlevel 1 (
    echo ERROR: Не удалось загрузить модуль parser_2gis
    pause
    exit /b 1
)

:: Создание исполняемого файла
echo =================================
echo Создание исполняемого файла...
echo =================================

:: Создание папки для сборки
if not exist "dist" mkdir dist
if exist "dist\parser-2gis-windows" rmdir /s /q "dist\parser-2gis-windows"

:: Сборка с PyInstaller
pyinstaller --onefile ^
    --name parser-2gis ^
    --distpath dist\parser-2gis-windows ^
    --workpath build ^
    --specpath build ^
    --add-data "parser_2gis\data\cities.json;parser_2gis\data" ^
    --add-data "parser_2gis\data\rubrics.json;parser_2gis\data" ^
    --hidden-import pydantic ^
    --hidden-import psutil ^
    --hidden-import openpyxl ^
    --collect-submodules parser_2gis ^
    --console ^
    parser-2gis.py

if errorlevel 1 (
    echo ERROR: Сборка не удалась
    pause
    exit /b 1
)

:: Копирование дополнительных файлов
echo Копирование дополнительных файлов...
copy README_RELEASE.md "dist\parser-2gis-windows\README.md"
copy CHANGELOG.md "dist\parser-2gis-windows\CHANGELOG.md" 2>nul

:: Создание пакетного файла для запуска
echo @echo off > "dist\parser-2gis-windows\run-example.bat"
echo :: Пример запуска Parser 2GIS Enhanced Edition >> "dist\parser-2gis-windows\run-example.bat"
echo echo Пример: Сбор кафе из Москвы с пагинацией >> "dist\parser-2gis-windows\run-example.bat"
echo parser-2gis.exe -i "https://2gis.ru/moscow/search/кафе" -o cafes-moscow.csv -f csv --parser.max-records 50 --writer.csv.add-rubrics yes >> "dist\parser-2gis-windows\run-example.bat"
echo pause >> "dist\parser-2gis-windows\run-example.bat"

:: Создание архива
echo Создание ZIP архива...
cd dist
powershell -command "Compress-Archive -Path 'parser-2gis-windows' -DestinationPath 'parser-2gis-enhanced-windows.zip' -Force"
cd ..

echo =================================
echo ✅ СБОРКА ЗАВЕРШЕНА УСПЕШНО!
echo =================================
echo Файлы в папке: dist\parser-2gis-windows\
echo Архив: dist\parser-2gis-enhanced-windows.zip
echo.
echo Размер архива:
dir "dist\parser-2gis-enhanced-windows.zip" | find ".zip"
echo.
echo Для тестирования запустите:
echo cd dist\parser-2gis-windows
echo parser-2gis.exe --help
echo.
pause