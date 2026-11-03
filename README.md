# alu-back-end

Python scripts that get employee todo data from an API and save it in
different formats. The API used is JSONPlaceholder.

All the scripts are in the `api` folder.

## What each script does

- `0-gather_data_from_an_API.py` - shows how many tasks an employee finished
- `1-export_to_CSV.py` - saves one employee's tasks to `USER_ID.csv`
- `2-export_to_JSON.py` - saves one employee's tasks to `USER_ID.json`
- `3-dictionary_of_list_of_dictionaries.py` - saves everyone's tasks to
  `todo_all_employees.json`

## How to run them

The first three need the employee id:

```
$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 voluptas quo tenetur perspiciatis explicabo natus
	 ...
```

The last one does not need an id, it goes through all the users:

```
$ python3 3-dictionary_of_list_of_dictionaries.py
```

## Why python and not bash

Bash can call an API with curl, but counting the tasks and turning them into
csv or json gets messy fast. Python is just easier for this kind of job.
