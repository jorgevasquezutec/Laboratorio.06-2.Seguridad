pip-install:
	pip install -r requirements.txt

test-curl:
	curl -X GET http://localhost:5000/group01 -H "X-API-KEY: gAAAAABlA6z4wcpvqFGkFtJNKMewQfLZ0vtGxj0AyHcbuR1Wrz9cQlCUEhewhBfcs61-C9IsOKgJysE6Ye9Vm1L5w1X1yKTL5Q=="
	curl -X GET http://localhost:5000/group01 -H "X-API-KEY: dAAAAABlA6z4wcpvqFGkFtJNKMewQfLZ0vtGxj0AyHcbuR1Wrz9cQlCUEhewhBfcs61-C9IsOKgJysE6Ye9Vm1L5w1X1yKTL5Q=="
	curl -X GET http://localhost:5000/group02 -H "X-API-KEY: gAAAAABlA6z4wcpvqFGkFtJNKMewQfLZ0vtGxj0AyHcbuR1Wrz9cQlCUEhewhBfcs61-C9IsOKgJysE6Ye9Vm1L5w1X1yKTL5Q=="
	curl -X GET http://localhost:5000/group03 -H "X-API-KEY: gAAAAABlA6z4wcpvqFGkFtJNKMewQfLZ0vtGxj0AyHcbuR1Wrz9cQlCUEhewhBfcs61-C9IsOKgJysE6Ye9Vm1L5w1X1yKTL5Q=="
	curl -X GET http://localhost:5000/group04 -H "X-API-KEY: gAAAAABlA6z4wcpvqFGkFtJNKMewQfLZ0vtGxj0AyHcbuR1Wrz9cQlCUEhewhBfcs61-C9IsOKgJysE6Ye9Vm1L5w1X1yKTL5Q=="

test-curl-injection:
	curl -X GET "http://127.0.0.1:5000/checkUser?user=profe%27%20OR%20%271%27=%271&pass=pass%27%20OR%20%271%27=%271"