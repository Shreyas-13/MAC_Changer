import subprocess
import argparse


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


def get_arguments():
    parser = argparse.ArgumentParser(description='Mac changer program')
    parser.add_argument('-i', '--interface', dest='interface', help='Name of interface')
    parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC Address')
    args = parser.parse_args()
    if not args.interface:
        parser.error("[-] Plaese specify an interface. Use --help for more info")
    elif not args.new_mac:
        parser.error("[-] Please provide a MAC address.  Use --help for more info")
    return args


arg = get_arguments()
change_mac(arg.interface, arg.new_mac)


