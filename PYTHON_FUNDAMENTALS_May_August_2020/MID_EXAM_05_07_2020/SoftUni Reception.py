import math

first_emlpyee = int(input())
second_emlpyee = int(input())
third_emlpyee = int(input())
students_count = int(input())

students_per_hour = first_emlpyee + second_emlpyee + third_emlpyee
students_left = students_count - students_per_hour
next_hours = 0

while students_count > 0:
    next_hours = students_left/3
    students_count -= students_per_hour

    if next_hours % 4:
        continue
print(f"Time needed: {math.ceil(next_hours)}h.")


# function nationalCourt([emp1, emp2, emp3, pplCount]) {
#
#   let pplServed = pplCount;
#   let timeNeeded = 0;
#
#   while (pplServed > 0) {
#     timeNeeded++;
#
#     if (timeNeeded % 4 === 0) {
#       continue;
#     }
#
#     pplServed -= emp1;
#     pplServed -= emp2;
#     pplServed -= emp3;
#
#   }
#   console.log(`Time needed: ${timeNeeded}h.`);
#
# }

