# Menu
def main():
    print("\nPrograma para convertir entre sistemas numéricos\n\n")
    print("1. Decimal a binario")  # Done
    print("2. Binario a decimal")  # Done
    print("3. Decimal a IEEE 754 de 32 bits")  # Done
    print("4. IEEE 32 bits a decimal")  # Done
    print("5. Binario a IEEE 754 de 32 bits")  # Done
    print("6. IEEE de 32 bits a binario")  # Done
    print("7. Decimal a IEEE 754 de 64 bits")  # Done
    print("8. IEEE 64 bits a decimal")  # Done
    print("9. Binario a IEEE 754 de 64 bits")  # Done
    print("10. IEEE de 64 bits a binario")  # Done
    print("11. Binario a hexadecimal")  # Done
    print("12. Hexadecimal a binario")  # Done
    print("13. Decimal a hexadecimal")  # Done
    print("14. Hexadecimal a decimal")  # Done
    print("15. Decimal a IEEE Hex ")  # Done
    print("16. IEEE Hex a decimal")  # Done

    opc = input("\nIngrese la opción que desea ejecutar")
    dict_op = {
        '1': {
            'text': '\nIngrese el número decimal para llevarlo binario\n\n',
            'function': dec2bin,
            'ad_params': [32],
            'res': '{num}, en decimal equivale a {res} en binario'
        },
        '2': {
            'text': '\nIngrese el número binario para llevarlo a decimal\n\n',
            'function':  bin2dec,
            'ad_params': [],
            'res': '{num}, en binario equivale a {res} en decimal'
        },
        '3': {
            'text': '\nIngrese el número decimal para llevarlo a IEEE 754 de 32 bits\n\n',
            'function':  decimal_to_ieee,
            'ad_params': [32],
            'res': '{num}, en decimal equivale a {res} en IEEE 754 de 32 bits'
        },
        '4': {
            'text': '\nIngrese el número IEEE 32 bits para llevarlo a Decimal bits\n\n',
            'function':  ieee_to_dec,
            'ad_params': [32],
            'res': '{num}, en IEEE 754 de 32 bits equivale a {res} en decimal'
        },
        '5': {
            'text': '\nIngrese el número binario para llevarlo a IEEE 754 de 32 bits \n\n',
            'function':  binario_to_ieee,
            'ad_params': [32],
            'res': '{num}, en binario equivale a {res} en IEEE 754 de 32 bits'
        },
        '6': {
            'text': '\nIngrese el número IEEE 32 bits para llevarlo a binario bits\n\n',
            'function':  ieee_to_bin,
            'ad_params': [32],
            'res': '{num}, en IEEE 754 de 32 bits equivale a {res} en binario'
        },

        '7': {
            'text': '\nIngrese el número decimal para llevarlo a IEEE 754 de 64 bits\n\n',
            'function':  decimal_to_ieee,
            'ad_params': [64],
            'res': '{num}, en decimal equivale a {res} en IEEE 754 de 64 bits'
        },

        '8': {
            'text': '\nIngrese el número IEEE 754 de 64 bits para llevarlo a decimal\n\n',
            'function':  ieee_to_dec,
            'ad_params': [64],
            'res': '{num}, en IEEE 754 de 64 bits equivale a {res} en decimal'
        },

        '9': {
            'text': '\nIngrese el número binario para llevarlo a IEEE 754 de 64 bits \n\n',
            'function': binario_to_ieee,
            'ad_params': [64],
            'res': '{num}, en binario equivale a {res} en IEEE 754 de 64 bits'
        },

        '10': {
            'text': '\nIngrese el número IEEE 64 bits para llevarlo a binario \n\n',
                    'function': ieee_to_bin,
            'ad_params': [64],
                    'res': '{num},  número IEEE 64 bits a {res} en binario'
        },

        '11': {
            'text': '\nIngrese el número binario para llevarlo a hexadecimal \n\n',
                    'function': bin_to_hexa,
            'ad_params': [],
                    'res': '{num}, en binario equivale a {res} en hexadecimal'
        },

        '12': {
            'text': '\nIngrese el número hexadecimal para llevarlo a binario \n\n',
                    'function': hexa_to_binary,
            'ad_params': [],
                    'res': '{num}, en hexadecimal equivale a {res} en binario'
        },

        '13': {
            'text': '\nIngrese el número decimal para llevarlo a hexadecimal \n\n',
                    'function': dec_to_hex,
            'ad_params': [],
                    'res': '{num}, en hexadecimal equivale a {res} en hexadecimal'
        },

        '14': {
            'text': '\nIngrese el número hexadecimal para llevarlo a decimal \n\n',
                    'function': hexa_to_dec,
            'ad_params': [],
                    'res': '{num}, en hexadecimal equivale a {res} en decimal'
        },

        '15': {
            'text': '\nIngrese el número decimal para llevarlo a IEEE Hex \n\n',
                    'function': dec_to_ieee_hex,
            'ad_params': [32],
                    'res': '{num}, en decimal equivale a {res} en IEEE hex'
        },

        '16': {
            'text': '\nIngrese el número IEEE hex para llevarlo a decimal \n\n',
                    'function': ieee_hex_to_dec,
            'ad_params': [32],
                    'res': '{num}, en IEEE hex equivale a {res} en decimal'
        },

    }
    """
    this method is used to ask if the user wants to run again the menu
    """
    def ask_to_execute_again():
        respuesta = input(
            "para continuar ingrese 1 si no cualquier otra tecla")
        if respuesta.upper() == "1":
            main()
        else:
            print("Fin")

    def execute(option):
        """
        it runs based on the option the menu option.
        Args:
            option (str): to decide which option from the menu wants to run
        """
        data_option = dict_op.get(option)
        num = input(data_option.get('text'))
        fun_res = data_option.get('function')
        params = data_option.get('ad_params')
        res = fun_res(num, *params)
        print(data_option.get('res').format(num=num, res=res))
        ask_to_execute_again()

    execute(opc)


