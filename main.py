# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from simplesqlite import SSQLite, Field


def example():
    db = SSQLite()

    db.create('user', Field('name').primary().text(), Field('age').integer().null())

    db.insert('user', {
        "name": "Carlos1",
        "age": 24
    }
              )

    # print(db)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    example()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
