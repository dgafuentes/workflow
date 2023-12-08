from prefect import flow, task
import time

@task(log_prints=True, tags=["sumas"])
def suma(x, y):
    result = x + y
    return result

@task(log_prints=True, tags=["multiplicaciones"])
def multiplicar():
    result = 3 * 3 
    return result

@task(log_prints=True, tags=["checks"])
def check():
    return "[+] Pasando la condicion"

@flow(name="First flow")
def main():
    num1 = 20
    num2 = 37
    do_suma = suma(num1, num2) # task 1
    print(do_suma)
    do_multiplicar = multiplicar() # task 2
    print(do_multiplicar)
    time.sleep(3)
    if do_multiplicar != 9:
        a = check() # task 3
        print("[+] Ejecutando una tarea pasando la comprobacion" + a)

if __name__ == "__main__":
    main()