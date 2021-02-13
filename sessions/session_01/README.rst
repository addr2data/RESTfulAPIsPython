Session 01
==========

Example (ex_01)
---------------

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

Step 6::

    $ python ex_01.py show --args -t

Step 7

- Review the **docopt** components in **ex_01.py**.

Step 8::

    $ python ex_01.py show --keys

Step 9::

    $ python ex_01.py show --keys -t

Step 10

- Review the contents of **ex_01.json**
- Review the **load_json** and **print_data** functions in **ex_01.py**.

Step 11::

    $ python ex_01.py hosts

Step 12::

    $ python ex_01.py hosts -p

Step 13::

    $ python ex_01.py hosts -t

Step 14::

    $ python ex_01.py hosts -pt

Step 15

- Review the **elif args['hosts']:** section of the **main** function in **ex_01.py**.

Step 16::

    $ python ex_01.py host_details apisim-001

Step 17::

    $ python ex_01.py host_details apisim-001 -i

Step 18::

    $ python ex_01.py host_details apisim-001 -n

Step 19::

    $ python ex_01.py host_details apisim-001 -m

Step 20::

    $ python ex_01.py host_details apisim-001 -inm

Step 21::

    $ python ex_01.py host_details all -inm

Step 22

- Review the **elif args['host_details']:** section of the **main** function in **ex_01.py**.

****

Exercise (ex_01)
----------------

- Add a command line option for showing the **version** information from **ex_01.json**.

****

Example (ex_02)
---------------

Step 1::

    $ python ex_02.py get endpts

Step 2::

    $ python ex_02.py get endpts -s

Step 3::

    $ python ex_02.py get endpts -r

Step 4::

    $ python ex_02.py get endpts -j

Step 5::

    $ python ex_02.py get endpts -t

Step 5::

    $ python ex_02.py get endpts -srjt

****

Exercise (ex_02)
----------------

- Add code to the **elif args['user']:** section to output **response headers** and **response body(json)** for your user account.
    + Use the **user_url** url, which can be found in the **response body(json)** from the **endpts** argument.

****

Example (ex_03)
---------------

