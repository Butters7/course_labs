<div align="center">
<h1><a id="intro">Лабораторная работа №7</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Давыдов Е.А.-8b9aff" alt="Contributor Badge"></a></div>

[x] 1. Разверните и подготовьте окружение для уязвимого приложения

```bash
bttrs@bttrs:~/Riski/course_labs/labs/lab07$ python3 -m venv venv
bttrs@bttrs:~/Riski/course_labs/labs/lab07$ source venv/bin/activate
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07$ pip install -r vulnerable-app/requirements.txt
Collecting Flask==2.0.1
  Using cached Flask-2.0.1-py3-none-any.whl (94 kB)
Collecting Werkzeug==2.0.3
  Using cached Werkzeug-2.0.3-py3-none-any.whl (289 kB)
Collecting Jinja2==3.0.1
  Using cached Jinja2-3.0.1-py3-none-any.whl (133 kB)
Collecting itsdangerous==2.0.1
  Using cached itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting click==8.0.1
  Using cached click-8.0.1-py3-none-any.whl (97 kB)
Collecting gunicorn==20.1.0
  Using cached gunicorn-20.1.0-py3-none-any.whl (79 kB)
Collecting SQLAlchemy==1.3.23
  Using cached SQLAlchemy-1.3.23.tar.gz (6.3 MB)
  Preparing metadata (setup.py) ... done
Collecting requests==2.19.1
  Using cached requests-2.19.1-py2.py3-none-any.whl (91 kB)
Collecting PyYAML==5.3.1
  Using cached PyYAML-5.3.1.tar.gz (269 kB)
  Preparing metadata (setup.py) ... done
Collecting pyjwt==1.7.1
  Using cached PyJWT-1.7.1-py2.py3-none-any.whl (18 kB)
Collecting cryptography==3.2
  Using cached cryptography-3.2-cp35-abi3-manylinux2010_x86_64.whl (2.6 MB)
Collecting MarkupSafe==2.0.1
  Using cached MarkupSafe-2.0.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (30 kB)
Collecting six==1.15.0
  Using cached six-1.15.0-py2.py3-none-any.whl (10 kB)
Collecting urllib3==1.23
  Using cached urllib3-1.23-py2.py3-none-any.whl (133 kB)
Collecting chardet==3.0.4
  Using cached chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna==2.7
  Using cached idna-2.7-py2.py3-none-any.whl (58 kB)
Collecting certifi==2018.4.16
  Using cached certifi-2018.4.16-py2.py3-none-any.whl (150 kB)
Collecting Django==2.2.0
  Using cached Django-2.2-py3-none-any.whl (7.4 MB)
Collecting paramiko==2.4.1
  Using cached paramiko-2.4.1-py2.py3-none-any.whl (194 kB)
Requirement already satisfied: setuptools>=3.0 in ./venv/lib/python3.10/site-packages (from gunicorn==20.1.0->-r vulnerable-app/requirements.txt (line 6)) (59.6.0)
Collecting cffi!=1.11.3,>=1.8
  Using cached cffi-2.0.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (216 kB)
Collecting sqlparse
  Using cached sqlparse-0.5.5-py3-none-any.whl (46 kB)
Collecting pytz
  Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Collecting pyasn1>=0.1.7
  Using cached pyasn1-0.6.1-py3-none-any.whl (83 kB)
Collecting bcrypt>=3.1.3
  Using cached bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
Collecting pynacl>=1.0.1
  Downloading pynacl-1.6.2-cp38-abi3-manylinux_2_34_x86_64.whl (1.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 2.0 MB/s eta 0:00:00
Collecting pycparser
  Using cached pycparser-2.23-py3-none-any.whl (118 kB)
Using legacy 'setup.py install' for SQLAlchemy, since package 'wheel' is not installed.
Using legacy 'setup.py install' for PyYAML, since package 'wheel' is not installed.
Installing collected packages: pytz, pyjwt, idna, chardet, certifi, Werkzeug, urllib3, sqlparse, SQLAlchemy, six, PyYAML, pycparser, pyasn1, MarkupSafe, itsdangerous, gunicorn, click, bcrypt, requests, Jinja2, Django, cffi, pynacl, Flask, cryptography, paramiko
  Running setup.py install for SQLAlchemy ... done
  Running setup.py install for PyYAML ... done
Successfully installed Django-2.2 Flask-2.0.1 Jinja2-3.0.1 MarkupSafe-2.0.1 PyYAML-5.3.1 SQLAlchemy-1.3.23 Werkzeug-2.0.3 bcrypt-5.0.0 certifi-2018.4.16 cffi-2.0.0 chardet-3.0.4 click-8.0.1 cryptography-3.2 gunicorn-20.1.0 idna-2.7 itsdangerous-2.0.1 paramiko-2.4.1 pyasn1-0.6.1 pycparser-2.23 pyjwt-1.7.1 pynacl-1.6.2 pytz-2025.2 requests-2.19.1 six-1.15.0 sqlparse-0.5.5 urllib3-1.23
```

[x] 2. Запустите уязвимое приложение

```bash
[+] up 3/3
 ✔ Image lab07-vulnerable-app       Built                                                                                                                                                                                  241.2s 
 ✔ Network lab07_default            Created                                                                                                                                                                                  0.3s 
 ✔ Container lab07-vulnerable-app-1 Created
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07$ curl http://localhost:8080
Vulnerable lab07 app v1.0(venv)
```

[x] 3. Запустите SAST Semgrep и проанализируйте выведенный лог в консоли и опишите логику правил для semgrep-rules.yml исходя из паттернов, которые используются. Отчет будет в директории SAST

