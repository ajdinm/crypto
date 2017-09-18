from termcolor import colored

def test(test_cases, f, f_name, ok_msg = 'OK', nok_msg = 'NOK', print_ok_case = False, print_nok_case = True):
    print '--- init testing ' + f_name + ' function ---'
    for test_case in test_cases:
        result = f(*test_case[:-1])
        is_ok = result == test_case[-1]
        to_print = ''
        color = 'green'
        if is_ok:
            to_print = to_print + 'OK'
        else:
            color = 'red'
            to_print = to_print + 'NOK'
        if (is_ok and print_ok_case) or (not is_ok and print_nok_case):
            to_print = to_print + ': ' + f_name + str(test_case[:-1]) 
            to_print = to_print + ': expected: ' + str(test_case[-1])
            to_print = to_print + '; got: ' + str(result)
        print colored(to_print, color)
    print '--- done testing ' + f_name + ' function ---\n'
