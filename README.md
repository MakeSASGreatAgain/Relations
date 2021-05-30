# Relations
Решение задания "Взаимосвязи"

Скрипт `script1.py` парсит xml файл в виде вложенных друг в друга словарей (для реализации этого мы решили использовать библиотеку `xmltodict`).
Из полученной структуры несложно затем вытащить зависимости и их проанализировать.
Для их визуализации мы решили использовать `graphviz` со следующими условными обозначениями:

* Шестигранники - компании
* Круги - процессы
* Квадраты - данные из БД

Решение выполнять все на `python` было связано с доступностью всех интересующих нас библиотек, что в целом позволило немного сократить объем работы.