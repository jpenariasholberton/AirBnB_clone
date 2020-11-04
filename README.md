![](https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67)

<h1 align="center">0x00. AirBnB clone - The console</h1>
<p align="center"></p>

---
### Project description

The objective of the project is to implement a simple copy of the AirBnB website on a server, not all the functions of the website will be implemented.

AirBnB clone - The console is the first part of the project that involves manipulating a storage system. This storage engine will give an abstraction between "My object" and "How they are stored and persisted". This means: from the console code (the shell itself) and from the front-end and RestAPI that you will build later.

The console will be a tool to validate this storage engine.

### Component diagram:

![Screen Shot 2020-10-29 at 10 29 31 AM](https://user-images.githubusercontent.com/66282703/97595483-b9bd9200-19d1-11eb-9ea8-ddaf409d8a61.png)

### Classes description:

N° |Class|Description
---|---|---
1|[Console](./console.py)|This is the command line interpreter.
2|[BaseModel](./models/base_model.py)|Class BaseModel that defines all common attributes/methods for other classes.
3|[FileStorage](./models/engine/file_storage.py)|Class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.
4|[User](./models/user.py)|User Class
5|[State](./models/state.py)|State Class
6|[City](./models/city.py)|City Class
7|[Amenity](./models/amenity.py)|Amenity Class
8|[Place](./models/place.py)|Place Class
9|[Review](./models/review.py)|Review Class


### Command table

N°|Command|Description
---|---|---
1|`quit` |Exits the console.
2|`EOF`|Exits the console.
3|`help` or `help <command>`|Lists all the commands.
4|`create <class name>`|Create an instance of the class and saves it to a JSON file.
5|`show <class name> <object id>` or `<class name>.show(<id>)`|Prints the string represenation of an instance based on the class name and its id.
6|`destroy <class name> <object id>` or `<class name>.destroy(<id>)`|Deletes an instance for the class name and its id.
7|`all` or `all <class name>` or `<class name>.all()`|Prints all the string representations of all the instances.
8|`update <class name> <id> <attribute name> "<attribute value>"` |Updates an instance based on the class name and id.
9|`<class name>.count()`|Retrieves the number of instances of a class.

### Installation:
```
git clone https://github.com/Cristhian-Carbonell/AirBnB_clone
$ cd AirBnB_clone
```
### Usage:
To run Interactive Mode
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
To run Non-Interactive Mode
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
### Usage examples:

![exem-use-console-2020-11-04-at-3](https://user-images.githubusercontent.com/66282703/98167361-f1877680-1eb6-11eb-8ea8-64bcde8f4fc4.gif)

### Environment
* Language: Python3
* OS: Ubuntu 14.04 LTS
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html)

### Authors
<p align="center">
    <h3 align="center">By:</h3>
    <h3 align="center">Jiseth Peña Arias</h3>
      <p align="center">
        <a href="https://twitter.com/jis_pena" target="_blank">
            <img alt="twitter_page" src="https://user-images.githubusercontent.com/66282703/98165523-0d3d4d80-1eb4-11eb-8a61-2777d8d3cd16.png" style="float: center; margin-right: 10px" height="50" width="50">
        </a>
        <a href="https://www.linkedin.com/in/jiseth-pe%C3%B1a-arias-82b9a363/" target="_blank">
            <img alt="linkedin_page" src="https://user-images.githubusercontent.com/66282703/98165372-c7808500-1eb3-11eb-917e-50fe829d7e65.png" style="float: center; margin-right: 10px" height="50"  width="50">
        </a>
        <a>
        </a>
      </p>
    <h3 align="center">Cristhian Carbonell</h3>
      <p align="center">
        <a href="https://twitter.com/CristhianCarbo9" target="_blank">
            <img alt="twitter_page" src="https://user-images.githubusercontent.com/66282703/98165523-0d3d4d80-1eb4-11eb-8a61-2777d8d3cd16.png" style="float: center; margin-right: 10px" height="50" width="50">
        </a>
        <a href="https://www.linkedin.com/in/cristhian-carbonell-2b517b1b0/" target="_blank">
            <img alt="linkedin_page" src="https://user-images.githubusercontent.com/66282703/98165372-c7808500-1eb3-11eb-917e-50fe829d7e65.png" style="float: center; margin-right: 10px" height="50"  width="50">
        </a>
        <a>
        </a>
</p>

__Holberton School - Colombia__
__Foundations - Higher-level programming__
__Noviembre 4, 2020.__