```bash
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07$ semgrep --config sast/semgrep-rules.yml \
  --json \
  --output sast/semgrep-report.json \
  vulnerable-app/

┌──── ○○○ ────┐
│ Semgrep CLI │
└─────────────┘

Rule sast.py-sql-injection-critical contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-sql-injection-critical and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-os-system-rce contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-os-system-rce and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-subprocess-rce contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-subprocess-rce and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-arbitrary-file-read contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-arbitrary-file-read and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-unsafe-pickle-deserialization contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-unsafe-pickle-deserialization and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-reflected-xss contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-reflected-xss and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-hardcoded-db-credentials contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-hardcoded-db-credentials and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-eval-user-input contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-eval-user-input and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.yaml-hardcoded-secrets-config contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-hardcoded-secrets-config and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.py-debug-mode-enabled contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-debug-mode-enabled and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-verbose-logging-sensitive contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-verbose-logging-sensitive and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-info-version-disclosure contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-info-version-disclosure and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-debug-endpoint-exposes-env contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-debug-endpoint-exposes-env and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.yaml-hardcoded-secrets-2 contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-hardcoded-secrets-2 and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.yaml-insecure-security-flags contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-insecure-security-flags and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.yaml-debug-and-unsafe-features contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-debug-and-unsafe-features and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Scanning 4 files (only git-tracked) with 16 Code rules:
            
  CODE RULES
                                                                                                                        
  Language   Rules   Files          Origin   Rules                                                                      
 ──────────────────────────        ────────────────                                                                     
  python        12       1          Custom      16                                                                      
  yaml           4       1                                                                                              
                                                                                                                        
                    
  SUPPLY CHAIN RULES
                  
  No rules to run.
                  
          
  PROGRESS
   
Rule sast.py-sql-injection-critical contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-sql-injection-critical and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-os-system-rce contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-os-system-rce and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-subprocess-rce contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-subprocess-rce and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-arbitrary-file-read contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-arbitrary-file-read and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-unsafe-pickle-deserialization contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-unsafe-pickle-deserialization and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-reflected-xss contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-reflected-xss and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-hardcoded-db-credentials contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-hardcoded-db-credentials and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-eval-user-input contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-eval-user-input and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.yaml-hardcoded-secrets-config contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-hardcoded-secrets-config and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.py-debug-mode-enabled contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-debug-mode-enabled and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-verbose-logging-sensitive contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-verbose-logging-sensitive and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-info-version-disclosure contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-info-version-disclosure and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-debug-endpoint-exposes-env contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-debug-endpoint-exposes-env and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.yaml-hardcoded-secrets-2 contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-hardcoded-secrets-2 and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.yaml-insecure-security-flags contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-insecure-security-flags and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.yaml-debug-and-unsafe-features contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-debug-and-unsafe-features and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00                                                                                                                        
                
                
┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 5 (5 blocking)
 • Rules run: 16
 • Targets scanned: 2
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 16 rules on 2 files: 5 findings.
```

Получился следующий JSON
```json
{
    "version": "1.147.0",
    "results": [
        {
            "check_id": "sast.py-info-version-disclosure",
            "path": "vulnerable-app/app.py",
            "start": {
                "line": 26,
                "col": 5,
                "offset": 385
            },
            "end": {
                "line": 26,
                "col": 39,
                "offset": 419
            },
            "extra": {
                "message": "Раскрытие версии приложения в ответе.",
                "metadata": {},
                "severity": "LOW",
                "fingerprint": "requires login",
                "lines": "requires login",
                "validation_state": "NO_VALIDATOR",
                "engine_kind": "OSS"
            }
        },
        {
            "check_id": "sast.py-os-system-rce",
            "path": "vulnerable-app/app.py",
            "start": {
                "line": 52,
                "col": 5,
                "offset": 1051
            },
            "end": {
                "line": 52,
                "col": 19,
                "offset": 1065
            },
            "extra": {
                "message": "RCE через os.system с данными пользователя.",
                "metadata": {},
                "severity": "CRITICAL",
                "fingerprint": "requires login",
                "lines": "requires login",
                "validation_state": "NO_VALIDATOR",
                "engine_kind": "OSS"
            }
        },
        {
            "check_id": "sast.py-arbitrary-file-read",
            "path": "vulnerable-app/app.py",
            "start": {
                "line": 68,
                "col": 14,
                "offset": 1434
            },
            "end": {
                "line": 68,
                "col": 29,
                "offset": 1449
            },
            "extra": {
                "message": "Чтение произвольного файла по пути из запроса (LFI/Path Traversal).",
                "metadata": {},
                "severity": "CRITICAL",
                "fingerprint": "requires login",
                "lines": "requires login",
                "validation_state": "NO_VALIDATOR",
                "engine_kind": "OSS"
            }
        },
        {
            "check_id": "sast.py-unsafe-pickle-deserialization",
            "path": "vulnerable-app/app.py",
            "start": {
                "line": 79,
                "col": 15,
                "offset": 1671
            },
            "end": {
                "line": 79,
                "col": 48,
                "offset": 1704
            },
            "extra": {
                "message": "Небезопасная десериализация через pickle.loads.",
                "metadata": {},
                "severity": "CRITICAL",
                "fingerprint": "requires login",
                "lines": "requires login",
                "validation_state": "NO_VALIDATOR",
                "engine_kind": "OSS"
            }
        },
        {
            "check_id": "sast.py-eval-user-input",
            "path": "vulnerable-app/app.py",
            "start": {
                "line": 88,
                "col": 14,
                "offset": 1909
            },
            "end": {
                "line": 88,
                "col": 24,
                "offset": 1919
            },
            "extra": {
                "message": "Опасное использование eval на пользовательском вводе.",
                "metadata": {},
                "severity": "HIGH",
                "fingerprint": "requires login",
                "lines": "requires login",
                "validation_state": "NO_VALIDATOR",
                "engine_kind": "OSS"
            }
        }
    ],
    "errors": [],
    "paths": {
        "scanned": [
            "vulnerable-app/app.py",
            "vulnerable-app/config.yaml"
        ]
    },
    "time": {
        "rules": [],
        "rules_parse_time": 0.024164915084838867,
        "profiling_times": {
            "config_time": 0.3701300621032715,
            "core_time": 0.9820055961608887,
            "ignores_time": 0.00012803077697753906,
            "total_time": 1.370509386062622
        },
        "parsing_time": {
            "total_time": 0.0,
            "per_file_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "very_slow_stats": {
                "time_ratio": 0.0,
                "count_ratio": 0.0
            },
            "very_slow_files": []
        },
        "scanning_time": {
            "total_time": 0.07058596611022949,
            "per_file_time": {
                "mean": 0.035292983055114746,
                "std_dev": 0.001133256069593358
            },
            "very_slow_stats": {
                "time_ratio": 0.0,
                "count_ratio": 0.0
            },
            "very_slow_files": []
        },
        "matching_time": {
            "total_time": 0.0,
            "per_file_and_rule_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "very_slow_stats": {
                "time_ratio": 0.0,
                "count_ratio": 0.0
            },
            "very_slow_rules_on_files": []
        },
        "tainting_time": {
            "total_time": 0.0,
            "per_def_and_rule_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "very_slow_stats": {
                "time_ratio": 0.0,
                "count_ratio": 0.0
            },
            "very_slow_rules_on_defs": []
        },
        "fixpoint_timeouts": [],
        "prefiltering": {
            "project_level_time": 0.0,
            "file_level_time": 0.0,
            "rules_with_project_prefilters_ratio": 0.0,
            "rules_with_file_prefilters_ratio": 0.6875,
            "rules_selected_ratio": 1.0,
            "rules_matched_ratio": 1.0
        },
        "targets": [],
        "total_bytes": 0,
        "max_memory_bytes": 98843584
    },
    "engine_requested": "OSS",
    "skipped_rules": [],
    "profiling_results": []
}
```

