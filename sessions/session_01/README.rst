Session 01
==========

Ex_01
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

    $ python ex_01.py -h

Step 5::

    $ python ex_01.py show --args

Step 6

Review the **docopt** components in **ex_01.py**.

Step 7::

    $ python ex_01.py show --keys

Step 8

Review the **load_json** and **print_data** functions in **ex_01.py**.

Step 9::

    $ python ex_01.py show hosts

Step 10::

    $ python ex_01.py show hosts -p

Step 11::

    $ python ex_01.py show hosts -t

Step 12::

    $ python ex_01.py show hosts -pt

Step 13

Review the **elif args['hosts']:** section of the **main** function in **ex_01.py**.