def dec2bin(n, num_bit):
    """
    used to turn a decimal with fraction part number into a binary number.
    Args:
        n (float): number to convert
        num_bit (int): number of iterations that the method will iterate when the decimal part doesnt found a 1 to finish the loop

    Returns:
        [str]: returns a string with the binary number from the decimal entered
    """
    if str(n)[0] == '-':
        n = str(n)[1:]

    def parte_ent(n):
        n = int(n)
        bin = ''
        if n > 0:
            res = int(n % 2)
            n = int(n / 2)
            bin = str(res) + bin
            return str(parte_ent(n))+bin
        return ''

    def parte_dec(n, cant, num_len):
        n = '0.' + n
        num = n.split('.')
        if cant > num_len:
            return ''
        cant += 1
        num[1] = 0 if num[1] == '' or num[1] == ' ' else num[1]
        if int(num[1]) > 0:
            n = float(n)
            n *= 2
            num = str(n).split('.')
            return num[0] + parte_dec(num[1], cant, num_len)
        return ''

    num = str(n).split('.')
    if len(num) == 2 and num[1] != '0':
        ent = parte_ent(num[0])
        num_len = len(ent)
        dec = parte_dec(num[1], 0, num_bit-num_len)
        return ent + '.' + dec
    else:
        return parte_ent(num[0])


def bin2dec(n):
    """[summary]
    Used to turn binary to decimal
    Args:
        n (float): number to turn into decimal 

    Returns:
        [str]: String result of the binary number entered
    """
    l = str(n).split(".")
    if len(l) == 2:
        ent = l[0][::-1]
        dec = l[1]
        nent = bin_parte_ent(ent)
        ndec = bin_parte_dec(dec)
        num = str(nent)+"."+str(ndec)[2:]
    else:
        ent = l[0][::-1]
        num = bin_parte_ent(ent)
    return num


def bin_parte_ent(n):
    """
    
    Args:
        n (str): to into decimal 

    Returns:
        [float]: decimal number  
    """
    cant = 0
    p = 0
    for i in n:
        cant = cant + int(i)*2**p
        p = p+1
    return cant


def bin_parte_dec(n):
    """

    Args:
        n (n):  decimal fraction from the binary number to turn into decimal

    Returns:
        [float]: decimal fraction  
    """
    cant = 0
    p = -1
    for i in n:
        cant = cant + int(i)*2**p
        p = p-1
    return cant