| Check ID | Severity | Строка | Описание |
|----------|----------|--------|----------|
| `py-os-system-rce` | CRITICAL | 52 | RCE через `os.system()` с данными пользователя |
| `py-arbitrary-file-read` | CRITICAL | 68 | LFI/Path Traversal — чтение произвольных файлов |
| `py-unsafe-pickle-deserialization` | CRITICAL | 79 | Небезопасная десериализация через `pickle.loads()` |
| `py-eval-user-input` | HIGH | 88 | Опасное использование `eval()` на пользовательском вводе |
| `py-info-version-disclosure` | LOW | 26 | Раскрытие версии приложения в HTTP-ответе |

### Логика правил `semgrep-rules.yml`

Файл содержит **16 правил** для Python и YAML, разделённых по severity:

**CRITICAL (5 правил):**

| Rule ID | Pattern | Описание |
|---------|---------|----------|
| `py-sql-injection-critical` | `cursor.execute("SELECT " + ...)` | SQL-инъекция через конкатенацию строк в запросе |
| `py-os-system-rce` | `os.system(...)` | RCE через выполнение системных команд |
| `py-subprocess-rce` | `subprocess.call(["sh", "-c", ...])` | Командная инъекция через subprocess с shell |
| `py-arbitrary-file-read` | `open(..., "r")` | Чтение произвольных файлов (LFI) |
| `py-unsafe-pickle-deserialization` | `pickle.loads(...)` | Десериализация недоверенных данных |

**HIGH (4 правила):**

| Rule ID | Pattern | Описание |
|---------|---------|----------|
| `py-reflected-xss` | `html = f"<h1>Results for: {q}</h1>"` | Reflected XSS — вывод пользовательского ввода в HTML |
| `py-hardcoded-db-credentials` | `DB_USER = "..."`, `DB_PASSWORD = "..."` | Захардкоженные учётные данные БД |
| `py-eval-user-input` | `eval(...)` | Выполнение произвольного кода через eval |
| `yaml-hardcoded-secrets-config` | `password: "..."`, `jwt_secret: "..."` | Секреты в YAML-конфигурации |

**MEDIUM (4 правила):**

| Rule ID | Pattern | Описание |
|---------|---------|----------|
| `py-debug-mode-enabled` | `app.config["DEBUG"] = True` | Включён debug-режим в production |
| `py-verbose-logging-sensitive` | `logging.basicConfig(level=logging.DEBUG)` | Избыточное логирование чувствительных данных |
| `py-debug-endpoint-exposes-env` | `env = dict(os.environ)` | Debug endpoint раскрывает переменные окружения |
| `yaml-insecure-security-flags` | `enable_csrf_protection: false` | Отключены механизмы защиты (CSRF, rate limit) |

**LOW (2 правила):**

| Rule ID | Pattern | Описание |
|---------|---------|----------|
| `py-info-version-disclosure` | `return "Vulnerable lab07 app v1.0"` | Раскрытие версии приложения |
| `yaml-debug-and-unsafe-features` | `debug: true`, `enable_remote_shell: true` | Включены опасные фичи в конфиге |

**Принцип работы правил:**
- **pattern** — точное совпадение с кодовой конструкцией (используется `...` как wildcard для любых аргументов)
- **paths.include** — ограничение области сканирования конкретными файлами
- **severity** — уровень критичности
- **languages** — целевой язык (python, yaml)

