import argparse
import random

parser = argparse.ArgumentParser(description='Random coordinates generator')
parser.add_argument('-x1', '--x1', default=0, type=float, help='Left x')
parser.add_argument('-x2', '--x2', default=1, type=float, help='Right x')
parser.add_argument('-y1', '--y1', default=0, type=float, help='Left y')
parser.add_argument('-y2', '--y2', default=1, type=float, help='Right y')
parser.add_argument('-z1', '--z1', default=0, type=float, help='Left z')
parser.add_argument('-z2', '--z2', default=1, type=float, help='Right z')
parser.add_argument('-N', '-n', '--num', default=1, type=int, help='Number of coordinates')
parser.add_argument('--file', default='rand_coord.txt', type=str, help='Output file')

args = parser.parse_args()

with open(args.file, 'w') as f:
    for _ in range(args.num):
        x = random.uniform(args.x1, args.x2)
        y = random.uniform(args.y1, args.y2)
        z = random.uniform(args.z1, args.z2)

        f.write(f'{x} {y} {z}\n')
