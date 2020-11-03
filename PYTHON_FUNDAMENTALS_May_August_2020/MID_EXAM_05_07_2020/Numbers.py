numbers = input().split(" ")
average = 0

numbers_list = []
greater_than_average = []
lower_than_average = []
greater_than_average_sorted = sorted(greater_than_average)
lower_than_average_sorted = sorted(lower_than_average)

for num in numbers:
    numbers_list.append(num)

list_sum = sum(map(int, numbers_list))
average = list_sum / len(numbers_list)

for num in numbers_list:
    if int(num) > average:
        greater_than_average.append(num)
    elif int(num) < average:
        lower_than_average.append(num)

if len(greater_than_average_sorted) > 0:
    print (" ".join(greater_than_average), end=" ")
else:
    print("No")



# using
# System;
# using
# System.Collections.Generic;
# using
# System.Linq;
# using
# System.Text;
# using
# System.Threading.Tasks;
#
# namespace
# Numbers
# {
#
#
# class Numbers
#     {
#         static
#     void
#     Main()
#     {
#         List < int > numbers = Console.ReadLine().Split().Select(int.Parse).ToList();
#     double
#     averageNum = numbers.Average();
#     List < int > biggers = new
#     List < int > ();
#
#     if (numbers.Count <= 1)
#     {
#     Console.WriteLine("No");
#     }
#     else
#     {
#     for (int i = 0; i < numbers.Count; i++)
#     {
#     if ((double)numbers[i] > averageNum)
#     {
#     biggers.Add(numbers[i]);
#     }
#     }
#     }
#
#     Console.WriteLine(string.Join(" ", biggers.OrderByDescending(x= > x).Take(5)));
#     }
#     }
#
# }