---

[x] 4. Запустите SAST Checkov по Dockerfile, compose и проанализируйте выведенный лог в консоли и опишите логику правил для `checkov-config.yaml` по Docker. Отчет будет в директории SAST

```bash
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07$ checkov \
    --framework dockerfile \
    --file vulnerable-app/Dockerfile docker-compose.yml \
    --output json \
    --output-file-path sast/checkov-report \
    --soft-fail
...
        "skipped_checks": [],
        "parsing_errors": []
    },
    "summary": {
        "passed": 50,
        "failed": 2,
        "skipped": 0,
        "parsing_errors": 0,
        "resource_count": 1,
        "checkov_version": "3.2.497"
    },
    "url": "Add an api key '--bc-api-key <api-key>' to see more detailed insights via https://bridgecrew.cloud"
}
...
```

Итоговый JSON в `results_json.json`

- Результат: **50 passed**, **2 failed**, 0 skipped

**Результаты сканирования (JSON summary):**

| Метрика | Значение |
|---------|----------|
| Passed | 50 |
| Failed | 2 |
| Skipped | 0 |
| Parsing errors | 0 |
| Resource count | 1 |

**Failed checks:**

| Check ID | Описание | Файл | Проблема |
|----------|----------|------|----------|
| `CKV_DOCKER_3` | Ensure that a user for the container has been created | Dockerfile | Контейнер запускается от root — нет инструкции `USER` |
| `CKV_DOCKER_2` | Ensure that HEALTHCHECK instructions have been added | Dockerfile | Отсутствует инструкция `HEALTHCHECK` для мониторинга состояния |

### Логика правил `checkov-config.yaml`

Конфигурационный файл определяет **политику безопасности** для Docker-образов:

**Структура конфига:**
```yaml
framework:        # Целевые фреймворки (docker, helm)
enforce:          # Список обязательных проверок
  docker:         # Проверки для Dockerfile
directory/file:   # Целевые директории и файлы для сканирования
```

**Enforce-правила для Docker (11 проверок):**

| Check ID | Описание | Категория |
|----------|----------|-----------|
| `CKV_DOCKER_2` | Наличие инструкции HEALTHCHECK | Availability |
| `CKV_DOCKER_3` | Создание non-root пользователя (USER) | Privilege Escalation |
| `CKV_DOCKER_5` | Избегать тег `latest` в базовом образе | Supply Chain |
| `CKV_DOCKER_7` | Использовать COPY вместо ADD | Security Best Practice |
| `CKV_DOCKER_8` | Явно задавать non-root пользователя | Privilege Escalation |
| `CKV_DOCKER_9` | Минимизировать attack surface образа | Hardening |
| `CKV_DOCKER_10` | Наличие HEALTHCHECK | Availability |
| `CKV_DOCKER_12` | Не хранить секреты в ENV | Secrets Management |
| `CKV_DOCKER_13` | Запрет privileged режима | Container Escape |
| `CKV_DOCKER_14` | Ограничить capabilities | Privilege Escalation |
| `CKV_DOCKER_16` | Предпочитать read-only root filesystem | Hardening |

**Принцип работы Checkov:**
- **framework** — указывает тип инфраструктуры для анализа (в данном случае docker, helm)
- **enforce** — список check_id, которые должны быть PASSED (иначе fail)
- **file/directory** — область сканирования
- **soft-fail** — если `true`, возвращает exit code 0 даже при failed checks
- **quiet** — минимальный вывод в консоль

[x] 5. Подготовка зависимостей Java и Maven‑скан для проведения SCA. Отчеты будут в директории SCA. Будет ошибка, которую надо поправить, что бы уязвимости определялись или добавить дополнительные уязвимости для их вывода в отчете

