# python -u main.py -lbs 50 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/1.out 2>&1 &
# python -u main.py -lbs 50 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.15 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/2.out 2>&1 &


# python -u main.py -lbs 50 -nc 100 -jr 0.1 -nb 10 -ls 5 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/2.out 2>&1 &

# python -u main.py -lbs 100 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/1.out 2>&1 &
# python -u main.py -lbs 10 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/2.out 2>&1 &
# python -u main.py -lbs 25 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 100 -did 0 -go resnet > out/3.out 2>&1 &


# python -u main.py -lbs 100 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 100 -did 0 -go cnn > out/4.out 2>&1 &
# python -u main.py -lbs 100 -nc 100 -jr 1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 100 -did 0 -go cnn > out/5.out 2>&1 &
# python -u main.py -lbs 50 -nc 100 -jr 0.1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 500 -did 0 -go cnn > out/6.out 2>&1 &
# python -u main.py -lbs 25 -nc 100 -jr 0.1 -nb 10 -ls 10 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 300 -did 0 -go cnn > out/7.out 2>&1 &
# python -u main.py -lbs 25 -nc 100 -jr 0.1 -nb 10 -ls 10 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 500 -did 0 -go cnn > out/8.out 2>&1 &

# python -u main.py -lbs 50 -nc 100 -jr 1 -nb 10 -ls 5 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 450 -did 0 -go cnn > out/8.out 2>&1 &
# python -u main.py -lbs 25 -nc 100 -jr 0.1 -nb 10 -ls 10 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 500 -did 0 -go cnn > out/9.out 2>&1 &
# python -u main.py -lbs 25 -nc 100 -jr 0.1 -nb 10 -ls 10 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 500 -did 0 -go cnn > out/10.out 2>&1 &
# python -u main.py -lbs 25 -nc 100 -jr 0.1 -nb 10 -ls 10 -lr 0.05 -data Cifar10 -m cnn -algo FedAvg -gr 500 -did 0 -go cnn > out/11.out 2>&1 &

# python -u main.py -lbs 10 -nc 100 -jr 0.1 -nb 10 -ls 10 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 300 -did 0 -go resnet > out/bs10.out 2>&1 &
# python -u main.py -lbs 50 -nc 100 -jr 0.1 -nb 10 -ls 10 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 300 -did 1 -go resnet > out/bs50.out 2>&1 &
# python -u main.py -lbs 25 -nc 100 -jr 0.1 -nb 10 -ls 10 -lr 0.05 -data Cifar10 -m resnet -algo FedAvg -gr 300 -did 0 -go resnet > out/bs25.out 2>&1 &

# python -u main.py -lbs 50 -nc 20 -jr 0.5 -nb 10 -ls 10 -lr 0.05 -data mnist -m resnet -algo FedAvg -gr 300 -did 0 -go resnet > out/bs50_mnist.out 2>&1 &

# python -u main.py -lbs 32 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 500 -did 0 -go cnn > out/mnist_fedavg_01.out 2>&1 &
# python -u main.py -lbs 64 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 500 -did 0 -go cnn > out/mnist_fedavg_02.out 2>&1 &
# python -u main.py -lbs 128 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 500 -did 0 -go cnn > out/mnist_fedavg_03.out 2>&1 &


# python -u main.py -lbs 32 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 500 -did 0 -go cnn -ls 5 > out/mnist_fedavg_04_iid_balance.out 2>&1 &
# python -u main.py -lbs 64 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 500 -did 0 -go cnn -ls 10 > out/mnist_fedavg_05_iid_balance.out 2>&1 &
# python -u main.py -lbs 128 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 500 -did 0 -go cnn -ls 20 > out/mnist_fedavg_06_iid_balance.out 2>&1 &

python -u main.py -lbs 16 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 300 -did 0 -go cnn -ls 10 > out/mnist_fedavg_01_noniid.out 2>&1 &
python -u main.py -lbs 32 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 300 -did 0 -go cnn -ls 10 > out/mnist_fedavg_02_noniid.out 2>&1 &
python -u main.py -lbs 64 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 300 -did 0 -go cnn -ls 10 > out/mnist_fedavg_03_noniid.out 2>&1 &
python -u main.py -lbs 128 -nc 100 -jr 0.1 -nb 10 -data mnist -m cnn -algo FedAvg -gr 300 -did 0 -go cnn -ls 10 > out/mnist_fedavg_04_noniid.out 2>&1 &