import os
from invoke import task, Collection
from app import app

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

namespace = Collection()


@task
def dev_server(c, port=5000):
    with c.cd(ROOT_DIR):
        c.run(f"flask run --host=0.0.0.0 --port {port}")


namespace.add_task(dev_server)


@task
def lint(c):
    with c.cd(ROOT_DIR):
        c.run("pylint app test")


namespace.add_task(lint)


@task
def format(c, check=False):
    with c.cd(ROOT_DIR):
        if check:
            c.run("black . --check", pty=True)
        else:
            c.run("black .", pty=True)


namespace.add_task(format)


@task
def test(c, debug=False):
    with c.cd(ROOT_DIR):
        c.run("python -m pytest {debug}".format(debug=" -s" if debug else ""), pty=True)


namespace.add_task(test)


@task
def db_create(c):
    from app import db

    db_path = app.config["SQLALCHEMY_DATABASE_URI"][len("sqlite:///") :]
    if os.path.isfile(db_path):
        os.remove(db_path)

    db.create_all()

    print("Sqlite database created at {}".format(app.config["SQLALCHEMY_DATABASE_URI"]))


db = Collection("db")
db.add_task(db_create, name="create")

namespace.add_collection(db)
