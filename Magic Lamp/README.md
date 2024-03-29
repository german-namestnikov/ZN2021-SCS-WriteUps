# Magic Lamp

## About

Данное задание было одним из завершающих в цепочке лаб и осталось одним из нерешенных участниками.
Поэтому давайте остановимся на нем поподробнее. Задания Magic Lamp и Magic Socket - имитация IOT, умных лампы и розетки.

## Description

> Important! You will need initial access to Johan lab machine to solve this task!  
>
> Modern companies use modern devices! Even lamps and sockets are online nowadays! Can you hack into the development lab and find a vulnerability in The Very Secure IOT protocol?
> 
> Visit johan lab at verymoderndev.com:41222
> Internal address: smart-lamp.vmd.inc:40230  

Так же был приложен [файл с логами](/Magic%20Lamp/task_logs.txt) взаимодействия клиента с сервером.

## Solution

Для начала получим всю возможную информацию из лог-файла. Лог содержит 2 части:  
1. Запись работы клиента
2. Лог взаимодействия клиент-сервера

Строки начинающиеся с > означают запрос, < - соответственно, ответ.  
По логам понятно, что клиент управляет несколькими умными устройствами. Так же видно, что управление осуществляется двумя девайсами, а один не используется. 
Так что наша цель поуправлять третьей лампочкой из списка.  

Часть строк повторяется, часть нет, поэтому попробуем разбить каждую строчку на части:

![![logs_analysis](/Magic%20Lamp/01.check_logs.png, "Log analysis")](/Magic%20Lamp/01.check_logs.png)

Структура пакета следующая:  
1. какая-то константа, повторяющаяся для каждого запроса
2. номер устройства (device ID)
3. код команды, переданной устройству
4. какая-то переменная, увеличивающаяся для каждого устройства отдельно
5. какая-то переменная, отличающаяся для каждого пакета.  

Последняя переменная - sha256hash:  
![![hash.png](/Magic%20Lamp/hash.png, "Hashident")](/Magic%20Lamp/hash.png)

Таким образом, чтобы получить управление последней лампой, нам необходимо сформировать пакет вида:  
Неизвестная константа - 0003 - 001 - Значение счетчика - Какой-то хэш.

По структуре лог-файла понятно, что новое значение счётчика, ожидаемое сервером, передается в ответе, поэтому его можно легко получить повторив существующий запрос из логов:  
![![counters.png](/Magic%20Lamp/counters.png, "Counters")](/Magic%20Lamp/counters.png)

Таким образом, единственная часть, которую необходимо получить - последняя переменная. Поскольку её значение меняется каждый запрос, но не меняется при отправке одинаковых запросов (см. скриншот выше) можем предположить, что подпись генерируется на основе данных пакета. Нужно перебрать возможные варианты генерации подписи:
1. хэш каждого значения из исходного пакета;
2. хэш нескольких значений из исходного пакета;
3. хэш от суммы оригинального сообщения с одним из параметров;
4. хэш от суммы оригинального сообщения с хэшэм одного из параметров.

Поскольку у нас уже есть пример сообщения и его хэша, перебирать можем локально:  
![![sign_brute.png](/Magic%20Lamp/sign_brute.png, "Bruting sign")](/Magic%20Lamp/sign_brute.png)  

Таким образом получается, что для подписи сообщения (создания последней переменной) используется  
<code> sha256sum(Сообщение + sha256sum(ID устройства)) </code>

Создаем небольшой скрипт, генерирующий запросы к 3-му устройству с подписью и получаем флаг:   
![![flag.png](/Magic%20Lamp/flag.png, "Getting flag")](/Magic%20Lamp/flag.png)  

Flag: <code> SCS_ZN2021{N3ver_Us3_week_S3cr3t5!} </code>
