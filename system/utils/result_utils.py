import h5py
import numpy as np
import os


def average_data(args, length=800):
    test_acc = get_all_results_for_one_algo(
        args, int(length))
    test_acc_data = np.average(test_acc, axis=0)


    max_accurancy = []
    for i in range(args.times):
        max_accurancy.append(test_acc[i].max())

    print("std for best accurancy:", np.std(max_accurancy))
    print("mean for best accurancy:", np.mean(max_accurancy))


def get_all_results_for_one_algo(args, length=800):
    test_acc = np.zeros((args.times, length))
    algo = args.dataset + "_" + args.algorithm
    for i in range(args.times):
        file_name = f"{algo}_{args.goal}_gr{args.global_rounds}_ls{args.local_steps}_bs{args.batch_size}_lr{args.local_learning_rate}"
        test_acc[i, :] = np.array(
            read_data_then_delete(file_name, delete=False))[:length]

    return test_acc


def read_data_then_delete(file_name, delete=False):
    file_path = "../results/" + file_name + ".h5"

    with h5py.File(file_path, 'r') as hf:
        rs_test_acc = np.array(hf.get('rs_test_acc'))

    if delete:
        os.remove(file_path)
    print("Length: ", len(rs_test_acc))

    return rs_test_acc