# About

Задание Welcome уже не первый раз становится причиной наибольшего числа неверных сабмитов. Цель этого задания - познакомить игроков с разными разделами платформы, ну и заодно проверить внимательность)  
Для решения этого задания необходимо было найти несколько частей флага, спрятанных где-то в рамках портала CTFd и соединить их в логичном порядке.

# Description

> At the last event, we found out that the Welcome task is one of the most difficult! Let's find the flag on our platform again! Flag format: SCS_ZN2021{S000000m3 l33333t t333xt} <- it's not flag ;) Fox lost something here: 01d_ch3
> 
> There are 6 parts of the flag.

# Solution

Первая часть флага (которая по факту является четвертой) находится прямо в писании задания:  

![![Flag part 4](/Welcome/part4.png "Welcome, Part 4")](/Welcome/part4.png)  

Из описания можно сразу получить небольшой хинт, флаг будет связан с кем-то по имени Fox. Участник с ником SomeFox был частью задания.

Остальные части флага были расположены в коде различных страниц платформы:  
<code> SCS_ZN20 </code>  
![![Flag part 1](/Welcome/part1.png "Welcome, Part 1")](/Welcome/part1.png)  
<code> 21{S0m3t1 </code>  
![![Flag part 2](/Welcome/part2.png "Welcome, Part 2")](/Welcome/part2.png)  
<code> mes_Y0u_sh </code>  
![![Flag part 3](/Welcome/part3.png "Welcome, Part 3")](/Welcome/part3.png)  
<code> ck_c4r3f </code>  
![![Flag part 5](/Welcome/part5.png "Welcome, Part 5")](/Welcome/part5.png)  
<code> u11!} </code>  
![![Flag part 6](/Welcome/part6.png "Welcome, Part 6")](/Welcome/part6.png)  

Итого получаем флаг:  
Flag: <code> SCS_ZN2021{S0m3t1mes_Y0u_sh01d_ch3ck_c4r3fu11!} </code>
