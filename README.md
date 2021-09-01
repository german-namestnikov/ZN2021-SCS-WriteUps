# ZN2021-SCS-WriteUps
Спасибо большое всем, кто участвовал в нашем ивенте на ZeroNights 2021!
Благодаря вам событие получилось действительно интересным и захватывающим!  

По просьбе участников публикуем райтапы к заданиям нашего ивента. Большая часть заданий была решена в ходе контеста, но не все :)

# О мероприятии

Игровая инфраструктура нашего контеста представляла собой небольшую лабу вымышленной компании Very Modern Development. Поскольку компания небольшая, серьезной защиты там не было - это снижало порог входа, а также позволяло балансировать между а
Структура лабы подразумевала, что для решения очередного таска необходимо получить доступ к той или иной её части. Всего было 2 крупных узла:  
- хост пользователя Alice;  
- хост пользователя Johan;  

В общем виде структура была следующей:

[![LabStruct](/LabStruct.png "Lab struct")](https://github.com/z0ok/ZN2021-SCS-WriteUps/blob/z0ok_parts/LabStruct.png)  

На файловых системах виртуальных машин располагались подсказки и файлы с заданиями. Для некоторых заданий виртуальные машины обеспечивали связность с внутренними сервисами.