```bash
[INFO] Downloaded 160,000/327,787 (49%)
[INFO] Downloaded 170,000/327,787 (52%)
[INFO] Downloaded 180,000/327,787 (55%)
[INFO] Downloaded 190,000/327,787 (58%)
[INFO] Downloaded 200,000/327,787 (61%)
[INFO] Downloaded 210,000/327,787 (64%)
[INFO] Downloaded 220,000/327,787 (67%)
[INFO] Downloaded 230,000/327,787 (70%)
[INFO] Downloaded 240,000/327,787 (73%)
[INFO] Downloaded 250,000/327,787 (76%)
[INFO] Downloaded 260,000/327,787 (79%)
[INFO] Downloaded 270,000/327,787 (82%)
[INFO] Downloaded 280,000/327,787 (85%)
[INFO] Downloaded 290,000/327,787 (88%)
[INFO] Downloaded 300,000/327,787 (92%)
[INFO] Downloaded 310,000/327,787 (95%)
[INFO] Downloaded 320,000/327,787 (98%)
[INFO] Downloaded 327,787/327,787 (100%)
[INFO] Completed processing batch 1/164 (1%) in 6,063ms
[INFO] Completed processing batch 2/164 (1%) in 3,754ms
[INFO] Completed processing batch 3/164 (2%) in 6,712ms
[INFO] Completed processing batch 4/164 (2%) in 7,117ms
[INFO] Completed processing batch 5/164 (3%) in 6,670ms
[INFO] Completed processing batch 6/164 (4%) in 7,315ms
[INFO] Completed processing batch 7/164 (4%) in 5,396ms
[INFO] Completed processing batch 8/164 (5%) in 7,126ms
[INFO] Completed processing batch 9/164 (5%) in 3,102ms
[INFO] Completed processing batch 10/164 (6%) in 3,326ms
[INFO] Completed processing batch 11/164 (7%) in 18,532ms
[INFO] Completed processing batch 12/164 (7%) in 14,301ms
[INFO] Completed processing batch 13/164 (8%) in 3,457ms
[INFO] Completed processing batch 14/164 (9%) in 4,425ms
[INFO] Completed processing batch 15/164 (9%) in 3,080ms
[INFO] Completed processing batch 16/164 (10%) in 3,598ms
[INFO] Completed processing batch 17/164 (10%) in 3,778ms
[INFO] Completed processing batch 18/164 (11%) in 3,150ms
[INFO] Completed processing batch 19/164 (12%) in 3,045ms
[INFO] Completed processing batch 20/164 (12%) in 2,553ms
[INFO] Completed processing batch 21/164 (13%) in 2,326ms
[INFO] Completed processing batch 22/164 (13%) in 3,283ms
[INFO] Completed processing batch 23/164 (14%) in 3,498ms
[INFO] Completed processing batch 24/164 (15%) in 5,981ms
[INFO] Completed processing batch 25/164 (15%) in 4,876ms
[INFO] Completed processing batch 26/164 (16%) in 5,674ms
[INFO] Completed processing batch 27/164 (16%) in 5,593ms
[INFO] Completed processing batch 28/164 (17%) in 12,651ms
[INFO] Completed processing batch 29/164 (18%) in 7,360ms
[INFO] Completed processing batch 30/164 (18%) in 10,506ms
[INFO] Completed processing batch 31/164 (19%) in 5,954ms
[INFO] Completed processing batch 32/164 (20%) in 4,252ms
[INFO] Completed processing batch 33/164 (20%) in 3,211ms
[INFO] Completed processing batch 34/164 (21%) in 6,232ms
[INFO] Completed processing batch 35/164 (21%) in 34,601ms
[INFO] Completed processing batch 36/164 (22%) in 26,713ms
[INFO] Completed processing batch 37/164 (23%) in 21,306ms
[INFO] Completed processing batch 38/164 (23%) in 11,454ms
[INFO] Completed processing batch 39/164 (24%) in 9,607ms
[INFO] Completed processing batch 40/164 (24%) in 3,941ms
[INFO] Completed processing batch 41/164 (25%) in 1,725ms
[INFO] Completed processing batch 42/164 (26%) in 2,035ms
[INFO] Completed processing batch 43/164 (26%) in 2,679ms
[INFO] Completed processing batch 44/164 (27%) in 2,736ms
[INFO] Completed processing batch 45/164 (27%) in 823ms
[INFO] Completed processing batch 46/164 (28%) in 12,317ms
[INFO] Completed processing batch 47/164 (29%) in 47,291ms
[INFO] Completed processing batch 48/164 (29%) in 27,284ms
[INFO] Completed processing batch 49/164 (30%) in 22,131ms
[INFO] Completed processing batch 50/164 (30%) in 17,681ms
[INFO] Completed processing batch 51/164 (31%) in 15,584ms
[INFO] Completed processing batch 52/164 (32%) in 14,000ms
[INFO] Completed processing batch 53/164 (32%) in 4,122ms
[INFO] Completed processing batch 54/164 (33%) in 7,857ms
[INFO] Completed processing batch 55/164 (34%) in 18,604ms
[INFO] Completed processing batch 56/164 (34%) in 30,648ms
[INFO] Completed processing batch 57/164 (35%) in 21,937ms
[INFO] Completed processing batch 58/164 (35%) in 12,434ms
[INFO] Completed processing batch 59/164 (36%) in 4,891ms
[INFO] Completed processing batch 60/164 (37%) in 7,500ms
[INFO] Completed processing batch 61/164 (37%) in 6,450ms
[INFO] Completed processing batch 62/164 (38%) in 11,775ms
[INFO] Completed processing batch 63/164 (38%) in 13,733ms
[INFO] Completed processing batch 64/164 (39%) in 4,131ms
[INFO] Completed processing batch 65/164 (40%) in 7,375ms
[INFO] Completed processing batch 66/164 (40%) in 5,275ms
[INFO] Completed processing batch 67/164 (41%) in 4,272ms
[INFO] Completed processing batch 68/164 (41%) in 7,205ms
[INFO] Completed processing batch 69/164 (42%) in 2,648ms
[INFO] Completed processing batch 70/164 (43%) in 3,777ms
[INFO] Completed processing batch 71/164 (43%) in 3,482ms
[INFO] Completed processing batch 72/164 (44%) in 2,860ms
[INFO] Completed processing batch 73/164 (45%) in 2,469ms
[INFO] Completed processing batch 74/164 (45%) in 3,685ms
[INFO] Completed processing batch 75/164 (46%) in 4,947ms
[INFO] Completed processing batch 76/164 (46%) in 22,317ms
[INFO] Completed processing batch 77/164 (47%) in 16,228ms
[INFO] Completed processing batch 78/164 (48%) in 10,666ms
[INFO] Completed processing batch 79/164 (48%) in 4,350ms
[INFO] Completed processing batch 80/164 (49%) in 6,022ms
[INFO] Completed processing batch 81/164 (49%) in 4,222ms
[INFO] Completed processing batch 82/164 (50%) in 5,271ms
[INFO] Completed processing batch 83/164 (51%) in 1,333ms
[INFO] Completed processing batch 84/164 (51%) in 26,183ms
[INFO] Completed processing batch 85/164 (52%) in 36,182ms
[INFO] Completed processing batch 86/164 (52%) in 61,765ms
[INFO] Completed processing batch 87/164 (53%) in 70,563ms
[INFO] Completed processing batch 88/164 (54%) in 59,205ms
[INFO] Completed processing batch 89/164 (54%) in 65,196ms
[INFO] Completed processing batch 90/164 (55%) in 62,281ms
[INFO] Completed processing batch 91/164 (55%) in 44,470ms
[INFO] Completed processing batch 92/164 (56%) in 38,960ms
[INFO] Completed processing batch 93/164 (57%) in 37,656ms
[INFO] Completed processing batch 94/164 (57%) in 33,389ms
[INFO] Completed processing batch 95/164 (58%) in 18,029ms
[INFO] Completed processing batch 96/164 (59%) in 18,348ms
[INFO] Completed processing batch 97/164 (59%) in 10,616ms
[INFO] Completed processing batch 98/164 (60%) in 2,254ms
[INFO] Completed processing batch 99/164 (60%) in 2,685ms
[INFO] Completed processing batch 100/164 (61%) in 3,965ms
[INFO] Completed processing batch 101/164 (62%) in 1,277ms
[INFO] Completed processing batch 102/164 (62%) in 2,593ms
[INFO] Completed processing batch 103/164 (63%) in 3,740ms
[INFO] Completed processing batch 104/164 (63%) in 4,398ms
[INFO] Completed processing batch 105/164 (64%) in 2,614ms
[INFO] Completed processing batch 106/164 (65%) in 3,908ms
[INFO] Completed processing batch 107/164 (65%) in 2,172ms
[INFO] Completed processing batch 108/164 (66%) in 2,272ms
[INFO] Completed processing batch 109/164 (66%) in 1,640ms
[INFO] Completed processing batch 110/164 (67%) in 1,845ms
[INFO] Completed processing batch 111/164 (68%) in 1,713ms
[INFO] Completed processing batch 112/164 (68%) in 1,713ms
[INFO] Completed processing batch 113/164 (69%) in 1,245ms
[INFO] Completed processing batch 114/164 (70%) in 1,552ms
[INFO] Completed processing batch 115/164 (70%) in 1,836ms
[INFO] Completed processing batch 116/164 (71%) in 2,654ms
[INFO] Completed processing batch 117/164 (71%) in 4,741ms
[INFO] Completed processing batch 118/164 (72%) in 2,046ms
[INFO] Completed processing batch 119/164 (73%) in 12,296ms
[INFO] Completed processing batch 120/164 (73%) in 4,852ms
[INFO] Completed processing batch 121/164 (74%) in 2,856ms
[INFO] Completed processing batch 122/164 (74%) in 2,762ms
[INFO] Completed processing batch 123/164 (75%) in 2,535ms
[INFO] Completed processing batch 124/164 (76%) in 1,010ms
[INFO] Completed processing batch 125/164 (76%) in 962ms
[INFO] Completed processing batch 126/164 (77%) in 957ms
[INFO] Completed processing batch 127/164 (77%) in 1,838ms
[INFO] Completed processing batch 128/164 (78%) in 2,292ms
[INFO] Completed processing batch 129/164 (79%) in 1,641ms
[INFO] Completed processing batch 130/164 (79%) in 1,629ms
[INFO] Completed processing batch 131/164 (80%) in 1,525ms
[INFO] Completed processing batch 132/164 (80%) in 2,056ms
[INFO] Completed processing batch 133/164 (81%) in 1,321ms
[INFO] Completed processing batch 134/164 (82%) in 1,557ms
[INFO] Completed processing batch 135/164 (82%) in 1,943ms
[INFO] Completed processing batch 136/164 (83%) in 808ms
[INFO] Completed processing batch 137/164 (84%) in 1,133ms
[INFO] Completed processing batch 138/164 (84%) in 1,002ms
[INFO] Completed processing batch 139/164 (85%) in 892ms
[INFO] Completed processing batch 140/164 (85%) in 858ms
[INFO] Completed processing batch 141/164 (86%) in 1,062ms
[INFO] Completed processing batch 142/164 (87%) in 631ms
[INFO] Completed processing batch 143/164 (87%) in 2,601ms
[INFO] Completed processing batch 144/164 (88%) in 953ms
[INFO] Completed processing batch 145/164 (88%) in 10,337ms
[INFO] Completed processing batch 146/164 (89%) in 8,809ms
[INFO] Completed processing batch 147/164 (90%) in 2,486ms
[INFO] Completed processing batch 148/164 (90%) in 3,446ms
[INFO] Completed processing batch 149/164 (91%) in 4,982ms
[INFO] Completed processing batch 150/164 (91%) in 1,482ms
[INFO] Completed processing batch 151/164 (92%) in 3,963ms
[INFO] Completed processing batch 152/164 (93%) in 1,160ms
[INFO] Completed processing batch 153/164 (93%) in 2,898ms
[INFO] Completed processing batch 154/164 (94%) in 3,280ms
[INFO] Completed processing batch 155/164 (95%) in 537ms
[INFO] Completed processing batch 156/164 (95%) in 1,328ms
[INFO] Completed processing batch 157/164 (96%) in 803ms
[INFO] Completed processing batch 158/164 (96%) in 2,322ms
[INFO] Completed processing batch 159/164 (97%) in 1,270ms
[INFO] Completed processing batch 160/164 (98%) in 934ms
[INFO] Completed processing batch 161/164 (98%) in 680ms
[INFO] Completed processing batch 162/164 (99%) in 1,190ms
[INFO] Completed processing batch 163/164 (99%) in 324ms
[INFO] Completed processing batch 164/164 (100%) in 1,877ms
[INFO] Updating CISA Known Exploited Vulnerability list: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
[INFO] Begin database defrag
[INFO] End database defrag (50200 ms)
[INFO] Check for updates complete (1734194 ms)
[+] NVD data updated
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07/sca$ mvn dependency:resolve
[INFO] Scanning for projects...
[INFO] 
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-dependency-plugin:2.8:resolve (default-cli) @ sca-demo ---
[INFO] 
[INFO] The following files have been resolved:
[INFO]    com.fasterxml.jackson.core:jackson-annotations:jar:2.4.0:compile
[INFO]    com.fasterxml.jackson.core:jackson-databind:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.module:jackson-module-jaxb-annotations:jar:2.4.6:compile
[INFO]    commons-codec:commons-codec:jar:1.2:compile
[INFO]    com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.jaxrs:jackson-jaxrs-base:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.core:jackson-core:jar:2.4.6:compile
[INFO]    org.codehaus.groovy:groovy-all:jar:2.1.6:compile
[INFO]    commons-httpclient:commons-httpclient:jar:3.1:compile
[INFO]    commons-logging:commons-logging:jar:1.0.4:compile
[INFO] 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  4.807 s
[INFO] Finished at: 2026-01-14T23:52:47+03:00
[INFO] ------------------------------------------------------------------------
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07/sca$ mvn dependency:copy-dependencies -DoutputDirectory=./lib
[INFO] Scanning for projects...
[INFO] 
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-dependency-plugin:2.8:copy-dependencies (default-cli) @ sca-demo ---
[INFO] jackson-annotations-2.4.0.jar already exists in destination.
[INFO] jackson-databind-2.4.6.jar already exists in destination.
[INFO] jackson-module-jaxb-annotations-2.4.6.jar already exists in destination.
[INFO] commons-codec-1.2.jar already exists in destination.
[INFO] jackson-jaxrs-json-provider-2.4.6.jar already exists in destination.
[INFO] jackson-jaxrs-base-2.4.6.jar already exists in destination.
[INFO] jackson-core-2.4.6.jar already exists in destination.
[INFO] groovy-all-2.1.6.jar already exists in destination.
[INFO] commons-httpclient-3.1.jar already exists in destination.
[INFO] commons-logging-1.0.4.jar already exists in destination.
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  2.317 s
[INFO] Finished at: 2026-01-14T23:53:17+03:00
[INFO] ------------------------------------------------------------------------
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07/sca$ ./dependency-check/bin/dependency-check.sh \
    --scan ../vulnerable-app \
    --scan lib \
    --format HTML --format JSON --format CSV \
    --project "lab07-vulnerable-app" \
    --out dependency-check-report \
    --data ~/.dependency-check-data \
    --noupdate \
    --disableOssIndex
[INFO] 

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://jeremylong.github.io/DependencyCheck/general/internals.html
   False Positives: https://jeremylong.github.io/DependencyCheck/general/suppression.html

💖 Sponsor: https://github.com/sponsors/jeremylong


[INFO] Analysis Started
[INFO] Finished Archive Analyzer (0 seconds)
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Jar Analyzer (0 seconds)
[INFO] Finished Central Analyzer (4 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (1 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (7 seconds)
[INFO] Finished CPE Analyzer (10 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (18 seconds)
[INFO] Writing HTML report to: /home/bttrs/Riski/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.html
[INFO] Writing JSON report to: /home/bttrs/Riski/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.json
[INFO] Writing CSV report to: /home/bttrs/Riski/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.csv
```

