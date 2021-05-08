# Лабораторная работа №5. Сегментация текста

Лабораторная работа выполнена для:
    - Алфавит - казахский
    - Тип букв - заглавные
    - Шрифт - Times New Roman
    - Размер шрифта - 40-52

## Сегментация символов

### Исходное изображение

![imgOriginal](../pictures_results/work_5/1_inverted.png)

### Выделенные символы в строке

![imgOut](../pictures_results/work_5/symbols/1.png) ![imgOut](../pictures_results/work_5/symbols/2.png) ![imgOut](../pictures_results/work_5/symbols/3.png) ![imgOut](../pictures_results/work_5/symbols/4.png) ![imgOut](../pictures_results/work_5/symbols/5.png) ![imgOut](../pictures_results/work_5/symbols/6.png) ![imgOut](../pictures_results/work_5/symbols/7.png) ![imgOut](../pictures_results/work_5/symbols/8.png) ![imgOut](../pictures_results/work_5/symbols/9.png) ![imgOut](../pictures_results/work_5/symbols/10.png) ![imgOut](../pictures_results/work_5/symbols/11.png) ![imgOut](../pictures_results/work_5/symbols/12.png) ![imgOut](../pictures_results/work_5/symbols/13.png) ![imgOut](../pictures_results/work_5/symbols/14.png) ![imgOut](../pictures_results/work_5/symbols/15.png) ![imgOut](../pictures_results/work_5/symbols/16.png) ![imgOut](../pictures_results/work_5/symbols/17.png) ![imgOut](../pictures_results/work_5/symbols/18.png) ![imgOut](../pictures_results/work_5/symbols/19.png) ![imgOut](../pictures_results/work_5/symbols/20.png) ![imgOut](../pictures_results/work_5/symbols/21.png) ![imgOut](../pictures_results/work_5/symbols/22.png) ![imgOut](../pictures_results/work_5/symbols/23.png) ![imgOut](../pictures_results/work_5/symbols/24.png) ![imgOut](../pictures_results/work_5/symbols/25.png) ![imgOut](../pictures_results/work_5/symbols/26.png) ![imgOut](../pictures_results/work_5/symbols/27.png) ![imgOut](../pictures_results/work_5/symbols/28.png) ![imgOut](../pictures_results/work_5/symbols/29.png) ![imgOut](../pictures_results/work_5/symbols/30.png) ![imgOut](../pictures_results/work_5/symbols/31.png) ![imgOut](../pictures_results/work_5/symbols/32.png) ![imgOut](../pictures_results/work_5/symbols/33.png) ![imgOut](../pictures_results/work_5/symbols/34.png)

### Анализ

Можно заметить, что алгоритм не может нормально сегментировать такую букву, как Ы. Это связано с тем, что невозможно без какой-то эвристики определить, стоит между буквами пробел или нормальное расстояние. В связи с этим, данную проблему нужно будет решать уже при распознавании символов.

## Сегментация текстовой области

### Исходное изображение

![imgOriginal](../pictures_results/work_5/2_inverted.png)

### Сегментированное изображение

![imgOut](../pictures_results/work_5/2_cutted.png)

### Анализ

Алгоритм сегментации текстовой области выделяет текст на основе профилей, в связи с чем может появиться ненатурально "высокая" область, так как в профили будут попадать маленькие части текста, по типу верхушки буквы Й.
