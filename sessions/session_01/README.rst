Session 01
==========

Exercise 01 (Intro to docopt)
-----------------------------

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

****

Attendee Activity (Intro to docopt)
-----------------------------------

- Add a command line option for showing the **version** information from **ex_01.json**.

****

****

Exercise 02 (Intro to requests)
-------------------------------

Step 1::

    $ python ex_02.py endpts

Step 2::

    $ python ex_02.py endpts --type

Step 3::

    $ python ex_02.py endpts -s

Step 4::

    $ python ex_02.py endpts -s --type

Step 5::

    $ python ex_02.py endpts -r

Step 6

- Review the four **X-RateLimit** header fields 
    + See **Exercise_002**, regarding **X-RateLimit-Reset**


Step 7::

    $ python ex_02.py endpts -j

Step 8::

    $ python ex_02.py endpts -t

Step 9::

    $ python ex_02.py endpts -t --type

Step 10

- Remove the block comments and review the code in **print_helper**.

Step 11::

    $ python ex_02.py endpts -t

Step 12

- Review the results from **Step 11**
- Swap the single line comment on the print statements

Step 13::

    $ python ex_02.py endpts -t

Step 14

- Review the results from **Step 13**
- Restore the original comments

Step 15::

    $ python ex_02.py endpts -srjt

****

****

Attendee Activity (Intro to requests)
-------------------------------------

- Using the **datetime** module, determine how the how long the **X-RateLimit-Reset** timer is.

- Add code to the **elif args['user']:** section to output **response headers** and **response body(json)** for your user account.
    + Use the **user_url** url, which can be found in the **response body(json)** from the **endpts** argument.

****

****

Exercise 03 (requests, basic auth and exception handling)
---------------------------------------------------------
Initial

- Start **vxrail-mock-api**

Step 1

- Review **ex_03a.py**
- Review **vxrail_interface_3a.py**


Step 2::

    $ python ex_03a.py collect


Step 3

- Review the exceptions that occurred.
- Comment **Step 2** in **vrail_interface_3a.py**
- Uncomment **Step 4** in **vrail_interface_3a.py**

Step 4::

    $ python ex_03a.py collect


Step 5

- Review the warning that occurred.
- Uncomment **Step 6** in **vrail_interface_3a.py**

Step 6::

    $ python ex_03a.py collect

Step 7

- Review the results
- Comment **Step 4** in **vrail_interface_3a.py**
- Uncomment **Step 8** in **vrail_interface_3a.py**

Step 8::

    $ python ex_03a.py collect

Step 9::

    $ python ex_03a.py collect -t

Step 10

- Review **ex_03b.py**
- Review **vxrail_interface_3b.py**

Step 11::

    $ python ex_03b.py collect

Step 12

- Review the results
- Comment **Step 11** in **vrail_interface_3b.py**
- Uncomment **Step 13** in **vrail_interface_3b.py**

Step 13::

    $ python ex_03b.py collect

Step 14

- Review **ex_03c.py**
- Review **vxrail_interface_3c.py**

Step 15::

    $ python ex_03c.py collect

Step 16

- Comment **Step 15** in **vrail_interface_3c.py**
- Uncomment **Step 17** in **vrail_interface_3c.py**

Step 17::

    $ python ex_03c.py collect

Step 18

- Review the results
- Comment **Step 17** in **vrail_interface_3c.py**
- Uncomment **Step 15** in **vrail_interface_3c.py**
- comment **Step 19a** in **vrail_interface_3c.py**
- Uncomment **Step 19b** in **vrail_interface_3c.py**

Step 19::

    $ python ex_03c.py collect

****

****

Attendee Activity (requests, basic auth and exception handling)
---------------------------------------------------------------

- to be added

****

****

Common HTTP Methods (as defined in RFC 7231)
--------------------------------------------

**GET**

- Transfer a current representation of the target resource

**POST**

- Perform resource-specific processing on the request payload

**PUT**

- Replace all current representations of the target resource with the request payload

**DELETE**

- Remove all current representations of the target resource

****

****

PATCH Method (as defined in RFC 5789)
-------------------------------------

**PATCH**

-  Requests that a set of changes, described in the request entity, be applied to the resource identified

****

****

HTTP Status Code Ranges
-----------------------

- Informational responses (100–199)
- Successful responses (200–299)
- Redirects (300–399)
- Client errors (400–499)
- Server errors (500–599)

****

****


