# Лабораторная работа №3. Выделение контуров на изображении

Реализовано:
    - Выделение контуров оператором Шарра 3х3 с формулой градиента $`G = |G_x| + |G_y|`$

После применения алгоритма выделения контуров изображение бинаризуется в соответствии с заданным порогом (подбирается для каждого изображения экспериментально)

## Результаты работы

### Мультяшное изображение

![](../pictures_src/nyam.jpg)
Исходное изображение

![](../pictures_results/work_1/semitone/nyam_semitone.png)
Полутоновое изображение

![](../pictures_results/work_3/nyam_Sharr_Operator_x.png)
Градиент по X

![](../pictures_results/work_3/nyam_Sharr_Operator_y.png)
Градиент по Y

![](../pictures_results/work_3/nyam_Sharr_Operator_xy.png)
Общий градиент с выделенными контурами (бинаризация Отцу)

#### Вывод: для мультяшного изображения алгоритм работает хорошо, контуры прослеживаются чётко

### Векторное изображение

![](../pictures_src/japan.jpg)
Исходное изображение

![](../pictures_results/work_1/semitone/japan_semi.png)
Полутоновое изображение

![](../pictures_results/work_3/japan_Sharr_Operator_x.png)
Градиент по X

![](../pictures_results/work_3/japan_Sharr_Operator_y.png)
Градиент по Y

![](../pictures_results/work_3/japan_Sharr_Operator_xy.png)
Общий градиент с выделенными контурами (бинаризация Отцу)

#### Вывод: для векторного изображения алгоритм работает хорошо, контуры прослеживаются чётко

### Фотография

![](../pictures_src/nando.jpg)
Исходное изображение

![](../pictures_results/work_1/semitone/nando_semitone.png)
Полутоновое изображение

![](../pictures_results/work_3/nando_Sharr_Operator_x.png)
Градиент по X

![](../pictures_results/work_3/nando_Sharr_Operator_y.png)
Градиент по Y

![](../pictures_results/work_3/nando_Sharr_Operator_xy.png)
Общий градиент с выделенными контурами (бинаризация Отцу)

#### Вывод: для фотографий такой фильтр работает не сильно хорошо, однако он удаляет лишний шум, прослеживаются главные очертания портрета

### Рукописный текст

![](../pictures_src/integral.jpg)
Исходное изображение

![](../pictures_results/work_1/semitone/integral_semitone.png)
Полутоновое изображение

![](../pictures_results/work_3/integral_Sharr_Operator_x.png)
Градиент по X

![](../pictures_results/work_3/integral_Sharr_Operator_y.png)
Градиент по Y

![](../pictures_results/work_3/integral_Sharr_Operator_xy.png)
Общий градиент с выделенными контурами (бинаризация Отцу)

#### Вывод: для рукописного текста такой фильтр работает не сильно хорошо, но общие очертания объектов выделяются

## Выводы
Алгоритм выделения контуров оператором Шарра хорошо себя показывает для векторных и мультяшных изображений, но не очень хорошо работает для фотографий с изображениями людей и рукописным текстом

