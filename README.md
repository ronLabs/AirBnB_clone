# AirBnB clone Project - The Console

## Description
This repository contains the files for Holberton's **AirBnB clone project**. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

- Usage Module CMD.
- Usage Module DateTime.
- Usage Module Uuid.
- Serialize and Deserialize the Files JSON.
- Usage args/Kwargs
- Usage Packges Python

## Install on PC

    $ git clone https://github.com/melisarv/AirBnB_clone.git
    $ cd AirBnB_clone
    $ ./console.py

### Commands CMD

| Command | Simple Usage             |
| ------- | ------------------------ |
| Quit    | Quit the Prompt          |
| Help    | Display help the console |
| Create  | Create New object        |
| Show    | Show the object          |
| All     | Display All objects      |
| Update  | Update objects           |
| Destroy | Destroy Objects          |

## How to Use it
**interactive mode**
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
**non-interactive mode**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Examples
```
(hbnb) create BaseModel
3db5387d-2fd6-494e-9b95-e5a62790c1fd
(hbnb) show BaseModel 2013187e-1bc9-4f8f-b0ae-8088e6a2ee43
[BaseModel] (3db5387d-2fd6-494e-9b95-e5a62790c1fd) {'created_at': datetime.datetime(2018, 11, 15, 3, 3, 56, 358245), 'updated_at': datetime.datetime(2018, 11, 15, 3, 3, 56, 358274), 'id': '3db5387d-2fd6-494e-9b95-e5a62790c1fd'}
(hbnb) update BaseModel 3db5387d-2fd6-494e-9b95-e5a62790c1fd name "Betty"
(hbnb) show BaseModel 3db5387d-2fd6-494e-9b95-e5a62790c1fd
[BaseModel] (3db5387d-2fd6-494e-9b95-e5a62790c1fd) {'created_at': datetime.datetime(2018, 11, 15, 3, 3, 56, 358245, 'updated_at': datetime.datetime(2018, 11, 15, 3, 3, 56, 358274), 'id': '3db5387d-2fd6-494e-9b95-e5a62790c1fd', 'name': "Betty"}
(hbnb) destroy BaseModel 3db5387d-2fd6-494e-9b95-e5a62790c1fd
(hbnb) show BaseModel 3db5387d-2fd6-494e-9b95-e5a62790c1fd
** no instance found **
(hbnb)

```

# AUTHORS
* Melisa Rojas
* Ronald Altamirano

