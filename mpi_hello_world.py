""" Minimal Hello World example with mpi4py

"""


from mpi4py import MPI

def mpi_hello_world():
    comm = MPI.COMM_WORLD
    process_id = comm.Get_rank()
    mpi_environment_size = comm.Get_size()
    node_name = MPI.Get_processor_name()

    print ("Hello World from MPI-process", process_id, \
           "of", mpi_environment_size, "total processes", \
           "running on node", node_name)


if __name__ == "__main__":
    mpi_hello_world()