def decimal_to_ieee(number, len_required):
    """
        method used to turn both 32 and 64 bit ieee 754
    Args:
        number (str): number that is going to be turned in ieee 754 format.
        len_required (int): number of bits.

    Returns:
        [str]: ieee 754 number with the precision provided.
    """
    number = float(number)
    sig = 0
    const = 1023
    to_rest = 12
    if number < 0:
        sig = 1
        number *= -1
    if len_required == 32:
        const = 127
        to_rest = 9
    num = dec2bin(number, len_required-to_rest)
    num_sp = str(num).split('.')
    number_movements = len(num_sp[0]) - 1
    exp = const + number_movements
    exp_bin = dec2bin(exp, len_required)
    mant = num[1:].replace('.', '')
    to_ret = str(sig) + exp_bin + mant
    to_complete = len(to_ret)
    to_ret += '0'*(len_required-to_complete)
    return to_ret


def binario_to_ieee(number, len_required):
    """
        used to generate a ieee 754 from the binary number provided.
    Args:
        number (str): binary number
        len_required (int): number of bits. 

    Returns:
        [str]: : ieee 754 number with the precision provided.
    """
    num_dec = bin2dec(number)
    return decimal_to_ieee(num_dec, len_required)


def ieee_to_dec(number, presition):
    """
    to turn a ieee 754 into a dec number.

    Args:
        number (str): number to turn.
        presition (int): number of bits

    Returns:
        str: decimal number from ieee 754
    """
    standard = ''
    if (presition == '32' or presition == 32):
        standard = 127
        exponent_len = 8
    else:
        standard = 1023
        exponent_len = 11
    # Sign
    sign = ""
    if (number[0] == "1"):
        sign = "-"
    # Exponent
    exponent = number[1:exponent_len + 1]
    # Exponent to decimal
    exponent = bin2dec(exponent) - standard
    # Mantisa
    mantisa = number[exponent_len + 1:]

    # 0's cutter
    i = len(mantisa)
    while (mantisa[i-1] != "1"):
        mantisa = mantisa[:-1]
        i -= 1
    mantisa = "1"+mantisa[:exponent]+"."+mantisa[exponent:]
    result = sign + bin2dec(mantisa)
    return result


def ieee_to_bin(number, presition):
    cadena = ''
    if str(number)[0] == '1':
        cadena = 'Negativo'
    decimal = ieee_to_dec(number, presition)
    return dec2bin(decimal, presition) + ' ' + cadena


def ieee_hex_to_dec(number, presition):
    ieee = hexa_to_binary(number)
    return ieee_to_dec(ieee, presition)


def hexa_to_binary(number):
    hex = {"A": "1010", "B": "1011", "C": "1100",
           "D": "1101", "E": "1110", "F": "1111"}
    i = len(number) - 1
    value = ""
    while(i >= 0):
        num = ""
        if (number[i] not in hex):
            num = dec2bin(number[i],23)
            # Agrega los 0's faltantes
            num = "0"*(4-len(num)) + num
        else:
            num = hex[number[i]]
        value = num + value
        i = i-1
    return value

def bin_to_hexa(bin):

    """
    turn a binary into hexa

    Args:
        bin (str): binary number
    """
    def ex_exp(num, hexa_dict):
        """to turn each block of 4 binary number into a hexa 

        Args:
            num (str): binary number
            hexa_dict (dict):dict for the letters that contains the hexa format

        Returns:
            [type]: [description]
        """
        acum = 0
        cont = 0
        to_ret = ''
        for i in num:
            acum += int(i)*(2**cont)
            cont += 1
            if cont > 3:
                acum = check_hex_val(acum, hexa_dict)
                to_ret = str(acum) + to_ret
                cont = 0
                acum = 0
        if cont > 0:
            check_hex_val(acum, hexa_dict)
            to_ret = str(acum) + to_ret
        return to_ret

    def check_hex_val(num, hexa_dict):
        return num if str(num) not in hexa_dict else hexa_dict.get(str(num))
    start_number = 10
    cr = 65
    hexa_dict = {str(num+start_number): chr(cr+num) for num in range(6)}
    num = str(bin).split('.') 
    reversed_number = num[0][::-1]
    parte_ent = ex_exp(reversed_number, hexa_dict)
    parte_dec = '0'
    if len(num) > 1:
        reversed_number_dec = num[1][::-1]
        parte_dec = ex_exp(reversed_number_dec, hexa_dict)
    return parte_ent + '.' + parte_dec


def dec_to_ieee_hex(num, pres):
    ieee = decimal_to_ieee(num, pres)
    ieee_hex = bin_to_hexa(ieee)
    return ieee_hex


def dec_to_hex(num):
    bin = dec2bin(num, 23)
    return bin_to_hexa(bin)


def hexa_to_dec(number):
    bin = hexa_to_binary(number)
    return bin2dec(bin)
