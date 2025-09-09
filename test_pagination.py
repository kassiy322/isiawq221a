#!/usr/bin/env python3
"""Тест парсера 2GIS с пагинацией - несколько страниц."""

import sys
import os
import csv

# Добавляем путь к модулю
sys.path.insert(0, os.path.dirname(__file__))

def test_pagination():
    """Тестируем парсер с пагинацией на нескольких страницах."""
    try:
        # Импортируем после добавления пути
        from parser_2gis import main as parser_main
        
        # URL для кафе в регионе с большим количеством результатов
        search_url = "https://2gis.ru/khimki/search/кафе"
        
        # Настраиваем аргументы для тестирования пагинации
        sys.argv = [
            'test_pagination.py',
            '-i', search_url,
            '-o', 'pagination_test.csv',
            '-f', 'csv',
            '--parser.max-records', '50',  # УВЕЛИЧИВАЕМ лимит для пагинации
            '--chrome.headless', 'no',     # Видимый браузер
            '--chrome.start-maximized', 'yes',
            '--parser.delay_between_clicks', '1500',  # 1.5 сек задержка
            '--writer.csv.add-rubrics', 'yes',
            '--writer.csv.add-comments', 'yes',
            '--writer.csv.columns-per-entity', '3',
            '--writer.verbose', 'yes',
        ]
        
        print(f"🔍 ТЕСТ ПАГИНАЦИИ для: {search_url}")
        print("Настройки:")
        print("- 50 записей максимум (для захвата нескольких страниц)")
        print("- Видимый браузер")
        print("- Задержка 1.5 сек между кликами")
        print("- Подробный вывод")
        print("\n⚠️  ВНИМАНИЕ: НЕ ЗАКРЫВАЙТЕ браузер!")
        print("📄 Ожидаем переход по нескольким страницам...\n")
        
        parser_main()
        print("\n✅ Парсер завершил работу.")
        
        # Анализируем результат пагинации
        output_file = 'pagination_test.csv'
        if os.path.exists(output_file):
            print(f"\n{'='*70}")
            print("📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ ПАГИНАЦИИ")
            print(f"{'='*70}")
            
            with open(output_file, 'r', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                headers = next(reader)
                rows = list(reader)
                
                total_records = len(rows)
                print(f"📈 Всего записей: {total_records}")
                
                if total_records >= 20:  # На одной странице обычно ~10-15 записей
                    print("✅ ПАГИНАЦИЯ РАБОТАЕТ! Собрано записей с нескольких страниц.")
                elif total_records >= 10:
                    print("⚠️  Возможно пагинация работает частично.")
                    print("   Проверьте логи на наличие сообщений о переходах между страницами.")
                else:
                    print("❌ ПАГИНАЦИЯ НЕ РАБОТАЕТ. Мало записей.")
                
                # Показываем найденные заведения
                print(f"\n📋 НАЙДЕННЫЕ ЗАВЕДЕНИЯ ({min(10, total_records)} из {total_records}):")
                for i, row in enumerate(rows[:10], 1):
                    name = row[0] if len(row) > 0 and row[0] else "Название не указано"
                    address = row[3] if len(row) > 3 and row[3] else "Адрес не указан"
                    print(f"{i:2d}. {name} - {address}")
                
                if total_records > 10:
                    print(f"    ... и еще {total_records - 10} записей")
                
                # Проверяем уникальность записей (дубликаты могут указывать на проблемы пагинации)
                names = [row[0] for row in rows if len(row) > 0 and row[0]]
                unique_names = set(names)
                duplicates = total_records - len(unique_names)
                
                if duplicates > 0:
                    print(f"\n⚠️  Найдено {duplicates} дубликатов - возможны проблемы с пагинацией")
                else:
                    print(f"\n✅ Дубликатов не найдено - пагинация работает корректно")
                
        else:
            print(f"\n❌ ОШИБКА: Файл '{output_file}' не создан!")
            
    except Exception as e:
        print(f"\n💥 ОШИБКА: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_pagination()