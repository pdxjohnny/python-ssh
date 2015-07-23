Python SSH In Parallel
---

This repo provides python files which execute ssh commands on a list of hosts
in parallel.

The arguments are the functions in the file so if I want to run the install
function I would do:

```bash
python apache.py install
```

If I wanted to run the status function I would do:

```bash
python apache.py status
```

Main
---

Before running commands on hosts you need to connect to them.

```python
HOSTS = [
    {
        "host":"example2.com",
        "username":"server_username",
        "password":"server_password"
    },
    {
        "host":"example3.com",
        "username":"server_username",
        "password":"server_password"
    }
]

# Run in parallel
THREADS = True
# print hostname with output
PRINT_HOST = True

def main():
    # This is done by passing connect_all the list of hosts.
    ssh.connect_all(HOSTS)
    # Call all functions in the argument list
    for function_name in sys.argv:
        try:
            function = getattr(sys.modules[__name__], function_name)
            function(print_host=PRINT_HOST, threads=THREADS)
        except Exception as error:
            pass
    # When you are done then you should call close_all.
    ssh.close_all()
```


Functions
---

Functions are arrays of commands to run in the ssh shell on the host.
This is an example of running a command on all hosts

```python
def status(**kwargs):
    command = [
        "service apache2 status",
    ]
    ssh.run_all(command, **kwargs)
```
