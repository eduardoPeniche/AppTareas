import time
# Simulate a delay in database processing to slow down terminal
def processing():
    print()
    message = "Procesando"
    print(message, end='', flush=True)
    for _ in range(4):
        time.sleep(0.5)
        print('.', end='', flush=True)