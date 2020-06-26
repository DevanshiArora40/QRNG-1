from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ

IBMQ.enable_account('a1d787ea78a947613a102d5f0050edbbd1fe485515d3f1fd1940af74aacc52515c69174e3951012ce6141dddd388e14563662d8052bb4a0c6e8d3fa3b892b5be')
provider = IBMQ.get_provider(hub='ibm-q')

q = QuantumRegister(3,'q')
c = ClassicalRegister(3,'c')
circuit = QuantumCircuit(q,c)
circuit.h(q) 
circuit.measure(q,c) 

backend = provider.get_backend('ibmq_london')
job = execute(circuit, backend, shots=8192)
                               
print('Job is executing...\n')                 
result = job.result()
counts = result.get_counts(circuit)

print('RESULT: ',counts,'\n')
print('Press any key to close')
input()
