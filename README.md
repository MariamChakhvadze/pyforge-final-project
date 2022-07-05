# PyForge Final Project

[![LICENSE](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/MariamChakhvadze/pyforge-final-project#License "Project's LICENSE section")

## Description

`pyforge-final-project` is a CLI application that connects to remote open-source compounds API and fetches data based on what the user instructs it. The fetched data is stored in a PostgreSQL managed database and the application can display the data in an ASCII table format anytime it will be instructed by a specific subcommand.

## Installation

In order to install and start using `pyforge-final-project`, you need to have **Docker** and **Docker Compose** installed on your system. Please refer to the [official installation guides](https://docs.docker.com/get-docker) for that purpose.

Depending on how you install **Docker Compose**, you will either have to run `docker-compose` or separated `docker compose`. Please keep this in mind.

```sh
$ cd pyforge-final-project
...

$ docker-compose up -d --build
...
```

This will run the containers in background, allowing you to access them at any time desired.

In order to uninstall the project, run:

```sh
$ docker-compose down
...
```

## User Guide

Once you install the project, you can connect to the container which hosts the CLI application and run certain commands.

For example:

```sh
$ docker-compose exec cli bash
...

$ python3 src/main.py
usage: main.py [-h] {get,print_table} ...

positional arguments:
  {get,print_table}

options:
  -h, --help         show this help message and exit

$ python3 src/main.py get
Downloading compound(s):  38%|██████████████████                                       | 3/8 [00:04<00:07,  1.46s/it]

$ python3 src/main.py print_table
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
| ID | Compound |     Name      |    Formula    |     InChI     |   InChIKey    |    SMILES     | Cross Links Count |
+====+==========+===============+===============+===============+===============+===============+===================+
| 1  | ADP      | ADENOSINE-... | C10 H15 N5... | InChI=1S/C... | XTWYTFMLZF... | c1nc(c2c(n... | 17                |
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
| 2  | ATP      | ADENOSINE-... | C10 H16 N5... | InChI=1S/C... | ZKHQWZAMYR... | c1nc(c2c(n... | 22                |
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
| 3  | STI      | 4-(4-METHY... | C29 H31 N7 O  | InChI=1S/C... | KTUFNOKKBV... | Cc1ccc(cc1... | 11                |
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
| 4  | ZID      | ISONICOTIN... | C27 H30 N8... | InChI=1S/C... | SURAWYIAXP... | c1cnccc1C(... | 1                 |
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
| 5  | DPM      | 3-[5-{[3-(... | C20 H24 N2 O8 | InChI=1S/C... | LCAXMKQKEY... | Cc1c(c(c([... | 4                 |
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
| 6  | XP9      | O-phosphon... | C13 H26 N ... | InChI=1S/C... | WUTPSGIFCC... | CC(C(C(=O)... | 3                 |
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
| 7  | 18W      | 3-[(5Z)-5-... | C20 H22 N2 O9 | InChI=1S/C... | MBSNQHZDAB... | Cc1c(c(c([... | 2                 |
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
| 8  | 29P      | 3-[(5S)-5-... | C20 H24 N2 O9 | InChI=1S/C... | DHEOBTWDCM... | Cc1c(c(c([... | 2                 |
+----+----------+---------------+---------------+---------------+---------------+---------------+-------------------+
```

In case you would want to fetch data only for a certain compound, you can enter:

```sh
$ python3 src/main.py get -c ADP
...
```

## Authors

See the [AUTHORS](AUTHORS) file for information regarding the authors of the project.

## License

`pyforge-final-project` is licensed under the permissive [MIT License](LICENSE).
