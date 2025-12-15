<div align="center">
<h1><a id="intro">Лабораторная работа №1</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Давыдов Е.А.-8b9aff" alt="Contributor Badge"></a></div>


1. Создайте локальный репозиторий на машине
2. Проинициализируйте репозиторий
![alt text](img/1-1.png)

3. Авторизуйтесь и спользуйте `GitHub CLI` для создания удаленного репозитория
![alt text](img/1-2.png)

Репозиторий: https://github.com/Butters7/riski_lab1

4. Создайте пустой README.md 
```bash
touch README.md
```

5. Используйте указание URL своего созданного репозитория для присвоения ветки`master` статуса `origin`
```bash
git remote add origin git@github.com:Butters7/riski_lab1.git
```

6. В локальном репозитории и сделайте `commit`
```bash
git add README.md
git commit -S -m "first commit"
```
ID коммита: e78f054  
![alt text](img/1-3.png)

7. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий
```bash
git push -u origin master
```
![alt text](img/1-4.png)

8. Создайте файл `hello.py` в локальном репозитории. Реализуйте **Hello appsecworld** на языке python используя несколько интерпретаторов с "грязным" кодом
![alt text](img/1-5.png)

9. Сделайте `commit` с флагом `-S`  
![alt text](img/1-6.png)
ID коммита: d511453

10. Измените исходный код, что бы скрипт запрашивал имя пользователя и выводил `Helloappsec world from @name`
![alt text](img/1-7.png)

11. Сделайте `commit` с флагом `-S` и сделайте публикацию в удаленный репозиторий.Проверьте вывод истории изменений  
ID коммита: d8e1111  
![alt text](img/1-8.png)

12. В локальном репозитории создайте ветку `patch1` и внесите изменения исправлению кода и модернизации до следующего вида, что бы код был рабочим. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий:
```bash
git checkout -b patch1
```
![alt text](img/1-9.png)
ID коммита: bab4b50

13. Проверьте, что ветка `patch1` в удалённом репозитории
![alt text](img/1-10.png)

14. Создайте `pull-request` в виде `patch1 -> master`
![alt text](img/1-11.png)

15. В ветке `patch1` добавьте в исходный код комментарии и убедитесь, что есть указанные изменения в `pull-request`  
ID коммита: 741776e
![alt text](img/1-12.png)
![alt text](img/1-13.png)

16. В удалённый репозитории выполните слияние `pull-request` для `patch1 -> master` и удалите ветку `patch1`
ID коммита: cbd576d
![alt text](img/1-14.png)

17. Стяните последние актуальные изменения и просмотрите историю изменений для `master`
![alt text](img/1-15.png)
![alt text](img/1-16.png)

18. Удалите локальную ветку `patch1`
```bash
git branch -d patch1
```

19. Создайте новую локальную ветку `patch2`.
```bash
git checkout -b patch2
```

20. Измените *code style* по своему усмотрению
![alt text](img/1-17.png)

21. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий исоздайте pull-request `patch2 -> master`  
ID коммита: 8952d54

22. В ветке **master** удаленного репозитория явно измените комментарий  
ID коммита: 47ffd57

23. Увидите, что в `pull-request` появились расхождения
![alt text](img/1-18.png)

24. Локально сделайте **rebase** и исправьте расхождения (это называется **конфликт**)
![alt text](img/1-19.png)
![alt text](img/1-20.png)

25. Сделайте `commit` и опубликуйте изменения в ветке `patch2`
ID коммита: 06d4011

26. Убедитесь, что пропали конфликтны. 
![alt text](img/1-21.png)

27. Сделайте `merge` для `pull-request` `patch2 -> master`.  
ID коммита: 5a9cd24
![alt text](img/1-22.png)

28. Подготовьте отчет `gist`.

29. Продемонстрируйте в материалах отчета историю коммитов на локальном и удаленном репозитории.
**Локально:**
![alt text](img/1-23.png)

**Удаленно:**
![alt text](img/1-24.png)

---
Copyright (c) 2025 Egor Davydov