# python -u main.py -lbs 50 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/1.out 2>&1 &
# python -u main.py -lbs 50 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.15 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/2.out 2>&1 &


# python -u main.py -lbs 50 -nc 100 -jr 0.1 -nb 10 -ls 5 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/2.out 2>&1 &

# python -u main.py -lbs 100 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/1.out 2>&1 &
# python -u main.py -lbs 10 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/2.out 2>&1 &
python -u main.py -lbs 25 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/3.out 2>&1 &