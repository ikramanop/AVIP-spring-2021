# Лабораторная работа №6. Классификация на основе признаков, анализ профилей

Лабораторная работа выполнена для:
    - Алфавит - казахский
    - Тип букв - заглавные
    - Шрифт - Times New Roman
    - Размер шрифта - 52

## Распознавание символов того же шрифта

### Исходное изображение

![imgOriginal](../pictures_results/work_5/1_inverted.png)

### Классификация символов на основе известных признаков

Выводятся лучшие гипотезы

1: 'А' - 1.0
2: 'Ғ' - 1.0
3: 'А' - 1.0
4: 'Й' - 1.0
5: 'Ь' - 0.9848854626021432
6: 'І' - 0.9765109639987718
7: 'Н' - 1.0
8: 'М' - 1.0
9: 'Е' - 1.0
10: 'Н' - 1.0
11: 'А' - 1.0
12: 'Л' - 1.0
13: 'Ь' - 0.9848854626021432
14: 'І' - 0.9765109639987718
15: 'С' - 1.0
16: 'Т' - 1.0
17: 'А' - 1.0
18: 'Н' - 1.0
19: 'С' - 1.0
20: 'Ь' - 0.9848854626021432
21: 'І' - 0.9765109639987718
22: 'Й' - 1.0
23: 'Л' - 1.0
24: 'А' - 1.0
25: 'С' - 1.0
26: 'Қ' - 0.9649852498539185
27: 'А' - 1.0
28: 'Н' - 1.0
29: 'Ж' - 1.0
30: 'А' - 1.0
31: 'Қ' - 0.9649852498539185
32: 'С' - 1.0
33: 'Ь' - 0.9848854626021432
34: 'І' - 0.9765109639987718

Получается строка (часть символов склеивается):  
А Ғ А Й Ы Н М Е Н А Л Ы С Т А Н С Ы Й Л А С Қ А Н Ж А Қ С Ы

### Анализ

Для символов того же шрифта алгоритм классификации работает хорошо, проблемы возникают только с символами вроде "Ы", которые, из-за особенностей сегментации, классифицируются как два разных символа. С этим можно бороться программно.

## Распознавание символов шрифта меньшего размера

### Исходное изображение

![imgOriginal](../pictures_results/work_5/2_inverted.png)

### Классификация символов на основе известных признаков (для шрифта большего размера)

Выводятся лучшие гипотезы

1: А - 0.8918967942000071
2: Ө - 0.69463640621348
3: Р - 0.9675617892284322
4: У - 0.9561747522754305
5: У - 0.8409792631343338
6: С - 0.8967129951578209
7: Ә - 0.7975843233552832
8: У - 0.9382380278690552
9: С - 0.8967129951578209
10: А - 0.8918967942000071
11: У - 0.9784274258373928
12: У - 0.9561747522754305
13: У - 0.8409792631343338
14: А - 0.9531471822533052
15: У - 0.8842642039664257
16: А - 0.8918967942000071
17: С - 0.8967129951578209
18: А - 0.9531471822533052
19: У - 0.9561747522754305
20: У - 0.8409792631343338
21: Р - 0.9675617892284322
22: У - 0.9784274258373928
23: А - 0.8918967942000071
24: А - 0.9531471822533052
25: Ө - 0.6982616985805089
26: С - 0.8967129951578209
27: Ч - 0.8912969315059714
28: А - 0.8918967942000071
29: У - 0.9526985178431207
30: А - 0.9531471822533052
31: У - 0.9561747522754305
32: У - 0.8409792631343338

Получается строка=:
А Ө Р У У С Ә У С А У У У А У А С А У У Р У А А Ө С Ч А У А У У

### Анализ

Для строки меньшего шрифта данный способ классификации вообще не подходит.
