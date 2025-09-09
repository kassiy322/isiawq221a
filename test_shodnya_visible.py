#!/usr/bin/env python3
"""Тест парсера 2GIS для кафе в Сходне (видимый браузер)."""

import sys
import os

# Добавляем путь к модулю
sys.path.insert(0, os.path.dirname(__file__))

def test_shodnya_cafes_visible():
    """Тестируем парсер для кафе в Сходне с видимым браузером."""
    try:
        # Импортируем после добавления пути
        from parser_2gis import main as parser_main
        
        # URL для кафе в Сходне (Химки) - используем более общий поиск
        shodnya_url = "https://2gis.ru/khimki/search/кафе"
        
        # Настраиваем аргументы командной строки
        sys.argv = [
            'test_shodnya_visible.py',
            '-i', shodnya_url,
            '-o', 'shodnya_cafes_visible.csv', 
            '-f', 'csv',
            '--parser.max-records', '10',  # Больше записей
            '--chrome.headless', 'no',     # Видимый браузер
            '--parser.delay_between_clicks', '1000',  # Задержка между кликами
        ]
        
        print(f"Запускаем парсер для: {shodnya_url}")
        print("Настройки: 10 записей, видимый браузер, задержка 1 сек")
        print("Браузер откроется - не закрывайте его вручную!")
        
        parser_main()
        print("Парсер завершил работу.")
        
        # Проверяем результат
        output_file = 'shodnya_cafes_visible.csv'
        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8-sig') as f:
                content = f.read()
                lines = content.split('\n')
                print(f"\\nСоздан файл с {len(lines)} строками")
                
                if len(lines) > 1:
                    print("\\nИзвлеченные кафе:")
                    for i, line in enumerate(lines[1:]):
                        if line.strip():
                            # Извлекаем название (первое поле)
                            parts = line.split(',')
                            if len(parts) > 0:
                                name = parts[0].strip('"')
                                print(f"{i+1}: {name}")
                    
                    # Подсчитаем количество записей (исключая заголовок и пустые строки)
                    data_lines = [line for line in lines[1:] if line.strip()]
                    print(f"\\nВсего найдено кафе: {len(data_lines)}")
                else:
                    print("\\nФайл содержит только заголовки - данные не извлечены")
        else:
            print(f"\\nФайл результата '{output_file}' не создан")
            
    except Exception as e:
        print(f"Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_shodnya_cafes_visible()