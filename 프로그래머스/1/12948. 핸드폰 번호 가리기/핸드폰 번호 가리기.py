def solution(phone_number):
    return '*'*len(phone_number[:-4]) + f'{phone_number[-4:]}'