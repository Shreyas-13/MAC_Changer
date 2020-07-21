import subprocess
import argparse
import re


def get_argument():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--interface', dest='interface', help='Interface name whose MAC is to be changed')
    parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC Address')
    args = parser.parse_args()
    if not args.interface:
        print('[-] No interface provided. Use --help for more info')
    elif not args.new_mac:
        print("[-] MAC Address not provided. Use --help for more info")
    return args


def get_current_mac(interface):
    cmd_output = str(subprocess.check_output(['ifconfig', interface]))
    search_results = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", cmd_output)
    if not search_results:
        print('[-] No MAC Address found')
    else:
        return search_results.group(0)


def change_mac(interface, new_mac):
    print('[+] Changing MAC Address of ' + interface + ' to ' + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


arg = get_argument()
currentMac = get_current_mac(arg.interface)
print('[+] Current MAC ' + str(currentMac))
if str(currentMac) != 'None':
    change_mac(arg.interface, arg.new_mac)
    currentMac = get_current_mac(arg.interface)
    print('[+] Current MAC ' + str(currentMac))
