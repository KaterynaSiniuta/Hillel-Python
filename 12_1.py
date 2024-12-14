import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    """
    Читає HTML-файл, видаляє HTML-теги та записує очищений текст у новий файл.
    :param html_file: Ім'я вхідного файлу з HTML-текстом.
    :param result_file: Ім'я файлу для запису очищеного тексту.
    """
    try:
        # Читання вхідного файлу
        with codecs.open(html_file, 'r', 'utf-8') as file:
            html_content = file.read()

        # Видалення HTML-тегів
        cleaned_content = re.sub(r'<[^>]*>', '', html_content)

        # Видалення зайвих порожніх рядків
        cleaned_lines = [line.strip() for line in cleaned_content.splitlines() if line.strip()]
        cleaned_text = '\n'.join(cleaned_lines)

        # Запис очищеного тексту у файл
        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(cleaned_text)

        print(f"Очищений текст успішно записаний у файл '{result_file}'.")

    except FileNotFoundError:
        print(f"Помилка: Файл '{html_file}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

# Виклик функції для прикладу
delete_html_tags('draft.html', 'cleaned.txt')