[x] 6. Запустите SCA CLI OWASP Dependency-Check для уязвимого приложения. Отчеты будут в директории SCA. Опишите как работает сканирование SCA для `pom.xml` и `app.py`

```bash
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07/sca$ ./dependency-check.sh 
OWASP Dependency-Check SCA
[*] Running scan using cached data in /home/bttrs/.dependency-check-data (no full re-download)
[*] Scanning:
    - /home/bttrs/Riski/course_labs/labs/lab07/vulnerable-app
    - /home/bttrs/Riski/course_labs/labs/lab07/sca/lib
[INFO] 

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://jeremylong.github.io/DependencyCheck/general/internals.html
   False Positives: https://jeremylong.github.io/DependencyCheck/general/suppression.html

💖 Sponsor: https://github.com/sponsors/jeremylong


[INFO] Analysis Started
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (8 seconds)
[INFO] Finished CPE Analyzer (8 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[INFO] Finished Sonatype OSS Index Analyzer (0 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (9 seconds)
[INFO] Writing HTML report to: /home/bttrs/Riski/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.html
[INFO] Writing JSON report to: /home/bttrs/Riski/course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.json
[+] Reports saved to: /home/bttrs/Riski/course_labs/labs/lab07/sca/dependency-check-report
[i] To refresh NVD data occasionally, run: bash sca/dependency-check.sh --update
```

