from docxtpl import DocxTemplate
import os


#
# # какая-то проверочная переменная из таблицы главного окна
# operation = ...
#
# if operation == "Продажа":
#
#     # определяем словарь переменных контекста,
#     # которые определены в шаблоне документа DOCX
#     context_sale = {}
#     context_sale['name_operation'] = 'Название транзакции'
#     context_sale['date_operation'] = 'Дата транзакции'
#     context_sale['summa_operation'] = 'Сумма транзакции'
#
#     doc_sale = DocxTemplate("sale_tpl.docx")
#     # подставляем контекст в шаблон
#     doc_sale.render(context_sale)
#     # сохраняем и смотрим, что получилось
#     doc_sale.save("generated_sale_docx.docx")
#
# elif operation == "Перемещение":
#
#     # определяем словарь переменных контекста,
#     # которые определены в шаблоне документа DOCX
#     context_moving = {}
#     context_moving['name_operation'] = 'Название транзакции'
#     context_moving['date_operation'] = 'Дата транзакции'
#     context_moving['summa_operation'] = 'Сумма транзакции'
#
#     doc_moving = DocxTemplate("moving_tpl.docx")
#     # подставляем контекст в шаблон
#     doc_moving.render(context_moving)
#     # сохраняем и смотрим, что получилось
#     doc_moving.save("generated_moving_docx.docx")
#
# elif operation == "Списание":
#
#     # определяем словарь переменных контекста,
#     # которые определены в шаблоне документа DOCX
#     context_offs = {}
#     context_offs['name_operation'] = 'Название транзакции'
#     context_offs['date_operation'] = 'Дата транзакции'
#     context_offs['summa_operation'] = 'Сумма транзакции'
#
#     doc_offs = DocxTemplate("offs_tpl.docx")
#     # подставляем контекст в шаблон
#     doc_offs.render(context_offs)
#     # сохраняем и смотрим, что получилось
#     doc_offs.save("generated_offs_docx.docx")
#
# elif operation == "Приемка":
#
#     # определяем словарь переменных контекста,
#     # которые определены в шаблоне документа DOCX
#     context_acceptance = {}
#     context_acceptance['name_operation'] = 'Название транзакции'
#     context_acceptance['date_operation'] = 'Дата транзакции'
#     context_acceptance['summa_operation'] = 'Сумма транзакции'
#
#     doc_acceptance = DocxTemplate("acceptance_tpl.docx")
#     # подставляем контекст в шаблон
#     doc_acceptance.render(context_acceptance)
#     # сохраняем и смотрим, что получилось
#     doc_acceptance.save("generated_acceptance_docx.docx")


def generate_document(operation):
    # определяем словарь переменных контекста, которые определены в шаблоне документа DOCX
    context = {
        'name_operation': 'Название транзакции',  # Переменная для имени операции
        'date_operation': 'Дата транзакции',  # Переменная для даты операции
        'summa_operation': 'Сумма транзакции'  # Переменная для суммы операции
    }

    # Словарь, который сопоставляет операции с соответствующими шаблонными файлами DOCX
    template_files = {
        "Продажа": "sale_tpl.docx",  # Шаблон для операции
        "Перемещение": "moving_tpl.docx",
        "Списание": "offs_tpl.docx",
        "Приемка": "acceptance_tpl.docx"
    }

    # Словарь, который сопоставляет операции с соответствующими выходными файлами DOCX
    output_files = {
        "Продажа": "generated_sale_docx.docx",  # Выходной файл для операции
        "Перемещение": "generated_moving_docx.docx",
        "Списание": "generated_offs_docx.docx",
        "Приемка": "generated_acceptance_docx.docx"
    }

    # Проверяем, существует ли переданная операция в словаре шаблонных файлов
    if operation in template_files:
        # Создаем объект DocxTemplate с соответствующим шаблонным файлом
        doc = DocxTemplate(template_files[operation])
        # Подставляем контекст в шаблон
        doc.render(context)
        # Сохраняем заполненный шаблон в соответствующий выходной файл
        output_file = output_files[operation]
        doc.save(output_file)
        print(f"Документ {output_file} и сохранен.")

        # Открываем созданный файл автоматически
        if os.name == 'nt':  # Если ОС Windows
            os.startfile(output_file)
        # elif os.name == 'posix':  # Если ОС Linux или MacOS
        #     os.system(f'open "{output_file}"')
        else:
            raise OSError(f"Unsupported operating system: {os.name}")
    else:
        # Выбрасываем ошибку, если операция не поддерживается
        raise ValueError(f"Unsupported operation: {operation}")


# Пример использования:
generate_document("Продажа")
