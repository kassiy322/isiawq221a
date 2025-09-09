#!/usr/bin/env python3
"""Полный тест парсера 2GIS для кафе в Сходне с расширенным сбором данных."""

import sys
import os
import csv

# Добавляем путь к модулю
sys.path.insert(0, os.path.dirname(__file__))

def test_shodnya_cafes_full_data():
    """Тестируем парсер для кафе в Сходне с полным сбором данных."""
    try:
        # Импортируем после добавления пути
        from parser_2gis import main as parser_main
        
        # URL для кафе в Сходне и окрестностях
        shodnya_url = "https://2gis.ru/khimki/search/кафе"
        
        # Настраиваем аргументы командной строки для максимального сбора данных
        sys.argv = [
            'test_shodnya_full.py',
            '-i', shodnya_url,
            '-o', 'shodnya_cafes_full.csv',
            '-f', 'csv',
            '--parser.max-records', '15',  # Больше записей
            '--chrome.headless', 'no',     # ВИДИМЫЙ браузер
            '--chrome.start-maximized', 'yes',  # Развернутое окно
            '--parser.delay_between_clicks', '2000',  # Задержка 2 сек между кликами
            '--writer.csv.add-rubrics', 'yes',  # Добавить рубрики
            '--writer.csv.add-comments', 'yes',  # Добавить комментарии
            '--writer.csv.columns-per-entity', '3',  # До 3 колонок для телефонов/email
            '--writer.csv.remove-empty-columns', 'no',  # НЕ удалять пустые колонки
            '--writer.csv.remove-duplicates', 'yes',  # Удалить дубликаты
            '--writer.verbose', 'yes',  # Подробный вывод
        ]
        
        print(f"Запускаем ПОЛНЫЙ парсер для: {shodnya_url}")
        print("Настройки:")
        print("- 15 записей максимум")
        print("- ВИДИМЫЙ браузер (развернутый)")
        print("- Задержка 2 сек между кликами")
        print("- Сбор рубрик, комментариев, до 3 телефонов/email")
        print("- Подробный вывод")
        print("\nБраузер откроется - НЕ ЗАКРЫВАЙТЕ его!")
        print("Процесс может занять несколько минут...")
        
        parser_main()
        print("\nПарсер завершил работу.")
        
        # Анализируем результат
        output_file = 'shodnya_cafes_full.csv'
        if os.path.exists(output_file):
            print(f"\n{'='*60}")
            print("РЕЗУЛЬТАТЫ ПОЛНОГО СБОРА ДАННЫХ")
            print(f"{'='*60}")
            
            with open(output_file, 'r', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                headers = next(reader)  # Заголовки
                rows = list(reader)
                
                print(f"Создан файл с {len(headers)} колонками и {len(rows)} записями")
                
                # Показываем все колонки
                print(f"\nКОЛОНКИ В CSV ({len(headers)}):")
                for i, header in enumerate(headers, 1):
                    print(f"{i:2d}. {header}")
                
                if rows:
                    print(f"\nНАЙДЕННЫЕ КАФЕ И РЕСТОРАНЫ ({len(rows)}):")
                    
                    for i, row in enumerate(rows, 1):
                        print(f"\n{i}. {'-'*50}")
                        
                        # Основные данные
                        name = row[0] if len(row) > 0 else "Не указано"
                        address = row[3] if len(row) > 3 else "Не указано"
                        print(f"Название: {name}")
                        print(f"Адрес: {address}")
                        
                        # Ищем телефоны (обычно в колонках после основных данных)
                        phones = []
                        emails = []
                        for j, cell in enumerate(row):
                            if cell and any(char.isdigit() for char in cell):
                                if '+7' in cell or cell.startswith('8') or len(cell.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')) >= 10:
                                    phones.append(cell)
                            elif '@' in cell and '.' in cell:
                                emails.append(cell)
                        
                        if phones:
                            print(f"Телефоны: {', '.join(phones[:3])}")  # Показать до 3 телефонов
                        else:
                            print("Телефоны: Не найдены")
                            
                        if emails:
                            print(f"Email: {', '.join(emails[:2])}")
                        else:
                            print("Email: Не найден")
                        
                        # Часы работы (обычно в колонке schedule или подобной)
                        schedule_idx = None
                        for idx, header in enumerate(headers):
                            if 'час' in header.lower() or 'работ' in header.lower() or 'schedule' in header.lower():
                                schedule_idx = idx
                                break
                        
                        if schedule_idx and len(row) > schedule_idx and row[schedule_idx]:
                            print(f"Часы работы: {row[schedule_idx]}")
                        else:
                            print("Часы работы: Не указаны")
                
                else:
                    print("\nНе найдено ни одной записи!")
                    print("Возможные причины:")
                    print("- Нет кафе в данном регионе")
                    print("- Проблемы с доступом к 2GIS") 
                    print("- Изменения в структуре сайта")
                
        else:
            print(f"\nОШИБКА: Файл результата '{output_file}' не создан!")
            
    except Exception as e:
        print(f"\nОШИБКА: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_shodnya_cafes_full_data()