[x] 7. Соберите единый отчет из всех сканирований в виде html, csv, json

[x] 8. Проанализируйте все уязвимости и обьясните для SAST Checkov сработки статуса Unknown. Классифицируйте их и укажите какие не должны быть в отчетах. Внесите исправления и запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл и отчет без уязвимостей.

В пункте 4 уже все разобрано. Исправил Dockerfile и при повторном сканировании все проверки пройдены

```bash
"summary": {
        "passed": 87,
        "failed": 0,
        "skipped": 0,
        "parsing_errors": 0,
        "resource_count": 1,
        "checkov_version": "3.2.497"
},
```

[x] 9. Опишите выведенные уязвимости для SAST Semgrep и принцип их работы. Поправьте скрипт app.py. Запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл app.py и отчет без уязвимостей.

Уязвимости расписаны в пункте 3. Исправил app.py и повторно запустил

```bash
(venv) bttrs@bttrs:~/Riski/course_labs/labs/lab07$ semgrep --config sast/semgrep-rules.yml     --json     --output sast/semgrep-report-fixed.json     vulnerable-app/

┌──── ○○○ ────┐
│ Semgrep CLI │
└─────────────┘

Rule sast.py-sql-injection-critical contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-sql-injection-critical and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-os-system-rce contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-os-system-rce and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-subprocess-rce contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-subprocess-rce and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-arbitrary-file-read contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-arbitrary-file-read and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-unsafe-pickle-deserialization contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-unsafe-pickle-deserialization and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-reflected-xss contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-reflected-xss and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-hardcoded-db-credentials contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-hardcoded-db-credentials and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-eval-user-input contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-eval-user-input and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.yaml-hardcoded-secrets-config contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-hardcoded-secrets-config and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.py-debug-mode-enabled contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-debug-mode-enabled and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-verbose-logging-sensitive contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-verbose-logging-sensitive and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-info-version-disclosure contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-info-version-disclosure and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-debug-endpoint-exposes-env contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-debug-endpoint-exposes-env and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.yaml-hardcoded-secrets-2 contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-hardcoded-secrets-2 and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.yaml-insecure-security-flags contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-insecure-security-flags and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.yaml-debug-and-unsafe-features contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-debug-and-unsafe-features and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Scanning 4 files (only git-tracked) with 16 Code rules:
            
  CODE RULES
                                                                                                                        
  Language   Rules   Files          Origin   Rules                                                                      
 ──────────────────────────        ────────────────                                                                     
  python        12       1          Custom      16                                                                      
  yaml           4       1                                                                                              
                                                                                                                        
                    
  SUPPLY CHAIN RULES
                  
  No rules to run.
                  
          
  PROGRESS
   
Rule sast.py-sql-injection-critical contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-sql-injection-critical and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-os-system-rce contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-os-system-rce and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-subprocess-rce contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-subprocess-rce and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-arbitrary-file-read contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-arbitrary-file-read and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-unsafe-pickle-deserialization contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-unsafe-pickle-deserialization and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-reflected-xss contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-reflected-xss and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-hardcoded-db-credentials contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-hardcoded-db-credentials and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-eval-user-input contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-eval-user-input and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.yaml-hardcoded-secrets-config contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-hardcoded-secrets-config and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.py-debug-mode-enabled contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-debug-mode-enabled and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-verbose-logging-sensitive contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-verbose-logging-sensitive and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-info-version-disclosure contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-info-version-disclosure and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.py-debug-endpoint-exposes-env contains an include pattern 'vulnerable-app/app.py' that will soon be interpreted as '/vulnerable-app/app.py' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.py-debug-endpoint-exposes-env and change it to '**/vulnerable-app/app.py'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/app.py'.
Rule sast.yaml-hardcoded-secrets-2 contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-hardcoded-secrets-2 and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.yaml-insecure-security-flags contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-insecure-security-flags and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
Rule sast.yaml-debug-and-unsafe-features contains an include pattern 'vulnerable-app/config.yaml' that will soon be interpreted as '/vulnerable-app/config.yaml' to comply with the Semgrepignore v2 and Gitignore specifications. To make this pattern permanently unanchored, edit rule sast.yaml-debug-and-unsafe-features and change it to '**/vulnerable-app/config.yaml'. To confirm the anchored behavior and avoid this warning, change it to '/vulnerable-app/config.yaml'.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00                                                                                                                        
                
                
┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 0 (0 blocking)
 • Rules run: 16
 • Targets scanned: 2
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 16 rules on 2 files: 0 findings.

✨ If Semgrep missed a finding, please send us feedback to let us know!
   See https://semgrep.dev/docs/reporting-false-negatives/
```

