# Лабораторная работа №2. Фильтрация изображений и морфологические операции

Реализован ранговый фильтр с возможностью выбора окна и порога

## Результаты

### Портрет

#### Исходное изображение
![](../pictures_src/nando_binary.png)

#### 1/9

![](../pictures_results/work_2/nando/1_of_9.png)

#### 2/9

![](../pictures_results/work_2/nando/2_of_9.png)

#### 3/9

![](../pictures_results/work_2/nando/3_of_9.png)

#### 4/9

![](../pictures_results/work_2/nando/4_of_9.png)

#### 5/9

![](../pictures_results/work_2/nando/5_of_9.png)

#### 6/9

![](../pictures_results/work_2/nando/6_of_9.png)

#### 7/9

![](../pictures_results/work_2/nando/7_of_9.png)

#### 8/9

![](../pictures_results/work_2/nando/8_of_9.png)

#### 9/9

![](../pictures_results/work_2/nando/9_of_9.png)

### Фотография рукописного текста

#### Исходное изображение
![](../pictures_src/integral_binary.png)

#### 1/9

![](../pictures_results/work_2/integral/1_of_9.png)

#### 2/9

![](../pictures_results/work_2/integral/2_of_9.png)

#### 3/9

![](../pictures_results/work_2/integral/3_of_9.png)

#### 4/9

![](../pictures_results/work_2/integral/4_of_9.png)

#### 5/9

![](../pictures_results/work_2/integral/5_of_9.png)

#### 6/9

![](../pictures_results/work_2/integral/6_of_9.png)

#### 7/9

![](../pictures_results/work_2/integral/7_of_9.png)

#### 8/9

![](../pictures_results/work_2/integral/8_of_9.png)

#### 9/9

![](../pictures_results/work_2/integral/9_of_9.png)

### Фотография печатного текста

#### Исходное изображение
![](../pictures_src/text_binary.png)

#### 1/9

![](../pictures_results/work_2/text/1_of_9.png)

#### 2/9

![](../pictures_results/work_2/text/2_of_9.png)

#### 3/9

![](../pictures_results/work_2/text/3_of_9.png)

#### 4/9

![](../pictures_results/work_2/text/4_of_9.png)

#### 5/9

![](../pictures_results/work_2/text/5_of_9.png)

#### 6/9

![](../pictures_results/work_2/text/6_of_9.png)

#### 7/9

![](../pictures_results/work_2/text/7_of_9.png)

#### 8/9

![](../pictures_results/work_2/text/8_of_9.png)

#### 9/9

![](../pictures_results/work_2/text/9_of_9.png)

### Вывод
Наилучший результат получается для значений ранга 2 и 3.
В целом, фильтр неплохо справляется с "крупным" шумом, не очень хорошо справляется с "мелким" шумом.
При маленьких значениях происходит высветление исходного изображения, потеря яркости и деталей вместе с шумом.
При больших значениях фильтр начинает создавать дополнительные шумовые вставки, лишь ухудшая исходное изображение.