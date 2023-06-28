# pip

## What does pip editable mean?
In the command: `pip install --editable .` or `pip install -e .`, the `--editable` option is used for development.

It means that if you change the files in the module, you won't have to reinstall it to see the changes.

In a production environment, this option shouldn't be used.

Some explanations about the command:

- the `.` is in fact the path to your module. As we are in the root folder of the module, we can just say here, which is what the dot means.

```
 pip install --editable .[all]
```
- the [all] after the dot means we want to install all dependencies, which is common when developing. Depending on your use of the module, you can install only parts of it:
  - the default (nothing after the dot) installs the minimum to make the module run.
  - [tests] installs the requirements to test the module.
  - [docs] installs the requirements to build the documentation.

some modules have extra options.


