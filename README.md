# Onboarding-bot

## Code architecture

```
onboarding_bot
├── README.md
├── database
│   ├── __init__.py
│   ├── config.py
│   ├── create_table.py
│   ├── repositories
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── setup.py
│   └── tests
│       ├── __init__.py
│       └── data
└── telegram_bot
    ├── __init__.py
    ├── config.py
    ├── handlers
    │   ├── __init__.py
    │   ├── admins
    │   │   ├── __init__.py
    │   │   └── authorization.py
    │   └── users
    │       ├── __init__.py
    │       ├── authorization.py
    │       ├── echo.py
    │       └── help.py
    ├── keyboards
    │   └── __init__.py
    ├── logs
    ├── main.py
    ├── middlewares
    │   ├── __init__.py
    │   └── throttling.py
    ├── requirements.txt
    ├── setup.py
    └── utils
        ├── __init__.py
        ├── misc
        │   ├── __init__.py
        │   ├── logging.py
        │   └── throttling.py
        ├── notify_admins.py
        └── set_bot_commands.py
```

## Launch instructions

1. Create `/.env` file with following data:
   ```
   TG_TOKEN=9999999999:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  # here you should paste your bot token
   ADMINS=[999999999, 111111111]  # here you should paste your user ids
   LOGS_BASE_PATH=logs  # here you should paste your path to the log files relative to the telegram_bot directory
   ```
2. Run in terminal from root folder:
    ```bash
    cd database/
    pip install -Ue ".[dev]"
    cd ../telegram_bot/
    pip install -Ue ".[dev]"
    python main.py
    ```

# Stopping instructions

In the terminal from which the bot was started, press Ctrl + C.

## Packages description

### database

A package containing all the scripts for creating and interacting with tables in a database, as well as testing these functions.

- __init\__.py

An empty file, which is necessary to directory as a package.

- config.py

A file containing all global environment variables. Here there is a `settings` object, which contains variables from the `.env` file. The object has the following values: 1) `DB_PATH`. Database path written in the form `dialect+driver://username:password@host:port/database`. If there is no such value in the file, the variable will contain  `None`. 2) `Config`. 2.1) `env_prefix`. Variables have a prefix in the `.env` file. By default, there is no prefix. 2.2) `env_file`. Contains the relative path to the `.env` file. By default, the file is located in the root folder of the project. 2.3) `env_file_encoding`. Contains the encoding of the `.env` file. By default, the file opens in utf-8 encoding.

- create_table.py

It is now a plug. In the future will create an `engine` and `sessionmaker` to access the database. In addition, it will have an object that stores `meta data` and the object of the database itself. Will have classes that describe the table. Will have a function that creates tables by classes in case they are not in the database.

- repositories

A package that contains functions to interact with all the necessary tables in the database.

| file name | description |
|---|---|
| __init\__.py | An empty file, which is necessary to directory as a package. |

- requirements.txt

Contains all the libraries required for installation and their versions, at which the developer guarantees that the product works.

- setup.py

A file containing the parameters for installing the package.

| object name | description |
|---|---|
| load_requirements | A function that parses the `requirements.txt` file and returns a list of libraries to install. |
| PKG_DIR | Contains the path to install the package. |
| PROJECT_ROOT_DIR | Contains the path to the project. |
| SETUP_KWARGS | Contains all the information loaded in the package. The default name of the package is `telegram_bot`. The default author is `Karina Gordeeva`. The default license is `MIT`. The default version of python is required `3.8 or higher`. The required default packages are searched for using the `find_packages function`. By default all files in installed packages are also installed. By default, the `load_requirements` function collects all required libraries. |

- tests

A package containing all the functions and data for testing the database interaction functions.

| name | description |
|---|---|
| __init\__.py | An empty file, which is necessary to directory as a package. | 
| data | Contains json files with test data for each table. |

### telegram_bot

A package containing all the scripts to run the bot.

- __init\__.py

An empty file, which is necessary to directory as a package.

- config.py

A file containing all global environment variables. Here there is a  `settings`  object, which contains variables from the  `.env`  file, and objects of storage –  `storage` , bot itself –  `bot` , dispatcher –  `dp`.