Уязвимостей не обнаружено

[x] 10. Доработайте SCA уязвимости, что бы они только остались в фиинальной версии отчетов.

Из пунктов 5-6

Найденные уязвимости:
  Библиотека: groovy-all-2.1.6.jar
  CVE: CVE-2015-3253, CVE-2016-6814
  Severity: CRITICAL
  ────────────────────────────────────────
  Библиотека: jackson-databind-2.4.6.jar
  CVE: CVE-2017-15095, CVE-2017-17485, CVE-2017-7525 + 45 more
  Severity: CRITICAL
  ────────────────────────────────────────
  Библиотека: commons-httpclient-3.1.jar
  CVE: CVE-2012-5783, CVE-2020-13956
  Severity: MEDIUM
  ────────────────────────────────────────
  Библиотека: jackson-core-2.4.6.jar
  CVE: CVE-2018-1000873
  Severity: MEDIUM
  ────────────────────────────────────────
  Библиотека: jackson-annotations-2.4.0.jar
  CVE: CVE-2018-1000873
  Severity: MEDIUM

[x] 11. Проверьте себя по найденным сработкам анализаторов и так вы сможете помочь себе разобраться в ситуации, если возникнут сложности

```bash
Unified SAST/SCA Report Generation
[-] generate_unified_report.sh not found or not executable

lab07 scanning complete - positive
Review:
  - Semgrep SAST findings
  - Checkov Docker/IaC findings
  - OWASP Dependency-Check SCA findings (CLI + Maven)
  - Unified reports in reports/ directory (CSV, HTML, JSON)
  - Open CSV in Excel/LibreOffice and save as XLSX/ODT
```

[x] 12. Делайте все коммиты на соответствующих шагах, далее заливайте изменения в удаленный репозиторий.

[x] 13.  Подготовьте отчет gist.

[x] 14. Почистите кеш от venv и остановите уязвимое приложение

```bash
```

---

Copyright (c) 2025 Egor Davydov
