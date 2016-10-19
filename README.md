# Boilerman
[Boilerman](https://github.com/sakisds/boilerman) is a simple boilerplate file generator written in Python using the [Pystache](https://github.com/defunkt/pystache) engine. It can generate any kind of file based on a definition file and [mustache](https://mustache.github.io/) templates.

## Installation
You can install this by cloning the repository and running `setup.py`:
```
$ git clone https://github.com/sakisds/boilerman.git
$ cd boilerman
$ python setup.py install
```

## How to use
To create a new set of files just call boilerman with the template's name:
```
$ boilerman latex
header.tex (Header File)
title (Document Title): Testing
date (Creation date): \today

document.tex (Document file)
```
Each template is made of one definition file (YAML) and one or more mustache templates. From our example:
```yaml
---
  title: "Header file"
  filepath: "header.tex"
  delimiters: "<< >>"
  variables:
    - {name: "name", description: "Document Title"}
    - {name: "date", description: "Creation date"}
...
---
  title: "Document File"
  filepath: "document.tex"
...
```

Here is the list of supported attributes:

| Attribute  | Optional? | Default | Description | 
| ---------- | --------- | ------- | ----------- |
| title      | No        |         | This file's title. It's not significant in any way. |
| filepath   | No        |         | The filename of the mustache template. It must be in the same folder. |
| delimiters | Yes       | {{ }}   | Mustache template delimiters. |
| variables  | Yes       | Empty   | The list of variables to replace. |

And each variable's attributes:

| Attribute   | Optional? | Default | Description | 
| ----------- | --------- | ------- | ----------- |
| name        | No        |         | The variable's name. For example, if the name is 'title' you should type `{{ title }}` in your template. |
| description | No        |         | User friendly description. |

Each definition file can contain attributes for as many template files as you need. These are stores by default in `~/.boilerman` or wherever the `BOILERMAN_TEMPLATES` environmental variable is pointing at. The `sample-templates` folder includes a couple of examples to get your started.

## TODO
Currently boilerman is very simple. Some things that are planned:
- Default values for variables.
- Ability to create files with a different filename.
- Command line arguments for variables so boilerman it can be used in scripts.

## License
This project is licensed under the MIT license, check the `LICENSE` file.
