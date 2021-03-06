# What is this mushroom?
<img src="./static_images/muhomor.jpg" width="600"/>

## Аннотация
Проект состоит из нескольких реализованных модулей, которые формируют сервис для определения видов грибов по фотографии.

## Сбор данных
Для обучения модели был собран датасет изображений. Были взяты самые распространенные в Центральной России виды грибов. 
На данный момент выделено 7 категорий. Датасет собирался с сайта https://na-dache.pro/griby/. Для парсинга данных с сайта использовалась программа, написанная на основе библиотеки 'Beautifulsoup'.  Таким образом, для каждого из классов было собрано 50-60 фотографий.
В итоге получился датасет, содержащий ~300 изображений.

## Препроцессинг
1. На первом этапе надо было привести снимки к одинаковому квадратному виду размера 128x128. Именно такое разрешение оптимально для нейросети convnext_base, из которой осуществлялся transfer learning для обучения нейросети.
2. На завершающем этапе препроцессинга выполнялась небольшая аугументация изображений, для того чтобы нейросеть не начинала быстро переобучаться.

## Обучение
Для достижения цели классификации различных видов грибов я использовал transfer learning из нейросети convnext_base,  показавшей на датасете ImageNet один из лучших результатов среди всех моделей, доступных в библиотеке Pytorch.
Я заменил последние слои на новые, с помощью которых модель могла бы делать предсказания всех классов.
Первоначально обучал нейросеть, заморозив основную часть, кроме нескольких последних слоев. 
Основная метрика результатов обучения была accuracy.
По итогам обучения на валидационной выборке модель достигла точности 100%.

## Имплементация в telegram бота
Для реализации проекта в сервис telegram была использована библиотека aiogram.

#### Структура бота:

##### main.py
Основной модуль, где реализованы обработчики сообщений: стартовое сообщение, проверка на необходимый тип медиа вложения — фотография, сохранение входной фотографии, после подготовленная фотография приходит на вход в модель и производится вывод результатов предсказания модели. 

##### function.py
Здесь происходит настройка среды и загрузка предобученной модели. Фотография после препроцессинга попадает в модель. Далее происходит декодирование результатов предсказания. 

### Заключение

По результатам проекта построена модель со 100% точностью предсказания (количество определяемых классов 7).

Проект находится в статусе постоянной доработки:
1. расширяется объём и разнобразие датасета
2. дорабатывается структура чат-бота

### Данные
Чекпоинт модели и датасет для обучения доступны по [ссылке](https://drive.google.com/drive/folders/13D6WcPJWHl8h1GIzyLXNPwZbeXLqWriK?usp=sharing)
