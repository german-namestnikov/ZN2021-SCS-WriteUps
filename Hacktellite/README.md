# Hacktellite

## Описание
> Important! You will need initial access to Alice lab machine to solve this task!
> 
> The attacker has found a suspicious image on one of the hosts. Can it be used for attack?
> 
> After you get the flag, use another one of your findings to access SSH: ssh -p41222 johan@verymoderndev.com

[WAV-файл](Hacktellite.wav)

## Решение
Задача сводилась к прямому декодированию звукового файла, содержащего в себе изображение, передаваемое в формате SSTV. На изображении можно было найти флаг, а также пароль, который можно было использовать в дальнейших активностях.

Для решения нужно было, во-первых, определить, что WAV-файл содержит именно SSTV -  и для многих участников уже этот этап создал значительные трудности. Специально для них мы подготовили хинт "May C.Macdonald and S.I.Kataev light your way!", содержащий имена разработчиков такого метода передачи изобоажений.

Во-вторых, как известно, SSTV также имеет несколько режимов работы, и участникам нужно было определить ту моду, которая применялась при кодировании изображения. Это довольно просто, учитывая, что многие средства декодирования SSTV также умеют в автоматическом режиме определять режим SSTV.

Третьим этапом решения являлось непосредственное декодирование изображения. При подготовке заданий для контеста нам удалось получить вменяемое качество при проигрывании звукового файла в микрофон Android-телефона с приложением Robot36, но при декодировании в зашумленном зале конференции, участники получали значительные искажения изображения при декодировании.


![Декодированное изображение](https://user-images.githubusercontent.com/22224745/131343825-8a4fa959-615c-4177-88d0-f353f5c0bf00.jpg)


Избежать таких искажений можно было, например, с помощью виртуального AUX-кабеля - этот способ отсеивает все шумы окружающего пространства и позволяет добиться максимального качества декодирования. 

Тем не менее, одним из самых оригинальных вариантов решения такой проблемы стал прямой перебор тех символов пароля и флага, которые были испорчены шумами - этот способ показал свою работоспособность как минимум в ходе одного из решений данного задания.