from docxtpl import DocxTemplate

# какая-то проверочная переменная из таблицы главного окна
operation = ...

if operation == "Продажа":

    # определяем словарь переменных контекста,
    # которые определены в шаблоне документа DOCX
    context_sale = {}
    context_sale['name_operation'] = 'Название транзакции'
    context_sale['date_operation'] = 'Дата транзакции'
    context_sale['summa_operation'] = 'Сумма транзакции'

    doc_sale = DocxTemplate("sale_tpl.docx")
    # подставляем контекст в шаблон
    doc_sale.render(context_sale)
    # сохраняем и смотрим, что получилось
    doc_sale.save("generated_sale_docx.docx")

elif operation == "Перемещение":

    # определяем словарь переменных контекста,
    # которые определены в шаблоне документа DOCX
    context_moving = {}
    context_moving['name_operation'] = 'Название транзакции'
    context_moving['date_operation'] = 'Дата транзакции'
    context_moving['summa_operation'] = 'Сумма транзакции'

    doc_moving = DocxTemplate("moving_tpl.docx")
    # подставляем контекст в шаблон
    doc_moving.render(context_moving)
    # сохраняем и смотрим, что получилось
    doc_moving.save("generated_moving_docx.docx")

elif operation == "Списание":

    # определяем словарь переменных контекста,
    # которые определены в шаблоне документа DOCX
    context_offs = {}
    context_offs['name_operation'] = 'Название транзакции'
    context_offs['date_operation'] = 'Дата транзакции'
    context_offs['summa_operation'] = 'Сумма транзакции'

    doc_offs = DocxTemplate("offs_tpl.docx")
    # подставляем контекст в шаблон
    doc_offs.render(context_offs)
    # сохраняем и смотрим, что получилось
    doc_offs.save("generated_offs_docx.docx")

elif operation == "Приемка":

    # определяем словарь переменных контекста,
    # которые определены в шаблоне документа DOCX
    context_acceptance = {}
    context_acceptance['name_operation'] = 'Название транзакции'
    context_acceptance['date_operation'] = 'Дата транзакции'
    context_acceptance['summa_operation'] = 'Сумма транзакции'

    doc_acceptance = DocxTemplate("acceptance_tpl.docx")
    # подставляем контекст в шаблон
    doc_acceptance.render(context_acceptance)
    # сохраняем и смотрим, что получилось
    doc_acceptance.save("generated_acceptance_docx.docx")

