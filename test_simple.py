#!/usr/bin/env python3
"""Простой тест для проверки работы парсера 2GIS."""

import sys
import os

# Добавляем путь к модулю
sys.path.insert(0, os.path.dirname(__file__))

def test_parser():
    """Тестируем парсер с минимальными настройками."""
    try:
        # Импортируем после добавления пути
        from parser_2gis import main as parser_main
        
        # Настраиваем аргументы командной строки
        sys.argv = [
            'test_simple.py',
            '-i', 'https://2gis.ru/moscow/search/аптеки',  # Используем тот же URL что и в тестах
            '-o', 'simple_test_output.csv',
            '-f', 'csv',
            '--parser.max-records', '3',  # Всего 3 записи для быстрого теста
            '--chrome.headless', 'yes',
        ]
        
        print("Запускаем парсер...")
        parser_main()
        print("Парсер завершил работу.")
        
        # Проверяем результат
        if os.path.exists('simple_test_output.csv'):
            with open('simple_test_output.csv', 'r', encoding='utf-8-sig') as f:
                content = f.read()
                lines = content.split('\n')
                print(f"Создан файл с {len(lines)} строками")
                if len(lines) > 1:
                    print("Первые строки:")
                    for i, line in enumerate(lines[:3]):
                        print(f"{i+1}: {line[:100]}...")
                else:
                    print("Файл содержит только заголовки")
        else:
            print("Файл результата не создан")
            
    except Exception as e:
        print(f"Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_parser()