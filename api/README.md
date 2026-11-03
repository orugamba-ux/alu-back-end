# api

The scripts for this project.

- `0-gather_data_from_an_API.py` - prints an employee's task progress
- `1-export_to_CSV.py` - writes their tasks to `USER_ID.csv`
- `2-export_to_JSON.py` - writes their tasks to `USER_ID.json`
- `3-dictionary_of_list_of_dictionaries.py` - writes all the employees to
  `todo_all_employees.json`

Run them with python3 and the employee id:

```
$ python3 0-gather_data_from_an_API.py 2
```

The last script takes no id.
