# alu-back-end

Python scripts that read employee TODO data from a REST API and save it in
different formats. The API used is JSONPlaceholder.

## api

| File | What it does |
| ---- | ------------ |
| `0-gather_data_from_an_API.py` | Prints how many tasks an employee finished, then lists the titles of the done ones |
| `1-export_to_CSV.py` | Saves all tasks of one employee into `USER_ID.csv` |
| `2-export_to_JSON.py` | Saves all tasks of one employee into `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Saves the tasks of every employee into `todo_all_employees.json` |

## How to run

The first three take the employee id as an argument:

```
$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 voluptas quo tenetur perspiciatis explicabo natus
	 ...
```

```
$ python3 1-export_to_CSV.py 2
$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
...
```

The last one needs no argument, it just goes through all the users:

```
$ python3 3-dictionary_of_list_of_dictionaries.py
$ cat todo_all_employees.json
```

## Notes

Bash can do API calls with curl, but once you start counting things and
building CSV or JSON out of it, it gets painful. Python is a much better fit
for this kind of job, which is the whole point of the project.
