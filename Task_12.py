# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


sum_of_numbers = int(input('Введите сумму чисел: '))
product_of_numbers = int(input('Введите произведение чисел: '))
result = []
for i in range (sum_of_numbers + product_of_numbers):
    if i == (sum_of_numbers * i - product_of_numbers) ** 0.5:
        result.append(i)
print(*result if len(result) == 2 else result + result)