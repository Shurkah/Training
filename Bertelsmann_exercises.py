start_num = 5 #provide some start number, replace 5 with a number you choose
end_num = 100#provide some end number that you stop when you hit, replace 100 with a number you choose
count_by = 2 #provide some number to count by, replace 2 with a number you choose 

# write a while loop that uses break_num as the ongoing number to 
# check against end_num
break_num = start_num
result = "Oops!  Looks like your start value is greater than the end value.  Please try again."
if start_num > end_num:
    print(result)
else:
    while break_num < end_num:
        break_num += count_by
        result = break_num

