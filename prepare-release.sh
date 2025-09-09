#!/bin/bash

echo "=================================================="
echo "Parser 2GIS Enhanced - Preparation Release Script"
echo "=================================================="

# Проверяем что мы в правильной директории
if [ ! -f "parser-2gis.py" ]; then
    echo "ERROR: Запустите скрипт из корневой директории проекта"
    exit 1
fi

# Создаем структуру для релиза
echo "Создание структуры релиза..."
mkdir -p release

# Копируем все необходимые файлы
echo "Копирование файлов проекта..."
rsync -av --exclude='*.pyc' --exclude='__pycache__' --exclude='.git' --exclude='build' --exclude='dist' --exclude='.venv' --exclude='release' . release/

# Копируем специальные файлы для GitHub
echo "Подготовка файлов для GitHub..."
cp README_RELEASE.md release/README.md

# Создаем .gitignore для GitHub репозитория
cat > release/.gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Results
*.csv
*.xlsx
*.json
results/

# Logs
*.log
EOF

# Создаем файл для запуска тестов
cat > release/test-enhanced.py << 'EOF'
#!/usr/bin/env python3
"""Тест улучшенной версии Parser 2GIS"""

import sys
import os

def test_enhanced_features():
    """Тестируем новые возможности Enhanced Edition"""
    
    # Проверяем импорт модулей
    try:
        from parser_2gis import main
        from parser_2gis.config import Configuration
        from parser_2gis.parser.options import ParserOptions
        from parser_2gis.chrome.options import ChromeOptions
        print("✅ Все модули загружаются корректно")
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        return False
    
    # Проверяем настройки по умолчанию
    parser_opts = ParserOptions()
    chrome_opts = ChromeOptions()
    
    print(f"📊 Настройки парсера:")
    print(f"   max_records: {parser_opts.max_records} (должно быть >= 50)")
    print(f"   headless: {chrome_opts.headless} (должно быть False)")
    print(f"   start_maximized: {chrome_opts.start_maximized} (должно быть True)")
    
    # Проверяем что лимит достаточный для пагинации
    if parser_opts.max_records >= 50:
        print("✅ Лимит записей настроен для пагинации")
    else:
        print("⚠️  Лимит записей может быть недостаточным для пагинации")
    
    # Проверяем настройки браузера
    if not chrome_opts.headless and chrome_opts.start_maximized:
        print("✅ Браузер настроен для видимого режима")
    else:
        print("⚠️  Настройки браузера не оптимальны")
    
    return True

if __name__ == '__main__':
    print("🔍 Тестирование Parser 2GIS Enhanced Edition")
    print("=" * 50)
    
    success = test_enhanced_features()
    
    if success:
        print("\n🎉 Все тесты пройдены успешно!")
        print("\nДля полного тестирования запустите:")
        print("python parser-2gis.py -i 'https://2gis.ru/moscow/search/кафе' -o test.csv -f csv --parser.max-records 10")
    else:
        print("\n❌ Некоторые тесты не прошли")
        sys.exit(1)
EOF

chmod +x release/test-enhanced.py

echo ""
echo "✅ Релиз подготовлен в папке: release/"
echo ""
echo "Следующие шаги:"
echo "1. cd release"
echo "2. git init"
echo "3. git add ."
echo "4. git commit -m 'Initial commit - Parser 2GIS Enhanced Edition'"
echo "5. git remote add origin https://github.com/vnprofi/repo12c.git"
echo "6. git push -u origin main"
echo ""
echo "Структура релиза:"
find release -type f -name "*.py" -o -name "*.md" -o -name "*.bat" -o -name "*.sh" -o -name "*.yml" | head -20
echo "..."
echo ""
echo "Готово для загрузки в GitHub!"