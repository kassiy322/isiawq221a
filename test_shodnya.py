#!/usr/bin/env python3
"""Тест парсера 2GIS для кафе в Сходне."""

import sys
import os

# Добавляем путь к модулю
sys.path.insert(0, os.path.dirname(__file__))

def test_shodnya_cafes():
    """Тестируем парсер для кафе в Сходне."""
    try:
        # Импортируем после добавления пути
        from parser_2gis import main as parser_main
        
        # URL для кафе в Сходне (Химки)
        shodnya_url = "https://2gis.ru/khimki/search/сходня кафе"
        
        # Настраиваем аргументы командной строки
        sys.argv = [
            'test_shodnya.py',
            '-i', shodnya_url,
            '-o', 'shodnya_cafes_result.csv',
            '-f', 'csv',
            '--parser.max-records', '5',  # Получим 5 записей
            '--chrome.headless', 'yes',
        ]
        
        print(f"Запускаем парсер для: {shodnya_url}")
        print("Настройки: 5 записей, headless режим")
        
        parser_main()
        print("Парсер завершил работу.")
        
        # Проверяем результат
        output_file = 'shodnya_cafes_result.csv'
        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8-sig') as f:
                content = f.read()
                lines = content.split('\n')
                print(f"\\nСоздан файл с {len(lines)} строками")
                
                if len(lines) > 1:
                    print("\\nПервые строки результата:")
                    for i, line in enumerate(lines[:5]):
                        if line.strip():
                            print(f"{i+1}: {line[:150]}...")
                    
                    # Подсчитаем количество записей (исключая заголовок и пустые строки)
                    data_lines = [line for line in lines[1:] if line.strip()]
                    print(f"\\nНайдено записей: {len(data_lines)}")
                else:
                    print("\\nФайл содержит только заголовки - данные не извлечены")
        else:
            print(f"\\nФайл результата '{output_file}' не создан")
            
    except Exception as e:
        print(f"Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_shodnya_cafes()