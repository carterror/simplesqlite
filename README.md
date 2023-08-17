## SimpleSQLite Library

### Simplesqlite is a sqlite3 based python library that provides a simple interface to communicate with a sqlite database

```python
from simplesqlite import SSQLite, Field

def example():
    db = SSQLite()

    db.create('user', Field('name').primary().text(), Field('age').integer().null())

    db.insert('user', {
        "name": "Carlos1",
        "age": 24
    })
```

