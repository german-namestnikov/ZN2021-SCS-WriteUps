# About  

Задание InsecureDE - одно из стартовых в нашем соревновании. Несложный веб, который по результату решения давал доступ к виртуальной машине Alice.

# Description

> Web IDE is a usefull and easy-to-setup tool for developers. Every modern company should use it. Or not?
>
> You (attacker) got password from phishing. Let's find out, if you can get in? IP: verymoderndev.com:40110 Creds: alice:mnvPaEiCWQrsu7g
>
> After you get the flag, use another one of your findings to access SSH: ssh -p40122 alice@verymoderndev.com


# Solution

По указанному даресу игроков ждала платформа облачной IDE [Codiad](http://codiad.com/). 

По первому же запросу в гугле легко находится [RCE exploit](https://www.exploit-db.com/exploits/49705) для данной версии.
Если запустить данный эксплоит в лоб - сплоит не отработает. Из подсказок в веб-интерфейсе IDE можно сделать вывод о том, что bash, захардкоженный в эксплоит, просто отсутствует в системе. Меняем bash на sh и легко получаем флаг.



Flag: SCS_ZN2021{Alw4ys_P4tch_y0ur_1DE!}
