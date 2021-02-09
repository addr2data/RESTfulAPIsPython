Session 01
==========

ex_01
-----

Step 1::

    $ cd sessions/session_01
    $ python
    >>> import ex_01
    >>> print(ex_01.__doc__)
    >>> print(type(ex_01.__doc__))
    >>> Cntl-Z
    $

Step 2::

    $ python ex_01.py

Step 3::

    $ python ex_01.py -h

Step 4::

    $ python ex_01.py --help

Step 5::

    $ python ex_01.py show --args

Step 6

- Review the **docopt** components in **ex_01.py**.

Step 7::

    $ python ex_01.py show --keys

Step 8

- Review the contents of **ex_01.json**
- Review the **load_json** and **print_data** functions in **ex_01.py**.

Step 9::

    $ python ex_01.py hosts

Step 10::

    $ python ex_01.py hosts -p

Step 11::

    $ python ex_01.py hosts -t

Step 12::

    $ python ex_01.py hosts -pt

Step 13

- Review the **elif args['hosts']:** section of the **main** function in **ex_01.py**.

Step 14::

    $ python ex_01.py host_details apisim-001

Step 15::

    $ python ex_01.py host_details apisim-001 -i

Step 16::

    $ python ex_01.py host_details apisim-001 -n

Step 17::

    $ python ex_01.py host_details apisim-001 -m

Step 18::

    $ python ex_01.py host_details apisim-001 -inm

Step 19::

    $ python ex_01.py host_details all -inm

Step 20

- Review the **elif args['host_details']:** section of the **main** function in **ex_01.py**.


Attendee exercise (ex_01)
-------------------------

- Add a command option for showing the **version** info from **ex_01.json**.



ex_02
-----

