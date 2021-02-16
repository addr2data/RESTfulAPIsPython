"""ex_01.

Usage:
    ex_01 show (--args | --keys) [-t]
    ex_01 hosts [-pt]
    ex_01 host_details <host_name> [-inm]

Arguments:
    show
    hosts
    host_details

Options:
    --args      Show docopt args
    --keys      Show dict_keys
    -p          Print pretty
    -t          Print type
    -i          Include ipAdresss details
    -n          Inlcude nic details
    -m          Include mac details


"""

from docopt import docopt
import simplejson as json


def print_data(data, pretty=False, object_type=False):
    """ Default arguments.
    
    Here we have two arguments that have defaults, therefore
    they are optional.
    """
    # Print pretty
    if pretty:
        # As an alternative, checkout 'pprint'
        print(json.dumps(data, indent=4, sort_keys=False))
    else:
        print(data)

    # Print type
    if object_type:  # Here we don't need the else statement
        print(type(data))


def load_json():
    """ Review PEP-343 (The "with" Statement).

    Here we are returning the json data from within the 'with' statement.
    This will not affect the operation of the 'with' statement iteself. 
    """
    with open('ex_01.json', 'r') as fin:
        return json.load(fin)


def main():
    """Excessive commenting is not Pythonic.

    We are using a lot comments in this module for training purposes.
    No need to do this in your code.
    """
    args = docopt(__doc__)

    # Here we make decisions based on arguments and options
    if args['show']:
        if args['--args']:
            print_data(args, object_type=args['-t'])
        elif args['--keys']:
            print_data(load_json().keys(), object_type=args['-t'])  # Using the dict keys() method to get a list of keys

    elif args['hosts']:
        json_data = load_json()['hostList']  # Assigning only a portion of json data

        # Positional arguments vs. keyword arguments (#1)
        print_data(json_data, args['-p'], args['-t'])

    	# Positional arguments vs. keyword arguments (#2)
        # print_data(json_data, object_type=args['-t'], pretty=args['-p'])

    	# Positional arguments vs. keyword arguments (#3)
        # print_data(object_type=args['-t'], pretty=args['-p'], json_data)

        # Positional arguments vs. keyword arguments (#4)
        # print_data(object_type=args['-t'], pretty=args['-p'], data=json_data)

    elif args['host_details']:
        if args['<host_name>'] == "all":
            json_data = load_json()['hostDetails']
        else:
            json_data = {}
            json_data[args['<host_name>']] = load_json()['hostDetails'][args['<host_name>']]

        output = []
        for key, val in json_data.items(): # Using the dict items method to get key and value
            host_info = []
            host_info.append(f"host={key}")
            if args['-i']:
                host_info.append(f"ipAddress={val['ipAddress']}")
            if args['-n']:
                host_info.append(f"nic={val['nic']}")
            if args['-m']:
                host_info.append(f"mac={val['mac']}")
            output.append(", ".join(host_info))  # Using string join method with a list

        print_data(output, True)


if __name__ == "__main__":
    main()
