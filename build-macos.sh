#!/bin/bash

echo "================================="
echo "Parser 2GIS - macOS Build Script"
echo "Enhanced Edition with Pagination"
echo "================================="

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 не найден. Установите Python 3.8+"
    exit 1
fi

echo "Python версия: $(python3 --version)"

# Проверка и создание виртуального окружения
if [ ! -d ".venv" ]; then
    echo "Создание виртуального окружения..."
    python3 -m venv .venv
fi

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source .venv/bin/activate

# Обновление pip
echo "Обновление pip..."
python -m pip install --upgrade pip

# Установка зависимостей для сборки
echo "Установка зависимостей для сборки..."
pip install pyinstaller setuptools wheel

# Установка проекта в режиме разработки
echo "Установка parser-2gis в dev режиме..."
pip install -e .

# Проверка установки
echo "Тестирование установки..."
python -c "from parser_2gis import main; print('Модуль загружен успешно')"
if [ $? -ne 0 ]; then
    echo "ERROR: Не удалось загрузить модуль parser_2gis"
    exit 1
fi

# Создание исполняемого файла
echo "================================="
echo "Создание исполняемого файла..."
echo "================================="

# Создание папки для сборки
mkdir -p dist
rm -rf dist/parser-2gis-macos

# Сборка с PyInstaller
pyinstaller --onefile \
    --name parser-2gis \
    --distpath dist/parser-2gis-macos \
    --workpath build \
    --specpath build \
    --add-data "parser_2gis/data/cities.json:parser_2gis/data" \
    --add-data "parser_2gis/data/rubrics.json:parser_2gis/data" \
    --hidden-import pydantic \
    --hidden-import psutil \
    --hidden-import openpyxl \
    --collect-submodules parser_2gis \
    --console \
    parser-2gis.py

if [ $? -ne 0 ]; then
    echo "ERROR: Сборка не удалась"
    exit 1
fi

# Копирование дополнительных файлов
echo "Копирование дополнительных файлов..."
cp README_RELEASE.md "dist/parser-2gis-macos/README.md"
[ -f CHANGELOG.md ] && cp CHANGELOG.md "dist/parser-2gis-macos/"

# Создание скрипта для запуска примера
cat > "dist/parser-2gis-macos/run-example.sh" << 'EOF'
#!/bin/bash
# Пример запуска Parser 2GIS Enhanced Edition
echo "Пример: Сбор кафе из Москвы с пагинацией"
./parser-2gis -i "https://2gis.ru/moscow/search/кафе" -o cafes-moscow.csv -f csv --parser.max-records 50 --writer.csv.add-rubrics yes
EOF

chmod +x "dist/parser-2gis-macos/run-example.sh"
chmod +x "dist/parser-2gis-macos/parser-2gis"

# Создание архива
echo "Создание архива..."
cd dist
tar -czf parser-2gis-enhanced-macos.tar.gz parser-2gis-macos/
cd ..

echo "================================="
echo "✅ СБОРКА ЗАВЕРШЕНА УСПЕШНО!"
echo "================================="
echo "Файлы в папке: dist/parser-2gis-macos/"
echo "Архив: dist/parser-2gis-enhanced-macos.tar.gz"
echo ""
echo "Размер архива:"
ls -lh "dist/parser-2gis-enhanced-macos.tar.gz"
echo ""
echo "Для тестирования запустите:"
echo "cd dist/parser-2gis-macos"
echo "./parser-2gis --help"
echo ""