| object name | description |
|---|---|
| settings | The object has the following values: 1)  `TG_TOKEN`. Here is the string value of  `TG_TOKEN`  from the  `.env`  file. If there is no such value in the file, the variable will contain  `None`. 2)  `ADMINS`. Here is the list read from the ADMINS variable in the .env file. If there is no such value in the file, the variable will contain  `None`. 3)  `LOGS_BASE_PATH`. This contains the relative path to the directory where the log files are saved. By default, files will be saved in the  `telegram_bot` directory. 4)  `START_FLOOD_MESSAGE`. Temporal variable. This contains the text sent when a ddos attack is attempted. By default, it has the value  `Too many requests!`. 5)  `STOP_FLOOD_MESSAGE`. Temporal variable. This contains the text sent when a user is unblocked after an attempted ddos attack. By default, it has the value  `You can repeat your request.`  6)  `Config`. 6.1)  `env_prefix`. Variables have a prefix in the  `.env`  file. By default, there is no prefix. 6.2)  `env_file`. Contains the relative path to the  `.env`  file. By default, the file is located in the root folder of the project. 6.3)  `env_file_encoding`. Contains the encoding of the  `.env` file. By default, the file opens in utf-8 encoding. |
| storage | Standard dispatcher storage. Not used yet. |
| bot | Creating an object of the bot itself with a previously fixed token and a default HTML mod. |
| dp | The bot dispatcher object associated with the created storage. |

- handlers

Contain scripts for handling certain actions. Actions are divided into 2 types of users: normal and privileged.

#### __init\__.py

Binds handlers for all types of users.

#### admins

Contain scripts describing the processing of privileged user actions.

| file name | description |
|---|---|
| __init\__.py | Binds processing scripts to the  `admins` folder. |
| autorization.py | At the moment is a plug. In the future it will be responsible for changing the status of the user: from normal to privileged. |

#### users

Contain scripts describing the processing of common user actions.

| file name | description |
|---|---|
| __init\__.py | Binds processing scripts to the  `users` folder. |
| authorization.py | At the moment is a plug. In the future, it will be responsible for changing the addition of information about the new user in the database. |
| echo.py | At the moment is a plug. In the future it will be responsible for handling messages that don't match all the other handlers. |
| help.py | At the moment is a plug. In the future it will be responsible for notifying users about bot features. |

- keyboards

Contain all keyboard generators.

| file name | description |
|---|---|
| __init\__.py | Binds all keyboard generators. |

- logs

Changeable folder location. Contain files with logs of each startup.

- main.py

The file that starts the bot.

| object name | description |
|---|---|
| on_startup | The function that starts all processes when the bot starts. Contains running logs, setting standard commands in the bot, and notifying privileged users of a successful launch. |
| on_shutdown | A function that starts all processes when the bot is turned off. Contains the notification of privileged users when the bot is terminated. |
executor.start_polling | Direct launch of the bot. |

- middlewares

Additional services to keep the bot running.

| file name | description |
|---|---|
| __init\__.py | Binds all services for further import. Binds existing services to the dispatcher during import. |
| throttling.py | Service responsible for the anti-flooding function. Contains `ThrottlingMiddleware` class, inherited from `BaseMiddleware`. During initialization, it takes a limit for receiving requests - `limit`. When it receives a message, it checks if the limit is violated. If the limit is violated, it silences the user and sends him a notification if the number of requests is exceeded. When the stub expires, it notifies the user about it. |

- requirements.txt

Contains all the libraries required for installation and their versions, at which the developer guarantees that the product works. 

- setup.py

A file containing the parameters for installing the package.

| object name | description |
|---|---|
| load_requirements | A function that parses the `requirements.txt` file and returns a list of libraries to install. |
| PKG_DIR | Contains the path to install the package. |
| PROJECT_ROOT_DIR | Contains the path to the project. |
| SETUP_KWARGS | Contains all the information loaded in the package. The default name of the package is `telegram_bot`. The default author is `Karina Gordeeva`. The default license is `MIT`. The default version of python is required `3.8 or higher`. The required default packages are searched for using the `find_packages function`. By default all files in installed packages are also installed. By default, the `load_requirements` function collects all required libraries. |

- utils

Contains all the necessary utilities for the bot.

#### __init\__.py

Binds all utilities together.

#### misc

Contains additional utilities.

| file name | description |
|---|---|
| __init\__.py | Binds all additional utilities. |
| logging.py | Utility that sets the logging settings. Contains `InterceptHandler` class, inherited from standard `logging.Handler`. The class specifies the desired logging levels. Also contains a function `setup` that sets these settings on the logger. By default, logging is done only on its own modules, starting with `INFO` level, in the format `{time} {level} {message}`. By default, the file in which the startup logs are saved is generated using the `file_{time}.log` template in the logs folder. |
| throttling.py | A utility that generates a decorator to the `throttling.py` add-on service. |

#### notify_admins.py

File containing notification functions for privileged users: `on_startup_notify` when the bot is started and `on_shutdown_notify` when it is disabled.

#### set_bot_commands.py

A file containing `set_default_commands` function to set the default commands in the user. The user has 2 commands by default: `start`, `help`.

