import os
from qiskit_ibm_runtime import QiskitRuntimeService

token = os.environ.get("QISKIT_IBM_TOKEN")

if not token:
	raise RuntimeError("Missing QISKIT_IBM_TOKEN")

service = QiskitRuntimeService(
	channel="ibm_quantum_platform",
	token=token,
	instance="open-instance"
)

backends = service.backends(operational=True)

print("\nSimulated quantum computers:\n")

for backend in backends:
	config = backend.configuration()
	status = backend.status()

	if config.simulator:
		print(
			f"\t{backend.name:<30} "
			f"has {status.pending_jobs} queues"
		)

print("\nReal quantum computers:\n")

for backend in backends:
	config = backend.configuration()
	status = backend.status()

	if not config.simulator:
		print(
			f"\t{backend.name:<30} "
			f"has {status.pending_jobs} queues "
			f"with {config.n_qubits} qubits"
		)
