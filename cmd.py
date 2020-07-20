import subprocess
import argparse

parser = argparse.ArgumentParser(description='Mac changer program')
parser.add_argument('-i', '--interface', dest='interface', help='Name of interface')
parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC Address')
args = parser.parse_args()

interface = args.interface
new_mac = args.new_mac

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac ])
subprocess.call(['ifconfig', interface, 'up'])
