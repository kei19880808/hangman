#1

def imput_number(x):
    """
    takes an int and returns it multiplied by 2.
    :param x:int.
    :return : x multiplied by 2
    """
    return x**2

result = imput_number(10)
print(result)

#2

def f_str(y1):
    '''
     prints the string passed in.
     :param y1 : str.
    '''
    print(y1)

f_str("p")

#3

def add_5(x,y,z,a=4,b=5):
    """
    returns the sum of each params multiplied by themselves.
    :param x: int
    :param y: int
    :param z: int
    :param a: int
    :param b: int
    :return: int sum of x^2,y^2,z^2,a^2 and b^2
    """
    return x**2 + y**2 + z**2 + a**2 + b**2

result = add_5(1,2,3)
print(result)

#4

def f(x):
    '''
    入力値を2で割った数値を出力します
    :param x: int
    :return:
    '''
    return int(x/2)
def g(y):
    return int(y*4)

result1 = f(2)
result2 = g(result1)
print(result2)

#5

def float_trans(z):
    '''
    Converts passed in str to float.
    :param z: str.
    :return: string is converted to float.
    '''
    try:
        return float(z)
    except ValueError:
        print("Could not convert the string to a float.")

result3 = float_trans(2)
print(result3)

